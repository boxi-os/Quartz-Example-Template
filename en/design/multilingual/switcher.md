---
title: The language switcher
description: Three forms, one of them visible — and where it sits.
section: Design
tags:
  - design
  - multilingual
translationKey: gestaltung/mehrsprachigkeit/umschalter
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

The switcher stands in the **toolbar in the header**, to the right of search, colour scheme switch
and reader mode. It shares their measurements: 44 px high, the same border, the same corners, the
same feedback on hover. Four controls in one row that differ in height read as a mistake.

## Three forms

The plugin knows three presentations. **All three are designed in this template**, one is visible —
which one is decided by `switcher.style` in the configuration.

| Form | What it is | What it is good for |
| --- | --- | --- |
| `dropdown` | a `<details>` element with a list below it | **in use here** — one control, however many languages |
| `links` | the languages side by side, separated by `\|` | two languages, plenty of room |
| `flags` | flag emoji instead of names | very tight, when the languages are known |

`dropdown` is chosen because it stands as **one** box next to the search field and does not grow
wider when a third language arrives. The list opens downwards, right-aligned under the button, with
the same shadow as search and preview — the only two other places in this template that really do
float above the page.

The other two forms are fully designed all the same: anyone switching to `links` or `flags` in the
app gets not an unstyled component but one that fits into the same bar. With `flags` the emoji grows
to reading size and the button stays square.

## What the switcher shows

- The **current language** stands as the button label and in the list as a highlighted,
  non-clickable entry with `aria-current`.
- The label is the **name in the language itself** (`switcher.label: native`) — "Deutsch" and
  "English", not "German". A language name you cannot read because you do not speak the language is
  no help.
- If there is **no translation** of this page, the entry leads to the home page of the other
  language (`switcher.missing: home`) and says so in its `title`. The alternatives would be to hide
  the entry — then the way out disappears — or to grey it out, which shows a dead end instead of
  offering a way.
- Every entry carries `lang` and `hreflang`. A screen reader therefore pronounces "English" in
  English, even in the middle of a German page.

## On a phone

The toolbar is a flex row with `wrap`. At 390 px the drawer button, the site name and four controls
share the space; the search gives up its word and becomes a square, the switcher keeps its name,
because two letters ("EN") say less than "English" and there is room for it.

## Remembering

`rememberChoice: true` stores the chosen language in `localStorage`. That is used by the root
redirect — which this site does not have, because its root is the German home page — and by the
notices above the page: once someone has switched to English, they get the notice in English from
then on, regardless of the browser language.
