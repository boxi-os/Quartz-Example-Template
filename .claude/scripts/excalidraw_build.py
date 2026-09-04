#!/usr/bin/env python3
"""Erzeugt Excalidraw-Zeichnungen (Obsidian-Excalidraw-Plugin) aus einer kleinen Spezifikation.

Claude entscheidet Inhalt, Struktur und Farben; dieses Skript berechnet Layout,
Geometrie, IDs und Bindungen und schreibt eine gueltige `.excalidraw.md`.

Aufrufe:
  python3 .claude/scripts/excalidraw_build.py spec.json [--out "99 Assets/Excalidraw/Name.excalidraw.md"] [--force]
  python3 .claude/scripts/excalidraw_build.py --validate "99 Assets/Excalidraw/Name.excalidraw.md"
  python3 .claude/scripts/excalidraw_build.py --example structure|flow|cheatsheet|overview

Spezifikation (JSON, flach):
  title       Titel der Zeichnung (Pflicht)
  kind        structure | flow | cheatsheet | overview   (Standard: structure)
  direction   down | right                               (nur structure/flow)
  font        entfaellt; Zeichnungen verwenden immer die sachliche Schrift
  groups      [{id, label, color}]
  nodes       [{id, label, shape, color, group, note}]
  edges       [{from, to, label, style: arrow|line, dashed}]
  cards       [{title, color, lines: [..]}]              (kind: cheatsheet)
  legend      [{color, label}]
Farben: blue green yellow red violet orange pink teal gray white
"""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import math
import random
import re
import sys
import time

PALETTE = {
    'blue':   ('#a5d8ff', '#1971c2'),
    'green':  ('#b2f2bb', '#2f9e44'),
    'yellow': ('#ffec99', '#f08c00'),
    'red':    ('#ffc9c9', '#e03131'),
    'violet': ('#d0bfff', '#6741d9'),
    'orange': ('#ffd8a8', '#e8590c'),
    'pink':   ('#fcc2d7', '#c2255c'),
    'teal':   ('#96f2d7', '#099268'),
    'gray':   ('#e9ecef', '#868e96'),
    'white':  ('#ffffff', '#1e1e1e'),
}
TEXT_COLOR = '#1e1e1e'
FONT_HAND, FONT_NORMAL = 1, 2  # Virgil, Helvetica
NODE_FONT = 20
NOTE_FONT = 16
TITLE_FONT = 28
CARD_TITLE_FONT = 20
CARD_BODY_FONT = 16
PAD = 16
MIN_NODE_W = 140
NODE_GAP = 40
LAYER_GAP = 90
GROUP_PAD = 28
GROUP_LABEL_H = 34
CARD_W = 330
CARD_GAP = 36

ID_ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


class Builder:
    def __init__(self, spec: dict):
        self.spec = spec
        self.elements: list[dict] = []
        self.rng = random.Random(spec.get('seed', 42))
        # Handschrift ist im Vault nicht zulaessig; ein 'font' in der Spec wird ignoriert.
        self.font = FONT_NORMAL
        self.rough = 0
        self.now = int(time.time() * 1000)

    # ---------- Hilfen ----------
    def new_id(self) -> str:
        return ''.join(self.rng.choice(ID_ALPHABET) for _ in range(8))

    def seed(self) -> int:
        return self.rng.randint(1, 2_000_000_000)

    def color(self, name: str | None):
        return PALETTE.get(str(name or 'gray').lower(), PALETTE['gray'])

    def text_size(self, text: str, font_size: int) -> tuple[float, float]:
        lines = text.split('\n')
        char_w = font_size * (0.62 if self.font == FONT_HAND else 0.56)
        w = max((len(l) for l in lines), default=1) * char_w
        h = len(lines) * font_size * 1.25
        return math.ceil(w), math.ceil(h)

    def base(self, typ: str, x: float, y: float, w: float, h: float, **kw) -> dict:
        el = {
            'id': self.new_id(), 'type': typ, 'x': round(x, 1), 'y': round(y, 1),
            'width': round(w, 1), 'height': round(h, 1), 'angle': 0,
            'strokeColor': TEXT_COLOR, 'backgroundColor': 'transparent',
            'fillStyle': 'solid', 'strokeWidth': 2, 'strokeStyle': 'solid',
            'roughness': self.rough, 'opacity': 100, 'groupIds': [], 'frameId': None,
            'roundness': None, 'seed': self.seed(), 'version': 1, 'versionNonce': self.seed(),
            'isDeleted': False, 'boundElements': [], 'updated': self.now, 'link': None, 'locked': False,
        }
        el.update(kw)
        self.elements.append(el)
        return el

    def text(self, x: float, y: float, content: str, font_size: int, align='left',
             container: dict | None = None, valign='top', color=TEXT_COLOR, group_ids=None) -> dict:
        w, h = self.text_size(content, font_size)
        el = self.base('text', x, y, w, h, strokeColor=color, text=content, originalText=content,
                       fontSize=font_size, fontFamily=self.font, textAlign=align, verticalAlign=valign,
                       containerId=container['id'] if container else None, autoResize=True, lineHeight=1.25,
                       groupIds=list(group_ids or []))
        if container:
            container['boundElements'].append({'id': el['id'], 'type': 'text'})
        return el

    def shape(self, kind: str, x: float, y: float, w: float, h: float, color_name: str | None,
              group_ids=None, opacity=100, stroke_style='solid', stroke_width=2) -> dict:
        fill, stroke = self.color(color_name)
        kind = kind if kind in ('rectangle', 'ellipse', 'diamond') else 'rectangle'
        roundness = {'type': 3} if kind == 'rectangle' else ({'type': 2} if kind == 'diamond' else None)
        return self.base(kind, x, y, w, h, strokeColor=stroke, backgroundColor=fill, roundness=roundness,
                         groupIds=list(group_ids or []), opacity=opacity, strokeStyle=stroke_style,
                         strokeWidth=stroke_width)

    def node_box(self, node: dict, x: float, y: float, w: float, h: float, group_ids=None) -> dict:
        label = self.node_label(node)
        box = self.shape(node.get('shape', 'rectangle'), x, y, w, h, node.get('color'), group_ids)
        tw, th = self.text_size(label, NODE_FONT)
        self.text(x + (w - tw) / 2, y + (h - th) / 2, label, NODE_FONT, align='center', container=box,
                  valign='middle', group_ids=group_ids)
        return box

    @staticmethod
    def node_label(node: dict) -> str:
        label = str(node.get('label') or node.get('id'))
        note = node.get('note')
        return f'{label}\n{note}' if note else label

    def node_size(self, node: dict) -> tuple[float, float]:
        tw, th = self.text_size(self.node_label(node), NODE_FONT)
        shape = node.get('shape', 'rectangle')
        w = max(MIN_NODE_W, tw + 2 * PAD)
        h = th + 2 * PAD
        if shape == 'ellipse':
            w, h = w * 1.25, h * 1.4
        elif shape == 'diamond':
            w, h = w * 1.5, h * 1.8
        return math.ceil(w), math.ceil(h)

    def arrow(self, src: dict, dst: dict, edge: dict, direction: str):
        # Start-/Endpunkte an den zugewandten Seiten.
        if direction == 'right':
            sx, sy = src['x'] + src['width'], src['y'] + src['height'] / 2
            ex, ey = dst['x'], dst['y'] + dst['height'] / 2
        elif direction == 'radial':
            sx, sy = src['x'] + src['width'] / 2, src['y'] + src['height'] / 2
            ex, ey = dst['x'] + dst['width'] / 2, dst['y'] + dst['height'] / 2
            # auf Rand des Ziels kuerzen
            dx, dy = ex - sx, ey - sy
            dist = math.hypot(dx, dy) or 1
            sx, sy = sx + dx / dist * (src['width'] / 2), sy + dy / dist * (src['height'] / 2)
            ex, ey = ex - dx / dist * (dst['width'] / 2), ey - dy / dist * (dst['height'] / 2)
        else:
            sx, sy = src['x'] + src['width'] / 2, src['y'] + src['height']
            ex, ey = dst['x'] + dst['width'] / 2, dst['y']
        style = 'line' if edge.get('style') == 'line' else 'arrow'
        el = self.base('arrow', sx, sy, abs(ex - sx), abs(ey - sy),
                       strokeColor=self.color(edge.get('color')) [1] if edge.get('color') else TEXT_COLOR,
                       points=[[0, 0], [round(ex - sx, 1), round(ey - sy, 1)]], lastCommittedPoint=None,
                       startBinding={'elementId': src['id'], 'focus': 0, 'gap': 4},
                       endBinding={'elementId': dst['id'], 'focus': 0, 'gap': 4},
                       startArrowhead=None, endArrowhead='arrow' if style == 'arrow' else None,
                       elbowed=False, strokeStyle='dashed' if edge.get('dashed') else 'solid')
        src['boundElements'].append({'id': el['id'], 'type': 'arrow'})
        dst['boundElements'].append({'id': el['id'], 'type': 'arrow'})
        label = edge.get('label')
        if label:
            tw, th = self.text_size(str(label), NOTE_FONT)
            mx, my = (sx + ex) / 2, (sy + ey) / 2
            self.text(mx - tw / 2, my - th / 2, str(label), NOTE_FONT, align='center', container=el, valign='middle')
        return el

    def group_box(self, group: dict, members: list[dict]) -> dict | None:
        if not members:
            return None
        x0 = min(m['x'] for m in members) - GROUP_PAD
        y0 = min(m['y'] for m in members) - GROUP_PAD - GROUP_LABEL_H
        x1 = max(m['x'] + m['width'] for m in members) + GROUP_PAD
        y1 = max(m['y'] + m['height'] for m in members) + GROUP_PAD
        fill, stroke = self.color(group.get('color'))
        box = self.base('rectangle', x0, y0, x1 - x0, y1 - y0, strokeColor=stroke, backgroundColor=fill,
                        roundness={'type': 3}, opacity=35, strokeStyle='solid', strokeWidth=1)
        # Hintergrund muss hinter die Knoten: ans Anfang der Liste.
        self.elements.remove(box)
        self.elements.insert(0, box)
        label = str(group.get('label') or group.get('id'))
        self.text(x0 + 12, y0 + 6, label, NOTE_FONT + 2, color=stroke)
        return box

    def title(self, x: float, y: float) -> dict:
        return self.text(x, y, str(self.spec['title']), TITLE_FONT)

    def legend(self, x: float, y: float):
        items = self.spec.get('legend') or []
        for i, item in enumerate(items):
            fill, stroke = self.color(item.get('color'))
            yy = y + i * 30
            self.base('rectangle', x, yy, 22, 22, strokeColor=stroke, backgroundColor=fill, roundness={'type': 3}, strokeWidth=1)
            self.text(x + 32, yy - 1, str(item.get('label', '')), NOTE_FONT)

    # ---------- Layouts ----------
    def layout_layers(self):
        spec = self.spec
        nodes = spec.get('nodes') or []
        if not nodes:
            raise SystemExit('FEHLER: nodes fehlen.')
        ids = [n['id'] for n in nodes]
        if len(set(ids)) != len(ids):
            raise SystemExit('FEHLER: doppelte node ids.')
        by_id = {n['id']: n for n in nodes}
        edges = [e for e in (spec.get('edges') or []) if e.get('from') in by_id and e.get('to') in by_id]
        bad = [e for e in (spec.get('edges') or []) if e not in edges]
        if bad:
            raise SystemExit(f'FEHLER: edges mit unbekannten ids: {bad}')
        direction = spec.get('direction', 'down')

        # Schichten: laengster Pfad ab Wurzeln; Zyklen werden durch Reihenfolge aufgebrochen.
        layer = {i: 0 for i in ids}
        parents = {i: [] for i in ids}
        for e in edges:
            parents[e['to']].append(e['from'])
        order = list(ids)
        for _ in range(len(ids)):
            changed = False
            for i in order:
                for p in parents[i]:
                    if layer[p] + 1 > layer[i] and layer[p] + 1 < len(ids):
                        layer[i] = layer[p] + 1
                        changed = True
            if not changed:
                break
        layers: dict[int, list[str]] = {}
        for i in ids:
            layers.setdefault(layer[i], []).append(i)
        # Reihenfolge je Schicht: Gruppe, dann Schwerpunkt der Eltern.
        pos: dict[str, float] = {}
        for depth in sorted(layers):
            members = layers[depth]
            def key(i):
                ps = [pos[p] for p in parents[i] if p in pos]
                bary = sum(ps) / len(ps) if ps else ids.index(i)
                return (str(by_id[i].get('group') or '~'), bary, ids.index(i))
            members.sort(key=key)
            for k, i in enumerate(members):
                pos[i] = k

        sizes = {i: self.node_size(by_id[i]) for i in ids}
        boxes: dict[str, dict] = {}
        title_h = TITLE_FONT * 1.25 + 40
        if direction == 'right':
            # Schichten entlang x, Knoten je Schicht entlang y.
            layer_w = {d: max(sizes[i][0] for i in m) for d, m in layers.items()}
            max_total_h = max(sum(sizes[i][1] for i in m) + NODE_GAP * (len(m) - 1) for m in layers.values())
            x = 0
            for d in sorted(layers):
                m = layers[d]
                total_h = sum(sizes[i][1] for i in m) + NODE_GAP * (len(m) - 1)
                y = title_h + (max_total_h - total_h) / 2
                for i in m:
                    w, h = sizes[i]
                    boxes[i] = (x + (layer_w[d] - w) / 2, y, w, h)
                    y += h + NODE_GAP
                x += layer_w[d] + LAYER_GAP * 1.4
        else:
            layer_h = {d: max(sizes[i][1] for i in m) for d, m in layers.items()}
            max_total_w = max(sum(sizes[i][0] for i in m) + NODE_GAP * (len(m) - 1) for m in layers.values())
            y = title_h
            for d in sorted(layers):
                m = layers[d]
                total_w = sum(sizes[i][0] for i in m) + NODE_GAP * (len(m) - 1)
                x = (max_total_w - total_w) / 2
                for i in m:
                    w, h = sizes[i]
                    boxes[i] = (x, y + (layer_h[d] - h) / 2, w, h)
                    x += w + NODE_GAP
                y += layer_h[d] + LAYER_GAP
        self.render_graph(by_id, edges, boxes, direction)

    def render_graph(self, by_id: dict, edges: list, boxes: dict, direction: str):
        groups = {g['id']: g for g in (self.spec.get('groups') or [])}
        group_ids = {gid: self.new_id() for gid in groups}
        els: dict[str, dict] = {}
        for i, (x, y, w, h) in boxes.items():
            g = by_id[i].get('group')
            if g and g not in groups:
                raise SystemExit(f'FEHLER: node {i} nennt unbekannte group {g}')
            els[i] = self.node_box(by_id[i], x, y, w, h, [group_ids[g]] if g else None)
        for e in edges:
            self.arrow(els[e['from']], els[e['to']], e, direction)
        for gid, g in groups.items():
            members = [els[i] for i in els if by_id[i].get('group') == gid]
            self.group_box(g, members)
        self.finish()

    def layout_cheatsheet(self):
        cards = self.spec.get('cards') or []
        if not cards:
            raise SystemExit('FEHLER: cards fehlen (kind: cheatsheet).')
        n = len(cards)
        cols = 2 if n <= 4 else (3 if n <= 9 else 4)
        title_h = TITLE_FONT * 1.25 + 40
        # Kartenhoehen berechnen
        prepared = []
        for c in cards:
            lines = [re.sub(r'`', '', str(l)) for l in (c.get('lines') or [])]
            body = '\n'.join(lines)
            _, bh = self.text_size(body or ' ', CARD_BODY_FONT)
            h = PAD + CARD_TITLE_FONT * 1.25 + 10 + bh + PAD
            prepared.append((c, body, h))
        # Zeilenweise anordnen, Zeilenhoehe = max der Zeile
        row_h = []
        for r in range(0, n, cols):
            row_h.append(max(h for _, _, h in prepared[r:r + cols]))
        for idx, (c, body, h) in enumerate(prepared):
            r, col = divmod(idx, cols)
            x = col * (CARD_W + CARD_GAP)
            y = title_h + sum(row_h[:r]) + r * CARD_GAP
            gid = self.new_id()
            fill, stroke = self.color(c.get('color'))
            box = self.base('rectangle', x, y, CARD_W, row_h[r], strokeColor=stroke, backgroundColor=fill,
                            roundness={'type': 3}, groupIds=[gid], strokeWidth=1)
            self.text(x + PAD, y + PAD, str(c.get('title', '')), CARD_TITLE_FONT, color=stroke, group_ids=[gid])
            # Trennlinie
            ly = y + PAD + CARD_TITLE_FONT * 1.25 + 4
            line = self.base('line', x + PAD, ly, CARD_W - 2 * PAD, 0, strokeColor=stroke, strokeWidth=1,
                             points=[[0, 0], [CARD_W - 2 * PAD, 0]], lastCommittedPoint=None,
                             startBinding=None, endBinding=None, startArrowhead=None, endArrowhead=None,
                             groupIds=[gid])
            if body:
                self.text(x + PAD, ly + 10, body, CARD_BODY_FONT, group_ids=[gid])
        self.finish()

    def layout_overview(self):
        spec = self.spec
        nodes = spec.get('nodes') or []
        groups = spec.get('groups') or []
        if not nodes and not groups:
            raise SystemExit('FEHLER: overview braucht groups und/oder nodes.')
        by_id = {n['id']: n for n in nodes}
        # Cluster: jede Gruppe; ungruppierte Knoten bilden je einen eigenen Cluster.
        clusters = []
        for g in groups:
            members = [n for n in nodes if n.get('group') == g['id']]
            clusters.append((g, members))
        for n in nodes:
            if not n.get('group'):
                clusters.append(({'id': n['id'], 'label': None, 'color': n.get('color')}, [n]))
        # Clustergroessen
        sizes = []
        for g, members in clusters:
            ws = [self.node_size(m)[0] for m in members] or [MIN_NODE_W]
            hs = [self.node_size(m)[1] for m in members] or [0]
            w = max(ws) + 2 * GROUP_PAD
            h = sum(hs) + NODE_GAP * 0.5 * max(0, len(members) - 1) + 2 * GROUP_PAD + (GROUP_LABEL_H if g.get('label') else 0)
            sizes.append((w, h))
        title = str(spec['title'])
        tw, th = self.text_size(title, TITLE_FONT)
        cw, ch = tw + 2 * PAD * 2, th + 2 * PAD * 1.5
        k = len(clusters)
        max_w = max(w for w, _ in sizes)
        max_h = max(h for _, h in sizes)
        rx = cw / 2 + max_w / 2 + 120 + (k - 4) * 25 if k > 4 else cw / 2 + max_w / 2 + 120
        ry = ch / 2 + max_h / 2 + 90 + (k - 4) * 25 if k > 4 else ch / 2 + max_h / 2 + 90
        cx, cy = rx + max_w, ry + max_h
        center = self.shape('ellipse', cx - cw / 2, cy - ch / 2, cw, ch, spec.get('color', 'yellow'))
        self.text(cx - tw / 2, cy - th / 2, title, TITLE_FONT, align='center', container=center, valign='middle')
        els: dict[str, dict] = {}
        for idx, ((g, members), (w, h)) in enumerate(zip(clusters, sizes)):
            ang = -math.pi / 2 + idx * 2 * math.pi / k
            gx, gy = cx + rx * math.cos(ang) - w / 2, cy + ry * math.sin(ang) - h / 2
            gid = self.new_id()
            fill, stroke = self.color(g.get('color'))
            box = self.base('rectangle', gx, gy, w, h, strokeColor=stroke, backgroundColor=fill, roundness={'type': 3},
                            opacity=35, strokeWidth=1)
            self.elements.remove(box)
            self.elements.insert(0, box)
            y = gy + GROUP_PAD
            if g.get('label'):
                self.text(gx + 12, gy + 6, str(g['label']), NOTE_FONT + 2, color=stroke)
                y += GROUP_LABEL_H
            for m in members:
                nw, nh = self.node_size(m)
                els[m['id']] = self.node_box(m, gx + (w - nw) / 2, y, nw, nh, [gid])
                y += nh + NODE_GAP * 0.5
            # Verbindungslinie Zentrum -> Cluster
            self.arrow(center, box, {'style': 'line'}, 'radial')
        for e in spec.get('edges') or []:
            if e.get('from') in els and e.get('to') in els:
                self.arrow(els[e['from']], els[e['to']], e, 'radial')
        self.finish(with_title=False)

    def finish(self, with_title: bool = True):
        xs = [e['x'] for e in self.elements] or [0]
        ys = [e['y'] for e in self.elements] or [0]
        x0, y0 = min(xs), min(ys)
        if with_title:
            self.title(x0, y0 - TITLE_FONT * 1.25 - 40 if y0 >= 0 else y0)
        ys2 = [e['y'] + e['height'] for e in self.elements]
        if self.spec.get('legend'):
            self.legend(x0, max(ys2) + 40)

    # ---------- Ausgabe ----------
    def build(self) -> dict:
        kind = self.spec.get('kind', 'structure')
        if kind in ('structure', 'flow'):
            if kind == 'flow' and 'direction' not in self.spec:
                self.spec['direction'] = 'right'
            self.layout_layers()
        elif kind == 'cheatsheet':
            self.layout_cheatsheet()
        elif kind == 'overview':
            self.layout_overview()
        else:
            raise SystemExit(f'FEHLER: unbekannte kind: {kind}')
        return {
            'type': 'excalidraw',
            'version': 2,
            'source': 'obsidian-wiki excalidraw_build.py',
            'elements': self.elements,
            'appState': {'theme': 'light', 'viewBackgroundColor': '#ffffff', 'currentItemStrokeColor': TEXT_COLOR,
                         'currentItemFontFamily': self.font, 'gridSize': None},
            'files': {},
        }


def to_markdown(scene: dict, spec: dict) -> str:
    text_elements = []
    for el in scene['elements']:
        if el['type'] == 'text':
            text_elements.append(f"{el['text']} ^{el['id']}")
    body = '\n\n'.join(text_elements)
    return (
        '---\n'
        'excalidraw-plugin: parsed\n'
        'generated_by: excalidraw_build\n'
        'tags: [excalidraw]\n'
        '---\n'
        '==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== '
        "You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. "
        "For more info check in plugin settings under 'Saving'\n\n\n"
        '# Excalidraw Data\n\n'
        '## Text Elements\n'
        f'{body}\n\n'
        '%%\n'
        '## Drawing\n'
        '```json\n'
        f'{json.dumps(scene, ensure_ascii=False)}\n'
        '```\n'
        '%%'
    )


def validate_file(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    m = re.search(r'## Drawing\s*```json\s*(\{.*\})\s*```', text, flags=re.S)
    if not m:
        m = re.search(r'# Drawing\s*```json\s*(\{.*\})\s*```', text, flags=re.S)
    if not m:
        m = re.search(r'```compressed-json', text)
        if m:
            print('HINWEIS: Zeichnung ist komprimiert gespeichert (Plugin-Format); strukturelle Pruefung nicht moeglich.')
            return 0
        print('FEHLER: kein Drawing-JSON gefunden.')
        return 1
    try:
        scene = json.loads(m.group(1))
    except Exception as exc:
        print(f'FEHLER: JSON nicht parsebar: {exc}')
        return 1
    els = scene.get('elements', [])
    ids = [e.get('id') for e in els]
    errors = []
    if len(ids) != len(set(ids)):
        errors.append('doppelte Element-IDs')
    known = set(ids)
    for e in els:
        for b in e.get('boundElements') or []:
            if b.get('id') not in known:
                errors.append(f"boundElements von {e.get('id')} zeigt auf unbekannte ID {b.get('id')}")
        if e.get('type') == 'text' and e.get('containerId') and e['containerId'] not in known:
            errors.append(f"Text {e.get('id')} hat unbekannten containerId {e['containerId']}")
        for key in ('startBinding', 'endBinding'):
            b = e.get(key)
            if b and b.get('elementId') not in known:
                errors.append(f"{key} von {e.get('id')} zeigt auf unbekannte ID {b.get('elementId')}")
    text_ids = set(re.findall(r'\^([A-Za-z0-9]{8})\s*$', text, flags=re.M))
    for e in els:
        if e.get('type') == 'text' and e['id'] not in text_ids:
            errors.append(f"Text-Element {e['id']} fehlt im Abschnitt Text Elements")
    for err in errors:
        print('FEHLER: ' + err)
    if not errors:
        print(f'OK: {len(els)} Elemente, Struktur konsistent.')
    return 1 if errors else 0


EXAMPLES = {
    'structure': {
        'title': 'CSS Layout: Ueberblick', 'kind': 'structure',
        'groups': [{'id': 'modern', 'label': 'Moderne Verfahren', 'color': 'green'}],
        'nodes': [
            {'id': 'layout', 'label': 'CSS Layout', 'shape': 'ellipse', 'color': 'yellow'},
            {'id': 'flow', 'label': 'Normal Flow', 'color': 'gray', 'note': 'Block und Inline'},
            {'id': 'flex', 'label': 'Flexbox', 'color': 'green', 'group': 'modern', 'note': 'eindimensional'},
            {'id': 'grid', 'label': 'CSS Grid', 'color': 'green', 'group': 'modern', 'note': 'zweidimensional'},
            {'id': 'pos', 'label': 'Positioning', 'color': 'blue'},
            {'id': 'cq', 'label': 'Container Queries', 'color': 'violet'},
        ],
        'edges': [
            {'from': 'layout', 'to': 'flow'}, {'from': 'layout', 'to': 'flex'}, {'from': 'layout', 'to': 'grid'},
            {'from': 'layout', 'to': 'pos'}, {'from': 'grid', 'to': 'cq', 'label': 'reagiert auf', 'dashed': True},
            {'from': 'flex', 'to': 'cq', 'dashed': True},
        ],
        'legend': [{'color': 'green', 'label': 'Standard heute'}, {'color': 'violet', 'label': 'neuere Ergaenzung'}],
    },
    'flow': {
        'title': 'Inbox-Workflow', 'kind': 'flow',
        'nodes': [
            {'id': 'in', 'label': 'Rohmaterial\nin 00 Inbox', 'color': 'gray'},
            {'id': 'check', 'label': 'Bestehendes\nWissen suchen', 'shape': 'diamond', 'color': 'yellow'},
            {'id': 'res', 'label': 'Resource\nanlegen', 'color': 'blue'},
            {'id': 'wiki', 'label': 'Wiki-Notiz\nergaenzen', 'color': 'green'},
            {'id': 'arch', 'label': 'Rohnotiz\narchivieren', 'color': 'gray'},
        ],
        'edges': [
            {'from': 'in', 'to': 'check'}, {'from': 'check', 'to': 'res', 'label': 'externe Quelle'},
            {'from': 'check', 'to': 'wiki', 'label': 'eigenes Wissen'}, {'from': 'res', 'to': 'arch'}, {'from': 'wiki', 'to': 'arch'},
        ],
    },
    'cheatsheet': {
        'title': 'Git Cheatsheet', 'kind': 'cheatsheet',
        'cards': [
            {'title': 'Status und Verlauf', 'color': 'blue', 'lines': ['git status', 'git log --oneline', 'git diff']},
            {'title': 'Aendern', 'color': 'green', 'lines': ['git add -p', 'git commit -m "..."', 'git restore <datei>']},
            {'title': 'Branches', 'color': 'violet', 'lines': ['git switch -c <name>', 'git merge <name>', 'git branch -d <name>']},
            {'title': 'Remote', 'color': 'orange', 'lines': ['git fetch', 'git pull --rebase', 'git push -u origin <name>']},
        ],
    },
    'overview': {
        'title': 'Webentwicklung', 'kind': 'overview', 'color': 'yellow',
        'groups': [
            {'id': 'front', 'label': 'Frontend', 'color': 'blue'},
            {'id': 'design', 'label': 'Design', 'color': 'pink'},
            {'id': 'tools', 'label': 'Werkzeuge', 'color': 'gray'},
            {'id': 'quality', 'label': 'Qualitaet', 'color': 'green'},
        ],
        'nodes': [
            {'id': 'html', 'label': 'HTML', 'group': 'front', 'color': 'blue'},
            {'id': 'css', 'label': 'CSS', 'group': 'front', 'color': 'blue'},
            {'id': 'js', 'label': 'JavaScript', 'group': 'front', 'color': 'blue'},
            {'id': 'typo', 'label': 'Typografie', 'group': 'design', 'color': 'pink'},
            {'id': 'color', 'label': 'Farbe', 'group': 'design', 'color': 'pink'},
            {'id': 'git', 'label': 'Git', 'group': 'tools', 'color': 'gray'},
            {'id': 'a11y', 'label': 'Accessibility', 'group': 'quality', 'color': 'green'},
            {'id': 'perf', 'label': 'Performance', 'group': 'quality', 'color': 'green'},
        ],
    },
}


def safe_name(title: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '', title).strip().rstrip('. ')
    return name or 'Zeichnung'


def main():
    ap = argparse.ArgumentParser(description='Excalidraw-Zeichnung aus Spezifikation bauen')
    ap.add_argument('spec', nargs='?', help='Pfad zur Spezifikation (JSON)')
    ap.add_argument('--out', help='Zieldatei .excalidraw.md; Standard: <drawing_root>/<Titel>.excalidraw.md')
    ap.add_argument('--force', action='store_true', help='generierte Datei ueberschreiben')
    ap.add_argument('--validate', help='vorhandene .excalidraw.md strukturell pruefen')
    ap.add_argument('--example', choices=sorted(EXAMPLES), help='Beispiel-Spezifikation ausgeben')
    ap.add_argument('--root', default=None, help='Vault-Wurzel; Standard: Projektwurzel')
    args = ap.parse_args()

    if args.example:
        print(json.dumps(EXAMPLES[args.example], ensure_ascii=False, indent=2))
        return 0
    if args.validate:
        return validate_file(Path(args.validate))
    if not args.spec:
        ap.print_help()
        return 2

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[2]
    try:
        spec = json.loads(Path(args.spec).read_text(encoding='utf-8'))
    except Exception as exc:
        raise SystemExit(f'FEHLER: Spezifikation nicht lesbar: {exc}')
    if not spec.get('title'):
        raise SystemExit('FEHLER: title fehlt in der Spezifikation.')

    if args.out:
        out = Path(args.out)
        if not out.is_absolute():
            out = root / out
    else:
        drawing_root = '99 Assets/Excalidraw'
        try:
            schema = json.loads((root / '90 Meta/Taxonomy/vault-schema.json').read_text(encoding='utf-8'))
            drawing_root = schema.get('drawing_root', drawing_root)
        except Exception:
            pass
        out = root / drawing_root / f'{safe_name(spec["title"])}.excalidraw.md'
    if not out.name.lower().endswith('.excalidraw.md'):
        raise SystemExit('FEHLER: Zieldatei muss auf .excalidraw.md enden.')
    if out.exists():
        head = out.read_text(encoding='utf-8', errors='replace')[:400]
        if 'generated_by: excalidraw_build' not in head:
            raise SystemExit(f'FEHLER: {out} wurde nicht von diesem Skript erzeugt (oder im Plugin bearbeitet). Nicht ueberschrieben.')
        if not args.force:
            raise SystemExit(f'FEHLER: {out} existiert. Mit --force ueberschreiben (Handbearbeitungen gehen verloren).')

    scene = Builder(spec).build()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(to_markdown(scene, spec), encoding='utf-8')
    spec_path = out.with_name(out.name[:-len('.excalidraw.md')] + '.excalidraw.spec.json')
    spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Zeichnung geschrieben: {out}')
    print(f'Spezifikation gesichert: {spec_path}')
    print(f'Einbetten mit: ![[{out.name[:-3]}]]')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
