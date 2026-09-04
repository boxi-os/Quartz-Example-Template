---
title: Tags
description: Markers under the title and in the body text.
section: Design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/tags
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Out of the box

Tags appear as links under the title, with a background and a border.

## In this template

**One rule for every place.** A tag looks the same in the tag list, in the properties, in "recently
changed" and in a folder listing: a pill with the hash in front of it, in the accent colour on a
tinted surface. A thing that looks different in four places is four things to learn.

**With one exception:** in the body text a tag loses its pill and keeps only the colour. A paragraph
full of pills is unreadable. To be seen under
[[en/formatting/special/arrows-and-emoji|Arrows, tags and emoji]].

The hash sits in the stylesheet as a `::before` and is slightly transparent — it belongs to the
tag, but it is not its name.

On hover the surface changes and the border appears in the accent colour; the pill does not jump
while doing so, because the border was already there, transparent.

> [!note] English tags, English tag pages
> The English pages carry English tags (`formatting` rather than `formatierung`), so each language
> gets its own tag pages. A shared tag would have collected both languages into one listing.
