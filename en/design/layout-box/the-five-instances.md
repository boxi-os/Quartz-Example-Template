---
title: The five instances
description: The same plugin, five times, for something different each time.
section: Design
tags:
  - design
  - layout-box
translationKey: gestaltung/layout-box/die-fuenf-instanzen
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

| Key | Place | Form | What it shows |
| --- | --- | --- | --- |
| `layoutBoxMark` | header | inline, SVG light/dark | image switching, `{{root}}`, `{{siteTitle}}` |
| `layoutBoxNote` | left column | `file:` with `.md`, collapsible | Markdown snippet, `<details>` |
| `layoutBoxHint` | left column | inline, mobile only | two instances controllable independently |
| `layoutBoxCta` | after the content | inline, own class | `{{frontmatter.…}}` |
| `layoutBoxColophon` | footer | inline | `{{locale}}`, `{{slug}}` |

## Why four of five use `html:` rather than `file:`

**A template package carries `quartz/styles/` and `quartz/static/fonts/` — nothing else.** Snippet
files and images stay behind. An instance with `file:` would arrive in the target project with a
link into nothing.

Inline HTML, by contrast, sits in the configuration entry and travels with the *Plugins* part. That
is also why the word mark is an inline SVG and not an image file.

The fifth instance deliberately uses the file route — it shows both: that it works, and that the
file has to be copied along when passing the template on.

## The design per place

The place in the layout decides the form: a box in the header is a word mark, the same component
after the content is a call to action with a surface and a bar, in the footer a centred, small line.

## An open limitation

When a template is imported, only **one** of the five instances currently survives. They all carry
the same derived name (`quartz-layout-box`), and the import matches entries by name. That is
measured and recorded as a finding.

> [!note] The English pages fill four of them themselves
> Content can be replaced per page, so every English page points `layoutBoxNote` at an English
> snippet and sets the hint, the call to action and the colophon in English. The *title* of a box
> cannot be replaced that way — see [[en/design/multilingual/limits|Where the two languages stop]].
