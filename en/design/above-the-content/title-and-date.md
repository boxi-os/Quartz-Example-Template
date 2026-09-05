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

From the frontmatter, otherwise from git, otherwise from the file system — in that order, set on
the *Created modified date* plugin. For a note that has never been committed the build warns:
*"isn't yet tracked by git, dates will be inaccurate"*.

> [!note] The format follows the page, not the site
> Quartz formats dates site-wide by `configuration.locale`, which is German here. The multilingual
> plugin's `localizeDates` re-formats every `<time>` element in the browser in the language of the
> page, so an English page shows an English date.
