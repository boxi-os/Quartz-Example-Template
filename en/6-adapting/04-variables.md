---
title: 6.4 – Variables
description: 66 variables the whole design is made of.
section: 6 – Adapting
tags:
  - adapting
translationKey: anpassen/variablen
---

**Neither this template's colours nor its measures live in the [[en/7-reference/01-glossary#Stylesheet|stylesheets]]; both come from 66
variables.** That is not cosmetics: after the import they stay editable in the app under *Styles →
Variables*, a value in [[en/7-reference/01-glossary#CSS and SCSS|SCSS]] does not.

## The six with the widest reach

| Token | Value | What changes |
| --- | --- | --- |
| `--tpl-space-md` | 1rem | [[en/7-reference/01-glossary#Base\|base]] gap; the whole scale hangs on it |
| `--tpl-target` | 44px | minimum size of **every** control |
| `--tpl-indent` | 0.85rem | one level in the [[en/7-reference/01-glossary#Explorer\|explorer]] *and* the table of contents |
| `--tpl-radius-md` | 8px | corners of cards, code blocks, [[en/7-reference/01-glossary#Callout\|callouts]] |
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

## What the 66 are

All 66 are our own `--tpl-*` tokens — the actual system. Typefaces and the colours of the palette
do not stand here but under *Styles → Basics*; from those Quartz itself writes `--bodyFont`,
`--secondary` and the rest. Until 2026-09-20 font stacks and Quartz variables stood here too, and
the font stacks hid Quartz's own fallback ([[en/6-adapting/03-typefaces|6.3]]).

Three groups among them are younger than the rest and deserve a sentence each:

- **Thirteen callout colours** (`--tpl-callout-note` to `--tpl-callout-quote`), light and dark
  each. They mean **status**, not palette: a `warning` that follows the accent colour is no longer
  a `warning`. And they are **measured, not chosen** — eleven of Quartz's twelve callout colours
  fail AA on a light ground. Every title colour holds 4.5:1 on the ground *and* on the tinted
  surface of its own box. Whoever changes one here can put it below that threshold, and the app
  says nothing about it.
- **Two for the scrim** behind every drawer (`--tpl-backdrop`, `--tpl-backdrop-blur`): dimming and
  blur, the same value for the navigation and the explorer.
- **Six switches for the side columns**, see the next section.

## The side columns: staying put or scrolling along

Whether a side column stays put while the page scrolls is decided by **three variables per
column**, and they belong together: a column that stays put needs a height cap (otherwise it runs
out of the window and does not stay put at all) and a soft lower edge (otherwise the cap cuts a
line in half). Whoever switches one switches all three.

| Variable | stays put | scrolls along |
| --- | --- | --- |
| `--tpl-col-…-position` | `sticky` | `static` |
| `--tpl-col-…-height` | `calc(100dvh - var(--tpl-header-h) - 2 * var(--tpl-space-lg))` | `none` |
| `--tpl-col-…-mask` | `var(--tpl-fade-mask-end)` | `none` |

`…` stands for `left` or `right`. **The default:** the right one stays put, the left one scrolls
along. A half state is possible and looks like a bug — `static` with a height cap is a column that
stops in the middle of the text and scrolls inside itself.

Switching the left one is a decision with consequences: this handbook's navigation is about
1640 px tall with a chapter open, about 2560 px on the home page, at a window height of 900 px.
Staying put there necessarily means "scrolls inside itself". The basic template comes to about
700 px and would simply stand still. The two columns switch at different widths: the left one from
901 px, the right one from 1201 px — below that they sit under the text, where staying put means
nothing.

## What does stand literally

Counted on 2026-09-21 across the 31 stylesheets, comments and variable declarations excluded:
**16 colour values** in three files. All for the same reason — a variable *cannot* stand in that
place.

| Where | What | Why |
| --- | --- | --- |
| `body-code` | 10 colours | The five syntax corrections — the replaced and the replacing value each. |
| `body-mermaid` | 4 colours | [[en/7-reference/01-glossary#Mermaid\|Mermaid]]'s error state and its two footnote colours, which it colours itself. |
| `a11y` | 2 greys | Inside `@media print`. On paper neither the light nor the dark palette applies. |
| everywhere | 20× `1px`/`2px` | Hairlines and focus rings. A line is one pixel wide, not one step of a grid. |
| everywhere | 56× `0.1em`, `1em` and others | Measures that relate to the type size rather than to the spacing scale — the padding of an inline-code pill, the size of an icon in line height. The three recurring letter-spacings became tokens on 2026-09-05. |
| 28 media queries | `480px`, `720px`, `900px`, `901px`, `1200px`, `1201px` | A media query cannot read a variable. |

## What repeats, and why it may

Two shapes stand in several stylesheets nearly word for word:

| Shape | in how many files |
| --- | ---: |
| The panel heading — heading face, uppercase, semibold, muted, `--tpl-tracking-label` | 9 |
| The hovered link — accent colour, underlined, `--tpl-underline-offset` | 8 |

That could be pulled into one shared file, and here that would be the wrong move. The stylesheets
are cut by component, and the documentation hangs off that: every page in this section carries the
table of the variables *its* component reads. Move the panel heading into `base.scss` and it
disappears from nine of those tables and turns up in one that nobody reads while adjusting the
[[en/7-reference/01-glossary#Backlinks|backlinks]].

What has to be shared are the **values** — and they are: `--tpl-tracking-label` and
`--tpl-underline-offset` stand once each and hold everywhere. The shape beside them is six lines,
readable where they take effect.

> [!note] A shared file would not be straightforward here anyway
> Sass solves this with partials (`_shared.scss`). The app does not allow a filename with a leading
> underscore, and a file without one would sit in the list under *Styles → Custom [[en/7-reference/01-glossary#CSS and SCSS|CSS]]* as a
> stylesheet that emits nothing.

## What Quartz does instead

**Out of the box** there are the nine colour variables and the typeface roles, but no scale for
spacing, radii, target sizes or motion. Values stand directly in the rules there. Anyone wanting to
change the base gap has to look for it in many places.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 48 variables are read by `base.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bodyFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 3 other components |
| `--col-ring-reach` | set in the stylesheet (`base.scss`) | only here |
| `--dark` | `#17171A` · dark `#FCFCFA` | 13 other components |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 22 other components |
| `--headerFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 15 other components |
| `--icon-chevron` | set in the stylesheet (`base.scss`) | Callout colours |
| `--light` | `#FCFCFA` · dark `#16171A` | 14 other components |
| `--tpl-col-left-height` | `none` | only here |
| `--tpl-col-left-mask` | `none` | only here |
| `--tpl-col-left-position` | `static` | only here |
| `--tpl-col-right-height` | `calc(100dvh - var(--tpl-header-h) - 2 * v…` | only here |
| `--tpl-col-right-mask` | `var(--tpl-fade-mask-end)` | only here |
| `--tpl-col-right-position` | `sticky` | only here |
| `--tpl-fade` | `14px` | only here |
| `--tpl-fade-mask` | set in the stylesheet (`base.scss`) | only here |
| `--tpl-focus-color` | `var(--secondary)` = `#1463A3` | only here |
| `--tpl-focus-offset` | `2px` | Callout colours |
| `--tpl-focus-width` | `2px` | Callout colours |
| `--tpl-header-h` | set in the stylesheet (`base.scss`) | The explorer, The navigation |
| `--tpl-header-pad` | set in the stylesheet (`base.scss`) | The header |
| `--tpl-icon-sm` | `0.95rem` | 3 other components |
| `--tpl-leading-normal` | `1.6` | The navigation |
| `--tpl-leading-snug` | `1.4rem` | 4 other components |
| `--tpl-leading-tight` | `1.25` | only here |
| `--tpl-motion` | `150ms ease` | 13 other components |
| `--tpl-page-fade` | `24px` | The header |
| `--tpl-radius-md` | `8px` | 17 other components |
| `--tpl-radius-sm` | `4px` | 10 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 19 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-space-lg` | `1.5rem` | 12 other components |
| `--tpl-space-md` | `1rem` | 18 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xl` | `2.5rem` | 5 other components |
| `--tpl-space-xs` | `0.5rem` | 20 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 other components |
| `--tpl-target` | `44px` | 12 other components |
| `--tpl-text-2xl` | `1.75rem` | Title and date |
| `--tpl-text-3xl` | `2.25rem` | Title and date, Error page |
| `--tpl-text-base` | `1rem` | 4 other components |
| `--tpl-text-lg` | `1.15rem` | Search, Link preview |
| `--tpl-text-sm` | `0.875rem` | 20 other components |
| `--tpl-text-xl` | `1.4rem` | The language switcher |
| `--tpl-tracking-caps` | `0.06em` | Code styling, 3.1 – Bases |
| `--tpl-tracking-label` | `0.08em` | 9 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
