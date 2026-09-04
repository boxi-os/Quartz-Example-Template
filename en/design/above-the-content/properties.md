---
title: The property table
description: The frontmatter table under the title.
section: Design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/eigenschaften
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Out of the box

A plain table in the text colour, collapsible.

## In this template

- on a **tinted surface** with a border and rounded corners
- the **header row** capitalised, small and muted — it is a label, not content
- the **key** muted and as wide as its text, the **value** takes the rest
- **value types** are distinguished: a number in figure width, a boolean as a coloured word, a list
  as a row of markers, an empty field in italics

To be seen under [[en/formatting/properties/data-types|Data types]], where one page brings all four
types with it.

## The finding about cell width

The obvious solution for "the key is as wide as its content" is `width: 1%` on the key cell.
Measured: the cell became 7.94 px wide — exactly 1 % of the table — and the key lay on top of the
value.

The way that works is the other way round: **`width: 100%` on the value cell.** It claims
everything that is left over and leaves the key its content width.
