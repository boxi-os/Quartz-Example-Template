---
title: Footer
description: What stands under every page — and which two parts it is made of.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/fusszeile
---

At the very bottom of every page stand two things that come from two different plugins and are
meant to look like one.

## Out of the box

The *Footer* plugin writes a “Created with Quartz” line with the year, and under it the links its
options name — two here: Quartz itself and the
[[en/design/layout-box/index|Layout Box plugin]]. Nothing about it is styled; the links inherit
whatever the body text gives them.

## In this template

- A **hairline** separates the footer from the text, in the same colour and the same width as every
  other rule on the page.
- Everything is set **muted and smaller**: the footer is apparatus, not content.
- The links are **not underlined** until they are hovered — unlike in the body text, where the
  underline is compulsory. Here they stand in a row of their own; that they are links is what the
  row says.
- Every link has **padding above and below**. They are small and often the last thing anyone tries
  to hit on a phone.
- The row of links **wraps** rather than overflowing.

## The second half is a layout box

The line below it — site name, language and the current page's path — does not come from the footer
plugin. It is one of the five instances of the Layout Box plugin, placed at `position: footer`. It
is there as the example for the three placeholders `{{siteTitle}}`, `{{locale}}` and `{{slug}}`; see
[[en/design/layout-box/the-five-instances|The five instances]].

That the two read as one block is the reason they are handled separately: the footer plugin brings
its own spacing and the layout box brings its own — and left alone, two different gaps would sit
between the two lines.

> [!note] Comments would be the third part
> The *Comments* plugin (giscus) is switched off in this template — it needs a GitHub repository
> that an importing site does not have. The styling travels along anyway (`site-comments.scss`), so
> that switching it on in the app does not drop an unstyled frame under every page.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 11 variables are read by `site-footer.scss` and `site-comments.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 21 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 16 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-xl` | `2.5rem` | 4 other components |
| `--tpl-space-xs` | `0.5rem` | 21 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
