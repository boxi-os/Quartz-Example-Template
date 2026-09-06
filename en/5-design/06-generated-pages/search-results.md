---
title: Search results
description: The list in the search overlay.
section: Design
tags:
  - design
  - page-types
translationKey: gestaltung/erzeugte-seiten/suchergebnisse
---

## Out of the box

Cards with a title, a path and an excerpt.

## In this template

- **Not cards but rows**, with hairlines between them. A list of ten framed boxes is restless.
- **The keyboard cursor and the pointer [[en/7-reference/01-glossary#Hover|hover]] look the same**: a tinted surface plus a bar on the
  left. The arrow keys move through the list, and the highlighted row is the only signal of where
  you are — it must not look different from what the pointer shows.
- **The excerpt** is truncated after two lines.
- **The match in the text** is marked with the same colour as `==highlight==` in the body text.
  "This is what you were looking for" means the same thing across the whole site.
- **The path** is set in the code typeface, muted and small — it is origin, not content.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 17 variables are read by `page-search-results.scss`. They can be changed in the app under *Styles → Variables* — without a line of [[en/7-reference/01-glossary#CSS and SCSS|CSS]].

| Variable | Value | also applies to |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 other components |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--textHighlight` | `rgba(226, 189, 92, 0.45)` · dark `rgba(140, 184, 218, 0.30)` | Body text |
| `--tpl-accent-bar` | `3px` | 5 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-3xs` | `0.125rem` | 6 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-text-base` | `1rem` | 4 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |

*This table is generated: it is read out of the [[en/7-reference/01-glossary#Stylesheet|stylesheets]] rather than kept by hand.*
<!-- QuartzControl:variables:end -->
