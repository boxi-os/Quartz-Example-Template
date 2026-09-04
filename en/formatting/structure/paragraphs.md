---
title: Paragraphs
description: How a paragraph comes about and how wide it gets.
section: Formatting
tags:
  - formatting
  - structure
translationKey: formatierung/struktur/absaetze
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## A paragraph

```md
A paragraph comes about through a blank line before and after it.

This one here is the second.
```

A paragraph comes about through a blank line before and after it.

This one here is the second.

## How wide a paragraph gets

The width is decided by the **page grid**, not by the paragraph. The `editorial` frame, which
content pages use, gives the text the middle of three columns and caps the whole page at 1440 px.

There is no limit on the individual paragraph in this template — it would be a second place where
the same thing is decided, and two such places contradict each other sooner or later. Anyone
wanting a narrower column changes the frame.

See [[en/design/foundations/frames|Frames]].
