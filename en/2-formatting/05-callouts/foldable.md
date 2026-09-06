---
title: Foldable callouts
description: A callout that can be folded away.
section: Formatting
tags:
  - formatting
  - callouts
translationKey: formatierung/callouts/faltbar
cover: "[[assets/covers/cover-callouts.svg]]"
---

A `-` or `+` after the type makes the [[en/7-reference/01-glossary#Callout|callout]] foldable.

````md
> [!question]- Folded (minus)
> Only appears when unfolded.

> [!question]+ Unfolded (plus)
> Starts open, can be folded away.
````

> [!question]- Folded (minus)
> Only appears when unfolded.

> [!question]+ Unfolded (plus)
> Starts open, can be folded away.

## In this template

The title is the control. It therefore gets a focus ring of its own in the type colour — **out of
the box** it is clickable but not recognisable as a control from the keyboard.

The arrow turns when unfolding; with `prefers-reduced-motion` on it jumps instead.

> [!warning] Folded content is still in the document
> Anyone searching or printing the page gets the folded text too. Foldable means "tidy", not
> "hidden".
