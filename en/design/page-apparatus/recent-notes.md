---
title: Recently changed
description: The most recent notes in the sidebar.
section: Design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/seitenapparat/zuletzt-geaendert
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Out of the box

A list of the most recently edited pages with date, description and tags.

## In this template

Limited to five entries, separated by hairlines, description truncated after two lines. Visible
only on the desktop — on a phone the sidebar stands above the content, and there this list is in
the way.

## A finding while building

This component uses **the same class names** as the folder and tag listings: `.section`, `.meta`,
`.desc`, `.tags`. The template's listing rules were not scoped at first and therefore landed here as
well — in the narrow sidebar the three-column grid stacked date and title on top of each other.

Since then every listing rule is scoped to `.page-listing`. The lesson: **a class name does not
belong to the component you first saw it in.**

> [!note] Both languages in one list
> The list is built from every page of the build, so a German page can appear in the sidebar of an
> English one. Like the search index, that would only be separated by one build per language — see
> [[en/design/multilingual/limits|Where the two languages stop]].
