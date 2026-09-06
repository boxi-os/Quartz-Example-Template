---
title: Code styling
description: Inline, blocks, the language label and the copy button.
section: Design
tags:
  - design
  - in-the-content
  - code
translationKey: gestaltung/im-inhalt/code
---

## Inline

**Out of the box** a box with a border. **In this template** a tint without a border — enough to
separate, too little to interrupt. Set slightly smaller (0.9em), because JetBrains Mono next to
Inter otherwise looks too big.

## Blocks

The surface comes from the template, not from the syntax theme: `keepBackground: false` makes shiki
set only the character colours. Only that way does the block fit in both colour schemes.

Since 2026-09-05 it is **lighter than the rest of the tint** and has a [[en/7-reference/01-glossary#Token|token]] of its own
(`--tpl-surface-code`, `#F1EFE9` in light mode, still `lightgray` in dark). A block is a large
area, and the tint that is right for one word of inline code turns twenty lines into a grey slab.
Measured, what it buys:

| Colour | on the old surface | on the new one |
| --- | --- | --- |
| Text (`#24292E`) | 10.69 : 1 | 12.76 : 1 |
| Blue (`#005CC5`) | 4.59 : 1 | 5.47 : 1 |
| Purple (`#6F42C1`) | 4.75 : 1 | 5.66 : 1 |
| Orange (`#E36209`) | 2.54 : 1 | 3.04 : 1 |

It is paid for in separation: the surface now stands at 1.12 : 1 against the page ground instead of
1.34 : 1. That is why the block takes its border from `--tpl-rule` — exactly the colour its fill
used to be.

## Five colours of the syntax theme are corrected

The lighter ground was not enough. So the count was made over the **whole built site**: every
`--shiki-light` and `--shiki-dark` value on all 333 pages, with its frequency and its [[en/7-reference/01-glossary#Contrast|contrast]]
against the code surface. Five pairs failed:

| Colour | what for | before | now |
| --- | --- | --- | --- |
| `#22863A` light | strings, tags (206×) | 4.02 : 1 | `#1F7A35` — 4.69 : 1 |
| `#D73A49` light | keywords (112×) | 3.98 : 1 | `#CA2938` — 4.70 : 1 |
| `#E36209` light | constants, [[en/7-reference/01-glossary#CSS and SCSS\|CSS]] variables (82×) | 3.04 : 1 | `#B04C07` — 4.70 : 1 |
| `#6A737D` light | comments (4×) | 4.19 : 1 | `#636B74` — 4.70 : 1 |
| `#6A737D` dark | comments (4×) | 2.74 : 1 | `#949CA4` — 4.74 : 1 |

Every correction keeps the hue and the saturation and changes only the lightness — `github-light`
still reads as `github-light`. It is the same thing this template does with Quartz's [[en/7-reference/01-glossary#Callout|callout]]
colours.

They have been checked on every run since: `--check-contrast` reads the five values out of
`body-code.scss` and measures them against `--tpl-surface-code`. 78 pairs have become 83; with the thirteenth callout, no longer skipped since 2026-09-05, 87.

> [!note] How that works technically
> shiki writes the colour **inline onto every single `<span>`**
> (`style="--shiki-light:#E36209;--shiki-dark:#FFAB70;"`), and an inline declaration beats any
> author rule that is not `!important`. So what is overridden is the *variable*, not `color` — then
> Quartz's own light/dark switch carries on doing what it should.
>
> What this does not cover: a language whose tokens produce a tenth colour would arrive unmeasured.
> The count is repeatable — grep `--shiki-light:` out of `public/`.

Long lines do not wrap, they scroll inside the block.

## The language label

At the top left stands the language — as an `::after` in the [[en/7-reference/01-glossary#Stylesheet|stylesheet]], not as an element. So it
does not end up in a copy, nor in the reading order.

## The copy button

**Out of the box** it appears only on [[en/7-reference/01-glossary#Hover|hover]] with a pointer — on a phone it is therefore
unreachable.

**In this template** it appears on hover, **on focus** and **permanently on devices without a
pointer** (`@media (hover: none)`). It measures 44 px, while the symbol inside stays small. It is
hidden through `opacity`, never through `display` — otherwise it would not be there for the
keyboard at all.

And it is **the icon alone**: no border, no surface. Its state is the colour of the icon, from
`gray` to `dark`.

> [!bug] The exception to the layering rule
> "Everything in `custom.scss` is unlayered and therefore beats the [[en/7-reference/01-glossary#Plugin|plugin]] styles" — true for
> component CSS, not for **resource stylesheets**. Quartz ships this button's styling in
> `static/resource-style-….css`, unlayered and linked *after* `index.css`. At equal specificity the
> later rule wins:
>
> ```css
> .clipboard-button { float: right; border: 1px solid; border-color: var(--dark);
>                     background-color: var(--light); margin: .3rem; padding: .4rem }
> ```
>
> Measured on the built page: the button still reported a 1px border and `--light` behind it,
> although every rule in this template said `border: none` and `background: transparent`. One
> descendant in the selector (`pre .clipboard-button`) settles it.

## Highlighted lines

Surface **and** a bar on the left. A tint alone is too weak on a block that is tinted anyway.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 22 variables are read by `body-code.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 other components |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-accent-bar` | `3px` | 5 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 other components |
| `--tpl-surface-code` | `color-mix(in srgb, var(--lightgray) 40%, …` · dark `var(--lightgray)` | only here |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-caps` | `0.06em` | 6.4 Variables, 3.1 Bases |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
