---
title: Colour scheme switch
description: The button between light and dark.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/farbschema
---

## Out of the box

A button with two symbols, one of which is visible depending on the scheme.

## In this template

It is part of the toolbar in the header and shares its measurements: 44 × 44 px, the same border,
the same corners as search, reader mode and the language switcher. A row of controls with differing
heights reads as a mistake.

On hover the border changes to the accent colour and the surface to the tinted variant — the same
feedback as with its neighbours.

## A finding while building

The first version of this file styled an `<input>`/`<label>` pair. There is none here: the
component is a single `<button class="darkmode">` with two SVGs in it. The rules hit nothing —
which only became visible when every selector of the template was checked against the built page.

Hence the rule that applies everywhere in this template: **look in the built HTML before writing a
rule.** Class names are no contract.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 10 variables are read by `nav-darkmode.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tpl-icon` | `1.1rem` | The explorer, Reader mode |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
