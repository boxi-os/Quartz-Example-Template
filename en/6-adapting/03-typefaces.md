---
title: 6.3 Typefaces
description: Three families, self-hosted — and why the @font-face rules are corrected by hand.
section: Adapting
tags:
  - adapting
translationKey: anpassen/schriften
---

| Role | Typeface | What for |
| --- | --- | --- |
| header | **Instrument Sans** | headings, labels, controls |
| body | **Inter** | body text, upright and italic |
| code | **JetBrains Mono** | code, numbers in tables, paths |

All three are under the SIL Open Font License and are **self-hosted** — four files, Latin subset,
157 KB together. No request goes to Google.

## Why self-host

**Out of the box** Quartz loads typefaces from Google Fonts — convenient, but every page request
goes to a third party in the process. This template sets `fontOrigin: 'local'` and switches the
fonts [[en/7-reference/01-glossary#Plugin|plugin]] off; with that, neither of the two Google routes runs.

## The finding behind it

When a font file is imported, the app creates a `@font-face` rule — **without `font-weight` and
without `font-style`**. With a variable font that means: the browser treats it as weight 400 and
distorts every bold cut itself instead of using the axis that ships with it. With two cuts of the
same family, the second displaces the first.

This template therefore corrects the generated block: with `font-weight: 400 700`, `font-style` and
`unicode-range`. On the page the difference can be seen on every bold word.

## Fallback

Every role has a real stack behind it (`ui-sans-serif, system-ui, …`). If a woff2 does not load,
the page falls back on something chosen, not on the browser's default.
