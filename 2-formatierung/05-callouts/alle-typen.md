---
title: Alle Callout-Typen
description: Dreizehn Typen mit ihren Zweitnamen — und warum ihre Farben hier neu gesetzt sind.
section: Formatierung
tags:
  - formatierung
  - callouts
translationKey: formatierung/callouts/alle-typen
cover: "[[assets/covers/cover-callouts.svg]]"
---

> [!note] note
> Der Standardtyp.

> [!abstract] abstract
> Zweitnamen: `summary`, `tldr`.

> [!info] info
> Sachliche Ergänzung.

> [!todo] todo
> Was noch zu tun ist.

> [!tip] tip
> Zweitnamen: `hint`, `important`.

> [!success] success
> Zweitnamen: `check`, `done`.

> [!question] question
> Zweitnamen: `help`, `faq`.

> [!warning] warning
> Zweitnamen: `caution`, `attention`.

> [!failure] failure
> Zweitnamen: `fail`, `missing`.

> [!danger] danger
> Zweitname: `error`.

> [!bug] bug
> Ein Fehler im Programm.

> [!example] example
> Ein Beispiel.

> [!quote] quote
> Zweitname: `cite`. Nimmt die Akzentfarbe der Seite statt einer eigenen.

## Was diese Vorlage anders macht

**Von Haus aus** setzt Quartz für diese dreizehn Typen zwölf Farben und lässt `note` die
Grundfarbe behalten. Gemessen gegen den hellen Seitengrund dieser Vorlage scheitern **elf von
dreizehn** an der WCAG-Schwelle von 4,5:1 — `note` erreicht 3,23:1, `question` nur 2,14:1. Durch
kommen nur `example` und `quote`. Im dunklen Modus dreht sich das Bild fast um: Dort scheitern vier,
und `example` ist eines davon (2,81:1). Das Rot von `danger`, `failure` und `bug` scheitert in
**beiden** Modi, bei 4,20 und 4,16:1.

**In dieser Vorlage** sind alle dreizehn neu gesetzt, je Modus einmal, und werden bei jedem Lauf
gemessen: gegen den Seitengrund *und* gegen die eigene getönte Fläche des Callouts. Der Farbton
bleibt erhalten — Blau bleibt Blau —, damit der Typ weiterhin an der Farbe erkennbar ist.

Die Zahlen dazu stehen unter [[6-anpassen/02-farben-und-kontrast|Farben und Kontrast]].
