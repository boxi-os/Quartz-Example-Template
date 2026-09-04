---
title: Error page
description: What appears at an address that does not exist.
section: Design
tags:
  - design
  - page-types
translationKey: gestaltung/seitentypen/fehlerseite
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Out of the box

The 404 page uses the same grid as every other page — with an explorer, a graph and backlinks
around an error message.

## In this template

It uses the **`focus`** frame. That stands on the same twelve-column grid as everything else and
sets the message in the same six columns the article otherwise occupies — both outer columns stay
reserved and empty. That is the point: an error page that puts its text somewhere other than the
rest of the site reads as a foreign page rather than a missing one.

The outer columns are empty because the configuration empties their component lists
(`positions: { left: [], right: [], … }`) — they are not built at all. No explorer, no graph, no
table of contents. Header and footer remain, and with the header, since the toolbar moved, so do
search and the colour scheme switch — before that the error page had neither.

The air above is set by the page's stylesheet, not by the frame: the padding of a frame moves the
header too, and a site whose word mark sits sixty pixels lower on the error page looks broken
rather than calm.

> [!tip] Why this is a decision of its own
> Anyone landing on an error page is looking for a way back — not for a map of the surroundings of
> their non-existent note. Everything that does not help with that is decoration on an error.

> [!note] The error page has no language
> Quartz writes one `404.html` for the whole site, so it stays in the site language. A visitor who
> mistypes an English address lands on the German error page.

To try it: call up any address that does not exist.
