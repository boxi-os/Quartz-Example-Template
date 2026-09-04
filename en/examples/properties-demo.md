---
title: Many properties
description: A page with a full frontmatter, to show the property table.
section: Examples
date: 2026-07-02
lastmod: 2026-09-01
tags:
  - examples
  - frontmatter
  - reference
aliases:
  - Frontmatter example
number: 42
truthy: true
falsy: false
list:
  - one
  - two
  - three
empty:
translationKey: beispiele/eigenschaften-demo
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

This page carries more frontmatter than is displayed. In the property table the template shows only
`description`, `tags` and `section` — everything else would be on every page and repeat what stands
above it anyway.

To see all fields, set the option `includeAll` to true in the app under *Plugins → Note
properties*.

See also [[en/formatting/properties/frontmatter|Frontmatter]] in the formatting reference.
