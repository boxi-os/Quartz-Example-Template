---
title: 1.4 So ist eine Seite aufgebaut
description: Überschriften bis zur sechsten Ebene, damit das Inhaltsverzeichnis vollständig ist.
section: Einstieg
date: 2026-08-14
lastmod: 2026-09-02
tags:
  - einstieg
  - typografie
translationKey: einstieg/so-ist-eine-seite-aufgebaut
---

Diese Seite ist absichtlich lang und tief gegliedert. Sie beantwortet zwei Fragen, die eine kurze
Seite nicht beantworten kann: Wie sieht das Inhaltsverzeichnis aus, wenn es alle sechs Ebenen
enthält? Und wie verhält sich die Seitenleiste, wenn sie länger wird als das Fenster?

## Wie breit der Text wird

Die Breite entscheidet das Seitenraster. Der Frame `editorial`, den Inhaltsseiten benutzen, teilt
die Seite in zwölf gleiche Spalten und gibt dem Text sechs davon — links drei für die Navigation,
rechts drei für Inhaltsverzeichnis und Rückverweise. Die Seite selbst ist auf 1440 Pixel begrenzt,
der Text landet damit bei 684 Pixeln, also rund 71 Zeichen.

### Warum nicht zusätzlich am Absatz

Eine zweite Begrenzung am einzelnen Absatz wäre eine zweite Stelle, an der über dieselbe Frage
entschieden wird. Zwei solche Stellen müssen von Hand in Übereinstimmung gehalten werden — und
irgendwann sind sie es nicht mehr.

#### Was das für breite Bildschirme heißt

Bleibt Platz übrig, geht er an die Spalten daneben, nicht an die Zeilenlänge.

##### Ab welcher Breite umgebrochen wird

Diese Vorlage bricht bei 1100 Pixeln auf zwei Spalten und bei 720 auf eine. Das sind die
projekteigenen Schwellen, nicht die von Quartz — sie liegen etwas enger, weil die linke Spalte hier
schmaler ist.

###### Die tiefste Ebene

Ab hier gibt das Inhaltsverzeichnis das Einrücken auf und markiert mit Punkten. Diese Überschrift
ist der Grund, warum diese Seite existiert.

## Struktur und Rhythmus

Der Abstand einer Überschrift liegt über ihr. Dadurch entsteht die Gruppe: Überschrift und der Text
darunter gehören sichtbar zusammen, und der Abstand nach oben trennt sie vom Vorherigen.

### Ebenen und Gewicht

Die ersten vier Ebenen unterscheiden sich in der Größe. Die letzten beiden nicht mehr — sie
wechseln zu Versalien und Sperrung, weil ein Unterschied von einem oder zwei Pixeln keine
Information ist, die jemand zuverlässig erkennt.

#### Eine Zwischenebene

Text auf Ebene vier.

##### Und noch eine

Text auf Ebene fünf.

###### Und die letzte

Text auf Ebene sechs.

## Elemente im Fließtext

Ein Absatz mit **Betonung**, *Kursivem*, `Code` und einem [[7-nachschlagen/index|internen Verweis]].
Dazu eine ==Hervorhebung== und eine Fußnote[^lang].

[^lang]: Fußnoten sammeln sich am Ende der Seite, abgetrennt durch eine Linie.

> [!tip] Ein Callout mittendrin
> Callouts unterbrechen den Lesefluss absichtlich. Deshalb haben sie einen Farbbalken links und
> keine volle Umrandung — sie sollen auffallen, ohne die Spalte zu zerschneiden.

### Eine Liste

1. Der erste Punkt
2. Der zweite Punkt
   - mit einer Anmerkung
   - und noch einer
3. Der dritte Punkt

### Eine Tabelle

| Breite | Raster | Blöcke nebeneinander |
| ------ | ------ | -------------------- |
| über 1100 px | 12 Spalten | drei: 3 / 6 / 3 |
| 801 bis 1100 px | 12 Spalten | zwei: 3 / 9, Apparat unter dem Text |
| bis 800 px | 1 Spalte | einer |

### Ein Codeblock

```ts
// Lange Zeilen scrollen, statt umzubrechen.
export function measure(text: string): number {
  return text.length
}
```

## Zum Schluss

Wer bis hierher gescrollt hat, sieht rechts im Inhaltsverzeichnis den aktuellen Abschnitt
hervorgehoben — Farbe, Schriftschnitt und ein Balken an der Linie. Drei Signale, weil eines davon
für einen Teil der Leser ausfällt.
