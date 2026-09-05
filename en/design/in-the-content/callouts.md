---
title: Callout colours
description: Twelve colours, all of them set anew and measured.
section: Design
tags:
  - design
  - in-the-content
  - callouts
translationKey: gestaltung/im-inhalt/callouts
---

## Out of the box

Quartz knows thirteen types and sets twelve colours for them; `note` keeps the base colour. Each
holds in both colour schemes alike, plus a border and a very pale surface.

Measured against the light ground of this template, **eleven of thirteen** fail the WCAG
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

- **A bar rather than a full frame.** A callout should stand out without cutting the column in two.
- **The title is the control** when the callout is foldable — with a focus ring of its own in the
  type colour.
- **Nested callouts** give up their frame and keep only the bar.

The check reads the colours **from the stylesheet**, not from a copy in the configuration. A value
changed here is measured here.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 19 variables are read by `body-callouts.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bg` | set in the stylesheet (`body-callouts.scss`) | only here |
| `--border` | set in the stylesheet (`body-callouts.scss`) | only here |
| `--callout-tint` | set in the stylesheet (`body-callouts.scss`) | only here |
| `--color` | — | only here |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--icon-chevron` | set in the stylesheet (`base.scss`) | Tokens |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tpl-accent-bar` | `3px` | 5 other components |
| `--tpl-focus-offset` | `2px` | Tokens |
| `--tpl-focus-width` | `2px` | Tokens |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 18 other components |
| `--tpl-space-xs` | `0.5rem` | 21 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
