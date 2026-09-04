---
title: Wie eine Excalidraw-Datei aufgebaut ist
description: Markdown außen, Zeichendaten innen — und der zweite, einfachere Weg.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - excalidraw
---

## Das Obsidian-Format: `.excalidraw.md`

Eine gewöhnliche Markdown-Datei mit vier Teilen:

````md
---
excalidraw-plugin: parsed
tags: [excalidraw]
---

⚠ Hinweis für Leser ohne Plugin

# Excalidraw Data

## Text Elements
Der Text jedes Textelements, mit Blockkennung ^abc123

## Drawing
```json
{ "type": "excalidraw", "version": 2, "elements": [...] }
```
````

Die Textelemente stehen doppelt: einmal lesbar unter `## Text Elements`, einmal im JSON. So findet
Obsidians Suche den Text in einer Zeichnung.

Das JSON kann auch **komprimiert** vorliegen (`compressed-json`, LZ-String) — Obsidian stellt das in
den Plugin-Einstellungen ein. Beides wird von Quartz gelesen; unkomprimiert ist besser
versionierbar, weil git die Änderungen zeigen kann.

## Der zweite Weg: `.excalidraw`

Reines JSON ohne Markdown-Hülle. Das Quartz-Plugin liest es genauso. Wer eine Zeichnung
programmatisch erzeugt, hat es damit einfacher.

## Wie die Zeichnung hier entstanden ist

Nicht von Hand: Ein Skript baut sie aus einer kleinen Spezifikation, die nur Inhalt beschreibt —
Knoten, Gruppen, Kanten, Farben. Layout, Geometrie und die internen Kennungen berechnet das Skript.

```json
{
  "title": "Aufbau des editorial-Frames",
  "kind": "structure",
  "groups": [{ "id": "links", "label": "Linke Spalte", "color": "teal" }],
  "nodes": [{ "id": "explorer", "label": "Explorer", "color": "teal", "group": "links" }],
  "edges": [{ "from": "frame", "to": "explorer" }]
}
```

Die Spezifikation liegt neben der Zeichnung unter `assets/Excalidraw/`. Wer die Zeichnung ändern
will, ändert die Spezifikation und baut neu — oder öffnet sie in Obsidian und zeichnet weiter.
