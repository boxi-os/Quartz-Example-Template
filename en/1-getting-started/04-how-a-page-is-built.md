---
title: 1.4 – How a page is built
description: The parts of a page with their names — and a deliberately long, deeply structured page on which all of them can be seen.
section: 1 – Getting started
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
| **Header** | at the top, across all columns | the word mark, the site name, the chapter, the search, the light/dark switch, reader mode, the language switcher |
| **Left column** (left) | on the left | the [[en/7-reference/01-glossary#Explorer\|explorer]] — the folder tree of all pages — and the box “About this handbook” |
| **Above the content** (beforeBody) | above the text | the [[en/7-reference/01-glossary#Breadcrumbs\|breadcrumbs]] (the path from the home page to here), the tags, the title, date and reading time |
| **Content** (body) | centre | the note itself |
| **The free area** (custom-8) | directly below the text | two boxes side by side: the recently changed pages and the [[en/7-reference/01-glossary#Backlinks\|backlinks]] (which pages link here) |
| **After the content** (afterBody) | below that | the box “Read on”, the property table, and on a phone the hint about the collapsed navigation |
| **Right column** (right) | on the right | the table of contents and the [[en/7-reference/01-glossary#Graph\|graph]] |
| **Footer** | at the bottom | the colophon line |

Seven of those are Quartz's own places. **The free area is not** — it is an eighth one this template
added to the page grid, because two boxes side by side cannot otherwise be expressed: Quartz knows
exactly one place below the text, and everything put there stands underneath everything else.

Which part lies where is decided by the page grid, called a **[[en/7-reference/01-glossary#Frame|frame]]** in Quartz — more on that in a
moment. What stands in each part is decided by the layout, in QuartzControl under *Layout*. What
each part looks like and why is chapter [[en/5-design/index|5 – The design]].

A drawing of it:
[[en/3-obsidian-formats/03-excalidraw/Structure of the editorial frame.excalidraw|Structure of the editorial frame]].

## How wide the text gets

The width is decided by the page grid. The `editorial` frame, which content pages use, divides the
page into twelve columns and gives the text the middle six — three on the left for navigation,
three on the right for the table of contents and the graph. The page itself is capped at 1440
pixels, which puts the text at 672 pixels, or roughly 70 characters.

### Why not on the paragraph as well

A second limit on the individual paragraph would be a second place where the same question is
decided. Two such places have to be kept in agreement by hand — and at some point they no longer
are.

#### What that means on wide screens

If space is left over, it goes to the columns beside the text, not to the line length.

##### At which width it breaks

This template breaks to two columns at 1200 pixels and to one at 900. Those are the project's own
thresholds, not Quartz's. Until 2026-09-09 the lower one stood at 800, and not for a design reason:
the explorer plugin's own stylesheet switches to its drawer at exactly `max-width: 800px`. Since the
template rewrites the plugins' rules against its own thresholds, the two numbers are a decision
again.

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
| from 1201 px | 12 columns | three: 3 / 6 / 3 |
| 901 to 1200 px | 12 columns | two: 3 / 9, apparatus below the text |
| up to 900 px | 1 column | one |

### A code block

```ts
// Long lines scroll instead of wrapping.
export function measure(text: string): number {
  return text.length
}
```

## Finally

Anyone who has scrolled this far can see two things in the table of contents on the right: a rule
that stands in the accent colour down to the point just read and stays grey below it — a progress
bar built out of the entries themselves — and the current section set in the accent colour. Where
the rule ends is where you are; which heading that is, the one coloured word beside it says.
