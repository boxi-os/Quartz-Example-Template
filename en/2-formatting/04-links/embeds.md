---
title: Embedding a page
description: Showing another page in the middle of this one.
section: 2 – Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/einbettungen
cover: "[[assets/covers/cover-links.svg]]"
---

An exclamation mark in front of the [[en/7-reference/01-glossary#Wikilink|wikilink]] embeds the content instead of linking to it.

```md
![[en/2-formatting/02-structure/horizontal-rules]]
```

![[en/2-formatting/02-structure/horizontal-rules]]

## Only one section

```md
![[en/2-formatting/04-links/wikilinks#Short form]]
```

![[en/2-formatting/04-links/wikilinks#Short form]]

## Only one block

With the block identifier from [[en/2-formatting/04-links/targets|Jump targets]]:

```md
![[en/2-formatting/04-links/targets#^keypoint]]
```

![[en/2-formatting/04-links/targets#^keypoint]]

That is the finest step: a single paragraph instead of a whole page or a section.

## An image from outside

A URL can be embedded too:

```md
![Description](https://example.com/image.png)
```

That loads from a foreign server on every page view. For a site meant to work offline and in ten
years' time, the file in the [[en/7-reference/01-glossary#Vault|vault]] is the better choice.

## What this template does differently

An embedded page gets a dashed bar on the left and a tinted surface — you should see where foreign
content begins and ends. **Out of the box** the embed is not visually separated from the
surrounding text.

> [!warning] Careful with chains
> If the embedded page embeds something in turn, the page quickly becomes hard to follow — and a
> circle (A embeds B, B embeds A) is an error that only the [[en/7-reference/01-glossary#Build|build]] reveals.

> [!bug] An embed brings its heading ids along
> Unchanged, at that. Quartz builds a heading's id from its text — “In this template” becomes
> `in-this-template` — and does not check on embedding whether the target page already has it. If a
> heading of the embedded page is called the same as one of the embedding page, **two** elements
> carry the same id.
>
> That is exactly what stood on this page until 2026-09-10: the embedded opening carries “In this
> template”, and so was the last section here called. Measured on the built page, that had three
> consequences:
>
> - The link in the [[en/5-design/04-beside-the-content/table-of-contents|table of contents]] jumped
>   to the **first** of the two — to pixel 1005 instead of 2681. On a duplicate id a browser always
>   takes the first.
> - The last entry of the outline was already marked at the **very top**. The plugin's script maps a
>   heading to its entry through the id; both headings therefore pointed at the same entry, and it
>   obeyed whichever stood higher up.
> - The progress bar consequently had a **hole**: halfway down, the first, second and fourth entries
>   were marked and the third was not.
>
> It can only be fixed where the ids are made. What helps here is renaming the heading — which is
> why the section above is called “What this template does differently” and not what the rest of
> this chapter calls it. Whoever embeds a whole page does well to check once whether two headings
> get in each other's way.
