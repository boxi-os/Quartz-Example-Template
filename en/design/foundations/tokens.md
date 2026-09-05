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
