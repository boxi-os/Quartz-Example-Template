---
title: 4.1 Title, description, date
description: The three statements every page should have — and where the date comes from when none is given.
section: 4 Controlling a page
tags:
  - controlling-a-page
date: 2026-09-06
translationKey: seiten-steuern/titel-beschreibung-datum
---

## `title`

The title stands as the heading above the page, in the browser tab, in the [[en/7-reference/01-glossary#Explorer|explorer]], in every list
and in every search result. If it is missing, Quartz takes the file name. This site sets it on
every page, because a file name like `headings` is not a title.

The explorer sorts by title, not by file name — which is why the chapters and sections of this
handbook carry their number in the title. See [[en/5-design/01-navigation/explorer|The explorer]].

## `description`

One sentence that describes the page. It appears in search results, in folder and tag lists, in
the preview when hovering a link and when sharing the address on social networks. Without it,
Quartz takes the first words of the text.

## `date` and `lastmod`

`date` is the creation date, `lastmod` that of the last change. Under the title this template shows
the modification date; the list “Recently changed” in the left column sorts by it as well. The
format follows the language of the page: an English page shows an English date.

### Where the date comes from when none is given

Quartz asks in turn: the [[en/7-reference/01-glossary#Frontmatter|frontmatter]], then [[en/7-reference/01-glossary#git|git]], then the file system. The order is set on the
[[en/7-reference/01-glossary#Plugin|plugin]] *Created modified date*, in QuartzControl under *Plugins*. This template leaves git out —
`frontmatter → filesystem` — and that has a measured reason.

> [!warning] A symlink takes Quartz's git dates away
> git — the program that records the history of files — would be the better source: a [[en/7-reference/01-glossary#Commit|commit]] date
> survives a copy, a restore and a fresh checkout; a file's modification time does not. It is
> missing here all the same. The content lives in an Obsidian [[en/7-reference/01-glossary#Vault|vault]] that `content/` points to
> through a [[en/7-reference/01-glossary#Symlink|symlink]]; the plugin follows the link and does find the vault's git, but then computes
> the file path against the project directory — and so asks for a path that leads back out of the
> vault. Every query fails. For **250 of 254 pages** the [[en/7-reference/01-glossary#Build|build]] log therefore said *“isn't yet
> tracked by git, dates will be inaccurate”*; only the four that carry a `lastmod` stayed quiet,
> because they never ask git at all. The bug is reported; as soon as it is fixed, `git` belongs
> back in the list.

What the file system delivers is the file's modification time — and that changes with every copy.
Whoever wants a date that stays writes it into the frontmatter. This page does.

What title and date *look like* stands in
[[en/5-design/02-above-the-content/title-and-date|Title and date]].
