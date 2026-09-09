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
in which eleven **parts** can lie — each a delimited piece of what makes a project. On import you
choose which of them to take over.

## The parts

| Part | What it carries | In this template |
| --- | --- | --- |
| Colours & fonts | the nine colour roles for light and dark, the three font roles, where fonts are loaded from | filled — [[en/6-adapting/02-colours-and-contrast\|6.2]], [[en/6-adapting/03-typefaces\|6.3]] |
| [[en/7-reference/01-glossary#CSS and SCSS\|CSS]] variables | your own values for variables, separately for light and dark | 53 variables — [[en/6-adapting/04-variables\|6.4]] |
| Custom CSS | `custom.scss` and all your own [[en/7-reference/01-glossary#Stylesheet\|stylesheets]] with their load order | 30 stylesheets — [[en/5-design/index\|chapter 5]] |
| Font files | the font files you brought along and their `@font-face` rules | four files, 157 KB — [[en/6-adapting/03-typefaces\|6.3]] |
| Layout | which component appears where, per page type, and the [[en/7-reference/01-glossary#Breakpoint\|breakpoints]] | filled — [[en/1-getting-started/04-how-a-page-is-built\|1.4]] |
| Custom [[en/7-reference/01-glossary#Frame\|frames]] | page grids you built yourself; registered anew in the target, not copied | three — [[en/6-adapting/05-page-grids\|6.5]] |
| [[en/7-reference/01-glossary#Plugin\|Plugins]] | all plugin entries with options, order and position | filled, among them five [[en/7-reference/01-glossary#Layout box\|layout boxes]] — [[en/5-design/05-layout-boxes/index\|5.5]] |
| Translations | texts changed in Quartz's language files | filled, with one limitation (below) |
| Theme presets | saved combinations of colours and typefaces | two: light and dark |
| Community theme | an installed theme with its settings | empty — this template is the theme itself |
| Content | the notes themselves | empty — the content lives in the [[en/7-reference/01-glossary#Vault\|vault]] |

The import shows beforehand which parts the package contains and what in the project is replaced
by them, and takes a [[en/7-reference/01-glossary#Snapshot|snapshot]] — a backup you can return to.

## What does not travel

Of a project's *files* a package carries only `quartz/styles/` (custom CSS) and
`quartz/static/fonts/` (font files). Everything else under `quartz/static/` stays behind: images,
logos and the snippet files of the layout boxes.

That is why four of the five layout boxes of this template take their content from the
configuration (`html:`) and travel completely with the part *Plugins*. The word mark, too, is an
inline SVG and not an image file. The fifth box — “About this handbook” — deliberately reads from
a file, to show both ways. Whoever wants to keep it copies `sidebar-note.md` and
`sidebar-note.en.md` by hand into `quartz/static/snippets/`. If the file is missing, that is not an
error: the plugin logs a warning and renders nothing; in the [[en/7-reference/01-glossary#Dev server|dev server]] a dashed placeholder with
the expected path appears.

**The content** does not travel — on purpose. A template is a design; your own notes come from
your own vault. The part *Content* exists for the rare case of a template that explains itself;
this one does that through the vault.

## Two known limitations

> [!bug] Only one of the five layout boxes survives the import
> All five instances carry the same derived name (`quartz-layout-box`), and the import matches
> plugin entries by name. Measured: of the five, one arrives. The other four you create anew under
> *Plugins* after the import; their settings stand in
> [[en/5-design/05-layout-boxes/the-five-instances|The five instances]].

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
