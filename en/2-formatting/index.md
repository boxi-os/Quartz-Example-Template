---
title: 2 Formatting
description: Every element Obsidian writes and Quartz renders — source and result side by side, 62 short pages in thirteen sections.
section: Formatting
tags:
  - formatting
translationKey: formatierung/index
cover: "[[assets/covers/cover-index.svg]]"
---

Notes in Obsidian are **Markdown**: text with a few characters in it that carry meaning — two
asterisks for bold, a hash for a heading, square brackets for a link. Quartz reads these
characters and makes the page from them. This chapter shows every element you can write this way
on a short page of its own: first the source in a code block, directly below it what the site
makes of it.

> [!tip] For copying
> The box at the top of every page is exactly what you type in Obsidian. Whoever wants to rebuild
> an element copies it — and compares the result with the one below.

## The thirteen sections

| Section | What is in it |
| --- | --- |
| [[en/2-formatting/01-text/index\|2.1 Text]] | bold, italic, strikethrough, highlighted, special characters, line breaks |
| [[en/2-formatting/02-structure/index\|2.2 Structure]] | headings, paragraphs, horizontal rules |
| [[en/2-formatting/03-lists/index\|2.3 Lists]] | unordered, ordered, tasks, nesting |
| [[en/2-formatting/04-links/index\|2.4 Links]] | [[en/7-reference/01-glossary#Wikilink\|wikilinks]], jump targets, external links, [[en/7-reference/01-glossary#Alias\|aliases]], embeds |
| [[en/2-formatting/05-callouts/index\|2.5 Callouts]] | all thirteen types, foldable, nested |
| [[en/2-formatting/06-code/index\|2.6 Code]] | inline, blocks, languages, line highlighting |
| [[en/2-formatting/07-tables/index\|2.7 Tables]] | basic form, alignment, cell contents, wide tables |
| [[en/2-formatting/08-math/index\|2.8 Mathematics]] | formulas inline and as a block |
| [[en/2-formatting/09-diagrams/index\|2.9 Diagrams]] | [[en/7-reference/01-glossary#Mermaid\|Mermaid]]: fourteen kinds of diagram on six pages |
| [[en/2-formatting/10-footnotes/index\|2.10 Footnotes]] | footnotes, variants, comments |
| [[en/2-formatting/11-properties/index\|2.11 Properties]] | [[en/7-reference/01-glossary#Frontmatter\|frontmatter]], data types, display |
| [[en/2-formatting/12-media/index\|2.12 Media]] | images, sizes, video, audio, documents, embeds |
| [[en/2-formatting/13-special/index\|2.13 Odds and ends]] | [[en/7-reference/01-glossary#HTML\|HTML]], escapes, arrows, emoji |

What is **not** a Markdown page — [[en/7-reference/01-glossary#Base|bases]], [[en/7-reference/01-glossary#Canvas|canvas]] and [[en/7-reference/01-glossary#Excalidraw|Excalidraw]] — stands in
[[en/3-obsidian-formats/index|3 Obsidian formats]]. What a page's frontmatter *does* — draft,
date, alias, cover image — stands in [[en/4-controlling-a-page/index|4 Controlling a page]].

## What Obsidian can do and Quartz cannot

Obsidian and Quartz speak almost the same language, but not quite. These deviations were measured
on the built site; the linked page shows in each case what works instead.

| In Obsidian | On the site | Where it stands |
| --- | --- | --- |
| Tasks with intermediate states (`[/]`, `[-]`, `[?]`) | only open and done; any other character becomes an empty box | [[en/2-formatting/03-lists/tasks\|Task lists]] |
| Inline footnote `^[text]` | stays as raw text | [[en/2-formatting/10-footnotes/variants\|Named and repeated footnotes]] |
| Arrows like `-->` become → | stay raw text; with *GitHub flavored markdown* they turn into `—>` | [[en/2-formatting/13-special/arrows-and-emoji\|Arrows, tags and emoji]] |
| A tag in running text | its link leads out of the site — a bug in Quartz | [[en/2-formatting/13-special/arrows-and-emoji\|Arrows, tags and emoji]] |
| Image with a size *and* an alt text | only one of the two | [[en/2-formatting/12-media/images\|Images]] |
| Embedded PDF from page 2 | always starts on page 1 | [[en/2-formatting/12-media/documents\|Documents]] |
| Definition lists | exist in neither; HTML steps in | [[en/2-formatting/13-special/html\|HTML in Markdown]] |

On top of that comes what deliberately looks different on this site than in Quartz out of the box
— the [[en/7-reference/01-glossary#Callout|callout]] colours, for instance. That does not stand here but in
[[en/5-design/index|5 The design]] with the component in question.
