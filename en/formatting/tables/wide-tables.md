---
title: Wide tables
description: What happens when a table does not fit the column.
section: Formatting
tags:
  - formatting
  - tables
translationKey: formatierung/tabellen/breite-tabellen
cover: "[[assets/covers/cover-tabellen.svg]]"
---

| Name | Label | Area | Default | Description |
| ------- | ----------- | ------- | -------- | ------------ |
| `--tpl-space-md` | Space medium | Space | 1rem | The base gap between blocks |
| `--tpl-space-lg` | Space large | Space | 1.5rem | Between blocks and around figures |
| `--tpl-radius-md` | Radius medium | Shape | 8px | Corners of cards and code blocks |
| `--tpl-focus-color` | Focus colour | State | var(--secondary) | Colour of the focus ring |
| `--tpl-indent` | Indent | Structure | 0.85rem | One level in explorer and table of contents |
| `--tpl-target` | Target size | Operation | 44px | Minimum size of every control |

This table is wider than the text column. It **scrolls inside itself** — the page stays put.

## Why that is not a given

Quartz wraps every table in a container (`.table-container`). The scrolling belongs there, not on
the table. The obvious first attempt — `display: block; overflow-x: auto` on the `<table>` itself —
takes the table layout apart: while building this template it made the keys and values of the
property table slide on top of each other.

A table that pushes the layout aside is the most common way to break a grid.
