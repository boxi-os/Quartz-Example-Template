---
title: Tables and media
description: Two elements that want to blow up the column.
section: Design
tags:
  - design
  - in-the-content
translationKey: gestaltung/im-inhalt/tabellen-und-medien
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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
