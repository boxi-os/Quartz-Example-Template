---
title: Fließtext
description: Die Breite des Textes, die Überschriftenskala und die Links darin.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - im-inhalt
translationKey: gestaltung/im-inhalt/fliesstext
---

## Die Breite des Textes

**In dieser Vorlage** entscheidet das Seitenraster, wie breit der Text wird — nicht eine Regel am
Absatz. Der [[7-nachschlagen/01-glossar#Frame|Frame]] gibt dem Inhalt sechs von zwölf Spalten, das sind 672 px auf einer Seite, die bei
1440 px gedeckelt ist — bei 1 rem Schriftgröße rund 70 Zeichen.

**Von Haus aus** macht Quartz dasselbe, nur mit anderen Zahlen: Es begrenzt die Seite über
`.page { max-width }`.

> [!note] Was hier einmal stand
> Eine frühere Fassung begrenzte den Fließtext zusätzlich auf 68 Zeichen. Das ist ein verbreiteter
> Rat, führt aber dazu, dass zwei Stellen dieselbe Frage beantworten — die Spaltenbreite und die
> Zeilenlänge — und bei jeder Änderung am Frame nachgezogen werden muss. Die Entscheidung liegt
> jetzt nur noch im Raster.

## Überschriften

Sechs Ebenen, aber nur vier Größen. Ebene 5 und 6 wechseln zu Versalien und Sperrung, weil ein
Unterschied von einem Pixel keine Information ist. Der Abstand liegt **über** der Überschrift, nie
darunter — die Lücke sagt, was zur Überschrift gehört.

## Links

Farbe **und** Unterstreichung. Die Unterstreichung ist halbtransparent und tief gesetzt, damit sie
die Unterlängen nicht zerschneidet; beim Überfahren wird sie deckend. Externe Links tragen einen
Pfeil.

## Zitate

Balken in der Akzentfarbe, getönte Fläche, aufrechter Text. **Von Haus aus** ist der Text kursiv —
über mehrere Zeilen liest sich das schlechter, und ein Zitat ist eine andere Stimme, kein anderer
Tonfall.

## Hervorhebung

`==markiert==` nimmt `textHighlight` — im hellen Modus ein warmes Gelb, im dunklen der Akzent mit
Transparenz. Beide sind gegen die Textfarbe gemessen.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 29 Variablen liest `body-content.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--icon-task-cancelled` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-task-doing` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-task-done` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-task-forwarded` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-task-open` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-task-question` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tertiary` | `#196B6B` · dunkel `#2CAFAD` | 2.9 – Diagramme, Die Instanzen |
| `--textHighlight` | `rgba(226, 189, 92, 0.55)` · dunkel `rgba(140, 184, 218, 0.30)` | Suchergebnisse |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 15 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 5 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
