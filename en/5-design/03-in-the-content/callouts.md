---
title: Callout colours
description: Thirteen types, all of them set anew and measured.
section: 5 – The design
tags:
  - design
  - in-the-content
  - callouts
translationKey: gestaltung/im-inhalt/callouts
---

## Out of the box

Quartz knows thirteen types and spreads ten colour values over them — three groups share one each,
and `quote` reads the accent colour. Each value holds in both colour schemes alike, plus a border
and a very pale surface.

Measured against the light ground of this template, **eleven of thirteen** fail the [[en/7-reference/01-glossary#WCAG|WCAG]]
threshold:

| Type | Default colour | against the light ground |
| --- | --- | --- |
| `note` | `#448aff` | 3.23 : 1 |
| `question` | `#dba642` | 2.14 : 1 |
| `tip` | `#00bfa5` | 2.27 : 1 |
| `danger` / `failure` / `bug` | `#db4242` | 4.20 : 1 — and 4.16 : 1 in dark mode |

## In this template

All thirteen are set anew, **once per mode**, and are measured twice on every run: against the page
ground and against their own tinted surface. The hue is kept — blue stays blue — so that the type
is still recognisable by its colour.

Plus three structural decisions:

- **A bar rather than a full [[en/7-reference/01-glossary#Frame|frame]].** A callout should stand out without cutting the column in two.
- **The title is the control** when the callout is foldable — with a focus ring of its own in the
  type colour.
- **Nested callouts** give up their frame and keep only the bar.

The check reads the colours **from the [[en/7-reference/01-glossary#Stylesheet|stylesheet]]**, not from a copy in the configuration. A value
changed here is measured here.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 31 variables are read by `body-callouts.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bg` | set in the stylesheet (`body-callouts.scss`) | only here |
| `--border` | set in the stylesheet (`body-callouts.scss`) | only here |
| `--callout-tint` | set in the stylesheet (`body-callouts.scss`) | only here |
| `--color` | — | only here |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--headerFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 15 other components |
| `--icon-chevron` | set in the stylesheet (`base.scss`) | 6.4 – Variables |
| `--light` | `#FCFCFA` · dark `#16171A` | 14 other components |
| `--tpl-accent-bar` | `3px` | 6 other components |
| `--tpl-callout-abstract` | `#0369A1` · dark `#67C7EF` | only here |
| `--tpl-callout-bug` | `#A21D62` · dark `#FF9BC8` | only here |
| `--tpl-callout-danger` | `#B02020` · dark `#FF9C93` | only here |
| `--tpl-callout-example` | `#6D28D9` · dark `#C3A6F7` | only here |
| `--tpl-callout-failure` | `#B02020` · dark `#FF9C93` | only here |
| `--tpl-callout-info` | `#0E7490` · dark `#5AC8DE` | only here |
| `--tpl-callout-note` | `#1D4ED8` · dark `#93B8FF` | only here |
| `--tpl-callout-question` | `#8A5A00` · dark `#E8C25E` | only here |
| `--tpl-callout-quote` | `var(--secondary)` = `#1463A3` | only here |
| `--tpl-callout-success` | `#136B34` · dark `#6DD68F` | only here |
| `--tpl-callout-tip` | `#0F766E` · dark `#5AD3BC` | only here |
| `--tpl-callout-todo` | `#0E7490` · dark `#5AC8DE` | only here |
| `--tpl-callout-warning` | `#9A4B06` · dark `#F0A868` | only here |
| `--tpl-focus-offset` | `2px` | 6.4 – Variables, The explorer |
| `--tpl-focus-width` | `2px` | 6.4 – Variables, The explorer |
| `--tpl-motion` | `150ms ease` | 13 other components |
| `--tpl-radius-md` | `8px` | 17 other components |
| `--tpl-radius-sm` | `4px` | 10 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-space-lg` | `1.5rem` | 12 other components |
| `--tpl-space-md` | `1rem` | 18 other components |
| `--tpl-space-xs` | `0.5rem` | 20 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
