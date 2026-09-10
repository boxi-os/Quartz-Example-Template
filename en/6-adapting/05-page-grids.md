---
title: 6.5 – Page grids
description: Four page grids of our own instead of the three that ship with Quartz.
section: 6 – Adapting
tags:
  - adapting
translationKey: anpassen/seitenraster
---

A frame is the grid of a page: which areas there are, where they sit, how wide they are.

On the desktop all four frames of this template share **one grid: twelve columns, a 4 rem gutter, a
20 px margin, capped at 1440 px.** That gives 1400 px of usable width, of which eleven gutters of
64 px take 704.

**The twelve columns are not all the same width.** The outer three on each side are computed to a
fixed size, so that an outer column together with its two gutters measures exactly 300 px; the
middle six share what is left. Why that is so stands further down under “Why the outer columns are
fixed” — the arithmetic is there too. Measured on the built page:

| Block | Columns | Width at 1440 px |
| --- | --- | --- |
| Navigation | 1–3 | 300 px |
| Text | 4–9 | 672 px |
| Apparatus | 10–12 | 300 px |

The gutter grew from 20 px to 2 rem on 2026-09-05 and to 4 rem on 2026-09-09 — the page was meant to
breathe more, and with fixed outer columns a wider gutter costs the text less than it used to. The
margin stayed at 20 px: it is the distance to the edge of the window, not the distance between two
things. The row gutter is 2 rem at every width.

> [!warning] On tablet and phone the gutter is narrower
> A twelve-column grid has eleven gutters whatever it contains, and they set its minimum width. At
> 4 rem that would be 704 px of gutter alone — more than a 390 px screen has at all. On a tablet it
> is therefore 3 rem, on a phone 1 rem, which puts the minimum at 216 px instead of 744. Measured
> before this exception existed: **every** page scrolled sideways by 18 px. The column gutter is
> invisible on a phone anyway, because there every area spans all twelve columns.

| Frame | Used by | Particularity |
| --- | --- | --- |
| `editorial` | content pages | all seven areas occupied, plus the free one below the text |
| `index` | folders, tags, [[en/7-reference/01-glossary#Base\|bases]] | geometrically the same as `editorial` |
| `focus` | error page | both outer columns reserved and empty, no apparatus |
| `drawing` | [[en/7-reference/01-glossary#Canvas\|canvas]] and [[en/7-reference/01-glossary#Excalidraw\|Excalidraw]] | no outer columns, everything across the full width |

That folder, tag, bases and error pages keep the right column too is deliberate: the text then
begins in the same place on **every** page, and jumping from an article to its folder no longer
shifts the line. Only `drawing` breaks with that, and there the content is a picture that needs the
width.

Every frame is laid out for **three widths**. The thresholds sit at 1200 and 900 px.

> [!example] The 900 used to be 800, and that was not a decision
> The [[en/7-reference/01-glossary#Explorer|explorer]] [[en/7-reference/01-glossary#Plugin|plugin]] switches to its drawer at exactly `max-width: 800px` in its own
> [[en/7-reference/01-glossary#Stylesheet|stylesheet]], and so do the search, the [[en/7-reference/01-glossary#Graph|graph]] and the canvas page. Breaking anywhere else left a
> band in which the two layouts contradicted each other — the explorer already a hamburger while the
> frame still laid the page out as a tablet. The frame followed the plugin.
>
> Since 2026-09-09 it goes the other way round: the template restates the rules of Quartz and of the
> four plugins against its own thresholds. The two numbers are a decision again.

On a tablet the right **column** falls away; its content slides below the text instead of
disappearing. On a phone everything stands one below the other.

**The order below the text is the same at both widths.** What the page says about itself comes
first — the two boxes in the free area, then the table of contents and the graph — and only then
what the site says about it: “Read on” and the property table. On a phone the table of contents
departs from that and stands *above* the text: an outline read after the article is no outline.

> [!example] What used to be wrong here
> For a long time `index` hid the right column on a tablet instead of moving it down, on the
> assumption that it was empty on a listing page: a list of links has no headings, hence no table
> of contents. Measured on `/formatierung/` it is not empty — the [[en/7-reference/01-glossary#Graph|graph]] lives there. On a tablet
> and on a phone it therefore vanished from every folder, tag and bases page. Since 2026-09-09
> `editorial` and `index` compute from the **same** function rather than letting two copies drift
> apart.

## What Quartz brings along

**Out of the box** there are `default` (three columns), `full-width` and `minimal`. They are built
in and their geometry cannot be changed — only selected.

**In this template** the four frames are built ourselves: number of columns, column widths, rows,
gaps, maximum width and alignment are set per width. An area that really has no business at one
width is hidden — a column that merely happens to be empty stays, so that the text column does not
wander.

## Why the outer columns are fixed

Out of the box all twelve columns would be `1fr` and share the space evenly — at every window width
all three blocks then shrink together. This template does it differently: the outer three columns on
each side carry a fixed width, so an outer column measures 300 px and stays there. What the page
loses in width, the text loses alone.

It is entered in the frame editor under *Grid*, in the **column widths** field: one input per
column, empty meaning `1fr`, and the values hold per breakpoint.

The arithmetic is where one stumbles: **an outer column is not one track but three** — plus the two
gutters between them, which belong to the area's own width. For 300 px at a gutter of 4 rem, fields
1–3 and 10–12 each take

```
calc((300px - 8rem) / 3)
```

— two gutters, hence `8rem` — and fields 4–9 stay empty. On a tablet the same arithmetic runs with
`6rem`, because the gutter is 3 rem there; on a phone it does not run at all, and all twelve columns
are equal again.

Measured on the built page, each against the variant with twelve `1fr` columns:

| Window | left | text | right | with `1fr` |
| ---: | ---: | ---: | ---: | --- |
| 1728 px | 300 | 672 | 300 | 302 / 668 / 302 |
| 1440 px | 300 | 672 | 300 | 302 / 668 / 302 |
| 1300 px | 300 | 532 | 300 | 267 / 598 / 267 |
| 1201 px | 300 | 433 | 300 | 242 / 549 / 242 |

Above 1440 px the two barely differ — the page is capped there, and 300 against 302 px is nothing.
The difference appears below that, and it is a decision about who pays.

> [!warning] The text alone pays the difference
> At 1201 px — just above the tablet break — the text column is left with 433 px instead of 549, a
> good 45 characters per line instead of 57. In exchange the [[en/7-reference/01-glossary#Explorer|explorer]] stands equally wide at every
> desktop width, and a folder tree that starts truncating its names at 1300 px is harder to use than
> a slightly shorter text line. The fixed values therefore belong on desktop and tablet and not on
> mobile, where the outer column spans the full width anyway.

On a tablet only the **left** three columns are fixed. A fixed track is incompressible, and each of
them raises the grid's minimum width: were 10–12 fixed as well, the grid could not go below 976 px,
and every page would scroll 92 px sideways in a 900 px window. Down there those three columns carry
text anyway, not an outer column.

## Two peculiarities of the editor

- A value may contain **no comma** — so no `minmax(0, 1fr)`.
- Lengths stand as numbers, not as [[en/7-reference/01-glossary#Token|tokens]]: a frame has to work even when someone imports only the
  *Frames* part and the variables are missing.

What a drawing of it looks like: [[en/3-obsidian-formats/03-excalidraw/index|Excalidraw]].
