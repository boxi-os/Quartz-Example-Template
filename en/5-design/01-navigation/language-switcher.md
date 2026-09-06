---
title: The language switcher
description: Three forms, one of them visible — and where it sits.
section: 5 The design
tags:
  - design
  - multilingual
translationKey: gestaltung/navigation/sprachumschalter
---

The switcher stands in the **toolbar in the header**, to the right of search, [[en/7-reference/01-glossary#Colour scheme|colour scheme]] switch
and reader mode. It shares their measurements: 44 px high, the same border, the same corners, the
same feedback on [[en/7-reference/01-glossary#Hover|hover]]. Four controls in one row that differ in height read as a mistake.

## Three forms

The [[en/7-reference/01-glossary#Plugin|plugin]] knows three presentations. **All three are designed in this template**, one is visible —
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

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 23 variables are read by `nav-language-switcher.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-icon-sm` | `0.95rem` | 6.4 Variables, The explorer |
| `--tpl-leading-snug` | `1.4rem` | 4 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dark `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-3xs` | `0.125rem` | 6 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |
| `--tpl-text-xl` | `1.4rem` | 6.4 Variables |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
