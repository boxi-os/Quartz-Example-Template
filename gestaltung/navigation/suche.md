---
title: Suche
description: Das Feld in der Leiste und die Überlagerung dahinter.
section: Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/suche
---

## Von Haus aus

Ein Knopf mit Lupe, der eine Überlagerung öffnet. Der Rand kommt aus `lightgray`.

## In dieser Vorlage

- Der Rand kommt aus **`gray`**, nicht aus `lightgray`. Das ist die Umsetzung der Kontrastregel:
  `lightgray` misst 1,34:1 gegen den Grund und darf deshalb nichts umranden, das man bedient.
- Der Knopf steht **im Kopfbereich**, ganz rechts, zusammen mit den drei anderen Bedienelementen.
  Er ist 44 px hoch wie seine Nachbarn. Am Telefon wird er ein Quadrat ohne Beschriftung.
- Die **Überlagerung** trägt einen echten Schatten. Den bekommt in dieser Vorlage nur, was
  wirklich über der Seite schwebt statt in ihr zu liegen: diese Überlagerung, die Linkvorschau,
  das Sprachmenü, die Schublade am Telefon und der große Graph. Fünf Stellen, und die Regel zählt,
  nicht die Zahl.
- Das **Eingabefeld** bekommt keinen Fokusring, sondern eine kräftigere Unterkante — ein Ring
  innerhalb eines abgerundeten Kastens sieht aus wie ein Fehler.
- **Ergebnisse**: Der Tastatur-Cursor und der Zeiger-Hover sehen gleich aus. Die Pfeiltasten
  bewegen sich durch die Liste, und die hervorgehobene Zeile ist das einzige Signal, wo man steht.
- Der **Treffer im Text** wird mit derselben Farbe markiert wie `==Hervorhebung==` im Fließtext.
  „Das hast du gesucht" heißt auf der ganzen Seite dasselbe.

Bei `prefers-reduced-transparency` wird die durchscheinende Fläche durch eine deckende ersetzt.

> [!bug] Das Feld erreicht seine Breite nie
> `nav-toolbar.scss` gibt ihm `flex: 0 1 15rem` — 240 px als Ausgangsbreite, schrumpfen erlaubt.
> Gemessen sind es **110 px**, und zwar bei 1728, 1440, 1100 und 900 px Fensterbreite gleichermaßen,
> obwohl die Werkzeugleiste dort nur 322 von 1400 px belegt. Der Grund steht eine Ebene tiefer:
> Quartz legt um jede Komponente einen eigenen `div` ohne Klasse, und *der* ist `flex: 0 1 auto` und
> schrumpft auf seinen Inhalt. Die 15 rem stehen am falschen Element. Der Knopf liest sich damit als
> Knopf statt als Feld — genau das, was die Breite verhindern sollte.

> [!note] Der Index umfasst beide Sprachen
> Es gibt einen Suchindex für die ganze Website, eine englische Seite kann also in einem deutschen
> Suchergebnis auftauchen. Trennen ließe sich das nur mit einem Build je Sprache — siehe
> [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].
