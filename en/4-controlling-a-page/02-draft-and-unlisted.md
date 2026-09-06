---
title: 4.2 Draft and unlisted
description: Two ways of holding a page back — one does not build it at all, the other only hides it.
section: Controlling a page
tags:
  - controlling-a-page
translationKey: seiten-steuern/entwurf-und-ungelistet
---

## `draft: true` — the page is not built

A draft stays in the vault and in Obsidian, but Quartz skips it when building. There is no file
for it in the output, no entry in the explorer, no search result; a link to it leads nowhere. That
is the way for everything not finished yet.

The plugin *Remove draft* takes care of it. If it is switched off, drafts are built like every
other page.

## `unlisted: true` — built, but invisible

An unlisted page exists on the site and can be reached through its address, but it appears in no
folder overview, no tag page and no search result. Whoever knows the address can read it; whoever
does not will not find it. That is the way for a page you only pass on by link.

## The two test pages

Two pages in this chapter demonstrate exactly that:

- [[en/4-controlling-a-page/draft|A draft]] — this link leads nowhere, because the page is not
  built. If it does appear, the plugin is off or the field is misspelt.
- [[en/4-controlling-a-page/unlisted|An unlisted page]] — this link works, but the page cannot
  be found in any list on this site.

> [!note] Unlisted does not mean secret
> The page lies on the web space like any other. A search engine can find it as soon as a link to
> it stands anywhere. What really is not meant to be public stays a draft.
