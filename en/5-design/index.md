---
title: 5 The design
description: What Quartz does out of the box and what this template changes about it — component by component, with the table of the variables each of them reads.
section: Design
tags:
  - design
translationKey: gestaltung/index
---

A Quartz site consists of **components**: the [[en/7-reference/01-glossary#Explorer|explorer]], the search, the table of contents, the
[[en/7-reference/01-glossary#Breadcrumbs|breadcrumbs]], the footer — each built by a [[en/7-reference/01-glossary#Plugin|plugin]], each with a look of its own. This chapter goes
through them in turn, sorted by their place on the page; the places are named in
[[en/1-getting-started/04-how-a-page-is-built|1.4 How a page is built]].

## How every page is built

Every page deals with **one** component and has two paragraphs:

> **Out of the box** — what Quartz does without any help.
> **In this template** — what is different here, and why.

The comparison stands right next to the element you are looking at. Whoever compares their own
site with this one finds the difference named that way. And whoever wants to change it finds, at
the bottom of the same page, the table **“Which variables apply here”**: the variables the
stylesheet of this component reads, with their value and a note on what else moves with them.
These tables are generated, not kept by hand; they cannot disagree with the stylesheets.

A **stylesheet** is the file in which the look is described — in the language [[en/7-reference/01-glossary#CSS and SCSS|CSS]], here in its
extension [[en/7-reference/01-glossary#CSS and SCSS|SCSS]]. This template has 30 of them, one per component, and every page here names its
own. They can be changed in QuartzControl under *Styles → Custom CSS*; when that is necessary and
when a variable is enough stands in [[en/6-adapting/01-changing-something|6.1 Changing something]].

## The sections

| Section | Components |
| --- | --- |
| [[en/5-design/01-navigation/index\|5.1 Navigation]] | explorer, search, [[en/7-reference/01-glossary#Colour scheme\|colour scheme]], reader mode, header, footer, language switcher |
| [[en/5-design/02-above-the-content/index\|5.2 Above the content]] | breadcrumbs, title and date, properties, tags |
| [[en/5-design/03-in-the-content/index\|5.3 In the content]] | body text, [[en/7-reference/01-glossary#Callout\|callouts]], code, tables and media |
| [[en/5-design/04-beside-the-content/index\|5.4 Beside the content]] | table of contents, [[en/7-reference/01-glossary#Backlinks\|backlinks]], [[en/7-reference/01-glossary#Graph\|graph]], recently changed |
| [[en/5-design/05-layout-boxes/index\|5.5 Layout boxes]] | one plugin, used five times |
| [[en/5-design/06-generated-pages/index\|5.6 Generated pages]] | folder and tag pages, search results, link preview, error page |

Two components stand elsewhere, because their stylesheet belongs to a section in chapter 2: the
diagrams under [[en/2-formatting/09-diagrams/index|2.9 Diagrams]] and the formulas under
[[en/2-formatting/08-math/index|2.8 Mathematics]]. And what lies under everything — colours,
typefaces, variables, page grids, [[en/7-reference/01-glossary#Accessibility|accessibility]] — is chapter [[en/6-adapting/index|6 Adapting]].

## The three decisions everything else rests on

1. **The width decides the grid** — the [[en/7-reference/01-glossary#Frame|frame]], in one place, not the paragraph on top of it.
2. **Colours are measured.** 89 pairs, all above the [[en/7-reference/01-glossary#WCAG|WCAG]] threshold, in both modes.
3. **Colour and measure do not stand in the stylesheets** but in 53 variables that stay editable
   in the app. What does stand there literally is named and justified.
