---
title: Inhalte in Zellen
description: Was in einer Zelle stehen darf und was geschützt werden muss.
section: Formatierung
tags:
  - formatierung
  - tabellen
translationKey: formatierung/tabellen/inhalte
---

```md
| Element | Beispiel |
| ------- | -------- |
| Betonung | **fett**, *kursiv* |
| Code | `const x = 1` |
| Link | [[formatierung/index\|Formatierung]] |
| Zeilenumbruch | erste Zeile<br>zweite Zeile |
```

| Element | Beispiel |
| ------- | -------- |
| Betonung | **fett**, *kursiv* |
| Code | `const x = 1` |
| Link | [[formatierung/index\|Formatierung]] |
| Zeilenumbruch | erste Zeile<br>zweite Zeile |

## Der senkrechte Strich

Ein `|` in einer Zelle beendet die Spalte. Er muss mit `\|` geschützt werden — **auch innerhalb
eines Wikilinks**, wo der Strich sonst Ziel und Text trennt:

```md
| [[formatierung/index\|Formatierung]] |
```

Das ist die häufigste Stolperstelle bei Tabellen in Obsidian.
