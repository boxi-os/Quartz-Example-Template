---
title: 3.3 Excalidraw
description: Diagrams that look hand-drawn and stay interactive on the site.
section: Obsidian formats
tags:
  - obsidian-formats
  - excalidraw
translationKey: obsidian-formate/excalidraw/index
---

Excalidraw is a drawing tool for sketches, diagrams and processes. As an Obsidian [[en/7-reference/01-glossary#Plugin|plugin]] it stores
the drawing in an `.excalidraw.md` — a [[en/7-reference/01-glossary#Markdown|Markdown]] file with embedded JSON.

The drawing in this [[en/7-reference/01-glossary#Vault|vault]]:
[[en/3-obsidian-formats/03-excalidraw/Structure of the editorial frame.excalidraw|Structure of the editorial frame]]

How the format is built: [[en/3-obsidian-formats/03-excalidraw/how-it-works|How it works]].

## What the Quartz plugin makes of it

Not an image but **interactive SVG**: it can be zoomed and panned. Shapes, text, arrows and
freehand strokes are redrawn, colours adapt to the [[en/7-reference/01-glossary#Colour scheme|colour scheme]] — for that the plugin keeps a
table of 63 pairs, each a light Excalidraw colour and its dark counterpart.

Embedded notes (`[[note]]` inside the drawing) are resolved and shown with their content.

## Two things worth knowing

**Editing needs the plugin in the vault.** In this vault it is installed. Without the plugin
Obsidian shows only the warning at the top of the file.

**The plugin is not a core part of Quartz.** It has to be installed through the plugin management —
unlike [[en/7-reference/01-glossary#Base|Bases]] and [[en/7-reference/01-glossary#Canvas|Canvas]], which are already there.

> [!warning] A drawing page stands on its own
> Unlike with canvas, here the plugin brings its own page grid and this template does not override
> it. A drawing page therefore has neither an [[en/7-reference/01-glossary#Explorer|explorer]] nor a page apparatus — and, measured on the
> built markup, **no language switcher** either: the two drawings are the one page pair on this
> site that is not linked at all. See
> [[en/6-adapting/07-two-languages/linking|How the two languages find each other]].

## The pages

- [[en/3-obsidian-formats/03-excalidraw/how-it-works|How an Excalidraw file is built]] — Markdown outside, drawing data inside — and the second, simpler way.
- [[en/3-obsidian-formats/03-excalidraw/Structure of the editorial frame.excalidraw|Structure of the editorial frame.excalidraw]]
