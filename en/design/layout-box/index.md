---
title: Layout box
description: A plugin that puts arbitrary markup at any place in the layout.
section: Design
tags:
  - design
  - layout-box
translationKey: gestaltung/layout-box/index
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

`quartz-layout-box` renders an HTML or Markdown snippet at any place in the page layout: header,
sidebars, before or after the content, footer. This template uses it **five times**, each time for
something different.

## What the plugin can do

| Possibility | Option |
| --- | --- |
| Content from a file | `file:` |
| Content from the configuration | `html:` |
| Markdown instead of HTML | let the file end in `.md` |
| A heading above it | `title:` |
| Collapsible | `collapsible:` and `collapsed:` |
| A CSS class of your own | `className:` |
| Replace placeholders | `placeholders:` |
| Controllable per page | `frontmatterKey:` |
| An image per colour scheme | classes `img-light` / `img-dark` |

## Placeholders

`{{title}}`, `{{slug}}`, `{{root}}`, `{{siteTitle}}`, `{{baseUrl}}`, `{{locale}}` and every
frontmatter field through `{{frontmatter.name}}`. `{{root}}` is the relative path to the home page —
so a link works even when the page sits in a sub-path.

## The design

The plugin deliberately ships **colourless** styles: width, image switching, a dashed placeholder
for missing files. That is the right decision for a component plugin — it leaves the appearance to
the site.

This template designs every class: `.layout-box`, `.layout-box-title`, `.layout-box-content`,
`.layout-box-missing`, plus five variants of its own.

Further: [[en/design/layout-box/the-five-instances|The five instances]] ·
[[en/design/layout-box/per-page|Controlling it per page]]
