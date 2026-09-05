---
title: Two languages
description: How the same site is made in German and English — from one vault and one build.
section: Design
tags:
  - design
  - multilingual
translationKey: gestaltung/mehrsprachigkeit/index
---

Quartz knows **one** `locale` per site. This template publishes two languages from one vault all
the same, with the `quartz-multilanguage` plugin.

## The layout

| | German | English |
| --- | --- | --- |
| Where the files sit | in the root of the vault | under `en/` |
| How the language is detected | `defaultLanguage` — nothing matches, so German | folder strategy: the first path segment is `en` |
| Addresses | `/formatierung/text/betonung` | `/en/formatting/text/emphasis` |
| File names | German | English |
| Tags | `formatierung`, `gestaltung`, … | `formatting`, `design`, … |

**The German notes did not have to move for this.** That is the reason for this cut: the folder
strategy could have demanded a `de/` as well, but then each of the 122 notes would have got a new
path and each of the 99 wikilinks a correction. A page no strategy matches falls into the default
language — that is enough.

## The parts

| Part | Where |
| --- | --- |
| Detection and linking | [[en/design/multilingual/linking\|How the two languages find each other]] |
| The switcher in the header | [[en/design/multilingual/switcher\|The language switcher]] |
| What stays monolingual | [[en/design/multilingual/limits\|Where the two languages stop]] |

## What else the plugin does

- **`<html lang>` per page.** The plugin writes the locale of its language into every page without a
  `lang` of its own. A screen reader changes its pronunciation by it, and the stylesheets of this
  template hang their explorer rule on it.
- **`hreflang` and `og:locale`.** Every page with a translation gets `<link rel="alternate">` to its
  siblings and an `x-default`. The configuration needs `baseUrl` for that.
- **Notices above the page.** Anyone landing on a German page with an English browser language gets
  a box at the top: "This page is also available in English." The text is only filled in by the
  browser and therefore appears in neither the search index nor the description.
- **Dates in the page language.** `localizeDates: true` re-formats every `<time>` element in the
  browser — the only thing about the Quartz interface that becomes bilingual without a second build.

## One build or two

This site is **one** build. That keeps the search, the graph and the addresses together, but it
costs the interface: everything Quartz labels itself follows `configuration.locale` and stays
German. For that the plugin knows `publishLanguages` — one build per language, each with its own
`locale` and its own `baseUrl`. What that means in each case is under
[[en/design/multilingual/limits|Where the two languages stop]].
