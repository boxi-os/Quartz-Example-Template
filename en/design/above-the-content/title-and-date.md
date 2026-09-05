---
title: Title and date
description: The heading of the page and the line below it.
section: Design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/titel-und-datum
---

## The title

**Out of the box** Quartz sets the page heading at the same size as an `h1` in the text.

**In this template** it is larger and more tightly tracked (`letter-spacing: -0.02em`), and its
lines are balanced rather than filled (`text-wrap: balance`): a title is skimmed, not read line by
line, and one that wraps after four words looks like an oversight.

On narrow screens it drops one step — at 390 px the full size would be half the screen.

## Date and reading time

**Out of the box** a line in the text colour.

**In this template** muted, smaller, and the parts are separated by a middle dot that is paler
still than the text. The values are the content; the punctuation steps back.

## Where the date comes from

From the frontmatter, otherwise from the file system — in that order, set on the *Created modified
date* plugin.

> [!warning] A symlink takes Quartz's git dates away
> Out of the box the order is `frontmatter → git → filesystem`, and git would be the better source:
> a commit date survives a copy, a restore and a fresh checkout, a file's modification time does
> not. It is missing here all the same. This site's content lives in an Obsidian vault that
> `content/` points to as a symlink; the plugin follows the symlink and does find the vault's git,
> but then computes the file's path against the project directory — and so asks for a path that
> leads back out of the vault. Every lookup fails. That is why **250 of the 254 pages** produced
> *"isn't yet tracked by git, dates will be inaccurate"* in the build log; the only silent ones were
> the four pages carrying a `lastmod` in their frontmatter, which never ask git in the first place.
> The date came from the file system the whole time, so `git` in the list was nothing but noise. The
> bug is reported; once it is fixed, `git` belongs back in front.

> [!note] The format follows the page, not the site
> Quartz formats dates site-wide by `configuration.locale`, which is German here. The multilingual
> plugin's `localizeDates` re-formats every `<time>` element in the browser in the language of the
> page, so an English page shows an English date.
