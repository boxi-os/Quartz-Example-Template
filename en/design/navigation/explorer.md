---
title: The explorer
description: The folder tree on the left — designed down to the fourth level.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/explorer
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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
  folder, the table of contents and the collapsible layout box drew four different ones.
- **Long names** are truncated rather than wrapped; three lines for a file name tear the tree
  apart.
- **A long tree scrolls inside itself** (60 % of the window height) rather than pushing the footer
  away, and fades out softly while doing so — but **only on the side where there is more to come**.
  At the very top the first row is whole, at the very bottom the last one is, and a tree that is
  showing everything anyway does not fade at all. Two registered lengths on `scroll(self block)`
  carry that; where there is nothing to scroll there is no timeline and both stay at zero.
- **On a phone it is a drawer.** The button sits in the app bar, becomes a cross when opened, the
  drawer travels in from the left over a darkened page, and the page itself does not scroll along
  meanwhile.

The best place to see this is under
[[en/handbook/basics/terms/abbreviations/list|List]] — four folders deep.

## Two languages, one tree

The explorer knows nothing about languages: it builds its tree from every page of the build, so
without help it would show the German and the English tree at once. The template solves that in
CSS. On a German page the `en` folder is hidden; on an English page everything except it is hidden,
and the folder's own row is taken out so that the English tree stands at the top level rather than
one indent in.

The plugin's own answer — a `filterFn` for the explorer — cannot be reached from here: it is taken
only from `quartz.ts`, and this project builds its layout from `quartz.config.yaml`. See
[[en/design/multilingual/limits|Where the two languages stop]].

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
> A stylesheet cannot cure that: "open" and "never touched" carry the same class, and CSS cannot
> tell the two apart.

The explorer **itself** — the whole component — is unfolded and stays that way; only on a phone
does it start closed, since otherwise half the navigation would stand in front of the text.

> [!bug] And one that was self-inflicted
> Exactly that went wrong for a while: a rule of this template gave the drawer button
> `display: grid` without restricting it to narrow windows. Because everything here is unlayered,
> that beat Quartz's own `display: none` — the button was there at 1600 px too. And the plugin's
> script ends with "if this button is visible, fold the tree". So the tree was folded on every
> desktop view, although it had been rendered.
