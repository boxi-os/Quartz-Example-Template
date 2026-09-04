---
title: All callout types
description: Thirteen types with their aliases — and why their colours are set anew here.
section: Formatting
tags:
  - formatting
  - callouts
translationKey: formatierung/callouts/alle-typen
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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

**Out of the box** Quartz ships twelve colours for these types. Measured against the light page
ground of this template, **eleven of them** fail the WCAG threshold of 4.5:1 — `note` reaches
3.23:1, `question` only 2.14:1. The red of `danger`, `failure` and `bug` even fails in both modes,
at around 4.2:1.

**In this template** all twelve are set anew, once per mode, and measured on every run: against the
page ground *and* against the callout's own tinted surface. The hue is kept — blue stays blue — so
that the type is still recognisable by its colour.

The numbers are under [[en/design/foundations/colours-and-contrast|Colours and contrast]].
