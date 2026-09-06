---
title: Tables and media
description: Two elements that want to blow up the column.
section: Design
tags:
  - design
  - in-the-content
translationKey: gestaltung/im-inhalt/tabellen-und-medien
---

## Tables

**Out of the box** Quartz frames the table and sets the padding directly on the element.

**In this template** there are no vertical lines and no outer frame: a hairline under each row, a
heavier one under the header, and the last row loses its line. The header is set in the heading
typeface and does not wrap.

The scrolling sits on the container Quartz puts around every table — **not on the table itself.**
The obvious first attempt (`display: block; overflow-x: auto` on the `<table>`) takes the table
layout apart: while building, it made the keys and values of the property table slide on top of
each other.

## Images

A delicate border and rounded corners. Without a border an image with a white background looks like
a hole on the warm ground of this page.

An explicitly set width (`![[image.png|300]]`) is kept; the template only caps it.

## Embeds

An `iframe` gets `aspect-ratio: 16/9`. Without that rule it collapses to zero height in a grid cell
— which happens exactly when the page uses a grid of its own, that is, everywhere in this template.

## Transcluded notes

A dashed bar and a tinted surface: you should see where foreign content begins and ends. **Out of
the box** an embed is not visually separated from the surrounding text.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 12 variables are read by `body-media.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 8 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
