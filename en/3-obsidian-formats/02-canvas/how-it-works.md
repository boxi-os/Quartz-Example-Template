---
title: How a canvas is built
description: JSON with nodes and edges.
section: Obsidian formats
tags:
  - obsidian-formats
  - canvas

---

A `.canvas` file is JSON with exactly two lists:

```json
{
  "nodes": [
    {
      "id": "a1",
      "type": "text",
      "text": "## A card\n\nWith Markdown in it.",
      "x": 0, "y": 0, "width": 320, "height": 160,
      "color": "4"
    }
  ],
  "edges": [
    { "id": "e1", "fromNode": "a1", "fromSide": "right", "toNode": "b2", "toSide": "left" }
  ]
}
```

## Kinds of node

| `type` | Content | Additional fields |
| --- | --- | --- |
| `text` | [[en/7-reference/01-glossary#Markdown\|Markdown]] directly in the card | `text` |
| `file` | a note from the [[en/7-reference/01-glossary#Vault\|vault]] | `file`, optionally `subpath` |
| `link` | a web page as an embedded view | `url` |
| `group` | a labelled [[en/7-reference/01-glossary#Frame\|frame]] around other cards | `label` |

## Geometry and colour

`x` and `y` are the coordinates of the top left corner — negative values are normal, the origin
lies somewhere in the middle. `width` and `height` in pixels.

`color` is either a digit from `"1"` to `"6"` (Obsidian's palette: red, orange, yellow, green,
cyan, purple) or a hex value.

## Edges

An edge connects two nodes and names the sides it docks to: `top`, `right`, `bottom`, `left`.
Optionally with `label`, `color` and arrowheads through `fromEnd`/`toEnd`.

## By hand or in Obsidian

The format is simple enough to write — but arranging by hand is tedious. In Obsidian you drag the
cards; the file is kept up to date while you do.

## Linking to one

A [[en/7-reference/01-glossary#Wikilink|wikilink]] to such a file needs the **extension**:

```md
[[en/3-obsidian-formats/01-bases/Formatting-Pages.base|Formatting pages]]
[[en/3-obsidian-formats/02-canvas/Structure of the template.canvas|Structure of the template]]
```

Quartz keeps the extension in the address of the page (`…/formatting-pages.base`), unlike with
Markdown files. Without it the link leads nowhere — and that does not stand out, because an
unresolved wikilink gets no special marking here.
