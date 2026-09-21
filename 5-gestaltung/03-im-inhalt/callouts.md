---
title: Callouts
description: Dreizehn Typen, alle neu gesetzt und gemessen.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - im-inhalt
  - callouts
translationKey: gestaltung/im-inhalt/callouts
---

## Von Haus aus

Quartz kennt dreizehn Typen und verteilt zehn Farbwerte darauf — drei Gruppen teilen sich je einen,
und `quote` liest die Akzentfarbe. Jeder Wert gilt in beiden Farbschemata gleich, dazu kommen ein
Rahmen und eine sehr blasse Fläche.

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

Die Prüfung liest die Farben **aus dem [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]]**, nicht aus einer Kopie in der Konfiguration.
Ein Wert, der hier geändert wird, wird auch hier gemessen.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 31 Variablen liest `body-callouts.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bg` | im Stylesheet gesetzt (`body-callouts.scss`) | nur hier |
| `--border` | im Stylesheet gesetzt (`body-callouts.scss`) | nur hier |
| `--callout-tint` | im Stylesheet gesetzt (`body-callouts.scss`) | nur hier |
| `--color` | — | nur hier |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--headerFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 15 weitere Komponenten |
| `--icon-chevron` | im Stylesheet gesetzt (`base.scss`) | 6.4 – Variablen |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 14 weitere Komponenten |
| `--tpl-accent-bar` | `3px` | 6 weitere Komponenten |
| `--tpl-callout-abstract` | `#0369A1` · dunkel `#67C7EF` | nur hier |
| `--tpl-callout-bug` | `#A21D62` · dunkel `#FF9BC8` | nur hier |
| `--tpl-callout-danger` | `#B02020` · dunkel `#FF9C93` | nur hier |
| `--tpl-callout-example` | `#6D28D9` · dunkel `#C3A6F7` | nur hier |
| `--tpl-callout-failure` | `#B02020` · dunkel `#FF9C93` | nur hier |
| `--tpl-callout-info` | `#0E7490` · dunkel `#5AC8DE` | nur hier |
| `--tpl-callout-note` | `#1D4ED8` · dunkel `#93B8FF` | nur hier |
| `--tpl-callout-question` | `#8A5A00` · dunkel `#E8C25E` | nur hier |
| `--tpl-callout-quote` | `var(--secondary)` = `#1463A3` | nur hier |
| `--tpl-callout-success` | `#136B34` · dunkel `#6DD68F` | nur hier |
| `--tpl-callout-tip` | `#0F766E` · dunkel `#5AD3BC` | nur hier |
| `--tpl-callout-todo` | `#0E7490` · dunkel `#5AC8DE` | nur hier |
| `--tpl-callout-warning` | `#9A4B06` · dunkel `#F0A868` | nur hier |
| `--tpl-focus-offset` | `2px` | 6.4 – Variablen |
| `--tpl-focus-width` | `2px` | 6.4 – Variablen |
| `--tpl-motion` | `150ms ease` | 13 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 17 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 10 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 12 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 20 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
