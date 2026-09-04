---
title: Frames
description: Drei eigene Seitenraster statt der drei mitgelieferten.
section: Gestaltung
tags:
  - gestaltung
  - grundlagen
translationKey: gestaltung/grundlagen/frames
---

Ein Frame ist das Raster einer Seite: welche Bereiche es gibt, wo sie liegen, wie breit sie sind.

Alle drei Frames dieser Vorlage teilen sich am Desktop **ein Raster: zwölf gleiche Spalten,
2 rem Rinne, 20 px Rand, gedeckelt auf 1440 px.** Das ergibt 1400 px nutzbare Breite; elf Rinnen zu
je 32 px nehmen 352 davon, eine Spalte misst also 87,33 px. Die drei Blöcke rasten darauf ein:

| Block | Spalten | Breite |
| --- | --- | --- |
| Navigation | 1–3 | 326 px |
| Text | 4–9 | 684 px |
| Apparat | 10–12 | 326 px |

Die Rinne ist am 05.09.2026 von 20 px auf 2 rem gewachsen — die Seite sollte lockerer wirken. Der
Rand blieb bei 20 px: Er ist der Abstand zum Fensterrand, nicht der zwischen zwei Dingen.

> [!warning] Am Telefon bleibt die Rinne bei 20 px
> Ein Zwölf-Spalten-Raster hat elf Rinnen, ganz gleich was darin steht, und die setzen seine
> Mindestbreite: 11 × 32 + 40 Rand sind 392 px und damit mehr als ein 390-px-Bildschirm hat.
> Gemessen, bevor diese Ausnahme existierte: **jede** Seite scrollte seitwärts um 18 px. Sichtbar
> ist die Spaltenrinne dort ohnehin nicht, weil mobil jeder Bereich über alle zwölf Spalten geht;
> die Zeilenrinne behält die vollen 2 rem.

| Frame | Genutzt von | Besonderheit |
| --- | --- | --- |
| `editorial` | Inhaltsseiten | alle sieben Bereiche belegt |
| `index` | Ordner, Tags, Bases | rechte Spalte bleibt frei, aber reserviert |
| `focus` | Fehlerseite | beide Randspalten leer, kein Apparat |

Dass auch Ordner-, Tag-, Bases- und Fehlerseiten die rechte Spalte behalten, ist Absicht: Der Text
beginnt dann auf **jeder** Seite an derselben Stelle, und der Sprung von einem Artikel zu seinem
Ordner verschiebt die Zeile nicht mehr.

Jeder Frame ist für **drei Breiten** ausgelegt. Die Schwellen liegen bei 1100 und 800 px. Die 800
sind nicht frei gewählt: Das Explorer-Plugin schaltet in seinem eigenen Stylesheet bei genau
`max-width: 800px` auf die Schublade um. Vorher stand hier 720, und zwischen 721 und 800 px
widersprachen sich die beiden — der Explorer war schon ein Hamburger, während der Frame die Seite
noch als Tablet auslegte.

Am Tablet fällt die rechte **Spalte** weg; ihr Inhalt rutscht unter den Text, statt zu verschwinden.
Mobil steht alles untereinander.

## Was Quartz mitbringt

**Von Haus aus** gibt es `default` (drei Spalten), `full-width` und `minimal`. Sie sind fest
eingebaut und lassen sich nicht in der Geometrie ändern — nur auswählen.

**In dieser Vorlage** sind die drei Frames selbst gebaut: Spaltenzahl, Zeilen, Abstände,
Maximalbreite und Ausrichtung sind je Breite gesetzt. Ein Bereich, der auf einer Breite wirklich
nichts zu suchen hat, wird ausgeblendet — eine Spalte, die nur gerade leer ist, bleibt dagegen
stehen, damit die Textspalte nicht wandert.

## Zwei Eigenheiten des Editors

- Ein Wert darf **kein Komma** enthalten — also kein `minmax(0, 1fr)`.
- Längen stehen als Zahl, nicht als Token: Ein Frame muss auch funktionieren, wenn jemand nur den
  Baustein *Frames* importiert und die Variablen fehlen.

Wie eine Zeichnung davon aussieht: [[obsidian-formate/excalidraw/index|Excalidraw]].
