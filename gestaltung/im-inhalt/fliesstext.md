---
title: Fließtext
description: Die Breite des Textes, die Überschriftenskala und die Links darin.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
translationKey: gestaltung/im-inhalt/fliesstext
---

## Die Breite des Textes

**In dieser Vorlage** entscheidet das Seitenraster, wie breit der Text wird — nicht eine Regel am
Absatz. Der Frame gibt dem Inhalt sechs von zwölf Spalten, das sind 684 px auf einer Seite, die bei
1440 px gedeckelt ist — bei 1 rem Schriftgröße rund 72 Zeichen.

**Von Haus aus** macht Quartz dasselbe, nur mit anderen Zahlen: Es begrenzt die Seite über
`.page { max-width }`.

> [!note] Was hier einmal stand
> Eine frühere Fassung begrenzte den Fließtext zusätzlich auf 68 Zeichen. Das ist ein verbreiteter
> Rat, führt aber dazu, dass zwei Stellen dieselbe Frage beantworten — die Spaltenbreite und die
> Zeilenlänge — und bei jeder Änderung am Frame nachgezogen werden muss. Die Entscheidung liegt
> jetzt nur noch im Raster.

## Überschriften

Sechs Ebenen, aber nur vier Größen. Ebene 5 und 6 wechseln zu Versalien und Sperrung, weil ein
Unterschied von einem Pixel keine Information ist. Der Abstand liegt **über** der Überschrift, nie
darunter — die Lücke sagt, was zur Überschrift gehört.

## Links

Farbe **und** Unterstreichung. Die Unterstreichung ist halbtransparent und tief gesetzt, damit sie
die Unterlängen nicht zerschneidet; beim Überfahren wird sie deckend. Externe Links tragen einen
Pfeil.

## Zitate

Balken in der Akzentfarbe, getönte Fläche, aufrechter Text. **Von Haus aus** ist der Text kursiv —
über mehrere Zeilen liest sich das schlechter, und ein Zitat ist eine andere Stimme, kein anderer
Tonfall.

## Hervorhebung

`==markiert==` nimmt `textHighlight` — im hellen Modus ein warmes Gelb, im dunklen der Akzent mit
Transparenz. Beide sind gegen die Textfarbe gemessen.
