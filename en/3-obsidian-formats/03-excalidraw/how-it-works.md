---
title: How an Excalidraw file is built
description: Markdown outside, drawing data inside — and the second, simpler way.
section: Obsidian formats
tags:
  - obsidian-formats
  - excalidraw

---

## The Obsidian format: `.excalidraw.md`

An ordinary [[en/7-reference/01-glossary#Markdown|Markdown]] file with four parts:

````md
---
excalidraw-plugin: parsed
tags: [excalidraw]
---

⚠ Notice for readers without the plugin

# Excalidraw Data

## Text Elements
The text of every text element, with a block identifier ^abc123

## Drawing
```json
{ "type": "excalidraw", "version": 2, "elements": [...] }
```
````

The text elements are there twice: once readable under `## Text Elements`, once in the JSON. That
is how Obsidian's search finds the text inside a drawing.

The JSON can also be **compressed** (`compressed-json`, LZ-String) — Obsidian sets that in the
[[en/7-reference/01-glossary#Plugin|plugin]] options. Quartz reads both; uncompressed versions better, because [[en/7-reference/01-glossary#git|git]] can show the changes.

## The second way: `.excalidraw`

Plain JSON without the Markdown shell. The Quartz plugin reads it just the same. Anyone generating
a drawing programmatically has an easier time with it.

## How the drawing here came about

Not by hand: a script [[en/7-reference/01-glossary#Build|builds]] it from a small specification that only describes content — nodes,
groups, edges, colours. Layout, geometry and the internal identifiers are calculated by the script.

```json
{
  "title": "Structure of the editorial frame",
  "kind": "structure",
  "groups": [{ "id": "left", "label": "Left column", "color": "teal" }],
  "nodes": [{ "id": "explorer", "label": "Explorer", "color": "teal", "group": "left" }],
  "edges": [{ "from": "frame", "to": "explorer" }]
}
```

The specification sits next to the drawing under `assets/Excalidraw/`. Anyone wanting to change the
drawing changes the specification and rebuilds — or opens it in Obsidian and carries on drawing.
