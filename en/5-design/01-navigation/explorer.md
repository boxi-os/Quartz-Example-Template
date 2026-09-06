---
title: The explorer
description: The folder tree on the left — designed down to the fourth level.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/explorer
---

On the left of the window stands the tree over all the notes. It is the component that took the
most design work in this template, because depth is the actual problem.

## Out of the box

Quartz indents every level and colours the active entry. On level three or four it is no longer
possible to tell which parent folder a file belongs to — the indent alone does not carry the
structure.

## In this template

- **A guide line per level.** Every nested list gets a hairline to its parent folder. At four
  levels that is four lines for the eye to find its way back along.
- **Weight falls with depth.** Level 1 is bold, level 2 semibold, from level 3 on normal and
  smaller. The head of a branch can therefore be found.
- **From level five on there is no further indent**, only the line — five indents leave no room for
  a word in a bar three columns wide.
- **A symbol in front of every row.** Folders carry a folder icon that looks different open and
  closed, files a file icon — both from the Lucide set. The row says *what* it is before it says
  what it is called.
- **The active entry** gets colour, semibold *and* a bar on the left.
- **The whole path to it is marked.** Every folder the open page sits under colours its name and
  its symbol in the accent, and the guide line of the direct parent colours with it. Before, an
  unfolded folder looked exactly like one somebody had unfolded by hand ten minutes earlier — the
  trail from the root to the current page was invisible.
- **Every disclosure arrow is the same Lucide chevron.** Before, the head of the tree, every
  folder, the table of contents and the collapsible [[en/7-reference/01-glossary#Layout box|layout box]] drew four different ones.
- **Long names** are truncated rather than wrapped; three lines for a file name tear the tree
  apart.
- **A long tree scrolls inside itself** (60 % of the window height) rather than pushing the footer
  away, and **fades out softly at the top and the bottom**. The box carries exactly as much padding
  as the edge is deep: at the very top the first row therefore sits *below* the gradient rather
  than inside it, at the very bottom the last row above it. Both ends are read at full strength;
  only what is passing through goes soft.
- **On a phone it is a drawer.** The button sits in the app bar, becomes a cross when opened, the
  drawer travels in from the left over a darkened page, and the page itself does not scroll along
  meanwhile.

It is best seen under [[en/2-formatting/05-callouts/basics|Callouts — the basic form]] — three
folders deep, and a fully unfolded branch in the explorer.

## Two languages, one tree

The explorer knows nothing about languages: it [[en/7-reference/01-glossary#Build|builds]] its tree from every page of the build, so
without help it would show the German and the English tree at once. The template solves that in
[[en/7-reference/01-glossary#CSS and SCSS|CSS]]. On a German page the `en` folder is hidden; on an English page everything except it is hidden,
and the folder's own row is taken out so that the English tree stands at the top level rather than
one indent in.

The [[en/7-reference/01-glossary#Plugin|plugin]]'s own answer — a `filterFn` for the explorer — cannot be reached from here: it is taken
only from `quartz.ts`, and this project builds its layout from `quartz.config.yaml`. See
[[en/6-adapting/07-two-languages/limits|Where the two languages stop]].

## Which element actually scrolls

That had to be settled before the mask and the edge could sit in the right place at all. Quartz
gives the inner list `max-height: 100%` — and the two browsers resolve that differently:

| | scrolling element | box | list |
| --- | --- | --- | --- |
| Chrome | the inner `ul` | 540 px, no overflow | 540 px, 148 px of overflow |
| Firefox | the box `.explorer-content` | 540 px, 148 px of overflow | 688 px, no overflow |

Measured on the same page: 148 px of overflow in both, but on two different elements. Everything
this template hangs on the scrolling — the soft edge, the contained overscroll, the thin scrollbar
— sits on `.explorer-content`. In Chrome that was an element which does not scroll.

The list therefore gives up its cap (`max-height: none; overflow: visible`), and the box is the one
scroller in both browsers.

## Two findings while building

The class names are misleading. **Only the root list is called `explorer-ul`**; every nested one is
called `ul.tree-item-children`. And **`.nav-file-title` is the link itself**, not its parent. The
first version of this file therefore styled into nothing — which was not visible, because Quartz's
own indent looked similar enough.

When folded, Quartz caps the whole component at `1.2em`. Anyone giving their heading a target size
of 44 px loses it entirely. This template therefore moves the folding to the content and leaves the
head standing.

## What the plugin cannot do

> [!warning] The folders start folded, and the option against it has no effect
> `@quartz-community/explorer` 0.1.0 knows `folderDefaultState: 'open'` and dutifully writes the
> value into the markup — its own script simply never reads it. It takes the fold state solely from
> `localStorage` and assumes *folded* for everything that is not in there. Open, therefore, are
> only the folders on the way to the current page.
>
> A [[en/7-reference/01-glossary#Stylesheet|stylesheet]] cannot cure that: "open" and "never touched" carry the same class, and CSS cannot
> tell the two apart.

The explorer **itself** — the whole component — is unfolded and stays that way; only on a phone
does it start closed, since otherwise half the navigation would stand in front of the text.

> [!bug] And one that was self-inflicted
> Exactly that went wrong for a while: a rule of this template gave the drawer button
> `display: grid` without restricting it to narrow windows. Because everything here is unlayered,
> that beat Quartz's own `display: none` — the button was there at 1600 px too. And the plugin's
> script ends with "if this button is visible, fold the tree". So the tree was folded on every
> desktop view, although it had been rendered.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 32 variables are read by `nav-explorer.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 other components |
| `--icon-close` | set in the stylesheet (`base.scss`) | only here |
| `--icon-file` | set in the stylesheet (`base.scss`) | only here |
| `--icon-folder` | set in the stylesheet (`base.scss`) | only here |
| `--icon-folder-open` | set in the stylesheet (`base.scss`) | only here |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-accent-bar` | `3px` | 5 other components |
| `--tpl-drawer-width` | `min(86vw, 340px)` | only here |
| `--tpl-icon` | `1.1rem` | Colour scheme switch, Reader mode |
| `--tpl-icon-sm` | `0.95rem` | 6.4 Variables, The language switcher |
| `--tpl-indent` | `0.85rem` | Table of contents |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-lg` | `14px` | 3 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dark `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
