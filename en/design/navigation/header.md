---
title: The header
description: Word mark, page title and the four controls in one row.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/kopfbereich
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

At the top stands the word mark, next to it the page title, at the right-hand end search, colour
scheme switch, reader mode and the language switcher. Below it a separating line.

## Out of the box

The header contains only the page title. There is no mark — you would have to build a component of
your own for that. Search and the two switches sit in the left sidebar.

## In this template

The mark comes from a **layout box instance** with an inline SVG, once light and once dark. It is
at the same time the link to the home page.

A few details:

- The **text of the mark is visually hidden** but present in the document. Otherwise the link would
  contain only an SVG and would have no accessible name. `display: none` would have been wrong here
  — that is exactly the mistake the first version contained.
- The four controls stand **in the header, not in the bar**. That is where they are looked for, and
  it is the only area every frame has — on the error page there used to be neither search nor
  colour scheme switch, because it has no sidebars.
- They form one **group** (`toolbar`) with `wrap`, so that four controls plus the site name still
  fit on a 360 px phone.
- On a phone the header becomes an **app bar**: it stays at the top while scrolling, runs the full
  width and takes the explorer's drawer button with it. The search gives up its word there and
  becomes a square like the others; it keeps its 44 px.

## It stays and it shrinks

Since 2026-09-05 the header sticks to the top of the window at every width, not only on a phone:
the four controls and the way back to the home page are what a reader reaches for in the middle of
a long article, and several pages here are three screens tall.

It shrinks while scrolling. What gets smaller is the **padding** and the site title — not the
controls: a target that changes size while you reach for it is worse than a tall bar. Measured:
61 px at rest, 49 px from 4 rem of scrolling on.

Two registered lengths carry it (`--tpl-header-pad`, `--tpl-header-title`), bound to
`scroll(root block)`. Nothing here moves on its own — the height is a function of the scroll
position, not of time — so with `prefers-reduced-motion` there is nothing to suppress.

> [!note] The shrinking needs scroll-driven animations
> Where there are none — measured on Firefox 155 — the header sticks as well but stays at its
> resting 61 px. Both are behind `@supports (animation-timeline: scroll())` — without that
> bracket the `animation` shorthand runs there as an animation with **zero duration**, and
> `fill: both` jumps straight to the end keyframe: in Firefox the header sat permanently in its
> *small* form.

Two things hang on it and are therefore in the same calculation:

- The **right column** sticks below the header rather than behind it: its `top` reads
  `--tpl-header-h` and travels up as the header shrinks.
- **Jump targets** keep the small bar's height free above themselves
  (`scroll-margin-block-start`), otherwise every heading from the table of contents would land
  behind the header.

## A finding while building

The plugin sets `width: 100%` on every layout box. In a flex row that made the mark 1376 px wide
and pushed the title onto the next line. `flex` does not lift a set width — it had to be taken back
explicitly.
