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
  Er ist 44 px hoch wie seine Nachbarn und 15 rem breit — breit genug, um als Feld gelesen zu
  werden, schmal genug, dass der Kopf weiter dem Seitentitel gehört. Am Telefon wird er ein Quadrat
  ohne Beschriftung.
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

> [!example] Warum die Breite in der Konfiguration steht und nicht im Stylesheet
> Sie stand einmal dort, als `flex: 0 1 15rem` an `.search` — und wirkte nicht: Gemessen waren es
> **110 px**, bei 1728, 1440, 1100 und 900 px gleichermaßen, obwohl die Werkzeugleiste dort nur 322
> von 1400 px belegte. Quartz legt um jede Komponente einer Gruppe einen eigenen `div` ohne Klasse
> und schreibt dessen Flex-Werte als **Inline-Stil** aus der Konfiguration. Das Flex-Element ist
> also der Wrapper, nicht `.search`, und ein Inline-Stil schlägt jedes Stylesheet.
>
> Die 15 rem stehen deshalb seit dem 05.09.2026 in `layout.groupOptions.basis` der Suche, zusammen
> mit `shrink: false`. Das zweite gehört dazu: Ein schrumpfbares Element steuert nur seine
> Inhaltsbreite zur Größe der Gruppe bei, die Gruppe blieb bei 322 px, während ihre Kinder 452
> wollten — und die Leiste brach auf zwei Zeilen um, der Kopf wuchs von 61 auf 101 px. Am Telefon
> nimmt `nav-toolbar.scss` die Breite wieder weg, mit `!important`, weil nur das gegen einen
> Inline-Stil ankommt.

> [!note] Der Index umfasst beide Sprachen
> Es gibt einen Suchindex für die ganze Website, eine englische Seite kann also in einem deutschen
> Suchergebnis auftauchen. Trennen ließe sich das nur mit einem Build je Sprache — siehe
> [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].
