---
title: Code in a sentence
description: A command in the middle of a sentence.
section: 2 Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/inline
cover: "[[assets/covers/cover-code.svg]]"
---

```md
A command like `npm run build` in the middle of a sentence.
```

A command like `npm run build` in the middle of a sentence.

## Backticks inside code

To show a backtick itself, wrap it in two:

```md
A `` ` `` in the middle of the text.
```

A `` ` `` in the middle of the text.

## In this template

**Out of the box** inline code gets a distinct box with a border.

**In this template** it is a tint without a border — enough to separate it from the body text, too
little to interrupt the sentence. The type is set slightly smaller (0.9em), because JetBrains Mono
next to Inter otherwise looks too big. Long identifiers may wrap (`overflow-wrap: anywhere`)
instead of blowing up the column.
