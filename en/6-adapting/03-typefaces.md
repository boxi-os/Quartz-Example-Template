---
title: 6.3 – Typefaces
description: Two families, self-hosted — and why the @font-face rules are replaced.
section: 6 – Adapting
tags:
  - adapting
translationKey: anpassen/schriften
---

| Role | Typeface | What for |
| --- | --- | --- |
| header | **Noto Sans** | headings, labels, controls |
| body | **Noto Sans** | body text, upright and italic |
| code | **Noto Sans Mono** | code, numbers in tables, paths |

Both are under the SIL Open Font License and are **self-hosted** — three files, Latin subset,
105 KB together. No request goes to Google.

Headings and body text share one family. The difference between them comes from size and
weight — headings stand at 600 —, not from a change of typeface. Until 2026-09-20 there were three
families (Instrument Sans, Inter, JetBrains Mono) in four files; one family fewer saves the site a
file and takes nothing from it that a reader could name.

## Why self-host

**Out of the box** Quartz loads typefaces from Google Fonts — convenient, but every page request
goes to a third party in the process. This template sets `fontOrigin: 'local'` and switches the
fonts [[en/7-reference/01-glossary#Plugin|plugin]] off; with that, neither of the two Google routes runs.

## The finding behind it

Until 2026-09-06, when a font file was imported the app created a `@font-face` rule **without
`font-weight` and without `font-style`**. With a variable font that meant: the browser treats it as
weight 400 and distorts every bold cut itself instead of using the axis that ships with it. With two
cuts of the same family the second displaced the first — exactly the case of the upright and italic
cuts this template brings for its text face.

**That is fixed.** The app now reads the weight axis and the italic bit out of the file itself and
writes both. One value is still missing: the `unicode-range`. Without it the browser loads the file
for characters the Latin subset does not contain at all, and then sets them from a typeface that has
no glyph for them instead of falling back to the stack.

This template therefore still replaces the generated block — with the same weights and styles the
app would write itself today, plus the range.

## Fallback

Quartz itself puts a stack behind every role — `system-ui, "Segoe UI", Roboto, …` for text,
`ui-monospace, SFMono-Regular, …` for code. If a woff2 does not load, the page falls back on
something chosen, not on the browser's default.
