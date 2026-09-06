---
title: All callout types
description: Thirteen types with their aliases — and why their colours are set anew here.
section: Formatting
tags:
  - formatting
  - callouts
translationKey: formatierung/callouts/alle-typen
cover: "[[assets/covers/cover-callouts.svg]]"
---

> [!note] note
> The default type.

> [!abstract] abstract
> Aliases: `summary`, `tldr`.

> [!info] info
> A factual addition.

> [!todo] todo
> What is still to be done.

> [!tip] tip
> Aliases: `hint`, `important`.

> [!success] success
> Aliases: `check`, `done`.

> [!question] question
> Aliases: `help`, `faq`.

> [!warning] warning
> Aliases: `caution`, `attention`.

> [!failure] failure
> Aliases: `fail`, `missing`.

> [!danger] danger
> Alias: `error`.

> [!bug] bug
> A fault in the program.

> [!example] example
> An example.

> [!quote] quote
> Alias: `cite`. Takes the accent colour of the page rather than one of its own.

## What this template does differently

**Out of the box** Quartz sets twelve colours for these thirteen types and lets `note` keep the
base colour. Measured against the light page ground of this template, **eleven of the thirteen**
fail the WCAG threshold of 4.5:1 — `note` reaches 3.23:1, `question` only 2.14:1. Only `example`
and `quote` get through. In dark mode the picture nearly inverts: four fail there, and `example` is
one of them (2.81:1). The red of `danger`, `failure` and `bug` fails in **both** modes, at 4.20 and
4.16:1.

**In this template** all thirteen are set anew, once per mode, and measured on every run: against
the page ground *and* against the callout's own tinted surface. The hue is kept — blue stays blue —
so that the type is still recognisable by its colour.

The numbers are under [[en/design/foundations/colours-and-contrast|Colours and contrast]].
