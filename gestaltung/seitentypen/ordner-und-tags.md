---
title: Ordner- und Tag-Seiten
description: Die Listen, die Quartz automatisch erzeugt.
section: Gestaltung
tags:
  - gestaltung
  - seitentypen
---

Für jeden Ordner und jeden Tag entsteht automatisch eine Seite mit einer Liste.

## Von Haus aus

Eine Aufzählung mit Datum, Titel, Beschreibung und Tags, untereinander.

## In dieser Vorlage

Ein **dreispaltiges Raster**: Datum in fester Breite links, Titel in der Mitte, Tags rechts. Die
feste Datumsspalte sorgt dafür, dass die Titel eine Kante bilden — und die Ziffern stehen in
Ziffernbreite untereinander.

Unter 720 px fällt das auf eine Spalte zusammen; das Datum ist der Teil, der wandert.

Beide Seitentypen nutzen den Frame **`index`**: zwei Spalten ohne rechte Leiste. Eine Liste von
Links braucht kein Inhaltsverzeichnis und keine Rückverweise.

## Zwei Funde beim Bauen

**`.desc` enthält den Titel, nicht die Beschreibung.** Wer den Namen wörtlich nimmt und die Klasse
gedämpft setzt, gräut jeden Eintragstitel auf jeder Listenseite aus.

**Dieselben Klassennamen benutzt „zuletzt geändert".** Ohne Eingrenzung auf `.page-listing` landet
das dreispaltige Raster in der 240 px schmalen Seitenleiste.

## Die Tag-Seite

Der Titel ist der Tag-Name als reiner Text. Diese Vorlage stellt ihm ein Rautenzeichen voran — als
`::before`, damit es nicht in der Vorlesereihenfolge landet.
