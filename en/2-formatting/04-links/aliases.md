---
title: Aliases
description: Making a page reachable under several names.
section: Formatting
tags:
  - formatting
  - links
aliases:
  - Second name for aliases
translationKey: formatierung/links/aliase
cover: "[[assets/covers/cover-links.svg]]"
---

In the frontmatter:

```md
---
aliases:
  - Second name
  - old/path
---
```

This page itself has an alias — it can also be reached under *Second name for aliases*.

## What that does

In **Obsidian**: the alias shows up in the quick switcher, and `[[Second name]]` finds the page.

On the **built site**: the *Alias redirects* plugin creates a small forwarding page for every
alias. Old links therefore keep working when a note has been renamed or moved.

## When it pays off

- A note is renamed but there are already links to it — the old path becomes an alias.
- A term has several common names.
- An abbreviation should find the same page as the spelled-out word.

An example with several aliases: [[en/4-controlling-a-page/03-aliases|A page with an alias]].

> [!note] Aliases carry the translation too
> The Obsidian plugin *Multilingual* writes the translated note name into exactly this field, and
> `quartz-multilanguage` can link the two languages by it. Three pages of this site are linked that
> way and nothing else — see [[en/6-adapting/07-two-languages/linking|How the two languages find each
> other]].
