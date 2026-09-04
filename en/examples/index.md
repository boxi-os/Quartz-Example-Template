---
title: Examples
description: Pages on which individual plugins and special cases can be shown.
section: Examples
tags:
  - examples
translationKey: beispiele/index
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

Every page here shows one special case.

- [[en/examples/long-article|A long article]] — headings down to the sixth level, so the table of
  contents on the right is filled completely
- [[en/examples/properties-demo|Many properties]] — a full frontmatter
- [[en/examples/alias|A page with an alias]] — reachable under several paths
- [[en/examples/layout-box-control|Controlling the layout box per page]] — the same component, set
  up differently

Two pages sit in the folder but never appear:

- a **draft** (`draft: true`) is not built at all
- an **unlisted** page (`unlisted: true`) is built but appears in no listing — it can only be
  reached through its path
