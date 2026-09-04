---
title: Code styling
description: Inline, blocks, the language label and the copy button.
section: Design
tags:
  - design
  - in-the-content
  - code
translationKey: gestaltung/im-inhalt/code
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Inline

**Out of the box** a box with a border. **In this template** a tint without a border — enough to
separate, too little to interrupt. Set slightly smaller (0.9em), because JetBrains Mono next to
Inter otherwise looks too big.

## Blocks

The surface comes from the template, not from the syntax theme: `keepBackground: false` makes shiki
set only the character colours. Only that way does the block fit in both colour schemes.

Since 2026-09-05 it is **lighter than the rest of the tint** and has a token of its own
(`--tpl-surface-code`, `#F1EFE9` in light mode, still `lightgray` in dark). A block is a large
area, and the tint that is right for one word of inline code turns twenty lines into a grey slab.
Measured, what it buys:

| Colour | on the old surface | on the new one |
| --- | --- | --- |
| Text (`#24292E`) | 10.69 : 1 | 12.76 : 1 |
| Blue (`#005CC5`) | 4.59 : 1 | 5.47 : 1 |
| Purple (`#6F42C1`) | 4.75 : 1 | 5.66 : 1 |
| Orange (`#E36209`) | 2.54 : 1 | 3.04 : 1 |

It is paid for in separation: the surface now stands at 1.12 : 1 against the page ground instead of
1.34 : 1. That is why the block takes its border from `--tpl-rule` — exactly the colour its fill
used to be.

> [!warning] One colour of the syntax theme stays below the threshold
> The orange `github-light` uses for CSS variable names reaches only 3.04 : 1 even on the lighter
> surface, against the 4.5 : 1 WCAG asks for text. That is not a consequence of this change — it
> was 2.54 : 1 before — but it is the one place in this template where a visible colour has not
> passed a measurement. Curing it would mean changing the syntax theme or overriding that one
> token.

Long lines do not wrap, they scroll inside the block.

## The language label

At the top left stands the language — as an `::after` in the stylesheet, not as an element. So it
does not end up in a copy, nor in the reading order.

## The copy button

**Out of the box** it appears only on hover with a pointer — on a phone it is therefore
unreachable.

**In this template** it appears on hover, **on focus** and **permanently on devices without a
pointer** (`@media (hover: none)`). It measures 44 px, while the symbol inside stays small. It is
hidden through `opacity`, never through `display` — otherwise it would not be there for the
keyboard at all.

And it is **the icon alone**: no border, no surface. Its state is the colour of the icon, from
`gray` to `dark`.

> [!bug] The exception to the layering rule
> "Everything in `custom.scss` is unlayered and therefore beats the plugin styles" — true for
> component CSS, not for **resource stylesheets**. Quartz ships this button's styling in
> `static/resource-style-….css`, unlayered and linked *after* `index.css`. At equal specificity the
> later rule wins:
>
> ```css
> .clipboard-button { float: right; border: 1px solid; border-color: var(--dark);
>                     background-color: var(--light); margin: .3rem; padding: .4rem }
> ```
>
> Measured on the built page: the button still reported a 1px border and `--light` behind it,
> although every rule in this template said `border: none` and `background: transparent`. One
> descendant in the selector (`pre .clipboard-button`) settles it.

## Highlighted lines

Surface **and** a bar on the left. A tint alone is too weak on a block that is tinted anyway.
