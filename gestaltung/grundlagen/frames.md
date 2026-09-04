---
title: Frames
description: Drei eigene Seitenraster statt der drei mitgelieferten.
section: Gestaltung
tags:
  - gestaltung
  - grundlagen
---

Ein Frame ist das Raster einer Seite: welche Bereiche es gibt, wo sie liegen, wie breit sie sind.

| Frame | Genutzt von | Aufbau am Desktop |
| --- | --- | --- |
| `editorial` | Inhaltsseiten | drei Spalten: Navigation · Text · Apparat |
| `index` | Ordner, Tags, Bases | zwei Spalten, rechte Leiste ausgeblendet |
| `focus` | Fehlerseite | eine Spalte, 680 px, zentriert |

Jeder ist für **drei Breiten** ausgelegt. Die Schwellen dieser Vorlage liegen bei 1100 und 720 px —
etwas enger als Quartz' eigene (1200 / 800), weil die linke Spalte hier schmaler ist.

## Was Quartz mitbringt

**Von Haus aus** gibt es `default` (drei Spalten), `full-width` und `minimal`. Sie sind fest
eingebaut und lassen sich nicht in der Geometrie ändern — nur auswählen.

**In dieser Vorlage** sind die drei Frames selbst gebaut: Spaltenbreiten, Zeilen, Abstände,
Maximalbreite und Ausrichtung sind je Breite gesetzt. Ein Bereich, der auf einer Breite nichts zu
suchen hat, wird ausgeblendet statt leer gelassen.

## Zwei Eigenheiten des Editors

- Ein Wert darf **kein Komma** enthalten — also kein `minmax(0, 1fr)`.
- Längen stehen als Zahl, nicht als Token: Ein Frame muss auch funktionieren, wenn jemand nur den
  Baustein *Frames* importiert und die Variablen fehlen.

Wie eine Zeichnung davon aussieht: [[obsidian-formate/excalidraw/index|Excalidraw]].
