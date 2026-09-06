---
title: Contents of a cell
description: What may stand in a cell and what has to be escaped.
section: 2 Formatting
tags:
  - formatting
  - tables
translationKey: formatierung/tabellen/inhalte
cover: "[[assets/covers/cover-tabellen.svg]]"
---

```md
| Element | Example |
| ------- | -------- |
| Emphasis | **bold**, *italic* |
| Code | `const x = 1` |
| Link | [[en/2-formatting/index\|Formatting]] |
| Line break | first line<br>second line |
```

| Element | Example |
| ------- | -------- |
| Emphasis | **bold**, *italic* |
| Code | `const x = 1` |
| Link | [[en/2-formatting/index\|Formatting]] |
| Line break | first line<br>second line |

## The vertical bar

A `|` in a cell ends the column. It has to be escaped as `\|` — **inside a [[en/7-reference/01-glossary#Wikilink|wikilink]] too**, where
the bar otherwise separates target from text:

```md
| [[en/2-formatting/index\|Formatting]] |
```

That is the most common stumbling block for tables in Obsidian.
