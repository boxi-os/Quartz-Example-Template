---
title: Emphasis
description: Bold, italic, struck through, highlighted — and which plugin delivers which of them.
section: Formatting
tags:
  - formatting
  - text
translationKey: formatierung/text/betonung
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## The five kinds of markup

```md
*italic* or _italic_
**bold** or __bold__
***bold and italic***
~~struck through~~
==highlighted==
```

*italic* or _italic_
**bold** or __bold__
***bold and italic***
~~struck through~~
==highlighted==

## Which comes from where

Two of the five do not come from Markdown itself:

| Markup | Comes from | Without the plugin |
| --- | --- | --- |
| `~~struck through~~` | GitHub Flavored Markdown | stays as raw text |
| `==highlighted==` | Obsidian Flavored Markdown | stays as raw text |

Both are active in this template. The highlight takes the colour `textHighlight` from the palette —
see [[en/design/in-the-content/body-text|Body text]].

## Inside a word

```md
A word with **inner** emphasis, and an under_score_ in the middle of a word.
```

A word with **inner** emphasis, and an under_score_ in the middle of a word.

The underscore inside a word is deliberately *not* read as italics — otherwise
`snake_case_names` would fall apart all the time.

## Superscript and subscript

Markdown knows neither; Quartz lets HTML through:

```md
H<sub>2</sub>O and E = mc<sup>2</sup>
```

H<sub>2</sub>O and E = mc<sup>2</sup>
