---
title: Search
description: The field in the bar and the overlay behind it.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/suche
---

## Out of the box

A button with a magnifying glass that opens an overlay. The border comes from `lightgray`.

## In this template

- The border comes from **`gray`**, not from `lightgray`. That is the contrast rule put into
  practice: `lightgray` measures 1.34:1 against the ground and may therefore not surround anything
  you operate.
- The button sits **in the header**, at the far right, together with the three other controls. It
  is 44 px high like its neighbours and 15 rem wide — wide enough to be read as a field, narrow
  enough that the header still belongs to the page title. On a phone it becomes a square without a
  label.
- The **overlay** carries a real shadow. In this template only what genuinely floats above the page
  rather than sitting in it gets one: this overlay, the link preview, the language menu, the drawer
  on a phone and the global graph. Five places — and it is the rule that counts, not the number.
- The **input field** gets no focus ring but a heavier bottom edge — a ring inside a rounded box
  looks like a mistake.
- **Results**: the keyboard cursor and the pointer hover look the same. The arrow keys move through
  the list, and the highlighted row is the only signal of where you are.
- The **match in the text** is marked with the same colour as `==highlight==` in the body text.
  "This is what you were looking for" means the same thing across the whole site.

With `prefers-reduced-transparency` the translucent surface is replaced by an opaque one.

> [!example] Why the width lives in the configuration and not in the stylesheet
> It lived there once, as `flex: 0 1 15rem` on `.search` — and had no effect: measured it was
> **110 px**, equally at 1728, 1440, 1100 and 900 px, even though the toolbar occupied only 322 of
> 1400 px. Quartz wraps every component of a group in a class-less `div` of its own and writes that
> div's flex values as an **inline style** from the configuration. The flex item is therefore the
> wrapper, not `.search`, and an inline style beats every stylesheet.
>
> Since 2026-09-05 the 15 rem live in the search plugin's `layout.groupOptions.basis`, together
> with `shrink: false`. The second belongs with it: a shrinkable item contributes only its content
> width to the group's size, so the group stayed at 322 px while its children wanted 452 — and the
> bar wrapped onto two rows, the header growing from 61 to 101 px. On a phone `nav-header.scss`
> takes the width back off, with `!important`, because nothing else beats an inline style.

> [!note] The index spans both languages
> There is one search index for the whole site, so a German page can turn up in an English search
> result. Splitting it would mean one build per language — see
> [[en/6-adapting/07-two-languages/limits|Where the two languages stop]].

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 18 variables are read by `nav-search.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-lg` | `14px` | 3 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dark `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-lg` | `1.15rem` | 6.4 Variables, Link preview |
| `--tpl-text-sm` | `0.875rem` | 18 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
