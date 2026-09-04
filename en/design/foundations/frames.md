---
title: Frames
description: Three page grids of our own instead of the three that ship with Quartz.
section: Design
tags:
  - design
  - basics
translationKey: gestaltung/grundlagen/frames
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

A frame is the grid of a page: which areas there are, where they sit, how wide they are.

On the desktop all three frames of this template share **one grid: twelve equal columns, a 20 px
gutter, a 20 px margin, capped at 1440 px.** That gives 1400 px of usable width, eleven gutters and
therefore a column of 98.33 px. The three blocks snap onto it:

| Block | Columns | Width |
| --- | --- | --- |
| Navigation | 1–3 | 335 px |
| Text | 4–9 | 690 px |
| Apparatus | 10–12 | 335 px |

| Frame | Used by | Particularity |
| --- | --- | --- |
| `editorial` | content pages | all seven areas occupied |
| `index` | folders, tags, bases | right column stays empty, but reserved |
| `focus` | error page | both outer columns empty, no apparatus |

That folder, tag, bases and error pages keep the right column too is deliberate: the text then
begins in the same place on **every** page, and jumping from an article to its folder no longer
shifts the line.

Every frame is laid out for **three widths**. The thresholds sit at 1100 and 800 px. The 800 are
not freely chosen: the explorer plugin switches to its drawer at exactly `max-width: 800px` in its
own stylesheet. Before, 720 stood here, and between 721 and 800 px the two contradicted each other
— the explorer was already a hamburger while the frame still laid the page out as a tablet.

On a tablet the right **column** falls away; its content slides below the text instead of
disappearing. On a phone everything stands one below the other.

## What Quartz brings along

**Out of the box** there are `default` (three columns), `full-width` and `minimal`. They are built
in and their geometry cannot be changed — only selected.

**In this template** the three frames are built ourselves: number of columns, rows, gaps, maximum
width and alignment are set per width. An area that really has no business at one width is hidden —
a column that merely happens to be empty stays, so that the text column does not wander.

## Two peculiarities of the editor

- A value may contain **no comma** — so no `minmax(0, 1fr)`.
- Lengths stand as numbers, not as tokens: a frame has to work even when someone imports only the
  *Frames* part and the variables are missing.

What a drawing of it looks like: [[en/obsidian-formats/excalidraw/index|Excalidraw]].
