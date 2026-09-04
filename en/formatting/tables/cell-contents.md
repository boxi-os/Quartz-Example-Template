---
title: Contents of a cell
description: What may stand in a cell and what has to be escaped.
section: Formatting
tags:
  - formatting
  - tables
translationKey: formatierung/tabellen/inhalte
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
| Element | Example |
| ------- | -------- |
| Emphasis | **bold**, *italic* |
| Code | `const x = 1` |
| Link | [[en/formatting/index\|Formatting]] |
| Line break | first line<br>second line |
```

| Element | Example |
| ------- | -------- |
| Emphasis | **bold**, *italic* |
| Code | `const x = 1` |
| Link | [[en/formatting/index\|Formatting]] |
| Line break | first line<br>second line |

## The vertical bar

A `|` in a cell ends the column. It has to be escaped as `\|` — **inside a wikilink too**, where
the bar otherwise separates target from text:

```md
| [[en/formatting/index\|Formatting]] |
```

That is the most common stumbling block for tables in Obsidian.
