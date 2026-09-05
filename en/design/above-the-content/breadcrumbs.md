---
title: Breadcrumbs
description: The path from the home page to here.
section: Design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/brotkrumen
---

## Out of the box

A row with the folders of the path, separated by a character.

## In this template

- The **last crumb is the current page**: set more heavily and not clickable. A link to the page
  you are standing on is a dead end.
- The **separator** is muted and cannot be selected — it should not end up in a copy.
- The row **wraps** rather than overflowing. Four levels deep, the path on a phone is longer than
  the screen.
- Every crumb has **padding above and below**, so that it can be hit on a touchscreen.

A deep example: [[en/handbook/basics/terms/abbreviations/list|List]] — there the whole path stands
over five stations.

> [!note] Not on the home page
> The component is configured with `condition: not-index`; on a folder home page the last crumb
> would be identical to the title below it.

> [!note] The language folder is a crumb too
> On an English page the path begins with `en` — it is a folder like any other, and Quartz has no
> reason to treat it differently.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 7 variables are read by `meta-breadcrumbs.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 21 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 21 other components |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 other components |
| `--tpl-space-3xs` | `0.125rem` | 7 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |
| `--tpl-underline-offset` | `0.18em` | 6 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
