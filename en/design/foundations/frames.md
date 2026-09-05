---
title: Frames
description: Three page grids of our own instead of the three that ship with Quartz.
section: Design
tags:
  - design
  - basics
translationKey: gestaltung/grundlagen/frames
---

A frame is the grid of a page: which areas there are, where they sit, how wide they are.

On the desktop all three frames of this template share **one grid: twelve equal columns, a 2 rem
gutter, a 20 px margin, capped at 1440 px.** That gives 1400 px of usable width; eleven gutters of
32 px take 352 of it, so a column measures 87.33 px. The three blocks snap onto it:

| Block | Columns | Width |
| --- | --- | --- |
| Navigation | 1–3 | 326 px |
| Text | 4–9 | 684 px |
| Apparatus | 10–12 | 326 px |

The gutter grew from 20 px to 2 rem on 2026-09-05 — the page was meant to breathe more. The margin
stayed at 20 px: it is the distance to the edge of the window, not the distance between two things.

> [!warning] On a phone the gutter stays at 20 px
> A twelve-column grid has eleven gutters whatever it contains, and they set its minimum width:
> 11 × 32 plus 40 of margin is 392 px, which is more than a 390 px screen has. Measured before this
> exception existed: **every** page scrolled sideways by 18 px. The column gutter is invisible there
> anyway, because on a phone every area spans all twelve columns; the row gutter keeps its full
> 2 rem.

| Frame | Used by | Particularity |
| --- | --- | --- |
| `editorial` | content pages | all seven areas occupied |
| `index` | folders, tags, bases | right column without a table of contents — there are no headings there |
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

> [!bug] Only `editorial` moves it down
> Below 1100 px, `index` and `focus` hide the right column instead. For `focus` it is empty, so
> that costs nothing. For `index` it is not: measured at 900 and at 390 px it carries
> `display: none`, so folder, tag and bases pages lose their **backlinks and the graph** entirely
> on a tablet and on a phone. On an article page both survive and merely move below the text. That
> is a bug in the frame, not a design.

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
