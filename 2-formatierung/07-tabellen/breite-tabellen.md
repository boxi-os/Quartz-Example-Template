---
title: Breite Tabellen
description: Was passiert, wenn eine Tabelle nicht in die Spalte passt.
section: 2 – Formatierung
tags:
  - formatierung
  - tabellen
translationKey: formatierung/tabellen/breite-tabellen
cover: "[[assets/covers/cover-tabellen.svg]]"
---

| Kennung | Bezeichnung | Bereich | Standard | Beschreibung |
| ------- | ----------- | ------- | -------- | ------------ |
| `--tpl-space-md` | Abstand mittel | Raum | 1rem | Der Grundabstand zwischen Blöcken |
| `--tpl-space-lg` | Abstand groß | Raum | 1.5rem | Zwischen Blöcken und um Figuren |
| `--tpl-radius-md` | Radius mittel | Form | 8px | Ecken von Karten und Codeblöcken |
| `--tpl-focus-color` | Fokusfarbe | Zustand | var(--secondary) | Farbe des Fokusrings |
| `--tpl-indent` | Einrückung | Struktur | 0.85rem | Eine Ebene in [[7-nachschlagen/01-glossar#Explorer\|Explorer]] und Inhaltsverzeichnis |
| `--tpl-target` | Zielgröße | Bedienung | 44px | Mindestgröße aller Bedienelemente |

Diese Tabelle ist breiter als die Textspalte. Sie **scrollt in sich selbst** — die Seite bleibt
stehen.

## Warum das nicht selbstverständlich ist

Quartz wickelt jede Tabelle in einen Container (`.table-container`). Das Scrollen gehört dorthin,
nicht auf die Tabelle. Der naheliegende erste Versuch — `display: block; overflow-x: auto` auf dem
`<table>` selbst — zerlegt das Tabellenlayout: Beim Bau dieser Vorlage rutschten dadurch die
Schlüssel und Werte der Eigenschaften-Tabelle übereinander.

Eine Tabelle, die das Layout zur Seite schiebt, ist der häufigste Weg, ein Raster kaputtzumachen.
