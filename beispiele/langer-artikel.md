---
title: Ein langer Artikel
description: Überschriften bis zur sechsten Ebene, damit das Inhaltsverzeichnis vollständig ist.
section: Beispiele
date: 2026-08-14
lastmod: 2026-09-02
tags:
  - beispiele
  - typografie
---

Diese Seite ist absichtlich lang und tief gegliedert. Sie beantwortet zwei Fragen, die eine kurze
Seite nicht beantworten kann: Wie sieht das Inhaltsverzeichnis aus, wenn es alle sechs Ebenen
enthält? Und wie verhält sich die Seitenleiste, wenn sie länger wird als das Fenster?

## Das Lesemaß

Der Fließtext ist auf 68 Zeichen begrenzt. Das ist die einzige wirksamste Entscheidung für
Lesbarkeit in dieser Vorlage — und diejenige, die am häufigsten verloren geht, sobald ein Layout
breiter wird. Tabellen, Codeblöcke, Diagramme und Bilder gelten nicht als Fließtext und dürfen die
ganze Spalte nehmen.

### Warum nicht die ganze Breite

Eine Zeile mit 140 Zeichen zwingt das Auge, den Zeilenanfang zu suchen. Auf einem 1728 Pixel
breiten Bildschirm wäre genau das die Folge, wenn der Text der Spalte folgte.

#### Was stattdessen mit der Breite passiert

Sie geht an die Spalten daneben: links die Navigation, rechts das Inhaltsverzeichnis und die
Rückverweise. Bleibt Platz übrig, bleibt er leer.

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

Ein Absatz mit **Betonung**, *Kursivem*, `Code` und einem [[handbuch/index|internen Verweis]].
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

| Breite | Frame | Spalten |
| ------ | ----- | ------- |
| über 1100 px | editorial | drei |
| 721 bis 1100 px | editorial | zwei |
| bis 720 px | editorial | eine |

### Ein Codeblock

```ts
// Der Block darf die ganze Spalte nehmen; das Lesemaß gilt hier nicht.
export function measure(text: string): number {
  return text.length
}
```

## Zum Schluss

Wer bis hierher gescrollt hat, sieht rechts im Inhaltsverzeichnis den aktuellen Abschnitt
hervorgehoben — Farbe, Schriftschnitt und ein Balken an der Linie. Drei Signale, weil eines davon
für einen Teil der Leser ausfällt.
