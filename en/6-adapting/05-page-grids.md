---
title: 6.5 Page grids
description: Three page grids of our own instead of the three that ship with Quartz.
section: Adapting
tags:
  - adapting
translationKey: anpassen/seitenraster
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

That holds for `editorial` and for `index` alike. Only `focus` really hides the column — there it
is empty, so that costs nothing.

> [!example] What used to be wrong here
> For a long time `index` hid the right column below 1100 px instead of moving it down, on the
> assumption that it was empty on a listing page: a list of links has no headings, hence no table
> of contents. Measured on `/formatierung/` it is not empty — backlinks and the graph live there.
> On a tablet and on a phone both therefore vanished from every folder, tag and bases page. Since
> 2026-09-05 `index` gives the right column the same row `editorial` does.

## What Quartz brings along

**Out of the box** there are `default` (three columns), `full-width` and `minimal`. They are built
in and their geometry cannot be changed — only selected.

**In this template** the three frames are built ourselves: number of columns, rows, gaps, maximum
width and alignment are set per width. An area that really has no business at one width is hidden —
a column that merely happens to be empty stays, so that the text column does not wander.

## Fixing the width of an outer column

The twelve columns are `1fr` and therefore share the space evenly — at every window width all three
blocks shrink together. Anyone wanting a fixed width instead enters it in the frame editor under
*Grid*, in the **column widths** field: one input per column, empty meaning `1fr`, and the values
hold per breakpoint.

The arithmetic is where one stumbles: **an outer column is not one track but three** — plus the two
gutters between them, which belong to the area's own width. For 320 px, fields 1–3 and 10–12 each
take

```
calc((320px - 4rem) / 3)
```

and fields 4–9 stay empty. Measured on the built page:

| Window | left | text | right |
| ---: | ---: | ---: | ---: |
| 1728 px | 320 | 696 | 320 |
| 1440 px | 320 | 696 | 320 |
| 1300 px | 320 | 556 | 320 |
| 1200 px | 320 | 456 | 320 |
| 1101 px | 320 | 357 | 320 |

For comparison with `1fr`: 326 / 684 / 326 at 1440 px and 266 / 564 / 266 at 1200 px.

> [!warning] The text alone pays the difference
> With `1fr` all three blocks lose together; with fixed outer columns only the text column does. At
> 1101 px — just above the tablet break — it is left with 357 px, a good 37 characters per line. The
> values therefore belong on the desktop breakpoint and not on tablet or mobile, where the outer
> column moves below the text or spans the full width anyway.

This template makes **no** use of it: it stays with twelve equal columns, because the text measure
is then a consequence of the grid rather than a second decision beside it — see
[[en/5-design/03-in-the-content/body-text|Body text]].

## Two peculiarities of the editor

- A value may contain **no comma** — so no `minmax(0, 1fr)`.
- Lengths stand as numbers, not as tokens: a frame has to work even when someone imports only the
  *Frames* part and the variables are missing.

What a drawing of it looks like: [[en/3-obsidian-formats/03-excalidraw/index|Excalidraw]].
