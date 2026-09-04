---
title: Data types
description: Text, number, boolean, list — and how they are displayed.
section: Formatting
tags:
  - formatting
  - frontmatter
number: 42
truthy: true
list:
  - one
  - two
  - three
empty:
translationKey: formatierung/eigenschaften/datentypen
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

This page carries four example fields itself. The property table above this text shows them.

````md
---
number: 42
truthy: true
falsy: false
list:
  - one
  - two
empty:
---
````

| Type | Notation | Display in this template |
| --- | --- | --- |
| Text | `field: value` | as it is |
| Number | `number: 42` | in figure width (`tabular-nums`) |
| Boolean | `truthy: true` | as a word, coloured positively |
| List | entries with `-` | as a row of markers |
| Empty | `empty:` | italic and muted |
| Date | `date: 2026-09-01` | formatted by locale |

## What is displayed is decided by the configuration

The *Note properties* plugin does not show everything by default, only the fields from
`includedProperties`. This template lists `description`, `tags`, `section` and the four demo fields
of this page there. A field a page does not have gets no row.
