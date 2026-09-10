---
title: Backlinks
description: What points at this page.
section: 5 – The design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/neben-dem-inhalt/rueckverweise
---

Directly below the text stands which other notes link to the current one — as a box beside the one
holding the [[en/5-design/04-beside-the-content/recent-notes|recently changed pages]].

## Out of the box

A list of titles. The empty state reads "No backlinks found".

## In this template

- The entries are separated by **hairlines** rather than by space — in a narrow column that saves
  room and reads more calmly.
- A long title is **truncated after two lines**. A list full of three-line titles is a wall.
- The **empty state** is set in italics and muted: it should look like an answer, not like an
  error.

## Where it stands

Until 2026-09-10 this box stood in the right column, below the table of contents. It now stands
below the text, because that is where it belongs: what points at a page is a question you ask
*after* reading, not beside it — and in the right column it shared the space with an outline that is
needed while reading.

It shares its row with the box “Recently changed” and is the right-hand one of the two. Above phone
width the two always stand side by side, even when one of them stays empty — the other then takes
the full width.

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

These 11 variables are read by `aside-backlinks.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--icon-arrow-up-right` | set in the stylesheet (`base.scss`) | only here |
| `--secondary` | `#1463A3` · dark `#699DC3` | 20 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 15 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
