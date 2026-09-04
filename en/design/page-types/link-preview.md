---
title: Link preview
description: What appears when hovering an internal link.
section: Design
tags:
  - design
  - page-types
translationKey: gestaltung/seitentypen/vorschau
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Out of the box

A box with the start of the target page.

## In this template

The second of exactly two places with a real shadow — it really does float above the page. An
opaque surface, because a translucent preview over body text is unreadable.

The content is **capped at 20 rem**, and at the cut lies a soft gradient: a truncated preview should
look cut, not broken.

What is left out inside it is what only gets in the way in a preview: callouts, tags and code
blocks. A preview should answer the question of whether the click is worth it — no more.

## Only with a pointer

With `@media (hover: none)` it is switched off entirely. From that follows a rule for the content:
**no information may exist only in a preview**, because on a phone there is none.
