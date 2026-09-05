---
title: The graph
description: The surroundings of a note as a network.
section: Design
tags:
  - design
  - page-apparatus
translationKey: gestaltung/seitenapparat/graph
---

## Out of the box

A box with the local surroundings, plus a symbol for opening the global view.

## In this template

The graph draws itself and takes its colours from the CSS variables at runtime. The template
therefore designs **only the box around it**, not the drawing:

- a **square field** (`aspect-ratio: 1`) — the local graph is round, and a wide box wastes the
  sidebar
- border and tinted surface as with the other panels
- the **symbol for the global view** is 44 px across and sits at the right of the heading row
- the **global view** gets the same shadow as the search — both really do float

A half-recoloured graph would be worse than one in foreign colours: the drawing resolves its own
colours, and a stylesheet working against that always catches only half of them.

**On narrow screens it is hidden** (`display: desktop-only`) — a net of dots in a column 390 px
wide shows nothing.
