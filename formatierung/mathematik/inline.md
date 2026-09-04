---
title: Formeln im Text
description: LaTeX mitten im Satz.
section: Formatierung
tags:
  - formatierung
  - mathematik
---

Ein Dollarzeichen umschließt die Formel:

```md
Die Masse-Energie-Äquivalenz $E = mc^2$ mitten im Satz.
```

Die Masse-Energie-Äquivalenz $E = mc^2$ mitten im Satz.

## Ein paar häufige Zeichen

```md
Brüche: $\frac{a}{b}$ · Wurzeln: $\sqrt{2}$ · Summen: $\sum_{i=1}^{n} i$
Griechisch: $\alpha, \beta, \gamma$ · Vergleiche: $a \leq b \neq c$
```

Brüche: $\frac{a}{b}$ · Wurzeln: $\sqrt{2}$ · Summen: $\sum_{i=1}^{n} i$
Griechisch: $\alpha, \beta, \gamma$ · Vergleiche: $a \leq b \neq c$

## Ein Dollarzeichen zeigen

Wer über Geld schreibt, schützt es:

```md
Das kostet \$5.
```

Das kostet \$5.

Gerendert wird mit KaTeX; eingestellt beim Plugin *LaTeX* über `renderEngine`.
