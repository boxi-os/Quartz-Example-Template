---
title: Displaying the properties
description: Where the table sits, what it shows and how to change that.
section: Formatting
tags:
  - formatting
  - frontmatter
translationKey: formatierung/eigenschaften/anzeige
cover: "[[assets/covers/cover-eigenschaften.svg]]"
---

The properties sit as a collapsible table between the date and the text.

## The adjusting screws

| Option | Effect |
| --- | --- |
| `includeAll: true` | shows **every** frontmatter field |
| `includedProperties` | shows only these, in this order |
| `excludedProperties` | hides individual ones |
| `hidePropertiesView: true` | switches the table off entirely |

In this template `includeAll` is `false` — otherwise every page would carry the same repetition of
what stands above it anyway.

## In this template

**Out of the box** the plugin renders a plain table in the text colour.

**In this template** it sits on a tinted surface with a border, the key is set muted and narrow,
the value takes the rest. The header row is small capitals — it is a label, not content.

One detail with a measurement behind it: the key column gets **no** width assigned; the value
column gets `width: 100%` instead. Both mean "the key is as wide as its content" — but only the
second way works. With `width: 1%` on the key the cell measured 7.94 px, and the text lay on top of
the value.
