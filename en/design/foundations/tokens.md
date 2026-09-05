---
title: Tokens
description: 50 variables the whole design is made of.
section: Design
tags:
  - design
  - basics
translationKey: gestaltung/grundlagen/tokens
---

**Neither this template's colours nor its measures live in the stylesheets; both come from 50
variables.** That is not cosmetics: after the import they stay editable in the app under *Styles →
Variables*, a value in SCSS does not.

## The six with the widest reach

| Token | Value | What changes |
| --- | --- | --- |
| `--tpl-space-md` | 1rem | base gap; the whole scale hangs on it |
| `--tpl-target` | 44px | minimum size of **every** control |
| `--tpl-indent` | 0.85rem | one level in the explorer *and* the table of contents |
| `--tpl-radius-md` | 8px | corners of cards, code blocks, callouts |
| `--tpl-accent-bar` | 3px | every accent bar |
| `--tpl-motion` | 150ms | every transition duration |

## Two line heights, not one

`--tpl-leading-normal` is 1.65 and applies to the body text. For everything set in
`--tpl-text-sm` or smaller there is `--tpl-leading-snug` at 1.45.

That is not a nicety. 1.65 is a ratio measured for 1 rem across six grid columns. The same number
at 0.875 rem in a bar three columns wide puts nearly 21 px between two lines of 14 px height — a
three-line paragraph then reads like three separate ones. That is exactly how the note box in the
sidebar looked. The three areas that consist of small type — left bar, right bar, footer — say it
once, instead of every component inside them repeating it.

## Three kinds of variable

1. **Font stacks** — the family plus a real fallback.
2. **Quartz variables where the template disagrees** — the border of controls, for instance. Those
   are read by *Quartz*, not by our stylesheets; they look unused and are not.
3. **Our own `--tpl-*` tokens** — the actual system.

## What does stand literally

Measured across the 34 stylesheets, comments excluded: **41 colour values** and **112 lengths**. All
for the same reason — a variable *cannot* stand in that place.

| Where | What | Why |
| --- | --- | --- |
| `body-callouts` | 24 colours | Thirteen callout hues in two modes, less the quote callout, which reads the accent colour. They mean **status**, not palette: a `warning` that follows the accent colour is no longer a `warning`. |
| `body-code` | 10 colours | The five syntax corrections — the replaced and the replacing value each. |
| `body-mermaid` | 2 reds | Mermaid's error state, which it colours itself. |
| `a11y` | 2 greys | Inside `@media print`. On paper neither the light nor the dark palette applies. |
| `nav-explorer` | 1 black | The scrim behind the drawer on a phone — not a colour, a dimming. |
| everywhere | 20× `1px`/`2px` | Hairlines and focus rings. A line is one pixel wide, not one step of a grid. |
| everywhere | 26× `0.06em`–`0.18em` | Letter-spacing. It relates to the type size, not to the spacing scale. |
| 13 rules | `720px`, `800px`, `801px` | A media query cannot read a variable. |

## What Quartz does instead

**Out of the box** there are the nine colour variables and the typeface roles, but no scale for
spacing, radii, target sizes or motion. Values stand directly in the rules there. Anyone wanting to
change the base gap has to look for it in many places.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 39 variables are read by `base.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--icon-chevron` | set in the stylesheet (`base.scss`) | Callout colours |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--tpl-fade` | `20px` | only here |
| `--tpl-fade-mask` | set in the stylesheet (`base.scss`) | only here |
| `--tpl-focus-color` | `var(--secondary)` = `#2A4E6C` | only here |
| `--tpl-focus-offset` | `2px` | Callout colours |
| `--tpl-focus-width` | `2px` | Callout colours |
| `--tpl-header-h` | set in the stylesheet (`base.scss`) | only here |
| `--tpl-header-pad` | set in the stylesheet (`base.scss`) | The header |
| `--tpl-icon-sm` | `0.95rem` | The explorer, The language switcher |
| `--tpl-leading-normal` | `1.65` | only here |
| `--tpl-leading-snug` | `1.45` | 3 other components |
| `--tpl-leading-tight` | `1.25` | only here |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-space-2xl` | `4rem` | Error page |
| `--tpl-space-3xs` | `0.125rem` | 7 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 18 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xl` | `2.5rem` | 5 other components |
| `--tpl-space-xs` | `0.5rem` | 21 other components |
| `--tpl-target` | `44px` | 12 other components |
| `--tpl-text-2xl` | `1.75rem` | Title and date |
| `--tpl-text-3xl` | `2.25rem` | Title and date, Error page |
| `--tpl-text-base` | `1rem` | 4 other components |
| `--tpl-text-lg` | `1.15rem` | Search, Link preview |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-text-xl` | `1.4rem` | The language switcher |
| `--tpl-tracking-caps` | `0.06em` | Code styling, Bases |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
