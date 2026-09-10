---
title: The property table
description: The frontmatter table under the title.
section: 5 – The design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/eigenschaften
---

## Where it stands

It once stood between the date and the text and today stands **below the article**, after the box
“Read on”. The reason is what it is for: whoever opens a page wants to read what is on it — not a
table of its metadata first. The two entries that genuinely help on arrival still stand at the top:
date and tags.

This page nonetheless sits in *Above the content*, because it belongs to the title block it
describes.

## Out of the box

A plain table in the text colour, collapsible.

## In this template

- on a **tinted surface** with a border and rounded corners
- the **header row** capitalised, small and muted — it is a label, not content, and since
  2026-09-05 it carries no rule beneath it: a second horizontal so close to the box's own edge
  reads as a seam
- the **key** muted and as wide as its text, the **value** takes the rest
- **value types** are distinguished: a number in figure width, a boolean as a coloured word, a list
  as a row of markers, an empty field in italics

To be seen under [[en/2-formatting/11-properties/data-types|Data types]], where one page brings all four
types with it.

## The finding about cell width

The obvious solution for "the key is as wide as its content" is `width: 1%` on the key cell.
Measured: the cell became 7.94 px wide — exactly 1 % of the table — and the key lay on top of the
value.

The way that works is the other way round: **`width: 100%` on the value cell.** It claims
everything that is left over and leaves the key its content width.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 16 variables are read by `meta-note-properties.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 other components |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--tpl-positive` | `#136B34` · dark `#6DD68F` | only here |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 15 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
