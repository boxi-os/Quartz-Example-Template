---
title: Wikilinks
description: The Obsidian notation for internal links.
section: Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/wikilinks
cover: "[[assets/covers/cover-links.svg]]"
---

```md
[[en/2-formatting/02-structure/headings]]
[[en/2-formatting/02-structure/headings|with text of your own]]
```

[[en/2-formatting/02-structure/headings]]
[[en/2-formatting/02-structure/headings|with text of your own]]

## Short form

As long as the file name is unique within the [[en/7-reference/01-glossary#Vault|vault]], it is enough on its own:

```md
[[headings]]
```

[[headings]]

The *Crawl links* [[en/7-reference/01-glossary#Plugin|plugin]] resolves the path at [[en/7-reference/01-glossary#Build|build]] time. This template runs on
`markdownLinkResolution: shortest` — the shortest unambiguous notation wins.

> [!note] Two languages, two file names
> This is one reason the English pages carry English file names: `headings` finds the English page,
> `ueberschriften` the German one. Had both languages used the same names, the short form would
> have become ambiguous — see [[en/6-adapting/07-two-languages/index|Two languages]].

## A link into nothing

```md
[[does-not-exist]]
```

[[does-not-exist]]

A wikilink to a page that does not exist stays a link. In Obsidian you recognise it by its pale
colour; on the built site it leads nowhere. Before publishing, a look at the list of unresolved
links in Obsidian is worth it.

## In this template

**Out of the box** Quartz colours internal links in the secondary colour, without an underline.

**In this template** they are underlined as well — a colour alone is no hint to some readers that
something can be clicked. The underline sits lower than usual (`text-underline-offset`) and is
semi-transparent, so that it does not cut through the descenders.
