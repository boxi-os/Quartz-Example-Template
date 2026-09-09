---
title: Ordered lists
description: Numbered lists and what the numbers really do.
section: 2 – Formatting
tags:
  - formatting
  - lists
translationKey: formatierung/listen/geordnet
cover: "[[assets/covers/cover-listen.svg]]"
---

```md
1. First step
2. Second step
3. Third step
```

1. First step
2. Second step
3. Third step

## The numbers in the source do not matter

[[en/7-reference/01-glossary#Markdown|Markdown]] numbers through on its own. Writing `1.` everywhere still yields 1, 2, 3 — handy when a
point is inserted later.

```md
1. First step
1. Second step
1. Third step
```

1. First step
1. Second step
1. Third step

## Nested and mixed

```md
1. A step
   1. Sub-step
   2. Another one
2. The next step
   - with a note
   - and another
```

1. A step
   1. Sub-step
   2. Another one
2. The next step
   - with a note
   - and another
