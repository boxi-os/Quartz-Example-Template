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

## A finding while building

The plugin sets `width: 100%` on every layout box. In a flex row that made the mark 1376 px wide
and pushed the title onto the next line. `flex` does not lift a set width — it had to be taken back
explicitly.
