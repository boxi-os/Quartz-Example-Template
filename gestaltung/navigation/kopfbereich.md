---
title: Kopfbereich
description: Wortmarke, Seitentitel und die drei Bedienelemente in einer Zeile.
section: Gestaltung
tags:
  - gestaltung
  - navigation
---

Oben steht die Wortmarke, daneben der Seitentitel, am rechten Ende Suche, Farbschema-Umschalter und
Lesemodus. Darunter eine Trennlinie.

## Von Haus aus

Der Kopfbereich enthält nur den Seitentitel. Eine Marke gibt es nicht — dafür müsste man eine
eigene Komponente bauen. Suche und die beiden Umschalter sitzen in der linken Seitenleiste.

## In dieser Vorlage

Die Marke kommt aus einer **Layout-Box-Instanz** mit Inline-SVG, einmal hell und einmal dunkel. Sie
ist zugleich der Link zur Startseite.

Zwei Feinheiten:

- Der **Text der Marke ist visuell versteckt**, aber im Dokument vorhanden. Der Link enthält sonst
  nur ein SVG und hätte keinen zugänglichen Namen. `display: none` wäre hier falsch gewesen — genau
  dieser Fehler steckte in der ersten Fassung.
- Die drei Bedienelemente stehen **im Kopf, nicht in der Leiste**. Dort sucht man sie, und es ist
  der einzige Bereich, den jeder Frame hat — auf der Fehlerseite gab es vorher weder Suche noch
  Farbschema-Umschalter, weil sie keine Seitenleisten hat.
- Am Telefon wird der Kopf zur **App-Leiste**: Er bleibt beim Scrollen oben stehen, läuft über die
  volle Breite und nimmt den Schubladen-Knopf des Explorers mit auf. Die Suche gibt dort ihr Wort
  auf und wird ein Quadrat wie die beiden anderen; ihre 44 px behält sie.

## Ein Fund beim Bauen

Das Plugin setzt `width: 100%` auf jede Layout-Box. In einer Flex-Zeile machte das die Marke
1376 px breit und schob den Titel in die nächste Zeile. `flex` hebt eine gesetzte Breite nicht auf —
sie musste ausdrücklich zurückgenommen werden.
