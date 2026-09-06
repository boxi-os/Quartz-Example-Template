---
title: Backlinks
description: What points at this page.
section: Design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/neben-dem-inhalt/rueckverweise
---

Below the table of contents stands which other notes link to the current one.

## Out of the box

A list of titles. The empty state reads "No backlinks found".

## In this template

- The entries are separated by **hairlines** rather than by space — in a narrow column that saves
  room and reads more calmly.
- A long title is **truncated after two lines**. A list full of three-line titles is a wall.
- The **empty state** is set in italics and muted: it should look like an answer, not like an
  error.

## On the wording

The template renames the component in its language file — "Links here" instead of "Backlinks".
That is a word from the tool, not from the language.

> [!warning] This renaming has no effect
> Measured: every visible heading on a Quartz 5 page comes from a component **[[en/7-reference/01-glossary#Plugin|plugin]]**, and each of
> those npm packages brings its own compiled translations with it. The project's language file does
> not reach them. The entry is in the template all the same — the mechanism is right, only its
> reach is small today.

> [!note] Backlinks do not cross the language boundary
> A German page links to German pages, an English one to English pages, so the two backlink lists
> stay separate. That is not something the plugin does — it follows from the fact that every page
> only links within its own tree.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 9 variables are read by `aside-backlinks.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
