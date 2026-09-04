---
title: Code im Text
description: Ein Befehl mitten im Satz.
section: Formatierung
tags:
  - formatierung
  - code
translationKey: formatierung/code/inline
---

```md
Ein Befehl wie `npm run build` mitten im Satz.
```

Ein Befehl wie `npm run build` mitten im Satz.

## Backticks im Code

Wer selbst einen Backtick zeigen will, umschließt mit zweien:

```md
Ein `` ` `` mitten im Text.
```

Ein `` ` `` mitten im Text.

## In dieser Vorlage

**Von Haus aus** bekommt Inline-Code einen deutlichen Kasten mit Rahmen.

**In dieser Vorlage** ist es eine Tönung ohne Rahmen — genug, um ihn vom Fließtext zu trennen, zu
wenig, um den Satz zu unterbrechen. Die Schrift ist etwas kleiner gesetzt (0.9em), weil JetBrains
Mono neben Inter sonst zu groß wirkt. Lange Bezeichner dürfen umbrechen (`overflow-wrap: anywhere`)
statt die Spalte zu sprengen.
