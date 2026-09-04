---
title: Arrows, tags and emoji
description: Small things Obsidian converts in passing.
section: Formatting
tags:
  - formatting
  - special
translationKey: formatierung/besonderes/pfeile-und-emoji
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Arrows

The *Obsidian flavored markdown* plugin turns character sequences into real arrows:

```md
--> and <-- and <--> and ==>
```

--> and <-- and <--> and ==>

## Tags in the text

```md
A sentence with an #inline-tag in the middle of it.
```

A sentence with an #inline-tag in the middle of it.

A tag in the body text counts just as much as one in the frontmatter: it appears on the tag page
and in the tag list.

**In this template** a tag inside a paragraph loses its pill shape and keeps only the colour — a
paragraph full of pills is unreadable. Under the title, where the tags stand collected, they keep
the pill.

### Tags with levels

A slash tiers tags:

```md
#area/sub-area
```

Every level gets a tag page of its own, and the parent collects the children as well. Good for a
vocabulary meant to grow — `#source/book` and `#source/article` then both sit under `#source`.

## Emoji

```md
Inserted directly: 📐 ✓ ⚠️
```

Inserted directly: 📐 ✓ ⚠️

> [!tip] Emoji are no substitute for text
> A screen reader reads out "warning sign", not "attention". Fine as decoration next to a word, not
> as the sole carrier of a piece of information.
