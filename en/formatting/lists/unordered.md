---
title: Unordered lists
description: Bullet lists and their nesting.
section: Formatting
tags:
  - formatting
  - lists
translationKey: formatierung/listen/ungeordnet
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
- First point
- Second point
- Third point
```

- First point
- Second point
- Third point

## Nested

Every level indents by two spaces.

```md
- First level
  - Second level
    - Third level
      - Fourth level
```

- First level
  - Second level
    - Third level
      - Fourth level

## Points over several lines

```md
- A point whose text is long enough to wrap,
  and whose second line sits flush under the first.

- A point with a paragraph of its own.

  The second paragraph still belongs to the same point.
```

- A point whose text is long enough to wrap,
  and whose second line sits flush under the first.

- A point with a paragraph of its own.

  The second paragraph still belongs to the same point.

## In this template

The bullet takes `--gray` instead of the text colour: it is structure, not content.
