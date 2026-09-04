---
title: Bases
description: Queries over the vault, as a table, cards or a list.
section: Obsidian formats
tags:
  - obsidian-formats
  - bases
translationKey: obsidian-formate/bases/index
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

A base is a saved query: it collects notes by criteria and shows them in one or several views. The
file is YAML and ends in `.base`.

Three examples in this vault, all of them over the notes of this site itself:

- [[en/obsidian-formats/bases/All-Views.base|All views]] — **all five forms of presentation** of
  the same data: table, cards, list, board and gallery
- [[en/obsidian-formats/bases/Formatting-Pages.base|Formatting pages]] — table and cards
- [[en/obsidian-formats/bases/Design-Pages.base|Design pages]] — list, grouped by area

How the format is built: [[en/obsidian-formats/bases/how-it-works|How it works]].

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
[[en/obsidian-formats/bases/All-Views.base|All views]].

## In this template

Bases pages use the **`index`** frame — two columns, no right-hand bar. A table needs no table of
contents.

> [!note] Bases are new
> They arrived with Obsidian 1.9 as a core feature. Older vaults do not have them; in the example
> vault the feature is switched on.

> [!warning] The switcher does not find these pages
> A `.base` file has no frontmatter, so it can carry no `translationKey`. The language switcher on
> such a page therefore offers the other language's home page instead of the corresponding base.
> See [[en/design/multilingual/limits|Where the two languages stop]].
