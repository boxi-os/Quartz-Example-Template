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
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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

## Why every instance has a key of its own

Without `frontmatterKey` a single `layoutBox: false` would switch off **all five** boxes at once.
The template therefore gives every instance a name of its own — which is also the procedure the
plugin documents for multiple use.

## What this is used for here

The English pages of this site use exactly this: they point `layoutBoxNote` at an English snippet
and give the hint, the call to action and the colophon English text. It is the only lever that makes a
per-language difference within one build.
