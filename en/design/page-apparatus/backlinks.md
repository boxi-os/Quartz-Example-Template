---
title: Backlinks
description: What points at this page.
section: Design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/seitenapparat/rueckverweise
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

Below the table of contents stands which other notes link to the current one.

## Out of the box

A list of titles. The empty state reads "No backlinks found".

## In this template

- The entries are separated by **hairlines** rather than by space — in a narrow column that saves
  room and reads more calmly.
- A long title is **truncated after two lines**. A list full of three-line titles is a wall.
- The **empty state** is set in italics and muted: it should look like an answer, not like an
  error.

## On the wording

The template renames the component in its language file — "Links here" instead of "Backlinks".
That is a word from the tool, not from the language.

> [!warning] This renaming has no effect
> Measured: every visible heading on a Quartz 5 page comes from a component **plugin**, and each of
> those npm packages brings its own compiled translations with it. The project's language file does
> not reach them. The entry is in the template all the same — the mechanism is right, only its
> reach is small today.

> [!note] Backlinks do not cross the language boundary
> A German page links to German pages, an English one to English pages, so the two backlink lists
> stay separate. That is not something the plugin does — it follows from the fact that every page
> only links within its own tree.
