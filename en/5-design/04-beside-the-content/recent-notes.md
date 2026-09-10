---
title: Recently changed
description: The most recent notes as a box below the text.
section: 5 – The design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/neben-dem-inhalt/zuletzt-geaendert
---

## Out of the box

A list of the most recently edited pages with date, description and tags.

## In this template

Capped at five entries, separated by hairlines, and **boiled down to one line of title plus date**.

Measured before the boiling down: one entry was 113 px tall, five of them filled 700 px of a sidebar
that also carried the tree and the note box. Today it is 54 px per entry and 320 px for the whole
box.

Two of the three lines were an accident. The rule for the box's own heading read
`.recent-notes h1, h2, h3` — and every entry title *is* an `h3`, so all five were being set in small
caps with letter-spacing. The selector now names the box's own child (`> h3`) and nothing deeper.
Description and tag pills are gone entirely: the one repeats the title at half the legibility, the
others are taller than the entry they label.

A third gap came from the `li` itself. Quartz gives every list item 1 rem above and below, the
[[en/7-reference/01-glossary#Backlinks|backlinks]] take it back, this box did not — 32 px per entry nobody had asked for, 160 of 408 px
in total. That is why it stood a head taller than the box beside it, and why the gap under the
heading read as an indent.

## Where it stands

**Below the text**, not in the sidebar, and there in a row with the backlinks — two boxes side by
side, always in two columns above phone width, one below the other underneath. Until 2026-09-10 it
stood at the top left in the sidebar under the [[en/7-reference/01-glossary#Explorer|explorer]]; there it was a third list in a column
that already carried two.

It is therefore no longer restricted to the desktop either. A box under the article is no obstacle
on a phone but the thing that comes after reading.

## Folder pages do not appear in it

`hideFolderPages: true` takes every `…/index` page out of the list, the two home pages included.
Without that option the box was the top of the outline rather than a list of notes: four folder and
home pages out of five, and on the home page it listed itself, twice, because both languages are
called “Example”.

That follows from this vault's file times tracking the outline — they are staggered so the list has
an order at all, and what stands at the top is then the table of contents. A box called “recently
edited” should show notes.

## A find while building

This component uses **the same class names** as the folder and tag listings: `.section`, `.meta`,
`.desc`, `.tags`. The template's listing rules were not scoped at first and therefore landed here as
well — in the then still narrow sidebar the three-column grid stacked date and title on top of each
other.

Since then every listing rule is scoped to `.page-listing`. The lesson: **a class name does not
belong to the component you first saw it in.**

> [!note] Both languages in one list
> The list is built from every page of the [[en/7-reference/01-glossary#Build|build]], so an English page can turn up in the box of a
> German one. There is no language filter — the option for it is a function and cannot be written in
> a YAML configuration. As with the search index, only one build per language would separate them —
> see [[en/6-adapting/07-two-languages/limits|Where the two languages stop]].

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 13 variables are read by `aside-recent-notes.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--secondary` | `#1463A3` · dark `#699DC3` | 20 other components |
| `--tpl-leading-snug` | `1.4rem` | 4 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 15 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
