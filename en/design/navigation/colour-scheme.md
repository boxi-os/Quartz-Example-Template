---
title: Colour scheme switch
description: The button between light and dark.
section: Design
tags:
  - design
  - navigation
translationKey: gestaltung/navigation/farbschema
---

## Out of the box

A button with two symbols, one of which is visible depending on the scheme.

## In this template

It is part of the toolbar in the header and shares its measurements: 44 × 44 px, the same border,
the same corners as search, reader mode and the language switcher. A row of controls with differing
heights reads as a mistake.

On hover the border changes to the accent colour and the surface to the tinted variant — the same
feedback as with its neighbours.

## A finding while building

The first version of this file styled an `<input>`/`<label>` pair. There is none here: the
component is a single `<button class="darkmode">` with two SVGs in it. The rules hit nothing —
which only became visible when every selector of the template was checked against the built page.

Hence the rule that applies everywhere in this template: **look in the built HTML before writing a
rule.** Class names are no contract.
