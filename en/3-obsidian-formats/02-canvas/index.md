---
title: 3.2 Canvas
description: An infinite surface with cards and connections.
section: Obsidian formats
tags:
  - obsidian-formats
  - canvas
translationKey: obsidian-formate/canvas/index
---

A canvas is a free surface: you put cards on it, connect them with arrows and arrange them spatially
rather than in a sequence. For connections that are not an outline.

The example in this [[en/7-reference/01-glossary#Vault|vault]]:
[[en/3-obsidian-formats/02-canvas/Structure of the template.canvas|Structure of the template]] — the seven
chapters of this handbook and how they hang together.

How the format is built: [[en/3-obsidian-formats/02-canvas/how-it-works|How it works]].

## In this template

A canvas page needs the **full width** — a surface in the narrow text column shows nothing. The
[[en/7-reference/01-glossary#Plugin|plugin]] does bring a page grid of its own for that, but this template overrides it: the
configuration puts Quartz's built-in `full-width` grid on the `canvas` page type. Measured on the
built page the result is header, surface and footer — no sidebars, no [[en/7-reference/01-glossary#Breadcrumbs|breadcrumbs]].

> [!bug] Links inside a file node lead nowhere
> A file node shows a note with all of its content — and the links inside it get the embedded
> note's folder prefixed **twice**. The reference to `en/design/foundations/frames` in the [[en/7-reference/01-glossary#Base|bases]]
> overview becomes, on this page,
> `../../../en/obsidian-formats/bases/../../../../en/obsidian-formats/bases/all-views.base` — a path
> that leads out of the site. Measured: **six per language**, all in the same file node, and the
> number grows with every link added to an embedded note.
>
> That is a bug in the `canvas-page` plugin, not in this template — the links are correct on their
> own pages. Anyone who needs them clicks the node's title and reads the note there.

> [!note] Zooming and panning
> On the built page the canvas can be zoomed with the mouse wheel and moved with the mouse button
> held down — it is not a [[en/7-reference/01-glossary#Snapshot|snapshot]] but the surface itself.

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 14 variables are read by `page-canvas.scss`. They can be changed in the app under *Styles → Variables* — without a line of [[en/7-reference/01-glossary#CSS and SCSS|CSS]].

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--dark` | `#17171A` · dark `#F3F4F6` | 13 other components |
| `--darkgray` | `#33322E` · dark `#D5D7DB` | 18 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#2A4E6C` · dark `#8CB8DA` | 20 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 18 other components |

*This table is generated: it is read out of the [[en/7-reference/01-glossary#Stylesheet|stylesheets]] rather than kept by hand.*
<!-- QuartzControl:variables:end -->

## The pages

- [[en/3-obsidian-formats/02-canvas/how-it-works|How a canvas is built]] — JSON with nodes and edges.
- [[en/3-obsidian-formats/02-canvas/Structure of the template.canvas|Structure of the template]] — a canvas
