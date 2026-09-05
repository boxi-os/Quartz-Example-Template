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

This page carries more frontmatter than is displayed. The template lists seven fields in
`includedProperties`: `description`, `tags` and `section`, which any page may have, plus `zahl`,
`wahr`, `liste` and `leer` — the four that exist only here and on
[[en/formatting/properties/data-types|Data types]], and that demonstrate the four value types. That
is why the table above counts seven.

Not shown are `falsch`, `aliases` and `translationKey`: the first is in the frontmatter but not in
the list, the other two are plumbing and would stand on nearly every page.

To see all fields, set the option `includeAll` to true in the app under *Plugins → Note
properties*.

See also [[en/formatting/properties/frontmatter|Frontmatter]] in the formatting reference.
