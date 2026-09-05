---
title: Ordner- und Tag-Seiten
description: Die Listen, die Quartz automatisch erzeugt.
section: Gestaltung
tags:
  - gestaltung
  - seitentypen
translationKey: gestaltung/seitentypen/ordner-und-tags
---

Für jeden Ordner und jeden Tag entsteht automatisch eine Seite mit einer Liste.

## Von Haus aus

Eine Aufzählung mit Datum, Titel, Beschreibung und Tags, untereinander.

## In dieser Vorlage

Ein **dreispaltiges Raster**: Datum in fester Breite links, Titel in der Mitte, Tags rechts. Die
feste Datumsspalte sorgt dafür, dass die Titel eine Kante bilden — und die Ziffern stehen in
Ziffernbreite untereinander.

Unter 720 px fällt das auf eine Spalte zusammen; das Datum ist der Teil, der wandert.

Am Desktop behalten Ordner- und Tag-Seiten die **rechte Spalte**, auch wenn nur Rückverweise darin
stehen. Damit beginnt die Liste genau dort, wo auf einer Inhaltsseite der Text beginnt — der Sprung
von einem Artikel zu seinem Ordner verschiebt die Zeile nicht mehr.

Beide Seitentypen nutzen den Frame **`index`**. Der unterscheidet sich vom `editorial` nur in
einem Punkt: Unter 1100 px blendet er die rechte Spalte aus, statt ihren Inhalt unter den Text zu
schieben. Ein Inhaltsverzeichnis gibt es hier ohnehin nicht — eine Liste von Links hat keine
Überschriften. Rückverweise und Graph aber schon, und die gehen dabei verloren; siehe den Befund
unter [[gestaltung/grundlagen/frames|Frames]].

## Zwei Funde beim Bauen

**`.desc` enthält den Titel, nicht die Beschreibung.** Wer den Namen wörtlich nimmt und die Klasse
gedämpft setzt, gräut jeden Eintragstitel auf jeder Listenseite aus.

**Dieselben Klassennamen benutzt „zuletzt geändert".** Ohne Eingrenzung auf `.page-listing` landet
das dreispaltige Raster in der schmalen Seitenleiste.

## Die Tag-Seite

Der Titel ist der Tag-Name als reiner Text. Diese Vorlage stellt ihm ein Rautenzeichen voran — als
`::before`, damit es nicht in der Vorlesereihenfolge landet.

> [!note] Zwei Sprachen, zwei Sätze Listen
> Zu jedem Ordner gibt es eine Ordnerseite, auch zu `en/`, und die englischen Seiten tragen
> englische Tags. Die Listen mischen die Sprachen deshalb nie — mit einer Ausnahme: die Ordnerseite
> von `en` selbst, die die englische Startseite ist und von Hand geschrieben wird.
