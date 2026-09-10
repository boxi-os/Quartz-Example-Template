---
title: 1.4 – So ist eine Seite aufgebaut
description: Die Teile einer Seite mit ihren Namen — und eine absichtlich lange, tief gegliederte Seite, an der man sie alle sieht.
section: 1 – Einstieg
tags:
  - einstieg
  - typografie
date: 2026-08-14
lastmod: 2026-09-06
translationKey: einstieg/so-ist-eine-seite-aufgebaut
---

Diese Seite hat zwei Aufgaben. Sie nennt die Teile, aus denen jede Seite dieser Website besteht —
damit die Kapitel 5 und 6 sie beim Namen nennen können. Und sie ist absichtlich lang und tief
gegliedert, damit man an ihr sieht, was eine kurze Seite nicht zeigen kann: ein Inhaltsverzeichnis
mit allen sechs Ebenen und eine Seitenleiste, die länger wird als das Fenster.

## Die Teile einer Seite

Am Desktop hat eine Seite drei Spalten, auf dem Tablet zwei, am Telefon eine. Die Namen in der
Tabelle sind die, die auch QuartzControl im Layout-Editor benutzt.

| Teil | Wo | Was darin steht |
| --- | --- | --- |
| **Kopfbereich** (header) | oben, über alle Spalten | die Wortmarke, der Websitename, das Kapitel, die Suche, der Schalter für hell und dunkel, der Lesemodus, der Sprachumschalter |
| **Linke Spalte** (left) | links | der [[7-nachschlagen/01-glossar#Explorer\|Explorer]] — der Ordnerbaum aller Seiten — und die Box „Über dieses Handbuch“ |
| **Über dem Inhalt** (beforeBody) | über dem Text | die [[7-nachschlagen/01-glossar#Brotkrumen\|Brotkrumen]] (der Pfad von der Startseite hierher), die Tags, der Titel, Datum und Lesezeit |
| **Inhalt** (body) | Mitte | die Notiz selbst |
| **Der freie Bereich** (custom-8) | direkt unter dem Text | zwei Kästen nebeneinander: die zuletzt geänderten Seiten und die [[7-nachschlagen/01-glossar#Rückverweise\|Rückverweise]] (welche Seiten hierher verlinken) |
| **Nach dem Inhalt** (afterBody) | darunter | die Box „Weiterlesen“, die Eigenschaften-Tabelle, am Telefon der Hinweis auf die eingeklappte Navigation |
| **Rechte Spalte** (right) | rechts | das Inhaltsverzeichnis und der [[7-nachschlagen/01-glossar#Graph\|Graph]] |
| **Fußzeile** (footer) | unten | die Impressumszeile |

Sieben davon sind Quartz' eigene Orte. **Der freie Bereich ist es nicht** — er ist ein achter, den
diese Vorlage im Seitenraster dazugebaut hat, weil zwei Kästen nebeneinander sonst nicht
auszudrücken sind: Quartz kennt unter dem Text genau eine Stelle, und alles, was dort steht, steht
untereinander.

Welcher Teil wo liegt, entscheidet das Seitenraster, in Quartz **[[7-nachschlagen/01-glossar#Frame|Frame]]** genannt — dazu gleich
mehr. Was in jedem Teil steht, entscheidet das Layout, in QuartzControl unter *Layout*. Wie jeder
Teil aussieht und warum, ist Kapitel [[5-gestaltung/index|5 – Die Gestaltung]].

Eine Zeichnung davon:
[[3-obsidian-formate/03-excalidraw/Aufbau des editorial-Frames.excalidraw|Aufbau des editorial-Frames]].

## Wie breit der Text wird

Die Breite entscheidet das Seitenraster. Der Frame `editorial`, den Inhaltsseiten benutzen, teilt
die Seite in zwölf Spalten und gibt dem Text die mittleren sechs — links drei für die Navigation,
rechts drei für Inhaltsverzeichnis und Graph. Die Seite selbst ist auf 1440 Pixel begrenzt, der Text
landet damit bei 672 Pixeln, also rund 70 Zeichen.

### Warum nicht zusätzlich am Absatz

Eine zweite Begrenzung am einzelnen Absatz wäre eine zweite Stelle, an der über dieselbe Frage
entschieden wird. Zwei solche Stellen müssen von Hand in Übereinstimmung gehalten werden — und
irgendwann sind sie es nicht mehr.

#### Was das für breite Bildschirme heißt

Bleibt Platz übrig, geht er an die Spalten daneben, nicht an die Zeilenlänge.

##### Ab welcher Breite umgebrochen wird

Diese Vorlage bricht bei 1200 Pixeln auf zwei Spalten und bei 900 auf eine. Das sind die
projekteigenen Schwellen, nicht die von Quartz. Bis zum 09.09.2026 stand die untere bei 800, und
zwar nicht aus Gestaltungsgründen: Das Explorer-Plugin schaltet in seinem eigenen Stylesheet bei
genau `max-width: 800px` auf die Schublade um. Seit die Vorlage die Regeln der Plugins auf ihre
eigenen Schwellen umschreibt, sind die zwei Zahlen wieder eine Entscheidung.

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
> [[7-nachschlagen/01-glossar#Callout|Callouts]] unterbrechen den Lesefluss absichtlich. Deshalb haben sie einen Farbbalken links und
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
| ab 1201 px | 12 Spalten | drei: 3 / 6 / 3 |
| 901 bis 1200 px | 12 Spalten | zwei: 3 / 9, Apparat unter dem Text |
| bis 900 px | 1 Spalte | einer |

### Ein Codeblock

```ts
// Lange Zeilen scrollen, statt umzubrechen.
export function measure(text: string): number {
  return text.length
}
```

## Zum Schluss

Wer bis hierher gescrollt hat, sieht rechts im Inhaltsverzeichnis zweierlei: eine Linie, die bis
zur eben gelesenen Stelle im Akzent steht und darunter grau bleibt — eine Fortschrittsanzeige, aus
den Einträgen selbst gebaut —, und den aktuellen Abschnitt im Akzent gesetzt. Wo die Linie endet,
steht man; welche Überschrift das ist, sagt das eine farbige Wort daneben.
