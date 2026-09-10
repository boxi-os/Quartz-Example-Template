---
title: 6.8 – The template package
description: What is inside a .qtpl file, what arrives in the project on import — and what deliberately does not travel.
section: 6 – Adapting
tags:
  - adapting
translationKey: anpassen/das-vorlagenpaket
---

A template travels as one file with the extension `.qtpl`. QuartzControl writes it out of a
project under *Templates* (export) and reads it into another one (import). The file is an archive
in which twelve **parts** can lie — each a delimited piece of what makes a project. On import you
choose which of them to take over.

## The parts

| Part | What it carries | In this template |
| --- | --- | --- |
| Colours & fonts | the nine colour roles for light and dark, the three font roles, where fonts are loaded from | filled — [[en/6-adapting/02-colours-and-contrast\|6.2]], [[en/6-adapting/03-typefaces\|6.3]] |
| [[en/7-reference/01-glossary#CSS and SCSS\|CSS]] variables | your own values for variables, separately for light and dark | 50 variables — [[en/6-adapting/04-variables\|6.4]] |
| Custom CSS | `custom.scss` and all your own [[en/7-reference/01-glossary#Stylesheet\|stylesheets]] with their load order | 30 stylesheets — [[en/5-design/index\|chapter 5]] |
| Font files | the font files you brought along and their `@font-face` rules | four files, 157 KB — [[en/6-adapting/03-typefaces\|6.3]] |
| Static files | everything under `quartz/static/` except the fonts: logos, images, text snippets | two snippets — [[en/5-design/05-layout-boxes/the-instances\|The instances]] |
| Layout | which component appears where, per page type, and the [[en/7-reference/01-glossary#Breakpoint\|breakpoints]] | filled — [[en/1-getting-started/04-how-a-page-is-built\|1.4]] |
| Custom [[en/7-reference/01-glossary#Frame\|frames]] | page grids you built yourself; registered anew in the target, not copied | four — [[en/6-adapting/05-page-grids\|6.5]] |
| [[en/7-reference/01-glossary#Plugin\|Plugins]] | all plugin entries with options, order and position | filled, among them seven [[en/7-reference/01-glossary#Layout box\|layout boxes]] — [[en/5-design/05-layout-boxes/index\|5.5]] |
| Translations | texts changed in Quartz's language files | filled, with one limitation (below) |
| Theme presets | saved combinations of colours and typefaces | two: light and dark |
| Community theme | an installed theme with its settings | empty — this template is the theme itself |
| Content | the notes themselves | empty — the content lives in the [[en/7-reference/01-glossary#Vault\|vault]] |

The import shows beforehand which parts the package contains and what in the project is replaced
by them, and takes a [[en/7-reference/01-glossary#Snapshot|snapshot]] — a backup you can return to.

## What travels and what does not

Of a project's *files* a package carries everything under `quartz/styles/` (custom CSS) and
everything under `quartz/static/` — the font files in a part of their own, logos, images and
snippet files in the part *Static files*.

That the latter exists is new: until 2026-09-06 everything except the fonts stayed behind, and a
layout box with `file:` arrived in the target project pointing at nothing — measured,
`layout-box-note` appeared on 0 of 334 pages. Since then the two snippet files travel along, and in
the target project every box renders.

The part counts along with what Quartz brings itself: of the six files under `quartz/static/`, four
are byte for byte Quartz's own scaffolding (`icon.png`, `og-image.png`, two giscus stylesheets) and
only the two snippets belong to the template. The preview therefore reports two additions rather
than six conflicts, and a target project never gets somebody else's scaffolding pushed over its own.

Six of the seven layout boxes take their content from the configuration (`html:`) all the same, and
the word mark is an inline SVG. Since 2026-09-06 that is no longer a necessity but a decision:
markup inside a config entry cannot arrive without that entry in the first place. The one `file:`
box — “About this handbook” — shows the other way. If its file should be missing after all, that is
not an error: the plugin logs a warning and renders nothing; in the [[en/7-reference/01-glossary#Dev server|dev server]] a dashed
placeholder with the expected path appears.

**The content** does not travel — on purpose. A template is a design; your own notes come from
your own vault. The part *Content* exists for the rare case of a template that explains itself;
this one does that through the vault.

## One known limitation

> [!warning] The part Translations does not change component headings
> “[[en/7-reference/01-glossary#Backlinks|Backlinks]]”, “[[en/7-reference/01-glossary#Graph|Graph]] View”, “Recent Notes” come from the plugins themselves, which bring their
> own language files. What you change in QuartzControl under *Configuration → Translations*
> reaches everything the Quartz core labels — not the component headings. Measured on the built
> page: all three stayed after the change. The mechanism is right; its reach is smaller than you
> would expect.

## Passing the template on yourself

Whoever has changed this template and wants to pass the result on exports a new package under
*Templates* — with the parts that changed. The recipient imports it into their project and
chooses the same parts. What they overwrite in doing so, the app tells them beforehand.
