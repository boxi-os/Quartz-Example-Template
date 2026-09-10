---
title: The instances
description: The same plugin, seven times, for something different each time.
section: 5 – The design
tags:
  - design
  - layout-box
aliases:
  - en/5-design/05-layout-boxes/the-five-instances
translationKey: gestaltung/layout-boxen/die-instanzen
---

| Key | Place | Form | What it shows |
| --- | --- | --- | --- |
| `layoutBoxMark` | header | inline, SVG light/dark | image switching, `{{root}}`, `{{siteTitle}}` |
| `layoutBoxPageName` | header | inline, empty `span` | `{{frontmatter.section}}` inside an attribute |
| `layoutBoxNote` | left column | `file:` with `.md`, collapsed | [[en/7-reference/01-glossary#Markdown\|Markdown]] snippet, `<details>` |
| `layoutBoxCta` | after the content | inline, own class | `{{root}}`, `{{siteTitle}}`, `title:` |
| `layoutBoxHint` | after the content | inline, mobile only | `display: mobile-only` on one instance |
| `layoutBoxColophon` | footer | inline | `{{locale}}`, `{{slug}}` |
| — | footer | inline, nothing but a `<style>` | `{{slug}}` as part of a selector |

The last one has no key in the [[en/7-reference/01-glossary#Frontmatter|frontmatter]], and it is not a box in the usual sense either: it
outputs nothing but a `<style>` and is hidden itself. Why it exists all the same stands further
down.

## Six of seven use `html:`, one uses `file:`

Until 6 September 2026 that was a necessity: snippet files live in `quartz/static/snippets/`, and no
[[en/7-reference/01-glossary#Part|part]] of a template package collected that folder. An instance with `file:` arrived in the
importing project pointing at nothing.

Since then the part *Static files* carries everything under `quartz/static/`, and both ways work.
The split has become a demonstration: the one `file:` instance shows the path through a file, the
six others show that markup inside a config entry cannot arrive without that entry in the first
place. That is also why the word mark stays an inline SVG.

## The design per place

The place in the layout decides the form: a box in the header is a word mark, the same component
after the content is a call to action with a surface and a bar, in the footer a small centred line.

## Four of them speak two languages

Four of the seven carry text and therefore stand in the configuration twice: once in German as the
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

The plugin reads the field `lang` from the page's frontmatter — the same one Quartz writes
`<html lang>` from — and merges the matching entry over the base setting. It needs no partner for
that: whether `lang` comes from the multilanguage plugin or was written by hand is all the same
to it.

The other three carry no prose: the word mark carries the site's name, which is not translated; the
chapter name in the bar comes out of the page's own frontmatter and is therefore already in its
language; and the last one outputs no text at all.

> [!info] This used to stand in every page
> Until 5 September 2026 there was no `byLang`, and every one of the 126 English pages carried four
> blocks in its own frontmatter — 876 lines all saying the same thing. The headings could not be
> translated at all, because the frontmatter control did not know a `title` back then. The plugin
> caught up on both that day.

## Two instances that display nothing

The two youngest boxes are not boxes. They use the plugin for what it is at heart: a way to get
markup to a particular place on the page — with placeholders resolved while that one page is
rendered.

**The chapter name in the bar** is an empty `span` that pulls its text out of an attribute via
`content: attr()`. That sounds roundabout and is the only way to survive a page with no frontmatter:
a placeholder it cannot resolve, the plugin leaves standing as literal text — with the value in the
text, 72 of the 345 built pages would have shown `{{frontmatter.section}}` in the bar. In an
attribute, exactly that can be tested (`[data-section^="{{"]`) and the box hidden.

**The folder-page marker** renders a `<style>` that knows only the current page. It is the only way
to mark, in the [[en/7-reference/01-glossary#Explorer|explorer]], the *folder page* you are standing on: the explorer plugin sets its
`.active` class on file rows only, a folder row carries nothing but a `data-folderpath`, and the
current page stands in `<body data-slug>`. No selector can compare two attributes with each other.
So the rule is built rather than looked for — `{{slug}}` is available while the page renders and
fills exactly the one value the selector needs.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 27 variables are read by `plugin-layout-box.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 other components |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 21 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--secondary` | `#1463A3` · dark `#699DC3` | 20 other components |
| `--tertiary` | `#196B6B` · dark `#2CAFAD` | Body text, 2.9 – Diagrams |
| `--tpl-accent-bar` | `3px` | 5 other components |
| `--tpl-leading-snug` | `1.4rem` | 4 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-radius-sm` | `4px` | 9 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 15 other components |
| `--tpl-space-3xs` | `0.125rem` | 6 other components |
| `--tpl-space-lg` | `1.5rem` | 11 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xl` | `2.5rem` | 5 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-surface` | `var(--lightgray)` = `#DDDDDD` | 6 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 other components |
| `--tpl-text-base` | `1rem` | 4 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-text-xs` | `0.78rem` | 9 other components |
| `--tpl-tracking-label` | `0.08em` | 8 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
