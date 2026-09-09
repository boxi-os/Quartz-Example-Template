---
title: Tags
description: Markers under the title and in the body text.
section: 5 – The design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/tags
---

## Out of the box

Tags appear as links under the title, with a background and a border.

## In this template

**One rule for every place.** A tag looks the same in the tag list, in the properties, in "recently
changed" and in a folder listing: a pill with the hash in front of it, in the accent colour on a
tinted surface. A thing that looks different in four places is four things to learn.

**With one exception:** in the body text a tag loses its pill and keeps only the colour. A paragraph
full of pills is unreadable. To be seen under
[[en/2-formatting/13-special/arrows-and-emoji|Arrows, tags and emoji]].

The hash sits in the [[en/7-reference/01-glossary#Stylesheet|stylesheet]] as a `::before` and is slightly transparent — it belongs to the
tag, but it is not its name.

On [[en/7-reference/01-glossary#Hover|hover]] the surface changes and the border appears in the accent colour; the pill does not jump
while doing so, because the border was already there, transparent.

> [!note] English tags, English tag pages
> The English pages carry English tags (`formatting` rather than `formatierung`), so each language
> gets its own tag pages. A shared tag would have collected both languages into one listing.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 12 variables are read by `meta-tag-list.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--icon-tag` | set in the stylesheet (`base.scss`) | only here |
| `--tag-background` | — | only here |
| `--tag-background-hover` | — | only here |
| `--tag-color` | — | only here |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
