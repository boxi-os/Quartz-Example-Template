---
title: Graph
description: Die Umgebung einer Notiz als Netz.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
---

## Von Haus aus

Ein Kasten mit der lokalen Umgebung, dazu ein Symbol zum Öffnen der Gesamtansicht.

## In dieser Vorlage

Der Graph zeichnet sich selbst und holt seine Farben zur Laufzeit aus den CSS-Variablen. Die
Vorlage gestaltet deshalb **nur den Kasten darum**, nicht die Zeichnung:

- ein **quadratisches Feld** (`aspect-ratio: 1`) — der lokale Graph ist rund, ein breiter Kasten
  verschenkt die Seitenleiste
- Rahmen und getönte Fläche wie bei den anderen Panels
- das **Symbol für die Gesamtansicht** ist 44 px groß und sitzt rechts in der Überschriftenzeile
- die **Gesamtansicht** bekommt denselben Schatten wie die Suche — beide schweben wirklich

Ein halb umgefärbter Graph wäre schlechter als ein fremdfarbiger: Die Zeichnung löst ihre Farben
selbst auf, und ein Stylesheet, das dagegen arbeitet, trifft immer nur die Hälfte.

**Auf schmalen Bildschirmen wird er ausgeblendet** (`display: desktop-only`) — ein Netz aus Punkten
in einer 390 px breiten Spalte zeigt nichts.
