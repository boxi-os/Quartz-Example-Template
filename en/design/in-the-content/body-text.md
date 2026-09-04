---
title: Body text
description: The width of the text, the heading scale and the links inside it.
section: Design
tags:
  - design
  - in-the-content
translationKey: gestaltung/im-inhalt/fliesstext
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## The width of the text

**In this template** the page grid decides how wide the text gets — not a rule on the paragraph.
The frame gives the content six of twelve columns, which is 690 px on a page capped at 1440 px — at
a font size of 1 rem, about 72 characters.

**Out of the box** Quartz does the same, only with different numbers: it caps the page through
`.page { max-width }`.

> [!note] What once stood here
> An earlier version additionally capped the body text at 68 characters. That is common advice, but
> it means two places answer the same question — the column width and the line length — and the
> second has to be pulled along on every change to the frame. The decision now lies in the grid
> alone.

## Headings

Six levels, but only four sizes. Levels 5 and 6 switch to capitals and letter-spacing, because a
difference of one pixel is not information. The space sits **above** the heading, never below — the
gap says what belongs to the heading.

## Links

Colour **and** underline. The underline is semi-transparent and set low, so that it does not cut
through the descenders; on hover it becomes opaque. External links carry an arrow.

## Quotes

Bar in the accent colour, tinted surface, upright text. **Out of the box** the text is italic — over
several lines that reads worse, and a quote is a different voice, not a different tone.

## Highlight

`==marked==` takes `textHighlight` — a warm yellow in light mode, the accent with transparency in
dark mode. Both are measured against the text colour.
