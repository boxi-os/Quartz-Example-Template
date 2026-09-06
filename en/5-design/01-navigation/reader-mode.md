---
title: Reader mode
description: Hiding the bars — and seeing that it is on.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/lesemodus
---

Reader mode hides the sidebars for as long as you stay on the page.

## Out of the box

A button that toggles the mode. The only feedback is that the page looks different.

## In this template

The button **shows its state**: with reader mode on, its border, surface and symbol change to the
accent colour. Anyone who hit it by accident can see what is going on — otherwise the only feedback
is that half the page has suddenly gone.

Measurements as with its neighbours: 44 × 44 px, the same border.

> [!tip] What reader mode is not
> It changes nothing about the content and nothing about the print. For printing this template
> removes the bars anyway — see [[en/6-adapting/06-accessibility|Accessibility]].

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 10 variables are read by `nav-reader-mode.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-icon` | `1.1rem` | Colour scheme switch, The explorer |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
