---
title: Excalidraw
description: Diagrams that look hand-drawn and stay interactive on the site.
section: Obsidian formats
tags:
  - obsidian-formats
  - excalidraw
translationKey: obsidian-formate/excalidraw/index
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

Excalidraw is a drawing tool for sketches, diagrams and processes. As an Obsidian plugin it stores
the drawing in an `.excalidraw.md` — a Markdown file with embedded JSON.

The drawing in this vault:
[[en/obsidian-formats/excalidraw/Structure of the editorial frame.excalidraw|Structure of the editorial frame]]

How the format is built: [[en/obsidian-formats/excalidraw/how-it-works|How it works]].

## What the Quartz plugin makes of it

Not an image but **interactive SVG**: it can be zoomed and panned. Shapes, text, arrows and
freehand strokes are redrawn, colours adapt to the colour scheme — the plugin brings a dark
counterpart for all 65 Excalidraw colours.

Embedded notes (`[[note]]` inside the drawing) are resolved and shown with their content.

## Two things worth knowing

**Editing needs the plugin in the vault.** In this vault it is installed. Without the plugin
Obsidian shows only the warning at the top of the file.

**The plugin is not a core part of Quartz.** It has to be installed through the plugin management —
unlike Bases and Canvas, which are already there.
