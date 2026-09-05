---
title: Breadcrumbs
description: The path from the home page to here.
section: Design
tags:
  - design
  - above-the-content
translationKey: gestaltung/ueber-dem-inhalt/brotkrumen
---

## Out of the box

A row with the folders of the path, separated by a character.

## In this template

- The **last crumb is the current page**: set more heavily and not clickable. A link to the page
  you are standing on is a dead end.
- The **separator** is muted and cannot be selected — it should not end up in a copy.
- The row **wraps** rather than overflowing. Four levels deep, the path on a phone is longer than
  the screen.
- Every crumb has **padding above and below**, so that it can be hit on a touchscreen.

A deep example: [[en/handbook/basics/terms/abbreviations/list|List]] — there the whole path stands
over five stations.

> [!note] Not on the home page
> The component is configured with `condition: not-index`; on a folder home page the last crumb
> would be identical to the title below it.

> [!note] The language folder is a crumb too
> On an English page the path begins with `en` — it is a folder like any other, and Quartz has no
> reason to treat it differently.
