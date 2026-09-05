---
title: Arrows, tags and emoji
description: Small things Obsidian converts in passing.
section: Formatting
tags:
  - formatting
  - special
translationKey: formatierung/besonderes/pfeile-und-emoji
---

## Arrows

Obsidian turns character sequences like `-->` into real arrows. The option for it is called
`parseArrows` and stands at `true` in this template. The line below shows what becomes of it:

```md
--> and <-- and <--> and ==>
```

--> and <-- and <--> and ==>

> [!failure] None of them survives to the site
> Measured on the built page it reads `—> and <— and <—> and ==>`. Two things go wrong there, and
> they are independent of each other:
>
> 1. **`parseArrows` converts nothing.** Counter-test with *GitHub flavored markdown* switched off:
>    the line then reads `--> and <-- and <--> and ==>`, still the raw text. The option is set and
>    stays without effect.
> 2. **The dash replacement happens anyway.** *GitHub flavored markdown* turns every `--` into an
>    em dash before anyone looks for an arrow. `-->` becomes `—>`.
>
> In Obsidian you see arrows, on the site you do not. Whoever means an arrow writes one:
> → ← ↔ ⇒ — this template's typefaces draw all four. See
> [[en/formatting/text/special-characters|Special characters]].

## Tags in the text

```md
A sentence with an #inline-tag in the middle of it.
```

A sentence with an #inline-tag in the middle of it.

A tag in the body text counts just as much as one in the frontmatter: it appears on the tag page
and in the tag list.

> [!bug] The link on it is broken
> Measured on the built page, the tag in the paragraph above points at
> `../../.././../../tags/inline-tag` — one `../` too many, a path that leads out of the site. The
> same tag in the list below the title links perfectly correctly. Both links are produced in the
> same build, just in different places: `parseTags` in *Obsidian flavored markdown* miscounts the
> way back to the root for a tag in the body text. A bug in Quartz, not in this template.

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
