---
title: Where the two languages stop
description: What stays monolingual in one build — measured, not assumed.
section: Design
tags:
  - design
  - multilingual
translationKey: gestaltung/mehrsprachigkeit/grenzen
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

This site is **one** build with `locale: de-DE`. The content is bilingual, the interface is not.
What that means in concrete terms:

## The Quartz interface stays German

Every visible label that does not come from a note takes its language from `configuration.locale` —
site-wide. Looked up in the built code of the plugins: the explorer reads `cfg?.locale`, the
backlinks `cfg.locale`; not a single component looks at the language of the page it is rendering.

Affected are: "Explorer", "Backlinks", "Graph View", "Table of Contents", "Recent Notes", the empty
state of the backlinks, the labels of the search.

**Dates are the exception.** `localizeDates: true` re-formats every `<time>` element in the browser
in the language of the page. That is the only thing the plugin can move at this boundary.

## The layout boxes: content yes, title no

Every English page sets four of the five boxes to English content in its frontmatter: the note box
points at an English snippet; the hint, the call to action and the colophon line stand there as
English HTML. The fifth is the word mark and carries the name of the site, which is not
translated.

What does **not** work is the title: the plugin's frontmatter control knows `hidden`, `file` and
`html`, but no `title`. The two titled boxes — "Über dieses Handbuch" in the left column and
"Weiterlesen" below the text — therefore carry a German heading over English content on English
pages too. The clean way to fix it would be a `title` option in the frontmatter
control of `quartz-layout-box`; it is recorded as a finding.

## One search, one graph, one listing

The search index spans both languages — a German page can turn up in an English search result. The
same goes for "Recently changed" and for the global graph. The backlinks separate by themselves,
because every page only links within its own tree.

## The error page has no language

Quartz writes **one** `404.html` for the whole site. Anyone who mistypes an English address lands on
the German error page.

## The explorer had to be separated by hand

The plugin brings a filter for the explorer with it (`languageExplorerFilter`), but the explorer
takes functions **only from `quartz.ts`** — YAML cannot carry a function. This project builds its
layout from `quartz.config.yaml`, so that route is closed.

It is solved in the stylesheet. The explorer writes a `data-folderpath` with the full path onto
every folder row and an absolute `href` onto every file — both are enough to hide the branch of the
other language:

```scss
html[lang^="de"] .explorer-ul > li:has(> [data-folderpath="en/index"]) { display: none; }
```

On an English page everything except that branch is hidden instead, and the header row of the `en`
folder with it — otherwise the whole English tree would stand one level indented under a folder
called "en".

## Pages without frontmatter cannot be linked

A `.base` or `.canvas` file is not Markdown and has no header lines. It can therefore carry neither
a `translationKey` nor an alias. Two such pages would only be linked by their path — and that
differs per language here. On these pages the switcher therefore offers the home page of the other
language.

## What a second build would solve

`publishLanguages: [de]`, or `QUARTZ_LANGS=en`, throws every other language away before rendering.
With two configurations — each with its own `locale` and its own `baseUrl` — two fully localised
sites come about, interface, own search and own error page included.

The price: two addresses instead of one, two builds, and a switcher pointing across the domain
boundary. For this example site the one build is the better choice — it is meant to show how the
plugin works, and that includes where it stops.
