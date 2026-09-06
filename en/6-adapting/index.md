---
title: 6 Adapting
description: Where a colour, a typeface, a spacing, the page grid or the languages come from — and how to change them, mostly without code.
section: Adapting
tags:
  - adapting
translationKey: anpassen/index
---

This template is built to be changed. Almost everything you might want to change is a
**variable**: a named value such as `--tpl-space-md: 1rem`, which QuartzControl shows under
*Styles → Variables* and which you override there, separately for light and dark. No code, no
file. Only when not the *value* but the *shape* is to change does it take a stylesheet — and even
for that there is a way that leaves the template itself untouched.

## What do I want to change?

| I want to … | Then |
| --- | --- |
| … change a colour — the accent, the ground, the callouts | [[en/6-adapting/02-colours-and-contrast\|6.2 Colours and contrast]] |
| … use a different typeface | [[en/6-adapting/03-typefaces\|6.3 Typefaces]] |
| … have more or less spacing, larger corners, other text sizes | [[en/6-adapting/04-variables\|6.4 Variables]] |
| … make the text wider, the sidebars narrower, break at other widths | [[en/6-adapting/05-page-grids\|6.5 Page grids]] |
| … know what the template does for keyboard, screen reader and print | [[en/6-adapting/06-accessibility\|6.6 Accessibility]] |
| … have a second language, or only one | [[en/6-adapting/07-two-languages/index\|6.7 Two languages]] |
| … bring the template into another project or pass it on | [[en/6-adapting/08-the-template-package\|6.8 The template package]] |
| … have a component *shaped* differently, not just coloured differently | [[en/6-adapting/01-changing-something\|6.1 Changing something]], ways 2 and 3 |

## The pages

1. [[en/6-adapting/01-changing-something|6.1 Changing something]] — the three levels, cheapest
   first, and where your own rule belongs so that it wins.
2. [[en/6-adapting/02-colours-and-contrast|6.2 Colours and contrast]] — the nine colour roles, two
   of them named the wrong way round, and the 89 measured pairs.
3. [[en/6-adapting/03-typefaces|6.3 Typefaces]] — three families, self-hosted, and why their
   `@font-face` rules are corrected.
4. [[en/6-adapting/04-variables|6.4 Variables]] — the 53 values the design is made of, and what
   does stand as a number in a file after all.
5. [[en/6-adapting/05-page-grids|6.5 Page grids]] — three frames, twelve columns, three widths.
6. [[en/6-adapting/06-accessibility|6.6 Accessibility]] — contrast, keyboard, target sizes, system
   settings, print.
7. [[en/6-adapting/07-two-languages/index|6.7 Two languages]] — how the same site comes about in
   two languages and where that stops.
8. [[en/6-adapting/08-the-template-package|6.8 The template package]] — the parts, what travels
   and what does not.

> [!warning] Two things first
> Changes to the template itself — way 2 in 6.1 — can be overwritten by the next import of a
> template package. And in `custom.scss` the app rewrites three blocks on every save; what you
> enter there by hand is gone with the next click. Both stand in full in 6.1.
