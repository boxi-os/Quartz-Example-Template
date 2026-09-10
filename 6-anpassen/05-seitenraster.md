---
title: 6.5 – Seitenraster
description: Vier eigene Seitenraster statt der drei mitgelieferten.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/seitenraster
---

Ein Frame ist das Raster einer Seite: welche Bereiche es gibt, wo sie liegen, wie breit sie sind.

Alle vier Frames dieser Vorlage teilen sich am Desktop **ein Raster: zwölf Spalten, 4 rem Rinne,
20 px Rand, gedeckelt auf 1440 px.** Das ergibt 1400 px nutzbare Breite, von denen elf Rinnen zu je
64 px 704 nehmen.

**Die zwölf Spalten sind nicht alle gleich breit.** Die äußeren drei auf jeder Seite sind fest
gerechnet, so dass eine Randspalte samt ihrer beiden Rinnen genau 300 px misst; die mittleren sechs
teilen sich, was übrig bleibt. Warum das so ist, steht weiter unten unter „Eine Randspalte fest
machen" — dort steht auch die Rechnung. Gemessen an der gebauten Seite:

| Block | Spalten | Breite bei 1440 px |
| --- | --- | --- |
| Navigation | 1–3 | 300 px |
| Text | 4–9 | 672 px |
| Apparat | 10–12 | 300 px |

Die Rinne ist am 05.09.2026 von 20 px auf 2 rem gewachsen und am 09.09.2026 auf 4 rem — die Seite
sollte lockerer wirken, und mit festen Randspalten kostet eine breitere Rinne den Text weniger als
vorher. Der Rand blieb bei 20 px: Er ist der Abstand zum Fensterrand, nicht der zwischen zwei
Dingen. Die Zeilenrinne ist auf jeder Breite 2 rem.

> [!warning] Auf Tablet und Telefon ist die Rinne schmaler
> Ein Zwölf-Spalten-Raster hat elf Rinnen, ganz gleich was darin steht, und die setzen seine
> Mindestbreite. Bei 4 rem wären das allein 704 px — mehr, als ein 390-px-Bildschirm überhaupt hat.
> Am Tablet sind es deshalb 3 rem, am Telefon 1 rem; damit liegt die Mindestbreite bei 216 px
> statt bei 744. Gemessen, bevor diese Ausnahme existierte: **jede** Seite scrollte seitwärts um
> 18 px. Sichtbar ist die Spaltenrinne am Telefon ohnehin nicht, weil dort jeder Bereich über alle
> zwölf Spalten geht.

| Frame | Genutzt von | Besonderheit |
| --- | --- | --- |
| `editorial` | Inhaltsseiten | alle sieben Bereiche belegt, dazu der freie unter dem Text |
| `index` | Ordner, Tags, [[7-nachschlagen/01-glossar#Base\|Bases]] | geometrisch derselbe wie `editorial` |
| `focus` | Fehlerseite | beide Randspalten reserviert und leer, kein Apparat |
| `drawing` | [[7-nachschlagen/01-glossar#Canvas\|Canvas]] und [[7-nachschlagen/01-glossar#Excalidraw\|Excalidraw]] | keine Randspalten, alles über die volle Breite |

Dass auch Ordner-, Tag-, Bases- und Fehlerseiten die rechte Spalte behalten, ist Absicht: Der Text
beginnt dann auf **jeder** Seite an derselben Stelle, und der Sprung von einem Artikel zu seinem
Ordner verschiebt die Zeile nicht mehr. Nur `drawing` bricht damit, und dort ist der Inhalt ein
Bild, das die Breite braucht.

Jeder Frame ist für **drei Breiten** ausgelegt. Die Schwellen liegen bei 1200 und 900 px.

> [!example] Die 900 waren einmal 800, und das war keine Entscheidung
> Das Explorer-Plugin schaltet in seinem eigenen [[7-nachschlagen/01-glossar#Stylesheet\|Stylesheet]] bei genau `max-width: 800px` auf die
> Schublade um, und dasselbe tun Suche, [[7-nachschlagen/01-glossar#Graph\|Graph]] und die Canvas-Seite. Wer woanders umbrach, bekam ein
> Band, in dem sich beide Auslegungen widersprachen — der [[7-nachschlagen/01-glossar#Explorer\|Explorer]] schon ein Hamburger, während der
> Frame die Seite noch als Tablet auslegte. Der Frame folgte deshalb dem Plugin.
>
> Seit dem 09.09.2026 geht es andersherum: Die Vorlage schreibt die Regeln von Quartz und der vier
> Plugins gegen ihre eigenen Schwellen um. Die zwei Zahlen sind damit wieder eine Entscheidung.

Am Tablet fällt die rechte **Spalte** weg; ihr Inhalt rutscht unter den Text, statt zu verschwinden.
Mobil steht alles untereinander.

**Die Reihenfolge unter dem Text ist auf beiden Breiten dieselbe.** Was die Seite über sich selbst
sagt, kommt zuerst — die zwei Kästen im freien Bereich, dann Inhaltsverzeichnis und Graph —, und
erst danach, was die Website über sie sagt: „Weiterlesen" und die Eigenschaften-Tabelle. Am Telefon
steht das Inhaltsverzeichnis abweichend davon *über* dem Text: Eine Gliederung, die man nach dem
Artikel liest, ist keine Gliederung mehr.

> [!example] Was hier einmal falsch war
> `index` hat die rechte Spalte am Tablet lange ausgeblendet statt sie nach unten zu schieben,
> in der Annahme, sie sei auf einer Listenseite leer: Eine Liste von Links hat keine Überschriften,
> also kein Inhaltsverzeichnis. Gemessen an `/formatierung/` ist sie es nicht — der Graph steht
> dort. Auf Tablet und Telefon verschwand er damit von jeder Ordner-, Tag- und Bases-Seite. Seit
> dem 09.09.2026 rechnen `editorial` und `index` mit **derselben** Funktion, statt zwei Kopien
> nebeneinander auseinanderlaufen zu lassen.

## Was Quartz mitbringt

**Von Haus aus** gibt es `default` (drei Spalten), `full-width` und `minimal`. Sie sind fest
eingebaut und lassen sich nicht in der Geometrie ändern — nur auswählen.

**In dieser Vorlage** sind die vier Frames selbst gebaut: Spaltenzahl, Spaltenbreiten, Zeilen,
Abstände, Maximalbreite und Ausrichtung sind je Breite gesetzt. Ein Bereich, der auf einer Breite wirklich
nichts zu suchen hat, wird ausgeblendet — eine Spalte, die nur gerade leer ist, bleibt dagegen
stehen, damit die Textspalte nicht wandert.

## Warum die Randspalten fest sind

Von Haus aus wären alle zwölf Spalten `1fr` und teilten sich den Platz gleichmäßig — bei jeder
Fensterbreite schrumpfen dann alle drei Blöcke zusammen. Diese Vorlage macht es anders: Die äußeren
drei Spalten auf jeder Seite tragen eine feste Breite, so dass eine Randspalte 300 px misst und dort
bleibt. Was die Seite an Breite verliert, verliert allein der Text.

Eingetragen wird das im Frame-Editor unter *Raster* im Feld **Spaltenbreiten**: ein Eingabefeld je
Spalte, leer heißt `1fr`, und die Werte gelten je Breakpoint für sich.

Die Rechnung dabei ist die Stelle, an der man stolpert: **Eine Randspalte ist kein Track, sondern
drei** — plus die zwei Rinnen dazwischen, die zur Fläche des Bereichs gehören. Für 300 px bei einer
Rinne von 4 rem bekommen die Felder 1–3 und 10–12 also je

```
calc((300px - 8rem) / 3)
```

— zwei Rinnen, deshalb `8rem` — und die Felder 4–9 bleiben leer. Am Tablet steht dieselbe Rechnung
mit `6rem`, weil die Rinne dort 3 rem ist; am Telefon steht sie gar nicht, dort sind alle zwölf
Spalten wieder gleich.

Gemessen an der gebauten Seite, jeweils gegen die Variante mit zwölf `1fr`-Spalten:

| Fenster | links | Text | rechts | mit `1fr` |
| ---: | ---: | ---: | ---: | --- |
| 1728 px | 300 | 672 | 300 | 302 / 668 / 302 |
| 1440 px | 300 | 672 | 300 | 302 / 668 / 302 |
| 1300 px | 300 | 532 | 300 | 267 / 598 / 267 |
| 1201 px | 300 | 433 | 300 | 242 / 549 / 242 |

Oberhalb von 1440 px unterscheiden sich die beiden kaum — die Seite ist dort gedeckelt, und 300
gegen 302 px ist nichts. Der Unterschied entsteht darunter, und er ist eine Entscheidung darüber,
wer zahlt.

> [!warning] Den Unterschied zahlt allein der Text
> Bei 1201 px — knapp über dem Tablet-Umbruch — bleiben der Textspalte 433 px statt 549, also gut
> 45 Zeichen je Zeile statt 57. Dafür steht der [[7-nachschlagen/01-glossar#Explorer|Explorer]] auf jeder Desktop-Breite gleich breit da,
> und ein Ordnerbaum, der bei 1300 px anfängt, seine Namen abzuschneiden, ist schlechter zu
> gebrauchen als eine etwas kürzere Textzeile. Die festen Werte gehören deshalb auf Desktop und
> Tablet und nicht auf Mobil, wo die Randspalte ohnehin über die ganze Breite geht.

Am Tablet sind nur die **linken** drei Spalten fest. Eine feste Spur ist nicht komprimierbar, und
jede von ihnen hebt die Mindestbreite des Rasters: Wären auch 10–12 fest, käme das Raster nicht
unter 976 px, und jede Seite scrollte in einem 900-px-Fenster um 92 px seitwärts. Dort unten tragen
diese drei Spalten ohnehin Text und keine Randspalte mehr.

## Zwei Eigenheiten des Editors

- Ein Wert darf **kein Komma** enthalten — also kein `minmax(0, 1fr)`.
- Längen stehen als Zahl, nicht als [[7-nachschlagen/01-glossar#Token|Token]]: Ein Frame muss auch funktionieren, wenn jemand nur den
  [[7-nachschlagen/01-glossar#Baustein|Baustein]] *Frames* importiert und die Variablen fehlen.

Wie eine Zeichnung davon aussieht: [[3-obsidian-formate/03-excalidraw/index|Excalidraw]].
