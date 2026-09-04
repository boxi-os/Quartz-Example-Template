---
title: Kopfbereich
description: Wortmarke und Seitentitel nebeneinander.
section: Gestaltung
tags:
  - gestaltung
  - navigation
---

Oben steht die Wortmarke, daneben der Seitentitel, darunter eine Trennlinie.

## Von Haus aus

Der Kopfbereich enthält nur den Seitentitel. Eine Marke gibt es nicht — dafür müsste man eine
eigene Komponente bauen.

## In dieser Vorlage

Die Marke kommt aus einer **Layout-Box-Instanz** mit Inline-SVG, einmal hell und einmal dunkel. Sie
ist zugleich der Link zur Startseite.

Zwei Feinheiten:

- Der **Text der Marke ist visuell versteckt**, aber im Dokument vorhanden. Der Link enthält sonst
  nur ein SVG und hätte keinen zugänglichen Namen. `display: none` wäre hier falsch gewesen — genau
  dieser Fehler steckte in der ersten Fassung.
- Der Bereich **bricht um**. Auf einem schmalen Bildschirm rutscht der Titel unter die Marke, statt
  gequetscht zu werden.

## Ein Fund beim Bauen

Das Plugin setzt `width: 100%` auf jede Layout-Box. In einer Flex-Zeile machte das die Marke
1376 px breit und schob den Titel in die nächste Zeile. `flex` hebt eine gesetzte Breite nicht auf —
sie musste ausdrücklich zurückgenommen werden.
