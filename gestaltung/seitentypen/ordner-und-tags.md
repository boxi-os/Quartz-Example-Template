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

Beide Seitentypen nutzen den Frame **`index`**, der geometrisch derselbe ist wie `editorial`. Ein
Inhaltsverzeichnis entsteht hier trotzdem nicht — eine Liste von Links hat keine Überschriften.
Rückverweise und Graphansicht schon, und die stehen rechts wie überall sonst.

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

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 11 Variablen liest `page-folder.scss` und `page-tag.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 7 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
