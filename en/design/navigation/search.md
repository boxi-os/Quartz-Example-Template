---
title: Search
description: The field in the bar and the overlay behind it.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/suche
---

## Out of the box

A button with a magnifying glass that opens an overlay. The border comes from `lightgray`.

## In this template

- The border comes from **`gray`**, not from `lightgray`. That is the contrast rule put into
  practice: `lightgray` measures 1.34:1 against the ground and may therefore not surround anything
  you operate.
- The button sits **in the header**, at the far right, together with the three other controls. It
  is 44 px high like its neighbours. On a phone it becomes a square without a label.
- The **overlay** carries a real shadow. In this template only what genuinely floats above the page
  rather than sitting in it gets one: this overlay, the link preview, the language menu, the drawer
  on a phone and the global graph. Five places — and it is the rule that counts, not the number.
- The **input field** gets no focus ring but a heavier bottom edge — a ring inside a rounded box
  looks like a mistake.
- **Results**: the keyboard cursor and the pointer hover look the same. The arrow keys move through
  the list, and the highlighted row is the only signal of where you are.
- The **match in the text** is marked with the same colour as `==highlight==` in the body text.
  "This is what you were looking for" means the same thing across the whole site.

With `prefers-reduced-transparency` the translucent surface is replaced by an opaque one.

> [!bug] The field never reaches its width
> `nav-toolbar.scss` gives it `flex: 0 1 15rem` — 240 px to start from, shrinking allowed. Measured
> it is **110 px**, equally at 1728, 1440, 1100 and 900 px of window width, even though the toolbar
> occupies only 322 of 1400 px there. The reason sits one level down: Quartz wraps every component
> in a class-less `div` of its own, and *that* one is `flex: 0 1 auto` and shrinks to its content.
> The 15 rem are on the wrong element. So the button reads as a button rather than as a field —
> exactly what the width was meant to prevent.

> [!note] The index spans both languages
> There is one search index for the whole site, so a German page can turn up in an English search
> result. Splitting it would mean one build per language — see
> [[en/design/multilingual/limits|Where the two languages stop]].
