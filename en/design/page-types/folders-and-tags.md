---
title: Folder and tag pages
description: The listings Quartz generates automatically.
section: Design
tags:
  - design
  - page-types
translationKey: gestaltung/seitentypen/ordner-und-tags
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
