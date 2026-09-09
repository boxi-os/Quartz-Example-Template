---
title: Inhalte in Zellen
description: Was in einer Zelle stehen darf und was geschützt werden muss.
section: 2 – Formatierung
tags:
  - formatierung
  - tabellen
translationKey: formatierung/tabellen/inhalte
cover: "[[assets/covers/cover-tabellen.svg]]"
---

```md
| Element | Beispiel |
| ------- | -------- |
| Betonung | **fett**, *kursiv* |
| Code | `const x = 1` |
| Link | [[2-formatierung/index\|Formatierung]] |
| Zeilenumbruch | erste Zeile<br>zweite Zeile |
```

| Element | Beispiel |
| ------- | -------- |
| Betonung | **fett**, *kursiv* |
| Code | `const x = 1` |
| Link | [[2-formatierung/index\|Formatierung]] |
| Zeilenumbruch | erste Zeile<br>zweite Zeile |

## Der senkrechte Strich

Ein `|` in einer Zelle beendet die Spalte. Er muss mit `\|` geschützt werden — **auch innerhalb
eines [[7-nachschlagen/01-glossar#Wikilink|Wikilinks]]**, wo der Strich sonst Ziel und Text trennt:

```md
| [[2-formatierung/index\|Formatierung]] |
```

Das ist die häufigste Stolperstelle bei Tabellen in Obsidian.
