---
title: Code in a sentence
description: A command in the middle of a sentence.
section: Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/inline
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
A command like `npm run build` in the middle of a sentence.
```

A command like `npm run build` in the middle of a sentence.

## Backticks inside code

To show a backtick itself, wrap it in two:

```md
A `` ` `` in the middle of the text.
```

A `` ` `` in the middle of the text.

## In this template

**Out of the box** inline code gets a distinct box with a border.

**In this template** it is a tint without a border — enough to separate it from the body text, too
little to interrupt the sentence. The type is set slightly smaller (0.9em), because JetBrains Mono
next to Inter otherwise looks too big. Long identifiers may wrap (`overflow-wrap: anywhere`)
instead of blowing up the column.
