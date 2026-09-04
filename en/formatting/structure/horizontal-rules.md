---
title: Horizontal rules
description: The dash between sections.
section: Formatting
tags:
  - formatting
  - structure
translationKey: formatierung/struktur/trennlinien
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
---
```

---

Three hyphens on a line of their own. The rule separates sections that do not deserve a heading of
their own.

> [!warning] Careful at the start of a file
> Three hyphens at the very top of the file open the **frontmatter**, not a rule. Anyone wanting to
> begin a page with a rule puts a paragraph in front of it.

## In this template

The rule is a hairline in `--tpl-rule` with generous space above and below (`--tpl-space-xl`).
**Out of the box** Quartz draws a heavier line with less air.
