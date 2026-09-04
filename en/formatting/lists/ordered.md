---
title: Ordered lists
description: Numbered lists and what the numbers really do.
section: Formatting
tags:
  - formatting
  - lists
translationKey: formatierung/listen/geordnet
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
1. First step
2. Second step
3. Third step
```

1. First step
2. Second step
3. Third step

## The numbers in the source do not matter

Markdown numbers through on its own. Writing `1.` everywhere still yields 1, 2, 3 — handy when a
point is inserted later.

```md
1. First step
1. Second step
1. Third step
```

1. First step
1. Second step
1. Third step

## Nested and mixed

```md
1. A step
   1. Sub-step
   2. Another one
2. The next step
   - with a note
   - and another
```

1. A step
   1. Sub-step
   2. Another one
2. The next step
   - with a note
   - and another
