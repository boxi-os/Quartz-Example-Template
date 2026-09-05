---
title: Canvas
description: Eine unendliche Fläche mit Karten und Verbindungen.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - canvas
translationKey: obsidian-formate/canvas/index
---

Ein Canvas ist eine freie Fläche: Man legt Karten darauf, verbindet sie mit Pfeilen und ordnet sie
räumlich statt in einer Reihenfolge. Für Zusammenhänge, die keine Gliederung sind.

Das Beispiel in diesem Vault: [[obsidian-formate/canvas/Aufbau der Vorlage.canvas|Aufbau der Vorlage]] —
die vier Bereiche dieser Website und wie sie zusammenhängen.

Wie das Format aufgebaut ist: [[obsidian-formate/canvas/wie-es-funktioniert|Wie es funktioniert]].

## In dieser Vorlage

Eine Canvas-Seite braucht die **volle Breite** — eine Fläche in der schmalen Textspalte zeigt
nichts. Das Plugin bringt dafür zwar ein eigenes Seitenraster mit, diese Vorlage überschreibt es
aber: In der Konfiguration steht für den Seitentyp `canvas` das mitgelieferte Quartz-Raster
`full-width`. Gemessen an der gebauten Seite ist das Ergebnis Kopfbereich, Fläche und Fußzeile —
keine Seitenleisten, keine Brotkrumen.

> [!bug] Links in einem Dateiknoten führen ins Leere
> Ein Dateiknoten zeigt eine Notiz mit ihrem ganzen Inhalt — und die Links darin bekommen den
> Ordner der eingebetteten Notiz **zweimal** vorangestellt. Aus dem Verweis auf
> `gestaltung/grundlagen/frames` in der Bases-Übersicht wird auf dieser Seite
> `../../obsidian-formate/bases/../../../gestaltung/grundlagen/frames` — ein Pfad, der aus der
> Website herausführt. Gemessen: **sieben je Sprache**, alle in demselben Dateiknoten, und die Zahl
> wächst mit jedem Link, der in einer eingebetteten Notiz dazukommt.
>
> Das ist ein Fehler im Plugin `canvas-page`, nicht in dieser Vorlage — die Links stimmen auf ihren
> eigenen Seiten. Wer sich darauf verlassen will, klickt den Knotentitel an und liest die Notiz
> dort.

> [!note] Zoomen und Verschieben
> Auf der gebauten Seite lässt sich das Canvas mit dem Mausrad zoomen und mit gedrückter Maustaste
> verschieben — es ist keine Momentaufnahme, sondern die Fläche selbst.
