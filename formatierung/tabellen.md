---
title: Tabellen
description: Ausrichtung, Formatierung in Zellen und was bei zu breiten Tabellen passiert.
section: Formatierung
tags:
  - referenz
  - formatierung
---

## Einfach

```md
| Spalte A | Spalte B |
| -------- | -------- |
| Wert     | Wert     |
| Wert     | Wert     |
```

| Spalte A | Spalte B |
| -------- | -------- |
| Wert     | Wert     |
| Wert     | Wert     |

## Ausrichtung

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

## Formatierung in Zellen

```md
| Element | Beispiel |
| ------- | -------- |
| Betonung | **fett**, *kursiv* |
| Code | `const x = 1` |
| Link | [[handbuch/index\|Handbuch]] |
```

| Element | Beispiel |
| ------- | -------- |
| Betonung | **fett**, *kursiv* |
| Code | `const x = 1` |
| Link | [[handbuch/index\|Handbuch]] |

Ein senkrechter Strich in einer Zelle muss mit `\|` geschützt werden — auch in einem Wikilink.

## Breite Tabelle

Eine Tabelle, die breiter ist als die Spalte, scrollt in sich selbst. Sie schiebt nie das Layout
zur Seite — das ist der häufigste Weg, ein Raster kaputtzumachen.

| Kennung | Bezeichnung | Bereich | Standard | Beschreibung |
| ------- | ----------- | ------- | -------- | ------------ |
| `--tpl-space-md` | Abstand mittel | Raum | 1rem | Der Grundabstand zwischen Blöcken |
| `--tpl-measure` | Lesemaß | Typografie | 68ch | Zeilenlänge des Fließtexts |
| `--tpl-radius-md` | Radius mittel | Form | 8px | Ecken von Karten und Codeblöcken |
| `--tpl-focus-color` | Fokusfarbe | Zustand | var(--secondary) | Farbe des Fokusrings |
| `--tpl-indent` | Einrückung | Struktur | 0.85rem | Eine Ebene in Explorer und Inhaltsverzeichnis |
