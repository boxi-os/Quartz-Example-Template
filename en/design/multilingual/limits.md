---
title: Where the two languages stop
description: What stays monolingual in one build — measured, not assumed.
section: Design
tags:
  - design
  - multilingual
translationKey: gestaltung/mehrsprachigkeit/grenzen
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

## The layout boxes are the exception

Four of the five boxes speak both languages — content and heading. That makes them the only control
on this site that reads the language of the *page* rather than the language of the site. It costs
four `byLang` entries in the configuration and not a line in the notes; what it looks like is in
[[en/design/layout-box/the-five-instances|The five instances]].

It is at the same time the proof of what the others fail on: the plugin can do this only because it
sees `fileData.frontmatter.lang`. Quartz's built-in components are handed `cfg.locale` at that
point and have no way of learning the page's language at all.

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

For the same reason they carry no `lang` and therefore count as German — `<html lang="de">`, and
the layout boxes show their German base setting even though the page sits under `en/`. Measured on
four pages: three bases and one canvas. Changing that would mean changing where the language comes
from: `.base` and `.canvas` are JSON and YAML, not Markdown, and have no place for a frontmatter
field.

## What a second build would solve

`publishLanguages: [de]`, or `QUARTZ_LANGS=en`, throws every other language away before rendering.
With two configurations — each with its own `locale` and its own `baseUrl` — two fully localised
sites come about, interface, own search and own error page included.

The price: two addresses instead of one, two builds, and a switcher pointing across the domain
boundary. For this example site the one build is the better choice — it is meant to show how the
plugin works, and that includes where it stops.
