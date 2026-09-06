---
title: Folder and tag pages
description: The listings Quartz generates automatically.
section: Design
tags:
  - design
  - page-types
translationKey: gestaltung/erzeugte-seiten/ordner-und-tags
---

For every folder and every tag a page with a listing is created automatically.

## Out of the box

A list with date, title, description and tags, one below the other.

## In this template

A **three-column grid**: the date in a fixed width on the left, the title in the middle, the tags on
the right. The fixed date column makes the titles form an edge — and the digits stand under one
another in figure width.

Below 720 px it collapses into one column; the date is the part that moves.

On the desktop, folder and tag pages keep the **right column**, even when only backlinks stand in
it. The listing therefore begins exactly where the text begins on a content page — jumping from an
article to its folder no longer shifts the line.

Both page types use the **`index`** frame, which is geometrically the same as `editorial`. There
is still no table of contents here — a list of links has no headings. Backlinks and the graph there
are, and they stand on the right as everywhere else.

## Two findings while building

**`.desc` contains the title, not the description.** Anyone taking the name literally and setting
the class muted greys out every entry title on every listing page.

**"Recently changed" uses the same class names.** Without being scoped to `.page-listing`, the
three-column grid lands in the narrow sidebar.

## The tag page

The title is the tag name as plain text. This template puts a hash in front of it — as a `::before`,
so that it does not end up in the reading order.

> [!note] Two languages, two sets of listings
> A folder page exists for every folder, `en/` included, and the English pages carry English tags.
> The listings therefore never mix the two languages — with one exception: the folder page of `en`
> itself, which is the English home page and is written by hand.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 12 variables are read by `page-listing.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 16 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-3xs` | `0.125rem` | 7 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-base` | `1rem` | 4 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
