---
title: Mathematik
description: LaTeX inline und als Block, gerendert mit KaTeX.
section: Formatierung
tags:
  - referenz
  - formatierung
---

Das Plugin *LaTeX* ist mit der Engine KaTeX aktiv.

## Inline

```md
Die Masse-Energie-Äquivalenz $E = mc^2$ mitten im Satz.
```

Die Masse-Energie-Äquivalenz $E = mc^2$ mitten im Satz.

## Als Block

```md
$$
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
$$
```

$$
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
$$

## Mehrzeilig

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

## Matrix

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

## Eine lange Formel

Auch hier gilt: was zu breit ist, scrollt in sich selbst statt die Spalte zu sprengen.

$$
f(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + a_5 x^5 + a_6 x^6 + a_7 x^7 + a_8 x^8 + a_9 x^9
$$
