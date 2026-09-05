---
title: Table of contents
description: The outline on the right — every level, not just three.
section: Design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/seitenapparat/inhaltsverzeichnis
---

## Out of the box

Quartz shows the headings of a page as a flat list with an indent. **The default is
`maxDepth: 3`** — everything from the fourth heading level on is missing, and only depths 0 and 1
turn up in the markup.

## In this template

`maxDepth` is set to **6**. With that every level down to `h6` appears; on a normal page those are
depths 0 to 4. To be seen under [[en/examples/long-article|A long article]].

Every step is designed separately:

- **The indent** grows by one `--tpl-indent` per level down to depth 4 — the same measure as in the
  explorer, so that the two bars line up with one another.
- **Size and weight** fall with depth; from depth 3 on the type is set smaller.
- **From depth 5 on** there is no further indent, only a dot as a marker. Five indents in a bar
  three columns wide leave no room for a word.
- **The current section** gets colour, semibold *and* a bar on the guide line. While scrolling, the
  bar is what you find.
- **It shows itself in full.** Quartz caps this component three times over — `flex: 0 0.5 auto`
  with `overflow-y: hidden`, plus `max-height: calc(100% - 2rem)` on the list and another rule in
  its base stylesheet. Together the three turn a long outline into a short stub with a scrollbar of
  its own, in the middle of a column that was already scrolling. All three are lifted here.
- **Scrolling happens one level up**, in the right column as a whole — with the same soft edge as
  in the explorer, and with one scrollbar instead of two inside each other. The column's padding is
  as deep as the edge, so that the first and the last entry do not sit underneath it.
- **No fading by opacity.** Quartz dims an entry that is currently out of view to `opacity: 0.35`;
  on this ground that measures below 3:1. The state remains, but it is said in colour, weight and
  bar — three signals, all of them measured.

## The right column stands still

A table of contents that scrolls away upwards with the text is a list of places you can no longer
jump to. From tablet width on, the right column therefore stays put (`position: sticky`) and
scrolls only inside itself when its content grows taller than the window.

Three things belong together for that, and without any one of them nothing happens at all:
`align-self: start` — a grid item otherwise fills its row, and something that is already at the
very top *and* the very bottom can stick nowhere —, a `top`, and a maximum height.

Since 2026-09-05 the `top` is no longer a fixed number but `--tpl-header-h` plus a gap: the header
sticks and shrinks as well, and the column travels up with it instead of leaving a gap that grows
with every scroll.

> [!note] The depth numbers are relative
> `depth-0` is not `h1` but the shallowest heading on the page. On a normal page that is `h2`, so
> `h6` lands on `depth-4`.
