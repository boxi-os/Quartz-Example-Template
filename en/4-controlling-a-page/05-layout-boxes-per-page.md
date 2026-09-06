---
title: 4.5 Layout boxes per page
description: Hiding, renaming or refilling a layout box on a single page — in the frontmatter, not in the configuration.
section: 4 Controlling a page
tags:
  - controlling-a-page
  - layout-box
layoutBoxNote: false
layoutBoxCta:
  html: "<p>On this one page this box shows a different text — set in the frontmatter, not in the configuration.</p>"
translationKey: seiten-steuern/layout-boxen-je-seite
---

A **layout box** is a box with content of its own that the [[en/7-reference/01-glossary#Plugin|plugin]] *quartz-layout-box* places at
one spot of the page layout — the word mark at the top, the box “About this handbook” on the
left, the box “Read on” below the text. This template has five of them; what each does stands in
[[en/5-design/05-layout-boxes/index|5.5 Layout boxes]]. Here it is about how a single page can
have one of them differently.

This page controls two of the five instances through its own [[en/7-reference/01-glossary#Frontmatter|frontmatter]]:

```yaml
---
layoutBoxNote: false
layoutBoxCta:
  html: "<p>A different text, on this page only.</p>"
---
```

**What you should see:** the box “About this handbook” in the left column is missing here — on
every other page it is there. And the box below this text shows different content than usual.

## The three forms

| In the frontmatter | Effect |
| --- | --- |
| `layoutBoxNote: false` | hide the box on this page |
| `layoutBoxNote: other.md` | load a different snippet from the same folder |
| `layoutBoxNote: {html: "…"}` | set your own content; `{file: "…"}` and `{hidden: true}` work too |

In the long form the key takes six fields: `hidden`, `file`, `html`, `title`, `collapsible` and
`collapsed`. A page may therefore also rename its box or fold it away, not just refill it.

## The five keys of this template

| Key | Place | What the box is |
| --- | --- | --- |
| `layoutBoxMark` | header | the word mark, one image per [[en/7-reference/01-glossary#Colour scheme\|colour scheme]] |
| `layoutBoxNote` | left column | “About this handbook”, from a [[en/7-reference/01-glossary#Markdown\|Markdown]] file, collapsible |
| `layoutBoxHint` | left column | a hint, on narrow screens only |
| `layoutBoxCta` | after the content | “Read on”, with placeholders |
| `layoutBoxColophon` | footer | the colophon line |

## Why every instance has a key of its own

Without `frontmatterKey` in the configuration a single `layoutBox: false` would switch off **all
five** boxes at once. The template therefore gives every instance a name of its own — which is
also the procedure the plugin documents for multiple use.

## When the frontmatter is the right place — and when it is not

What holds for **this one page** belongs here. What holds for **every page of one language**
belongs in the configuration under `byLang` — otherwise the same exception stands in a hundred
files. That is exactly what happened here once: the English pages carried their four boxes
themselves, until the plugin got `byLang`. See
[[en/5-design/05-layout-boxes/the-five-instances|The five instances]].

When both apply, the frontmatter wins. The order is:

1. this page's frontmatter
2. `byLang` for this page's language
3. the entry's [[en/7-reference/01-glossary#Base|base]] setting

This page is the proof of it: in both languages its box below the text shows its own text from
the frontmatter, but carries the heading `byLang` sets for that language.
