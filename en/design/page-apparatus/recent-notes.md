---
title: Recently changed
description: The most recent notes in the sidebar.
section: Design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/seitenapparat/zuletzt-geaendert
---

## Out of the box

A list of the most recently edited pages with date, description and tags.

## In this template

Limited to five entries, separated by hairlines, and **boiled down to one line of title plus a
date**. Visible only on the desktop — on a phone the sidebar stands above the content, and there
this list is in the way.

Measured before the boiling down: one entry was 113 px tall, and five of them filled 700 px of a
bar that also carries the tree and a note box. Afterwards: 57 px per entry, 398 px for the box.

Two of the three lines were an accident. The rule for the box's own heading read
`.recent-notes h1, h2, h3` — and every entry title *is* an `h3`, so all five were being set in
small caps with letter-spacing. The selector now names the box's own child (`> h3`) and nothing
deeper. The description and the tag pills are gone entirely: the one repeats the title at half the
legibility, the others are taller than the entry they label.

## A finding while building

This component uses **the same class names** as the folder and tag listings: `.section`, `.meta`,
`.desc`, `.tags`. The template's listing rules were not scoped at first and therefore landed here as
well — in the narrow sidebar the three-column grid stacked date and title on top of each other.

Since then every listing rule is scoped to `.page-listing`. The lesson: **a class name does not
belong to the component you first saw it in.**

> [!note] Both languages in one list
> The list is built from every page of the build, so a German page can appear in the sidebar of an
> English one. Like the search index, that would only be separated by one build per language — see
> [[en/design/multilingual/limits|Where the two languages stop]].

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 13 variables are read by `aside-recent-notes.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tpl-leading-snug` | `1.45` | 3 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-xs` | `0.5rem` | 21 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-text-xs` | `0.78rem` | 8 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
