---
title: Formula blocks
description: Displayed formulas, over several lines and as a matrix.
section: 2 Formatting
tags:
  - formatting
  - math
translationKey: formatierung/mathematik/bloecke
cover: "[[assets/covers/cover-mathematik.svg]]"
---

Two dollar signs set the formula as a block of its own:

```md
$$
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
$$
```

$$
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
$$

## Aligned over several lines

```md
$$
\begin{aligned}
a &= b + c \\
  &= d + e + f \\
  &= g
\end{aligned}
$$
```

$$
\begin{aligned}
a &= b + c \\
  &= d + e + f \\
  &= g
\end{aligned}
$$

The `&` marks the place where the lines line up.

## Matrices

```md
$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$
```

$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

## Formulas that are too wide

$$
f(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + a_5 x^5 + a_6 x^6 + a_7 x^7 + a_8 x^8 + a_9 x^9
$$

The same applies here: what is too wide scrolls inside itself instead of blowing up the column.
