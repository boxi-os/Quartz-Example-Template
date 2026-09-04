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
- Der Knopf steht **im Kopfbereich**, ganz rechts, zusammen mit den drei anderen Bedienelementen. Er ist
  44 px hoch und rund 15 rem breit — breit genug, um als Feld gelesen zu werden, schmal genug, dass
  der Kopf weiter dem Seitentitel gehört. Am Telefon wird er ein Quadrat ohne Beschriftung.
- Die **Überlagerung** ist eine von genau zwei Stellen dieser Vorlage mit echtem Schatten. Sie
  schwebt wirklich über der Seite, also darf sie es auch zeigen.
- Das **Eingabefeld** bekommt keinen Fokusring, sondern eine kräftigere Unterkante — ein Ring
  innerhalb eines abgerundeten Kastens sieht aus wie ein Fehler.
- **Ergebnisse**: Der Tastatur-Cursor und der Zeiger-Hover sehen gleich aus. Die Pfeiltasten
  bewegen sich durch die Liste, und die hervorgehobene Zeile ist das einzige Signal, wo man steht.
- Der **Treffer im Text** wird mit derselben Farbe markiert wie `==Hervorhebung==` im Fließtext.
  „Das hast du gesucht" heißt auf der ganzen Seite dasselbe.

Bei `prefers-reduced-transparency` wird die durchscheinende Fläche durch eine deckende ersetzt.

> [!note] Der Index umfasst beide Sprachen
> Es gibt einen Suchindex für die ganze Website, eine englische Seite kann also in einem deutschen
> Suchergebnis auftauchen. Trennen ließe sich das nur mit einem Build je Sprache — siehe
> [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].
