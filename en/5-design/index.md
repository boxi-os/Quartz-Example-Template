---
title: 5 The design
description: What Quartz does out of the box, and what this template changes about it — per component.
section: Design
tags:
  - design
translationKey: gestaltung/index
---

Every page in this area treats **one** component and has two paragraphs:

> **Out of the box** — what Quartz does without being asked.
> **In this template** — what is different here, and why.

The comparison stands right next to the element you are looking at while reading it. A collected
list of all the differences would be possible too, but it would be far away from the thing itself.

## The areas

| Area | Components |
| --- | --- |
| [[en/6-adapting/02-colours-and-contrast\|Foundations]] | colours, typefaces, tokens, frames, accessibility, adapting |
| [[en/5-design/01-navigation/explorer\|Navigation]] | explorer, search, colour scheme, reader mode, header, footer |
| [[en/5-design/04-beside-the-content/table-of-contents\|Page apparatus]] | table of contents, backlinks, graph, recently changed |
| [[en/5-design/02-above-the-content/breadcrumbs\|Above the content]] | breadcrumbs, title, date, properties, tags |
| [[en/5-design/03-in-the-content/body-text\|In the content]] | body text, callouts, code, tables, media |
| [[en/5-design/06-generated-pages/folders-and-tags\|Page types]] | folder and tag listings, preview, search, error page |
| [[en/5-design/05-layout-boxes/index\|Layout box]] | the template's own plugin in five flavours |
| [[en/6-adapting/07-two-languages/index\|Two languages]] | detection, linking, the switcher, and where it stops |

## The three decisions everything else rests on

1. **The width decides the grid** — the frame, in one place, not the paragraph as well.
2. **Colours are measured.** 87 pairs, all above the WCAG threshold, in both modes.
3. **Neither colour nor measure lives in the stylesheets** — both come from 53 variables that stay
   editable in the app. What does stand literally is named and accounted for.
