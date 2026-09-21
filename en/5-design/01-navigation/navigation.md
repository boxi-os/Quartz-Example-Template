---
title: The navigation
description: The accordion on the left, the drawer on a phone, “Previous” and “Next” below the text.
section: 5 – The design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/navigation
---

Two navigations lead through this handbook: on the left a menu over all chapters, below every text
“Previous” and “Next”. Both come from the same [[en/7-reference/01-glossary#Plugin|plugin]],
`quartz-navigations`, which brings one component with ten forms; this site uses two of them.

## Out of the box

For navigation Quartz brings the [[en/5-design/01-navigation/explorer|explorer]], a folder tree. It
stood here too until 2026-09-20. A tree shows everything at once, and with seven chapters holding
more than a hundred notes between them, that is more rows unfolded than the column is tall. The
explorer has been switched off since and is still designed — whoever switches it on finds it
ready.

## The menu on the left

The form is called **accordion**: every chapter is a row that unfolds.

- **One chapter is open, and it is the one you are reading in.** Opening another closes the
  previous one. Which one stands open is decided by the page being read — a second memory for it
  in the browser is left out on purpose, it could only contradict the page.
- **The whole row unfolds.** The chapter page itself stands as the first entry *inside* the
  unfolded chapter, under the heading “Overview”. Before, the row was a link and only a 24 px wide
  arrow at the edge unfolded it.
- **“Home” stands at the very top** and leads to the home page.
- **The order** comes first from the number in front of the file name, then from the title. The
  numbers stand in the title as well — that is where the reader sees them. They are not cut off:
  the option for that also cut them out of “1 – Getting started”, and the menu then said
  “– Getting started”.
- **Drafts and unlisted pages** are missing from the menu, as everywhere else
  ([[en/4-controlling-a-page/02-draft-and-unlisted|4.2]]).

## On a phone

Below 900 px the menu becomes a **drawer**. Its button sits in the app bar at the top left, the
drawer slides over a darkened and slightly blurred page, and a close button of its own stands in
the drawer itself. There the rows get their thumb height of 44 px back; in the sidebar on a desktop
32 px is right.

## Previous and next

Below every text stand two buttons to the previous and the next page. The order runs through the
whole outline, across chapter boundaries — a handbook is read in order, and at the end of a chapter
the way leads into the next one instead of into a dead end.

They stand **at the very bottom**: after the text, the two boxes, “Read on” and the properties.
That is where one looks for the way to the next page. On a phone the two buttons stand one above
the other, so that a long page title does not have to wrap inside half a button, and on the home
page, where there is no “Previous”, no empty box stands. The plugin does both itself since
version 0.3.1.

“Previous” and “Next” are set small, in capitals and letter-spaced — the same label as above the
boxes beside them.

## What the template adds

Almost nothing, and that is on purpose. The plugin designs rows, folds, pager and drawer itself,
through some sixty variables of its own. The template connects these variables to its own —
colours, spacing, radii, shadows —, and adds what there is no variable for: the blur behind the
drawer, the thumb height on a phone, the pager's label.

The plugin's variables therefore do **not** stand under *Styles → Variables*: it declares them on
its own element, and a value from outside would never arrive there. What can be changed are the
`--tpl-*` tokens they hang on — the table below.

## The other eight

All ten forms are designed, not only the two you see here — whoever switches another one on gets
it ready. One of them, a horizontal chapter bar in the header, stood here for an afternoon and
failed on a sum: the seven chapter names are about 880 px wide together, and the header has about
680 px left beside the word mark and the controls.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 27 variables are read by `nav-navigations.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--gray` | `#5F5F5F` · dark `#A1A1A1` | 22 other components |
| `--headerFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 15 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 14 other components |
| `--tpl-accent-bar` | `3px` | 6 other components |
| `--tpl-backdrop` | `rgba(0, 0, 0, 0.3)` | The explorer |
| `--tpl-backdrop-blur` | `4px` | The explorer |
| `--tpl-drawer-width` | `min(86vw, 340px)` | The explorer |
| `--tpl-header-h` | set in the stylesheet (`base.scss`) | 6.4 – Variables, The explorer |
| `--tpl-icon` | `1.1rem` | 3 other components |
| `--tpl-icon-sm` | `0.95rem` | 3 other components |
| `--tpl-indent` | `0.85rem` | Table of contents, The explorer |
| `--tpl-leading-normal` | `1.6` | 6.4 – Variables |
| `--tpl-motion` | `150ms ease` | 13 other components |
| `--tpl-radius-md` | `8px` | 17 other components |
| `--tpl-radius-sm` | `4px` | 10 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 19 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 25 other components |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dark `0 6px 24px rgba(0, 0, 0, 0.55)` | 5 other components |
| `--tpl-space-2xs` | `0.25rem` | 16 other components |
| `--tpl-space-lg` | `1.5rem` | 12 other components |
| `--tpl-space-md` | `1rem` | 18 other components |
| `--tpl-space-xs` | `0.5rem` | 20 other components |
| `--tpl-target` | `44px` | 12 other components |
| `--tpl-text-sm` | `0.875rem` | 20 other components |
| `--tpl-text-xs` | `0.78rem` | 10 other components |
| `--tpl-tracking-label` | `0.08em` | 9 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
