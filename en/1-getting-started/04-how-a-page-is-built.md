---
title: 1.4 How a page is built
description: The parts of a page with their names — and a deliberately long, deeply structured page on which all of them can be seen.
section: 1 Getting started
tags:
  - getting-started
  - typography
date: 2026-08-14
lastmod: 2026-09-06
translationKey: einstieg/so-ist-eine-seite-aufgebaut
---

This page has two jobs. It names the parts every page of this site is made of — so that chapters 5
and 6 can call them by name. And it is deliberately long and deeply structured, so that it shows
what a short page cannot: a table of contents with all six levels, and a sidebar that grows longer
than the window.

## The parts of a page

On the desktop a page has three columns, on a tablet two, on a phone one. The names in the table
are the ones QuartzControl uses in the layout editor as well.

| Part | Where | What stands in it |
| --- | --- | --- |
| **Header** | at the top, across all columns | the word mark, the site name, the search, the light/dark switch, reader mode, the language switcher |
| **Left column** (left) | on the left | the [[en/7-reference/01-glossary#Explorer\|explorer]] — the folder tree of all pages —, the box “About this handbook”, the recently changed pages |
| **Above the content** (beforeBody) | above the text | the [[en/7-reference/01-glossary#Breadcrumbs\|breadcrumbs]] (the path from the home page to here), the title, date and reading time, the property table, the tags |
| **Content** (body) | centre | the note itself |
| **After the content** (afterBody) | below the text | the box “Read on” |
| **Right column** (right) | on the right | the table of contents, the [[en/7-reference/01-glossary#Backlinks\|backlinks]] (which pages link here), the [[en/7-reference/01-glossary#Graph\|graph]] |
| **Footer** | at the bottom | the colophon line |

Which part lies where is decided by the page grid, called a **[[en/7-reference/01-glossary#Frame|frame]]** in Quartz — more on that in a
moment. What stands in each part is decided by the layout, in QuartzControl under *Layout*. What
each part looks like and why is chapter [[en/5-design/index|5 The design]].

A drawing of it:
[[en/3-obsidian-formats/03-excalidraw/Structure of the editorial frame.excalidraw|Structure of the editorial frame]].

## How wide the text gets

The width is decided by the page grid. The `editorial` frame, which content pages use, divides the
page into twelve equal columns and gives the text six of them — three on the left for navigation,
three on the right for the table of contents and the backlinks. The page itself is capped at 1440
pixels, which puts the text at 684 pixels, or roughly 71 characters.

### Why not on the paragraph as well

A second limit on the individual paragraph would be a second place where the same question is
decided. Two such places have to be kept in agreement by hand — and at some point they no longer
are.

#### What that means on wide screens

If space is left over, it goes to the columns beside the text, not to the line length.

##### At which width it breaks

This template breaks to two columns at 1100 pixels and to one at 800. Those are the project's own
thresholds, not Quartz's — they sit a little tighter because the left column is narrower here.

###### The deepest level

From here on the table of contents gives up indenting and marks with dots. This heading is the
reason this page exists.

## Structure and rhythm

The space of a heading sits above it. That is what creates the group: heading and the text below it
visibly belong together, and the space above separates them from what came before.

### Levels and weight

The first four levels differ in size. The last two no longer do — they switch to capitals and
letter-spacing, because a difference of one or two pixels is not information anyone recognises
reliably.

#### An intermediate level

Text on level four.

##### And another

Text on level five.

###### And the last

Text on level six.

## Elements in the body text

A paragraph with **emphasis**, *italics*, `code` and an [[en/7-reference/index|internal link]]. Plus a
==highlight== and a footnote[^long].

[^long]: Footnotes collect at the end of the page, separated by a line.

> [!tip] A callout in the middle
> [[en/7-reference/01-glossary#Callout|Callouts]] interrupt the flow of reading on purpose. That is why they have a colour bar on the left
> and no full border — they should stand out without cutting the column in two.

### A list

1. The first point
2. The second point
   - with a note
   - and another
3. The third point

### A table

| Width | Grid | Blocks side by side |
| ------ | ------ | -------------------- |
| over 1100 px | 12 columns | three: 3 / 6 / 3 |
| 801 to 1100 px | 12 columns | two: 3 / 9, apparatus below the text |
| up to 800 px | 1 column | one |

### A code block

```ts
// Long lines scroll instead of wrapping.
export function measure(text: string): number {
  return text.length
}
```

## Finally

Anyone who has scrolled this far can see the current section highlighted in the table of contents
on the right — colour, weight and a bar on the rule. Three signals, because one of them fails for
some readers.
