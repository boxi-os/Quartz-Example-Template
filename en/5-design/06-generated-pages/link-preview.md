---
title: Link preview
description: What appears when hovering an internal link.
section: Design
tags:
  - design
  - page-types
translationKey: gestaltung/erzeugte-seiten/vorschau
---

## Out of the box

A box with the start of the target page.

## In this template

It carries a real shadow — one of the five places that genuinely float above the page. An
opaque surface, because a translucent preview over body text is unreadable.

The content is **capped at 20 rem**, and at the cut lies a soft gradient: a truncated preview should
look cut, not broken.

What is left out inside it is what only gets in the way in a preview: [[en/7-reference/01-glossary#Callout|callouts]], tags and code
blocks. A preview should answer the question of whether the click is worth it — no more.

## Only with a pointer

With `@media (hover: none)` it is switched off entirely. From that follows a rule for the content:
**no information may exist only in a preview**, because on a phone there is none.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 13 variables are read by `page-popover.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--tpl-radius-lg` | `14px` | 3 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dark `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-lg` | `1.15rem` | 6.4 Variables, Search |
| `--tpl-text-sm` | `0.875rem` | 18 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
