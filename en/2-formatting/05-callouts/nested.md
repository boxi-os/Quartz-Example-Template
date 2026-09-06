---
title: Nested callouts
description: A callout inside a callout — and where the limit is.
section: Formatting
tags:
  - formatting
  - callouts
translationKey: formatierung/callouts/verschachtelt
cover: "[[assets/covers/cover-callouts.svg]]"
---

````md
> [!info] Outside
> Text in the outer callout.
>
> > [!tip] Inside
> > The inner one loses its frame but keeps the colour bar.
````

> [!info] Outside
> Text in the outer [[en/7-reference/01-glossary#Callout|callout]].
>
> > [!tip] Inside
> > The inner one loses its [[en/7-reference/01-glossary#Frame|frame]] but keeps the colour bar.

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
