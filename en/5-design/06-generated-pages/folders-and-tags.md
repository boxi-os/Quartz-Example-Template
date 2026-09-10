---
title: Folder and tag pages
description: The listings Quartz generates automatically.
section: 5 – The design
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

On the desktop, folder and tag pages keep the **right column**, even when only the [[en/7-reference/01-glossary#Graph|graph]] stands in
it. The listing therefore begins exactly where the text begins on a content page — jumping from an
article to its folder no longer shifts the line.

Both page types use the **`index`** [[en/7-reference/01-glossary#Frame|frame]], which is geometrically the same as `editorial`. There
is still no table of contents here — a list of links has no headings. The graph there is, and it
stands on the right as everywhere else; the [[en/7-reference/01-glossary#Backlinks|backlinks]] stand below the listing, as on every
other page.

> [!bug] On a folder page the graph shows a single dot
> Even when the page is linked to. That is a bug in the plugin and cannot be fixed from a template —
> the details stand under [[en/5-design/04-beside-the-content/graph|The graph]]. What does show the
> connections all the same are the backlinks below the listing.

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

These 14 variables are read by `page-listing.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#FCFCFA` | 13 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 21 other components |
| `--icon-tag` | set in the stylesheet (`base.scss`) | Tags |
| `--secondary` | `#1463A3` · dark `#699DC3` | 20 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-3xs` | `0.125rem` | 6 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xl` | `2.5rem` | 5 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-base` | `1rem` | 4 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
