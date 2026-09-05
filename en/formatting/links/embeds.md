---
title: Embedding a page
description: Showing another page in the middle of this one.
section: Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/einbettungen
---

An exclamation mark in front of the wikilink embeds the content instead of linking to it.

```md
![[en/formatting/structure/horizontal-rules]]
```

![[en/formatting/structure/horizontal-rules]]

## Only one section

```md
![[en/formatting/links/wikilinks#Short form]]
```

![[en/formatting/links/wikilinks#Short form]]

## Only one block

With the block identifier from [[en/formatting/links/targets|Jump targets]]:

```md
![[en/formatting/links/targets#^keypoint]]
```

![[en/formatting/links/targets#^keypoint]]

That is the finest step: a single paragraph instead of a whole page or a section.

## An image from outside

A URL can be embedded too:

```md
![Description](https://example.com/image.png)
```

That loads from a foreign server on every page view. For a site meant to work offline and in ten
years' time, the file in the vault is the better choice.

## In this template

An embedded page gets a dashed bar on the left and a tinted surface — you should see where foreign
content begins and ends. **Out of the box** the embed is not visually separated from the
surrounding text.

> [!warning] Careful with chains
> If the embedded page embeds something in turn, the page quickly becomes hard to follow — and a
> circle (A embeds B, B embeds A) is an error that only the build reveals.
