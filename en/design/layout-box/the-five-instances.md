---
title: The five instances
description: The same plugin, five times, for something different each time.
section: Design
tags:
  - design
  - layout-box
translationKey: gestaltung/layout-box/die-fuenf-instanzen
---

| Key | Place | Form | What it shows |
| --- | --- | --- | --- |
| `layoutBoxMark` | header | inline, SVG light/dark | image switching, `{{root}}`, `{{siteTitle}}` |
| `layoutBoxNote` | left column | `file:` with `.md`, collapsible | Markdown snippet, `<details>` |
| `layoutBoxHint` | left column | inline, mobile only | two instances controllable independently |
| `layoutBoxCta` | after the content | inline, own class | `{{frontmatter.…}}` |
| `layoutBoxColophon` | footer | inline | `{{locale}}`, `{{slug}}` |

## Why four of five use `html:` rather than `file:`

**A template package carries `quartz/styles/` and `quartz/static/fonts/` — nothing else.** Snippet
files and images stay behind. An instance with `file:` would arrive in the target project with a
link into nothing.

Inline HTML, by contrast, sits in the configuration entry and travels with the *Plugins* part. That
is also why the word mark is an inline SVG and not an image file.

The fifth instance deliberately uses the file route — it shows both: that it works, and that the
file has to be copied along when passing the template on.

## The design per place

The place in the layout decides the form: a box in the header is a word mark, the same component
after the content is a call to action with a surface and a bar, in the footer a centred, small line.

## An open limitation

When a template is imported, only **one** of the five instances currently survives. They all carry
the same derived name (`quartz-layout-box`), and the import matches entries by name. That is
measured and recorded as a finding.

## Four of them speak both languages

Four of the five carry text and therefore stand in the configuration twice: once in German as the
base setting, once in English under `byLang`.

```yaml
options:
  file: sidebar-note.md
  title: Über dieses Handbuch
  byLang:
    en:
      file: sidebar-note.en.md
      title: About this handbook
```

The plugin reads the page's `lang` frontmatter field — the one Quartz writes `<html lang>` from —
and merges the matching entry over the base setting. It needs no companion for that: whether `lang`
comes from the multilanguage plugin or was written by hand makes no difference to it.

The fifth is the site mark. It carries the name of the site, which is not translated, and therefore
stays without `byLang`.

> [!info] This used to sit in every page
> Until 5 September 2026 there was no `byLang`, and each of the 126 English pages carried four
> blocks in its own frontmatter — 876 lines all saying the same thing. The headings could not be
> translated at all, because the frontmatter control knew no `title` back then. The plugin caught
> up on both that day.
