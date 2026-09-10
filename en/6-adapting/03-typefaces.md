---
title: 6.3 – Typefaces
description: Three families, self-hosted — and why the @font-face rules are replaced.
section: 6 – Adapting
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

Until 2026-09-06, when a font file was imported the app created a `@font-face` rule **without
`font-weight` and without `font-style`**. With a variable font that meant: the browser treats it as
weight 400 and distorts every bold cut itself instead of using the axis that ships with it. With two
cuts of the same family the second displaced the first — exactly the case of this template's upright
and italic Inter.

**That is fixed.** The app now reads the weight axis and the italic bit out of the file itself and
writes both. One value is still missing: the `unicode-range`. Without it the browser loads the file
for characters the Latin subset does not contain at all, and then sets them from a typeface that has
no glyph for them instead of falling back to the stack.

This template therefore still replaces the generated block — with the same weights and styles the
app would write itself today, plus the range.

## Fallback

Every role has a real stack behind it (`ui-sans-serif, system-ui, …`). If a woff2 does not load,
the page falls back on something chosen, not on the browser's default.
