---
title: Many properties
description: A page with a full frontmatter, to show the property table.
section: Examples
date: 2026-07-02
lastmod: 2026-09-01
tags:
  - examples
  - frontmatter
  - reference
aliases:
  - Frontmatter example
number: 42
truthy: true
falsy: false
list:
  - one
  - two
  - three
empty:
translationKey: beispiele/eigenschaften-demo
---

This page carries more frontmatter than is displayed. The template lists thirteen fields in
`includedProperties`: `description`, `tags` and `section`, which any page may have, plus the five
demo fields — `number`, `truthy`, `falsy`, `list`, `empty` — and the same five again under their
German names, because the German version of this page calls them that. A field a page does not have
gets no row; that is why the table above counts eight.

Not shown are `aliases` and `translationKey`: both are plumbing and would stand on nearly every
page.

To see all fields, set the option `includeAll` to true in the app under *Plugins → Note
properties*.

See also [[en/formatting/properties/frontmatter|Frontmatter]] in the formatting reference.
