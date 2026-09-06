---
title: Formelblöcke
description: Abgesetzte Formeln, mehrzeilig und als Matrix.
section: Formatierung
tags:
  - formatierung
  - mathematik
translationKey: formatierung/mathematik/bloecke
cover: "[[assets/covers/cover-mathematik.svg]]"
---

Zwei Dollarzeichen setzen die Formel als eigenen Block:

```md
$$
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
$$
```

$$
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
$$

## Mehrzeilig ausgerichtet

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

Das `&` markiert die Stelle, an der die Zeilen bündig stehen.

## Matrizen

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

## Zu breite Formeln

$$
f(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + a_5 x^5 + a_6 x^6 + a_7 x^7 + a_8 x^8 + a_9 x^9
$$

Auch hier gilt: Was zu breit ist, scrollt in sich selbst statt die Spalte zu sprengen.
