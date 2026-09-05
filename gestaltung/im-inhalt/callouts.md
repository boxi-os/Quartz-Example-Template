---
title: Callouts
description: Zwölf Farben, alle neu gesetzt und gemessen.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
  - callouts
translationKey: gestaltung/im-inhalt/callouts
---

## Von Haus aus

Quartz kennt dreizehn Typen und setzt zwölf Farben dafür; `note` behält die Grundfarbe. Jede gilt
in beiden Farbschemata gleich, dazu kommen ein Rahmen und eine sehr blasse Fläche.

Gemessen gegen den hellen Grund dieser Vorlage scheitern **elf von dreizehn** an der WCAG-Schwelle:

| Typ | Standardfarbe | gegen hellen Grund |
| --- | --- | --- |
| `note` | `#448aff` | 3,23 : 1 |
| `question` | `#dba642` | 2,14 : 1 |
| `tip` | `#00bfa5` | 2,27 : 1 |
| `danger` / `failure` / `bug` | `#db4242` | 4,20 : 1 — und 4,16 : 1 im dunklen Modus |

## In dieser Vorlage

Alle dreizehn sind neu gesetzt, **je Modus einmal**, und werden bei jedem Lauf zweifach gemessen:
gegen den Seitengrund und gegen die eigene getönte Fläche. Der Farbton bleibt erhalten — Blau bleibt
Blau —, damit der Typ weiterhin an der Farbe erkennbar ist.

Dazu drei Struktur-Entscheidungen:

- **Balken statt Vollrahmen.** Ein Callout soll auffallen, ohne die Spalte zu zerschneiden.
- **Der Titel ist das Bedienelement**, wenn der Callout faltbar ist — mit eigenem Fokusring in der
  Typfarbe.
- **Verschachtelte Callouts** geben ihren Rahmen auf und behalten nur den Balken.

Die Prüfung liest die Farben **aus dem Stylesheet**, nicht aus einer Kopie in der Konfiguration.
Ein Wert, der hier geändert wird, wird auch hier gemessen.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 19 Variablen liest `body-callouts.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bg` | im Stylesheet gesetzt (`body-callouts.scss`) | nur hier |
| `--border` | im Stylesheet gesetzt (`body-callouts.scss`) | nur hier |
| `--callout-tint` | im Stylesheet gesetzt (`body-callouts.scss`) | nur hier |
| `--color` | — | nur hier |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--icon-chevron` | im Stylesheet gesetzt (`base.scss`) | Tokens |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-focus-offset` | `2px` | Tokens |
| `--tpl-focus-width` | `2px` | Tokens |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
