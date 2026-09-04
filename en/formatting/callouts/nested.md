---
title: Nested callouts
description: A callout inside a callout — and where the limit is.
section: Formatting
tags:
  - formatting
  - callouts
translationKey: formatierung/callouts/verschachtelt
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

````md
> [!info] Outside
> Text in the outer callout.
>
> > [!tip] Inside
> > The inner one loses its frame but keeps the colour bar.
````

> [!info] Outside
> Text in the outer callout.
>
> > [!tip] Inside
> > The inner one loses its frame but keeps the colour bar.

## Two levels deep

````md
> [!example] First level
> > [!note] Second level
> > > [!tip] Third level
> > > It works, but it is rarely a good idea.
````

> [!example] First level
> > [!note] Second level
> > > [!tip] Third level
> > > It works, but it is rarely a good idea.

## In this template

A nested callout gives up its own frame and keeps only the colour bar on the left. Two complete
boxes inside one another read as a mistake, not as structure.

**Out of the box** the inner callout keeps its whole frame, corners and all.
