---
title: The header
description: Word mark, page title and the four controls in one row.
section: 5 – The design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/kopfbereich
---

At the top stands the word mark, next to it the page title, at the right-hand end search, colour
scheme switch, reader mode and the language switcher. Below it a separating line.

## Out of the box

The header contains only the page title. There is no mark — you would have to [[en/7-reference/01-glossary#Build|build]] a component of
your own for that. Search and the two switches sit in the left sidebar.

## In this template

The mark comes from a **[[en/7-reference/01-glossary#Layout box|layout box]] instance** with an inline SVG, once light and once dark. It is
at the same time the link to the home page.

A few details:

- The **text of the mark is visually hidden** but present in the document. Otherwise the link would
  contain only an SVG and would have no accessible name. `display: none` would have been wrong here
  — that is exactly the mistake the first version contained.
- The four controls stand **in the header, not in the bar**. That is where they are looked for, and
  it is the only area every [[en/7-reference/01-glossary#Frame|frame]] has — on the error page there used to be neither search nor
  [[en/7-reference/01-glossary#Colour scheme|colour scheme]] switch, because it has no sidebars.
- They form one **group** (`toolbar`) with `wrap`, so that four controls plus the site name still
  fit on a 360 px phone.
- On a phone the header becomes an **app bar**: it stays at the top while scrolling, runs the full
  width and takes the [[en/7-reference/01-glossary#Explorer|explorer]]'s drawer button with it. The search gives up its word there and
  becomes a square like the others; it keeps its 44 px.

## It stays, the title goes

Since 05.09.2026 the header sticks to the top of the window at every width, not just on the phone:
the four controls and the way back to the start page are what one reaches for in the middle of a
long article, and several pages here are three screens tall.

Its height does not change while it does. What changes is the page around it: the header is one of
**two layers**, and the other one scrolls away. Above the text sits the `beforeBody` area with the
breadcrumb, the tags, the heading and the date — the page's own title block, and it leaves with the
text. The bar stays. That is the change while scrolling, and it needs no effect: it follows from
where things are.

So that the bar still says something in that state, it carries **two names side by side** — the
site's and the chapter's (`{{frontmatter.section}}`, from every note's frontmatter). The chapter
does not repeat the heading, so both may stand there permanently; a reader who has scrolled past
the heading still knows where they are.

> [!note] There was an effect here, and it ran in two browsers out of three
> Until 09.09.2026 the header shrank by 8px while scrolling, traded the site name for the page name
> and carried a progress line. All three hung on `animation-timeline` — CSS bound to the scroll
> position rather than to the clock. Chromium and WebKit do that, **Firefox does not**: measured on
> the installed 155.0.1, all five queries negative, and it has not been in sight for years. The
> effects sat behind `@supports` and therefore simply did not happen there — the most visible
> element of the site was one thing in two engines and another in the third.
>
> The progress line is gone without replacement, and that is no loss: the
> [[en/5-design/04-beside-the-content/table-of-contents|table of contents]] already marks how far
> the page has been read, and it does so with a script from the plugin — so in every browser.

Two things depend on the header's height and are therefore part of the same calculation:

- The **right column** sticks below the header rather than hidden under it: its `top` reads
  `--tpl-header-h`, the same calculation the header takes its own height from.
- **Jump targets** keep the height of the bar free above themselves, plus the 24px of the fade below
  it (`scroll-margin-block-start`) — otherwise every heading jumped to lands behind the header or
  inside the gradient that closes it off.

## A finding while building

The [[en/7-reference/01-glossary#Plugin|plugin]] sets `width: 100%` on every layout box. In a flex row that made the mark 1376 px wide
and pushed the title onto the next line. `flex` does not lift a set width — it had to be taken back
explicitly.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 15 variables are read by `nav-header.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--titleFont` | `"Instrument Sans", ui-sans-serif, system-…` | only here |
| `--tpl-header-pad` | set in the stylesheet (`base.scss`) | 6.4 Variables |
| `--tpl-header-title` | set in the stylesheet (`base.scss`) | only here |
| `--tpl-page-fade` | `24px` | only here |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-space-2xs` | `0.25rem` | 14 other components |
| `--tpl-space-sm` | `0.75rem` | 10 other components |
| `--tpl-space-xs` | `0.5rem` | 19 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-base` | `1rem` | 4 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
