---
title: Tokens
description: 50 variables the whole design is made of.
section: Design
tags:
  - design
  - basics
translationKey: gestaltung/grundlagen/tokens
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

**No stylesheet in this template contains a colour or a length as a number.** Everything reads
variables. That is not cosmetics: after the import they stay editable in the app under *Styles →
Variables*, a value in SCSS does not.

## The six with the widest reach

| Token | Value | What changes |
| --- | --- | --- |
| `--tpl-space-md` | 1rem | base gap; the whole scale hangs on it |
| `--tpl-target` | 44px | minimum size of **every** control |
| `--tpl-indent` | 0.85rem | one level in the explorer *and* the table of contents |
| `--tpl-radius-md` | 8px | corners of cards, code blocks, callouts |
| `--tpl-accent-bar` | 3px | every accent bar |
| `--tpl-motion` | 150ms | every transition duration |

## Two line heights, not one

`--tpl-leading-normal` is 1.65 and applies to the body text. For everything set in
`--tpl-text-sm` or smaller there is `--tpl-leading-snug` at 1.45.

That is not a nicety. 1.65 is a ratio measured for 1 rem across six grid columns. The same number
at 0.875 rem in a bar three columns wide puts nearly 21 px between two lines of 14 px height — a
three-line paragraph then reads like three separate ones. That is exactly how the note box in the
sidebar looked. The three areas that consist of small type — left bar, right bar, footer — say it
once, instead of every component inside them repeating it.

## Three kinds of variable

1. **Font stacks** — the family plus a real fallback.
2. **Quartz variables where the template disagrees** — the border of controls, for instance. Those
   are read by *Quartz*, not by our stylesheets; they look unused and are not.
3. **Our own `--tpl-*` tokens** — the actual system.

## What Quartz does instead

**Out of the box** there are the nine colour variables and the typeface roles, but no scale for
spacing, radii, target sizes or motion. Values stand directly in the rules there. Anyone wanting to
change the base gap has to look for it in many places.
