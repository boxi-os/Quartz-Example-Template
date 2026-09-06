---
title: Formulas in a sentence
description: LaTeX in the middle of a sentence.
section: 2 Formatting
tags:
  - formatting
  - math
translationKey: formatierung/mathematik/inline
cover: "[[assets/covers/cover-mathematik.svg]]"
---

A single dollar sign encloses the formula:

```md
Mass-energy equivalence $E = mc^2$ in the middle of a sentence.
```

Mass-energy equivalence $E = mc^2$ in the middle of a sentence.

## A few common symbols

```md
Fractions: $\frac{a}{b}$ · roots: $\sqrt{2}$ · sums: $\sum_{i=1}^{n} i$
Greek: $\alpha, \beta, \gamma$ · comparisons: $a \leq b \neq c$
```

Fractions: $\frac{a}{b}$ · roots: $\sqrt{2}$ · sums: $\sum_{i=1}^{n} i$
Greek: $\alpha, \beta, \gamma$ · comparisons: $a \leq b \neq c$

## Showing a dollar sign

Anyone writing about money escapes it:

```md
That costs \$5.
```

That costs \$5.

Rendering is done with KaTeX; set on the *LaTeX* [[en/7-reference/01-glossary#Plugin|plugin]] through `renderEngine`.
