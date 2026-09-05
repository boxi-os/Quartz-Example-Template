---
title: Callout colours
description: Twelve colours, all of them set anew and measured.
section: Design
tags:
  - design
  - in-the-content
  - callouts
translationKey: gestaltung/im-inhalt/callouts
---

## Out of the box

Quartz ships twelve type colours, each the same in both colour schemes, plus a border and a very
pale surface.

Measured against the light ground of this template, **eleven of twelve** fail the WCAG threshold:

| Type | Default colour | against the light ground |
| --- | --- | --- |
| `note` | `#448aff` | 3.23 : 1 |
| `question` | `#dba642` | 2.14 : 1 |
| `tip` | `#00bfa5` | 2.27 : 1 |
| `danger` / `failure` / `bug` | `#db4242` | 4.20 : 1 — and 4.16 : 1 in dark mode |

## In this template

All thirteen are set anew, **once per mode**, and are measured twice on every run: against the page
ground and against their own tinted surface. The hue is kept — blue stays blue — so that the type
is still recognisable by its colour.

Plus three structural decisions:

- **A bar rather than a full frame.** A callout should stand out without cutting the column in two.
- **The title is the control** when the callout is foldable — with a focus ring of its own in the
  type colour.
- **Nested callouts** give up their frame and keep only the bar.

The check reads the colours **from the stylesheet**, not from a copy in the configuration. A value
changed here is measured here.
