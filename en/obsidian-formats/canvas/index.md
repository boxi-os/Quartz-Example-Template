---
title: Canvas
description: An infinite surface with cards and connections.
section: Obsidian formats
tags:
  - obsidian-formats
  - canvas
translationKey: obsidian-formate/canvas/index
---

A canvas is a free surface: you put cards on it, connect them with arrows and arrange them spatially
rather than in a sequence. For connections that are not an outline.

The example in this vault:
[[en/obsidian-formats/canvas/Structure of the template.canvas|Structure of the template]] — the four
areas of this site and how they hang together.

How the format is built: [[en/obsidian-formats/canvas/how-it-works|How it works]].

## In this template

A canvas page needs the **full width** — a surface in the narrow text column shows nothing. The
plugin does bring a page grid of its own for that, but this template overrides it: the
configuration puts Quartz's built-in `full-width` grid on the `canvas` page type. Measured on the
built page the result is header, surface and footer — no sidebars, no breadcrumbs.

> [!bug] Links inside a file node lead nowhere
> A file node shows a note with all of its content — and the links inside it get the embedded
> note's folder prefixed **twice**. The reference to `en/design/foundations/frames` in the bases
> overview becomes, on this page,
> `../../../en/obsidian-formats/bases/../../../../en/design/foundations/frames` — a path that leads
> out of the site. Measured: **seven per language**, all in the same file node, and the number grows
> with every link added to an embedded note.
>
> That is a bug in the `canvas-page` plugin, not in this template — the links are correct on their
> own pages. Anyone who needs them clicks the node's title and reads the note there.

> [!note] Zooming and panning
> On the built page the canvas can be zoomed with the mouse wheel and moved with the mouse button
> held down — it is not a snapshot but the surface itself.
