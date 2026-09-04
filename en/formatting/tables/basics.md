---
title: Tables — the basic form
description: Rows, columns and the header.
section: Formatting
tags:
  - formatting
  - tables
translationKey: formatierung/tabellen/grundform
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
| Column A | Column B |
| -------- | -------- |
| Value    | Value    |
| Value    | Value    |
```

| Column A | Column B |
| -------- | -------- |
| Value    | Value    |
| Value    | Value    |

The hyphens in the second row separate header from body. Their number does not matter — three are
enough.

## In this template

**Out of the box** Quartz frames the table and sets the padding on the element itself.

**In this template** there are no vertical lines and no outer frame: only a hairline under each row
and a heavier one under the header. The header is set in the heading typeface and does not wrap.
The last row loses its line — otherwise it floats above nothing.
