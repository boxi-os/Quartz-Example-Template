---
title: Body text
description: The width of the text, the heading scale and the links inside it.
section: Design
tags:
  - design
  - in-the-content
translationKey: gestaltung/im-inhalt/fliesstext
---

## The width of the text

**In this template** the page grid decides how wide the text gets — not a rule on the paragraph.
The frame gives the content six of twelve columns, which is 684 px on a page capped at 1440 px — at
a font size of 1 rem, about 72 characters.

**Out of the box** Quartz does the same, only with different numbers: it caps the page through
`.page { max-width }`.

> [!note] What once stood here
> An earlier version additionally capped the body text at 68 characters. That is common advice, but
> it means two places answer the same question — the column width and the line length — and the
> second has to be pulled along on every change to the frame. The decision now lies in the grid
> alone.

## Headings

Six levels, but only four sizes. Levels 5 and 6 switch to capitals and letter-spacing, because a
difference of one pixel is not information. The space sits **above** the heading, never below — the
gap says what belongs to the heading.

## Links

Colour **and** underline. The underline is semi-transparent and set low, so that it does not cut
through the descenders; on hover it becomes opaque. External links carry an arrow.

## Quotes

Bar in the accent colour, tinted surface, upright text. **Out of the box** the text is italic — over
several lines that reads worse, and a quote is a different voice, not a different tone.

## Highlight

`==marked==` takes `textHighlight` — a warm yellow in light mode, the accent with transparency in
dark mode. Both are measured against the text colour.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 23 variables are read by `body-content.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tertiary` | `#9C4221` · dark `#E8A56B` | Diagrams, The five instances |
| `--textHighlight` | `rgba(226, 189, 92, 0.45)` · dark `rgba(140, 184, 218, 0.30)` | Search results |
| `--tpl-accent-bar` | `3px` | 5 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 18 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xl` | `2.5rem` | 5 other components |
| `--tpl-space-xs` | `0.5rem` | 21 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
