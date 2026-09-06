---
title: Emphasis
description: Bold, italic, struck through, highlighted — and which plugin delivers which of them.
section: Formatting
tags:
  - formatting
  - text
translationKey: formatierung/text/betonung
cover: "[[assets/covers/cover-text.svg]]"
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

Two of the five do not come from [[en/7-reference/01-glossary#Markdown|Markdown]] itself:

| Markup | Comes from | Without the [[en/7-reference/01-glossary#Plugin\|plugin]] |
| --- | --- | --- |
| `~~struck through~~` | GitHub Flavored Markdown | stays as raw text |
| `==highlighted==` | Obsidian Flavored Markdown | stays as raw text |

Both are active in this template. The highlight takes the colour `textHighlight` from the palette —
see [[en/5-design/03-in-the-content/body-text|Body text]].

## Inside a word

```md
A word with **inner** emphasis, and an under_score_ in the middle of a word.
```

A word with **inner** emphasis, and an under_score_ in the middle of a word.

The underscore inside a word is deliberately *not* read as italics — otherwise
`snake_case_names` would fall apart all the time.

## Superscript and subscript

Markdown knows neither; Quartz lets [[en/7-reference/01-glossary#HTML|HTML]] through:

```md
H<sub>2</sub>O and E = mc<sup>2</sup>
```

H<sub>2</sub>O and E = mc<sup>2</sup>
