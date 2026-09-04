---
title: Formulas in a sentence
description: LaTeX in the middle of a sentence.
section: Formatting
tags:
  - formatting
  - math
translationKey: formatierung/mathematik/inline
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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

Rendering is done with KaTeX; set on the *LaTeX* plugin through `renderEngine`.
