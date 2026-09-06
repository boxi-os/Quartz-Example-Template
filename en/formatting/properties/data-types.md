---
title: Data types
description: Text, number, boolean, list — and how they are displayed.
section: Formatting
tags:
  - formatting
  - frontmatter
number: 42
truthy: true
falsy: false
list:
  - one
  - two
  - three
empty:
translationKey: formatierung/eigenschaften/datentypen
cover: "[[assets/covers/cover-eigenschaften.svg]]"
---

This page carries five example fields itself. The property table above this text shows them.

````md
---
number: 42
truthy: true
falsy: false
list:
  - one
  - two
empty:
---
````

| Type | Notation | Display in this template |
| --- | --- | --- |
| Text | `field: value` | as it is |
| Number | `number: 42` | in figure width (`tabular-nums`) |
| Boolean | `wahr: true` / `falsch: false` | as a word — true in the positive colour, false muted |
| List | entries with `-` | as a row of markers |
| Empty | `empty:` | italic and muted |
| Date | `date: 2026-09-01` | formatted by locale |

## What is displayed is decided by the configuration

The *Note properties* plugin does not show everything by default, only the fields from
`includedProperties`. This template lists `description`, `tags`, `section` and the five demo fields
of this page — in both languages, because the German version names them in German. A field a page
does not have gets no row.
