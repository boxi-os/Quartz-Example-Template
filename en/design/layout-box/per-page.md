---
title: Controlling it per page
description: Hiding a box on a single page or filling it differently.
section: Design
tags:
  - design
  - layout-box
layoutBoxNote: false
layoutBoxCta:
  html: "<p>On this one page this box shows a different text — set in the frontmatter, not in the configuration.</p>"
translationKey: gestaltung/layout-box/je-seite-steuern
---

This page controls two of the five instances through its own frontmatter:

```yaml
---
layoutBoxNote: false
layoutBoxCta:
  html: "<p>A different text, on this page only.</p>"
---
```

**What you should see:** the box in the left column is missing here — on every other page it is
there. And the box below this text shows different content than usual.

## The three forms

| In the frontmatter | Effect |
| --- | --- |
| `layoutBoxNote: false` | hide the box on this page |
| `layoutBoxNote: other.md` | load a different snippet from the same folder |
| `layoutBoxNote: {html: "…"}` | set your own content; `{file: "…"}` and `{hidden: true}` work too |

In the long form the key takes six fields: `hidden`, `file`, `html`, `title`, `collapsible` and
`collapsed`. A page may therefore also rename its box or fold it away, not just refill it.

## Why every instance has a key of its own

Without `frontmatterKey` a single `layoutBox: false` would switch off **all five** boxes at once.
The template therefore gives every instance a name of its own — which is also the procedure the
plugin documents for multiple use.

## When the frontmatter is the right place — and when it isn't

What holds for **this one page** belongs here. What holds for **every page of one language**
belongs in the configuration under `byLang` — otherwise the same exception stands in a hundred
files. That is exactly what happened here once: the English pages carried their four boxes
themselves, until the plugin got `byLang`. See
[[en/design/layout-box/the-five-instances|The five instances]].

When both apply, the frontmatter wins. The order is:

1. this page's frontmatter
2. `byLang` for this page's language
3. the entry's base setting

This page is the proof of it: in both languages its call-to-action box shows its own text from the
frontmatter, but carries the heading `byLang` sets for that language.
