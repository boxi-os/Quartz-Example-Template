---
title: Error page
description: What appears at an address that does not exist.
section: 5 – The design
tags:
  - design
  - page-types
translationKey: gestaltung/erzeugte-seiten/fehlerseite
---

## Out of the box

The 404 page uses the same grid as every other page — with an [[en/7-reference/01-glossary#Explorer|explorer]], a [[en/7-reference/01-glossary#Graph|graph]] and [[en/7-reference/01-glossary#Backlinks|backlinks]]
around an error message.

## In this template

It uses the **`focus`** [[en/7-reference/01-glossary#Frame|frame]]. That stands on the same twelve-column grid as everything else and
sets the message in the same six columns the article otherwise occupies — both outer columns stay
reserved and empty. That is the point: an error page that puts its text somewhere other than the
rest of the site reads as a foreign page rather than a missing one.

The outer columns are empty because the configuration empties their component lists
(`positions: { left: [], right: [], … }`) — they are not built at all. No explorer, no graph, no
table of contents. Header and footer remain, and with the header, since the toolbar moved, so do
search and the [[en/7-reference/01-glossary#Colour scheme|colour scheme]] switch — before that the error page had neither.

The air above is set by the page's [[en/7-reference/01-glossary#Stylesheet|stylesheet]], not by the frame: the padding of a frame moves the
header too, and a site whose word mark sits sixty pixels lower on the error page looks broken
rather than calm.

> [!tip] Why this is a decision of its own
> Anyone landing on an error page is looking for a way back — not for a map of the surroundings of
> their non-existent note. Everything that does not help with that is decoration on an error.

> [!note] The error page has no language
> Quartz writes one `404.html` for the whole site, so it stays in the site language. A visitor who
> mistypes an English address lands on the German error page.

To try it: call up any address that does not exist.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 6 variables are read by `page-404.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dark `#A1A3A8` | 20 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-space-2xl` | `4rem` | 6.4 Variables |
| `--tpl-space-md` | `1rem` | 17 other components |
| `--tpl-space-xl` | `2.5rem` | 4 other components |
| `--tpl-text-3xl` | `2.25rem` | 6.4 Variables, Title and date |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
