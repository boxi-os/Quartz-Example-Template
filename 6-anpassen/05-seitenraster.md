---
title: 6.5 Seitenraster
description: Drei eigene Seitenraster statt der drei mitgelieferten.
section: Anpassen
tags:
  - anpassen
translationKey: anpassen/seitenraster
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
| `index` | Ordner, Tags, [[7-nachschlagen/01-glossar#Base\|Bases]] | rechte Spalte ohne Inhaltsverzeichnis — dort gibt es keine Überschriften |
| `focus` | Fehlerseite | beide Randspalten leer, kein Apparat |

Dass auch Ordner-, Tag-, Bases- und Fehlerseiten die rechte Spalte behalten, ist Absicht: Der Text
beginnt dann auf **jeder** Seite an derselben Stelle, und der Sprung von einem Artikel zu seinem
Ordner verschiebt die Zeile nicht mehr.

Jeder Frame ist für **drei Breiten** ausgelegt. Die Schwellen liegen bei 1100 und 800 px. Die 800
sind nicht frei gewählt: Das Explorer-Plugin schaltet in seinem eigenen [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]] bei genau
`max-width: 800px` auf die Schublade um. Vorher stand hier 720, und zwischen 721 und 800 px
widersprachen sich die beiden — der [[7-nachschlagen/01-glossar#Explorer|Explorer]] war schon ein Hamburger, während der Frame die Seite
noch als Tablet auslegte.

Am Tablet fällt die rechte **Spalte** weg; ihr Inhalt rutscht unter den Text, statt zu verschwinden.
Mobil steht alles untereinander.

Das gilt für `editorial` und für `index` gleichermaßen. Nur `focus` blendet die Spalte wirklich
aus — dort ist sie leer, das kostet nichts.

> [!example] Was hier einmal falsch war
> `index` hat die rechte Spalte unter 1100 px lange ausgeblendet statt sie nach unten zu schieben,
> in der Annahme, sie sei auf einer Listenseite leer: Eine Liste von Links hat keine Überschriften,
> also kein Inhaltsverzeichnis. Gemessen an `/formatierung/` ist sie es nicht — [[7-nachschlagen/01-glossar#Rückverweise|Rückverweise]] und
> Graphansicht stehen dort. Auf Tablet und Telefon verschwanden damit beide von jeder Ordner-, Tag-
> und Bases-Seite. Seit dem 05.09.2026 hat `index` dieselbe Zeile für die rechte Spalte wie
> `editorial`.

## Was Quartz mitbringt

**Von Haus aus** gibt es `default` (drei Spalten), `full-width` und `minimal`. Sie sind fest
eingebaut und lassen sich nicht in der Geometrie ändern — nur auswählen.

**In dieser Vorlage** sind die drei Frames selbst gebaut: Spaltenzahl, Zeilen, Abstände,
Maximalbreite und Ausrichtung sind je Breite gesetzt. Ein Bereich, der auf einer Breite wirklich
nichts zu suchen hat, wird ausgeblendet — eine Spalte, die nur gerade leer ist, bleibt dagegen
stehen, damit die Textspalte nicht wandert.

## Eine Randspalte fest machen

Die zwölf Spalten sind `1fr` und teilen sich damit den Platz gleichmäßig — bei jeder Fensterbreite
schrumpfen alle drei Blöcke zusammen. Wer stattdessen eine feste Breite will, trägt sie im
Frame-Editor unter *Raster* im Feld **Spaltenbreiten** ein: ein Eingabefeld je Spalte, leer heißt
`1fr`, und die Werte gelten je Breakpoint für sich.

Die Rechnung dabei ist die Stelle, an der man stolpert: **Eine Randspalte ist kein Track, sondern
drei** — plus die zwei Rinnen dazwischen, die zur Fläche des Bereichs gehören. Für 320 px bekommen
die Felder 1–3 und 10–12 also je

```
calc((320px - 4rem) / 3)
```

und die Felder 4–9 bleiben leer. Gemessen an der gebauten Seite:

| Fenster | links | Text | rechts |
| ---: | ---: | ---: | ---: |
| 1728 px | 320 | 696 | 320 |
| 1440 px | 320 | 696 | 320 |
| 1300 px | 320 | 556 | 320 |
| 1200 px | 320 | 456 | 320 |
| 1101 px | 320 | 357 | 320 |

Zum Vergleich mit `1fr`: 326 / 684 / 326 bei 1440 px und 266 / 564 / 266 bei 1200 px.

> [!warning] Den Unterschied zahlt allein der Text
> Mit `1fr` verlieren alle drei Blöcke gemeinsam, mit festen Rändern nur die Textspalte. Bei
> 1101 px — knapp über dem Tablet-Umbruch — bleiben ihr 357 px, also gut 37 Zeichen je Zeile. Die
> Werte gehören deshalb auf den Desktop-Breakpoint und nicht auf Tablet oder Mobil, wo die
> Randspalte ohnehin unter den Text rückt oder ganz über die Breite geht.

Diese Vorlage macht davon **keinen** Gebrauch: Sie bleibt bei zwölf gleichen Spalten, weil die
Textbreite dann eine Folge des Rasters ist und nicht eine zweite Entscheidung daneben — siehe
[[5-gestaltung/03-im-inhalt/fliesstext|Fließtext]].

## Zwei Eigenheiten des Editors

- Ein Wert darf **kein Komma** enthalten — also kein `minmax(0, 1fr)`.
- Längen stehen als Zahl, nicht als [[7-nachschlagen/01-glossar#Token|Token]]: Ein Frame muss auch funktionieren, wenn jemand nur den
  [[7-nachschlagen/01-glossar#Baustein|Baustein]] *Frames* importiert und die Variablen fehlen.

Wie eine Zeichnung davon aussieht: [[3-obsidian-formate/03-excalidraw/index|Excalidraw]].
