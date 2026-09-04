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

## Highlighted lines

Surface **and** a bar on the left. A tint alone is too weak on a block that is tinted anyway.
