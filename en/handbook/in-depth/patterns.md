---
title: Patterns
description: Recurring decisions of this template.
section: Handbook
tags:
  - handbook
  - reference
translationKey: handbuch/vertiefung/muster
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## What is the same everywhere

Three patterns repeat in every component:

1. **Headings of the sidebars** are small, capitalised and grey — they are labels, not content.
2. **A state is never shown by colour alone.** The active entry in the explorer has colour, weight
   *and* a bar.
3. **Borders of controls** take `--gray`, not `--lightgray`. The delicate tone is enough for a
   separating line, but not for the border of something you operate.

See also [[en/handbook/basics/terms/glossary|Glossary]].
