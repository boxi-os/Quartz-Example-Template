---
title: Ausrichtung
description: Doppelpunkte in der Trennzeile steuern die Spaltenausrichtung.
section: Formatierung
tags:
  - formatierung
  - tabellen
---

```md
| Links | Zentriert | Rechts |
| :---- | :-------: | -----: |
| a     |     b     |      c |
| aaaa  |    bbbb   |   cccc |
```

| Links | Zentriert | Rechts |
| :---- | :-------: | -----: |
| a     |     b     |      c |
| aaaa  |    bbbb   |   cccc |

| Doppelpunkt | Wirkung |
| --- | --- |
| `:---` | linksbündig (Standard) |
| `:---:` | zentriert |
| `---:` | rechtsbündig |

> [!tip] Zahlen gehören nach rechts
> Ziffern lassen sich nur vergleichen, wenn die Einer untereinander stehen. Für Spalten mit Zahlen
> also `---:` — und in dieser Vorlage kommt in Listen zusätzlich `tabular-nums` dazu, damit die
> Ziffern gleich breit sind.
