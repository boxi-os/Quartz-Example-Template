---
title: 3.2 – Canvas
description: An infinite surface with cards and connections.
section: 3 – Obsidian formats
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

> [!bug] Links inside a file node can lead nowhere
> A file node shows a note with all of its content — and the links inside it get the embedded
> note's folder prefixed **once more**. Whether the target still holds after that depends on how
> deep the note lies. Measured on 2026-09-06: with the seven chapter pages as nodes (one folder
> level deep) **113 links** were broken in the English version — the reference to the glossary
> became `../../../en/1-getting-started/../../../en/7-reference/01-glossary`, a path that leads out
> of the site. With the present seven nodes, all two or three levels deep, no link is broken except
> the one to the draft, which is broken on purpose. That is why no chapter pages sit here. A link
> in a *text node* is not resolved at all — `[[…]]` stays there as text. And a file node's label is
> the file name, not the title.
>
> That is a bug in the `canvas-page` plugin, not in this template — the links are correct on their
> own pages. Anyone who needs them clicks the node's title and reads the note there.

> [!note] Zooming and panning
> On the built page the canvas can be zoomed with the mouse wheel and moved with the mouse button
> held down — it is not a [[en/7-reference/01-glossary#Snapshot|snapshot]] but the surface itself.

## The pages

- [[en/3-obsidian-formats/02-canvas/how-it-works|How a canvas is built]] — JSON with nodes and edges.
- [[en/3-obsidian-formats/02-canvas/Structure of the template.canvas|Structure of the template]] — a canvas

<!-- QuartzControl:variables:start -->
## Which variables apply here

These 14 variables are read by `page-canvas.scss`. They can be changed in the app under *Styles → Variables* — without a line of CSS.

| Variable | Value | also applies to |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 other components |
| `--dark` | `#17171A` · dark `#FCFCFA` | 13 other components |
| `--darkgray` | `#333333` · dark `#DDDDDD` | 18 other components |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 other components |
| `--light` | `#FCFCFA` · dark `#16171A` | 13 other components |
| `--secondary` | `#1463A3` · dark `#699DC3` | 20 other components |
| `--tpl-motion` | `150ms ease` | 12 other components |
| `--tpl-radius-md` | `8px` | 16 other components |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 other components |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 10 other components |
| `--tpl-rule-width` | `1px` | 24 other components |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 other components |
| `--tpl-target` | `44px` | 11 other components |
| `--tpl-text-sm` | `0.875rem` | 19 other components |

*This table is generated: it is read out of the stylesheets rather than kept by hand.*
<!-- QuartzControl:variables:end -->
