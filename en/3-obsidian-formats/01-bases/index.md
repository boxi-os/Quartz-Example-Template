---
title: 3.1 Bases
description: Queries over the vault, as a table, cards or a list.
section: Obsidian formats
tags:
  - obsidian-formats
  - bases
translationKey: obsidian-formate/bases/index
---

A base is a saved query: it collects notes by criteria and shows them in one or several views. The
file is [[en/7-reference/01-glossary#YAML|YAML]] and ends in `.base`.

Three examples in this [[en/7-reference/01-glossary#Vault|vault]], all of them over the notes of this site itself:

- [[en/3-obsidian-formats/01-bases/All-Views.base|All views]] — **all five forms of presentation** of
  the same data: table, cards, list, board and gallery
- [[en/3-obsidian-formats/01-bases/Formatting-Pages.base|Formatting pages]] — table and cards
- [[en/3-obsidian-formats/01-bases/Design-Pages.base|Design pages]] — list, grouped by area

How the format is built: [[en/3-obsidian-formats/01-bases/how-it-works|How it works]].

## The five forms of presentation

A base can show the same data in five ways; the switches sit at the top of the page.

| View | What it is good for |
| --- | --- |
| **Table** | comparing many columns, sorting by one of them |
| **Cards** | few details per entry, skimmed side by side |
| **List** | compact, one below the other, with grouping |
| **Board** | split into columns by a field, like a kanban |
| **Gallery** | large-format, for entries with an image |

All five are designed in this template — to be seen under
[[en/3-obsidian-formats/01-bases/All-Views.base|All views]].

## In this template

Bases pages use the **`index`** [[en/7-reference/01-glossary#Frame|frame]], the same one folder and tag pages use. No table of
contents arises there, because a table has no headings; the right column still stands, so the table
begins where the text otherwise begins — beside the content on the desktop, in a row of its own
below that.

> [!warning] Bases speak English
> Above every view stands a line such as *“Showing 45 of 45 entries”*, and the column headings
> carry the English field names (`Description`). Both come from the compiled [[en/7-reference/01-glossary#Plugin|plugin]] `bases-page`
> and cannot be changed through the language file or an option. On a German page that is a line in
> the wrong language; the template therefore sets it quietly instead of removing it — a line that
> steps back disturbs less than one that shouts.

> [!note] Bases are new
> They arrived with Obsidian 1.9 as a core feature. Older vaults do not have them; in the example
> vault the feature is switched on.

> [!warning] The switcher does not find these pages
> A `.base` file has no [[en/7-reference/01-glossary#Frontmatter|frontmatter]], so it can carry no `translationKey`. The language switcher on
> such a page therefore offers the other language's home page instead of the corresponding base.
> See [[en/6-adapting/07-two-languages/limits|Where the two languages stop]].

## The pages

- [[en/3-obsidian-formats/01-bases/All-Views.base|All Views]] — a base
- [[en/3-obsidian-formats/01-bases/Design-Pages.base|Design Pages]] — a base
- [[en/3-obsidian-formats/01-bases/Formatting-Pages.base|Formatting Pages]] — a base
- [[en/3-obsidian-formats/01-bases/how-it-works|How a base is built]] — Filters, formulas and views — the YAML format explained.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 30 variables are read by `page-bases.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 other components |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 other components |
| `--ink` | — | only here |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-leading-snug` | `1.4rem` | 4 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 8 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-3xs` | `0.125rem` | 6 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-caps` | `0.06em` | 6.4 Variables, Code styling |
| `--tpl-tracking-label` | `0.08em` | 8 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
