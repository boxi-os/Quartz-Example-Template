---
title: Farben und Kontrast
description: Neun Rollen, zwei davon verkehrt herum benannt — und 78 gemessene Paare.
section: Gestaltung
tags:
  - gestaltung
  - grundlagen
---

## Die neun Rollen

Quartz benennt seine Palette nach Rollen. **Zwei davon lesen sich rückwärts:** `light` ist der
*Hintergrund*, `dark` der *Text* — auch im dunklen Modus, wo `light` fast schwarz ist. Wer das
übersieht, baut sein erstes dunkles Farbschema falsch herum.

| Rolle | Wofür | hell | dunkel |
| --- | --- | --- | --- |
| `light` | Seitengrund | `#FCFCFA` | `#16171A` |
| `lightgray` | Linien, Karten, Codeblöcke | `#DEDCD5` | `#2E3036` |
| `gray` | Sekundärtext **und jeder Rand eines Bedienelements** | `#5F5D57` | `#A1A3A8` |
| `darkgray` | Fließtext | `#33322E` | `#D5D7DB` |
| `dark` | Überschriften | `#17171A` | `#F3F4F6` |
| `secondary` | Links, der eine Akzent | `#2A4E6C` | `#8CB8DA` |
| `tertiary` | Link-Hover, aktive Navigation | `#9C4221` | `#E8A56B` |
| `highlight` | getönte Fläche | 10 % Akzent | 12 % Akzent |
| `textHighlight` | `==Hervorhebung==` | warmes Gelb | Akzent, 30 % |

Die beiden Akzente sind mit Absicht **zwei verschiedene Farben** und nicht zwei Helligkeiten
derselben. `tertiary` markiert, was gerade angefasst oder gerade aktiv ist; wenn es nur eine
dunklere Variante von `secondary` wäre, sähe man dem Ergebnis nicht an, welche der beiden Rollen
gerade greift. Ein tiefes Navy und ein warmes Sienna beantworten diese Frage auf einen Blick — und
beide messen sich gegen jeden Grund, auf dem sie vorkommen (6,36:1 für Sienna auf dem Seitengrund,
4,76:1 auf einer Karte).

## Was gemessen wird

**78 Paare**, bei jedem Lauf: jede Text-auf-Grund-Kombination in beiden Modi, die Alpha-Farben über
den Grund gerechnet, und alle zwölf Callout-Farben gegen den Grund *und* gegen ihre eigene getönte
Fläche. Der knappste Wert liegt bei 4,68:1 gegen eine Schwelle von 4,5.

## Die eine Ausnahme, und wohin sie führt

`lightgray` erreicht nur 1,34:1 gegen den Grund. Das ist Absicht: Es ist Trennlinie *und* Fläche
zugleich, und WCAG 1.4.11 verlangt 3:1 von *Bedienelementen*, nicht von einer Zierlinie. Hebe man
es auf 3:1, würde jeder Codeblock mittelgrau.

Die Pflicht verschwindet dadurch nicht, sie wandert: **Alles, was man bedient, zieht seinen Rand
aus `gray`.** Umgesetzt ist das über drei Variablen, die von `lightgray` auf `gray` gezogen wurden
— `--background-modifier-border` und ihresgleichen.

**Von Haus aus** prüft Quartz nichts davon; die mitgelieferte Palette scheitert an mehreren
Stellen, am deutlichsten bei den Callout-Farben.
