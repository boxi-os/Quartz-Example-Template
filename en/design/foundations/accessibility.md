---
title: Accessibility
description: What this template does for it — and why it is usually only one line more.
section: Design
tags:
  - design
  - basics
  - accessibility
translationKey: gestaltung/grundlagen/barrierefreiheit
---

## No state hangs on colour alone

The active entry in the explorer has colour, weight **and** a bar. A completed task is muted **and**
struck through. An external link is a different colour **and** carries an arrow. Anyone who cannot
tell colours apart loses no information by it.

## Operable from the keyboard

Every control has a visible focus ring — a single rule through `:focus-visible`, with a colour of
its own on tinted surfaces, so that the ring does not lie on its own colour. `outline: none` occurs
nowhere in this template.

The copy button on a code block appears on hover, on focus *and* permanently on devices without a
pointer. **Out of the box** it is visible only on hover — and therefore unreachable on a phone.

## Target sizes

Everything you tap is at least 44 px across (`--tpl-target`). WCAG 2.2 asks for 24; 44 is the size
at which nobody has to aim.

## System settings are honoured

| Setting | Effect |
| --- | --- |
| `prefers-reduced-motion` | sets `--tpl-motion` to 0 — one place for every transition |
| `prefers-reduced-transparency` | replaces the translucent surfaces of search and graph |
| `forced-colors` | draws borders where the template otherwise works with surfaces |
| Print | removes every bar, writes out link targets, prevents breaks inside blocks |

## What is missing

Quartz renders **no skip link**, and a stylesheet cannot add one — the element has to be in the
markup to be focusable. On a page with an explorer, reaching the article by keyboard therefore
costs one tab stop per row of the tree. The design for it is ready; it takes effect as soon as such
a link exists.

<!-- QuartzControl:variables:start -->
## Which variables apply here

This variable is read by `a11y.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
