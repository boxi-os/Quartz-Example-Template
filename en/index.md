---
title: Minimal and readable
description: The example template for QuartzControl — all ten parts, every component designed, every contrast measured.
section: Start
tags:
  - template
  - start
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

This site is the example content for the template **Minimal and readable**. It exists so that the
design can be seen: an explorer needs folders, a table of contents needs headings, a graph needs
links.

> [!tip] Four ways in
> Each area shows something different about the same design.

| Area | What is in it |
| --- | --- |
| [[en/formatting/index\|Formatting]] | Every Obsidian element as source and rendered result — 45 short pages |
| [[en/obsidian-formats/index\|Obsidian formats]] | Bases, Canvas and Excalidraw: three file types that are not notes |
| [[en/design/index\|Design]] | Per component: what Quartz does out of the box, and what this template changes |
| [[en/handbook/index\|Handbook]] | Four folder levels deep — so that the explorer and the breadcrumbs have something to show |

## The three decisions everything rests on

1. **The width decides the grid.** The frame gives the text its column; there is no second limit on
   the individual paragraph that could fall out with it.
2. **Colours are measured.** 78 pairs meet WCAG AA in light and dark, the twelve callout types
   included. Quartz's own callout colours do not — eleven of twelve fail.
3. **No stylesheet contains a number.** Everything reads variables that stay editable in the app
   after the import.

## Where the content is kept

In an **Obsidian vault** of its own. The project points at it with a symlink instead of holding a
copy. Change something here and you change it at the source.

One long page is worth a look: [[en/examples/long-article|A long article]] — headings down to the
sixth level, so the table of contents is complete.
