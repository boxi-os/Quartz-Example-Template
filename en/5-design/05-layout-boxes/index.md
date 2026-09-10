---
title: 5.5 – Layout boxes
description: A plugin that puts arbitrary markup at any place in the layout.
section: 5 – The design
tags:
  - design
  - layout-box
translationKey: gestaltung/layout-boxen/index
---

`quartz-layout-box` renders an [[en/7-reference/01-glossary#HTML|HTML]] or [[en/7-reference/01-glossary#Markdown|Markdown]] snippet at any place in the page layout: header,
sidebars, before or after the content, footer. This template uses it **seven times**, each time for
something different — twice of those without a box coming out of it at all.

## What the plugin can do

| Possibility | Option |
| --- | --- |
| Content from a file | `file:` |
| Content from the configuration | `html:` |
| Markdown instead of HTML | let the file end in `.md` |
| A heading above it | `title:` |
| Collapsible | `collapsible:` and `collapsed:` |
| A [[en/7-reference/01-glossary#CSS and SCSS\|CSS]] class of your own | `className:` |
| Replace placeholders | `placeholders:` |
| Controllable per page | `frontmatterKey:` |
| Different per language | `byLang:` |
| An image per [[en/7-reference/01-glossary#Colour scheme\|colour scheme]] | classes `img-light` / `img-dark` |

## Placeholders

`{{title}}`, `{{slug}}`, `{{root}}`, `{{siteTitle}}`, `{{baseUrl}}`, `{{locale}}`, `{{lang}}` and
every [[en/7-reference/01-glossary#Frontmatter|frontmatter]] field through `{{frontmatter.name}}`. `{{root}}` is the relative path to the home
page — so a link works even when the page sits in a sub-path.

`{{locale}}` names the language of **the page** (from the `lang` frontmatter field) and only falls
back to `configuration.locale` when the page has none. `{{lang}}` is its front part: `en` rather
than `en-US`.

## The design

The [[en/7-reference/01-glossary#Plugin|plugin]] deliberately ships **colourless** styles: width, image switching, a dashed placeholder
for missing files. That is the right decision for a component plugin — it leaves the appearance to
the site.

This template designs every class: `.layout-box`, `.layout-box-title`, `.layout-box-content`,
`.layout-box-missing`, plus seven variants of its own.

Further: [[en/5-design/05-layout-boxes/the-instances|The instances]] ·
[[en/4-controlling-a-page/05-layout-boxes-per-page|Controlling it per page]]

## The pages

- [[en/5-design/05-layout-boxes/the-instances|The instances]] — The same plugin, seven times, for something different each time.
