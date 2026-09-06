---
title: 4.3 Aliases
description: Making a page reachable under several paths — the plugin Alias redirects creates the redirects.
section: Controlling a page
tags:
  - controlling-a-page
aliases:
  - Second name
  - en/4-controlling-a-page/another-path
translationKey: seiten-steuern/aliase
---

An **alias** is a second name for a page. In Obsidian the quick switcher finds a note under its
alias too, and a `[[Alias]]` points to it. On the site the plugin *Alias redirects* builds a small
redirect page for every alias: whoever opens the old address lands on the new one.

```yaml
---
aliases:
  - Second name
  - en/4-controlling-a-page/another-path
---
```

This page can thereby be reached under three addresses: its own, `/Second name` and
`/en/4-controlling-a-page/another-path`. An alias may be a word or a whole path.

## What for

**A page was renamed or moved.** The old path as an alias keeps old links alive — bookmarks,
references from other sites, search engine hits.

**A term has two names.** “Backlinks” and “references back” mean the same; an alias lets both be
found.

**Connecting a translation.** An alias that matches the title of the page in the other language
connects the two for the language switcher — see
[[en/4-controlling-a-page/07-translation|4.7 Translation]].

> [!warning] Every alias is a page
> The plugin builds a redirect file of its own for every alias. A hundred aliases are a hundred
> more files in the output. That is not an error, but a reason to set aliases where they do
> something.

How to *write* aliases and what a link to one looks like:
[[en/2-formatting/04-links/aliases|Aliases]] in chapter 2.
