---
title: Wie ein Canvas aufgebaut ist
description: JSON mit Knoten und Kanten.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - canvas
---

Eine `.canvas`-Datei ist JSON mit genau zwei Listen:

```json
{
  "nodes": [
    {
      "id": "a1",
      "type": "text",
      "text": "## Eine Karte\n\nMit Markdown darin.",
      "x": 0, "y": 0, "width": 320, "height": 160,
      "color": "4"
    }
  ],
  "edges": [
    { "id": "e1", "fromNode": "a1", "fromSide": "right", "toNode": "b2", "toSide": "left" }
  ]
}
```

## Knotenarten

| `type` | Inhalt | Zusätzliche Felder |
| --- | --- | --- |
| `text` | Markdown direkt in der Karte | `text` |
| `file` | eine Notiz aus dem Vault | `file`, optional `subpath` |
| `link` | eine Webseite als eingebettete Ansicht | `url` |
| `group` | ein beschrifteter Rahmen um andere Karten | `label` |

## Geometrie und Farbe

`x` und `y` sind die Koordinaten der linken oberen Ecke — negative Werte sind normal, der Ursprung
liegt irgendwo in der Mitte. `width` und `height` in Pixeln.

`color` ist entweder eine Ziffer von `"1"` bis `"6"` (Obsidians Palette: rot, orange, gelb, grün,
cyan, lila) oder ein Hex-Wert.

## Kanten

Eine Kante verbindet zwei Knoten und benennt die Seiten, an denen sie andockt: `top`, `right`,
`bottom`, `left`. Optional mit `label`, `color` und Pfeilspitzen über `fromEnd`/`toEnd`.

## Von Hand oder in Obsidian

Das Format ist einfach genug, um es zu schreiben — aber das Anordnen von Hand ist mühsam. In
Obsidian zieht man die Karten; die Datei wird dabei gepflegt.


## Verlinken

Ein Wikilink auf eine solche Datei braucht die **Endung**:

```md
[[obsidian-formate/bases/Formatierungsseiten.base|Formatierungsseiten]]
[[obsidian-formate/canvas/Aufbau der Vorlage.canvas|Aufbau der Vorlage]]
```

Quartz behält die Endung im Adressteil der Seite (`…/formatierungsseiten.base`), anders als bei
Markdown-Dateien. Ohne sie geht der Link ins Leere — und das fällt nicht auf, weil ein
unaufgelöster Wikilink hier keine besondere Auszeichnung bekommt.
