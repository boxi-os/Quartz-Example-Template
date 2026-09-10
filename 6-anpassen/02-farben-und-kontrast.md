---
title: 6.2 – Farben und Kontrast
description: Neun Rollen, zwei davon verkehrt herum benannt — und 93 gemessene Paare.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/farben-und-kontrast
---

## Die neun Rollen

Quartz benennt seine Palette nach Rollen. **Zwei davon lesen sich rückwärts:** `light` ist der
*Hintergrund*, `dark` der *Text* — auch im dunklen Modus, wo `light` fast schwarz ist. Wer das
übersieht, baut sein erstes dunkles [[7-nachschlagen/01-glossar#Farbschema|Farbschema]] falsch herum.

| Rolle | Wofür | hell | dunkel |
| --- | --- | --- | --- |
| `light` | Seitengrund | `#FCFCFA` | `#16171A` |
| `lightgray` | Linien, Karten, Codeblöcke | `#DDDDDD` | `#2E2E2E` |
| `gray` | Sekundärtext **und jeder Rand eines Bedienelements** | `#5F5F5F` | `#A1A1A1` |
| `darkgray` | Fließtext | `#333333` | `#DDDDDD` |
| `dark` | Überschriften | `#17171A` | `#FCFCFA` |
| `secondary` | Links, der eine Akzent | `#1463A3` | `#699DC3` |
| `tertiary` | Link-Hover, aktive Navigation | `#196B6B` | `#2CAFAD` |
| `highlight` | getönte Fläche | 10 % Akzent | 12 % Akzent |
| `textHighlight` | `==Hervorhebung==` | warmes Gelb, 55 % | Akzent, 30 % |

Die beiden Akzente sind mit Absicht **zwei verschiedene Farben** und nicht zwei Helligkeiten
derselben. `tertiary` markiert, was gerade angefasst oder gerade aktiv ist; wenn es nur eine
dunklere Variante von `secondary` wäre, sähe man dem Ergebnis nicht an, welche der beiden Rollen
gerade greift. Ein klares Mittelblau und ein dunkles Petrol beantworten diese Frage auf einen
Blick — nah genug beieinander, dass die Seite eine Farbfamilie hat, weit genug auseinander, dass
man den Wechsel sieht.

Beide messen sich gegen **jeden** Grund, auf dem sie vorkommen, nicht nur gegen den Seitengrund:
6,11:1 und 6,09:1 auf der Seite, 4,62:1 und 4,61:1 auf einer Karte. Der zweite Wert ist der, den
man übersieht — ein Link in einem [[7-nachschlagen/01-glossar#Callout|Callout]] oder in einer Code-Beschriftung steht auf genau dieser
Fläche.

## Was gemessen wird

**93 Paare**, bei jedem Lauf: jede Text-auf-Grund-Kombination in beiden Modi, die Alpha-Farben über
den Grund gerechnet, alle dreizehn Callout-Farben gegen den Grund *und* gegen ihre eigene getönte
Fläche, und seit dem 05.09.2026 die fünf korrigierten Farben des Syntax-Themas gegen die Fläche des
Codeblocks. Der knappste Wert liegt bei 4,61:1 gegen eine Schwelle von 4,5 — der überfahrene Link
auf einer Karte, und genau dafür wurde `tertiary` am 09.09.2026 noch einmal abgedunkelt.

Die drei Prüfungen lesen ihre Werte aus verschiedenen Dateien, aber nach demselben Prinzip: aus
`palette.mjs`, aus `body-callouts.scss` und aus `body-code.scss` — immer aus dem, was ausgeliefert
wird, nie aus einer zweiten Liste, die man vergessen kann.

## Die eine Ausnahme, und wohin sie führt

`lightgray` erreicht nur 1,32:1 gegen den Grund. Das ist Absicht: Es ist Trennlinie *und* Fläche
zugleich, und WCAG 1.4.11 verlangt 3:1 von *Bedienelementen*, nicht von einer Zierlinie. Hebe man
es auf 3:1, würde jeder Codeblock mittelgrau.

Die Pflicht verschwindet dadurch nicht, sie wandert: **Alles, was man bedient, zieht seinen Rand
aus `gray`.** Umgesetzt ist das über drei Variablen, die von `lightgray` auf `gray` gezogen wurden
— `--background-modifier-border` und ihresgleichen.

**Von Haus aus** prüft Quartz nichts davon; die mitgelieferte Palette scheitert an mehreren
Stellen, am deutlichsten bei den Callout-Farben.
