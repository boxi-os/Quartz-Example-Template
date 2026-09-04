---
title: Search
description: The field in the bar and the overlay behind it.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/suche
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Out of the box

A button with a magnifying glass that opens an overlay. The border comes from `lightgray`.

## In this template

- The border comes from **`gray`**, not from `lightgray`. That is the contrast rule put into
  practice: `lightgray` measures 1.34:1 against the ground and may therefore not surround anything
  you operate.
- The button sits **in the header**, at the far right, together with the three other controls. It
  is 44 px high and around 15 rem wide — wide enough to be read as a field, narrow enough that the
  header still belongs to the page title. On a phone it becomes a square without a label.
- The **overlay** is one of exactly two places in this template with a real shadow. It really does
  float above the page, so it may show it.
- The **input field** gets no focus ring but a heavier bottom edge — a ring inside a rounded box
  looks like a mistake.
- **Results**: the keyboard cursor and the pointer hover look the same. The arrow keys move through
  the list, and the highlighted row is the only signal of where you are.
- The **match in the text** is marked with the same colour as `==highlight==` in the body text.
  "This is what you were looking for" means the same thing across the whole site.

With `prefers-reduced-transparency` the translucent surface is replaced by an opaque one.

> [!note] The index spans both languages
> There is one search index for the whole site, so a German page can turn up in an English search
> result. Splitting it would mean one build per language — see
> [[en/design/multilingual/limits|Where the two languages stop]].
