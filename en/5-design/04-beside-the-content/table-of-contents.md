---
title: Table of contents
description: The outline on the right — every level, not just three.
section: 5 – The design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/neben-dem-inhalt/inhaltsverzeichnis
---

## Out of the box

Quartz shows the headings of a page as a flat list with an indent. **The default is
`maxDepth: 3`** — everything from the fourth heading level on is missing, and only depths 0 and 1
turn up in the markup.

## In this template

`maxDepth` is set to **6**. With that every level down to `h6` appears; on a normal page those are
depths 0 to 4. To be seen under [[en/1-getting-started/04-how-a-page-is-built|A long article]].

Every step is designed separately:

- **The indent** grows by one `--tpl-indent` per level down to depth 4 — the same measure as in the
  [[en/7-reference/01-glossary#Explorer|explorer]], so that the two bars line up with one another.
- **Size and weight** fall with depth; from depth 3 on the type is set smaller.
- **From depth 5 on** there is no further indent, only a dot as a marker. Five indents in a bar
  three columns wide leave no room for a word.
- **How far you are** is what the guide line says: it stands in the accent colour down to the
  heading that has just gone by and stays grey below it. A progress bar built out of the entries
  themselves — they stack with no gaps, so their 2 px borders make one line.
- **Where you are** is what one word says: the last marked entry stands in the accent colour.
  Weight stays out of it — the entries are 13 px, and a jump to 600 reflows the whole column on
  every scroll.
- **It shows itself in full.** Quartz caps this component three times over — `flex: 0 0.5 auto`
  with `overflow-y: hidden`, plus `max-height: calc(100% - 2rem)` on the list and another rule in
  its [[en/7-reference/01-glossary#Base|base]] [[en/7-reference/01-glossary#Stylesheet|stylesheet]]. Together the three turn a long outline into a short stub with a scrollbar of
  its own, in the middle of a column that was already scrolling. All three are lifted here.
- **Scrolling happens one level up**, in the right column as a whole — with the same soft edge as
  in the explorer, and with one scrollbar instead of two inside each other. The column's padding is
  as deep as the edge, so that the first and the last entry do not sit underneath it.
- **No fading by opacity.** Quartz dims an entry that has not been read yet to `opacity: 0.35`; on
  this ground that measures below 3:1. The state remains, but it is said in two steps of the
  palette — `--gray` and `--darkgray`, both measured — rather than in opacity.

## The right column stands still

A table of contents that scrolls away upwards with the text is a list of places you can no longer
jump to. As long as there is a right column at all — that is, from 1201 px — it therefore stays put
(`position: sticky`) and scrolls only inside itself when its content grows taller than the window.
On a tablet there is no column left for anything to stick in: table of contents and graph stand
there as two boxes side by side below the text.

Three things belong together for that, and without any one of them nothing happens at all:
`align-self: start` — a grid item otherwise fills its row, and something that is already at the
very top *and* the very bottom can stick nowhere —, a `top`, and a maximum height.

Since 2026-09-05 the `top` is no longer a fixed number but `--tpl-header-h` plus a gap: the header
sticks too, and the column reads its height from the same arithmetic instead of carrying a second
copy of it.

> [!note] The depth numbers are relative
> `depth-0` is not `h1` but the shallowest heading on the page. On a normal page that is `h2`, so
> `h6` lands on `depth-4`.

> [!note] Quartz does not mark where you are but how far you got
> The plugin's observer sets `.in-view` on **every** entry whose heading is above the bottom of the
> viewport and removes it from the rest — a “read this far” mark, not a “you are here”. Take it for
> the latter and on a long page you colour half the outline, and half an outline being emphasised
> emphasises nothing.
>
> The rule is the right use for it: a scale is allowed to be half full. Where it ends is the current
> place — and that is exactly the last marked entry, the marked one with no marked one after it.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 17 variables are read by `aside-toc.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#FCFCFA` | 13 other components |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--secondary` | `#1463A3` · dark `#699DC3` | 20 other components |
| `--tpl-indent` | `0.85rem` | The explorer |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-3xs` | `0.125rem` | 6 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
