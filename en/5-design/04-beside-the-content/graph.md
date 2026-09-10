---
title: The graph
description: The surroundings of a note as a network.
section: 5 – The design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/neben-dem-inhalt/graph
---

## Out of the box

A box with the local surroundings, plus a symbol for opening the global view.

## In this template

The graph draws itself and takes its colours from the [[en/7-reference/01-glossary#CSS and SCSS|CSS]] variables at runtime. The template
therefore designs **only the box around it**, not the drawing:

- a **square field** (`aspect-ratio: 1`) — the local graph is round, and a wide box wastes the
  sidebar
- border and tinted surface as with the other panels
- the **symbol for the global view** is 44 px across and sits at the right of the heading row
- the **global view** gets the same shadow as the search — both really do float

A half-recoloured graph would be worse than one in foreign colours: the drawing resolves its own
colours, and a [[en/7-reference/01-glossary#Stylesheet|stylesheet]] working against that always catches only half of them.

**On narrow screens it is hidden** (`display: desktop-only`) — a net of dots in a column 390 px
wide shows nothing.

## What is missing on folder pages

On a **folder or chapter page** the box holds a single dot, even when the page has links. That is a
bug in the plugin and cannot be fixed from a template.

The script normalises addresses in two places and differently in each. It keys its data set with
`simplifySlug`, which strips a trailing `index` and keeps the slash before it, turning
`2-formatting/01-text/index` into `2-formatting/01-text/`. The centre of the graph it takes from the
address bar instead, and there it strips that slash. For every page whose address ends in a slash —
which is exactly the folder pages — it therefore looks for a node it never created: no edges, one
dot.

The same page reached as `…/01-text/index` shows nine nodes and eight edges. One character of
difference.

Hiding the box there is not possible either: Quartz' `not-index` condition means the home page
alone, and anything finer needs code rather than configuration. What does show a folder page's
connections are the [[en/7-reference/01-glossary#Backlinks|backlinks]] and the list in the text above.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 17 variables are read by `aside-graph.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--tpl-radius-lg` | `14px` | 3 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dark `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
