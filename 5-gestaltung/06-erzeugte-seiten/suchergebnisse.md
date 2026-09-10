---
title: Suchergebnisse
description: Die Liste in der Suchüberlagerung.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - seitentypen
translationKey: gestaltung/erzeugte-seiten/suchergebnisse
---

## Von Haus aus

Karten mit Titel, Pfad und Textausschnitt.

## In dieser Vorlage

- **Keine Karten, sondern Zeilen** mit Haarlinien dazwischen. Eine Liste von zehn gerahmten Kästen
  ist unruhig.
- **Der Tastatur-Cursor und der Zeiger-Hover sehen gleich aus**: getönte Fläche plus Balken links.
  Die Pfeiltasten bewegen sich durch die Liste, und die hervorgehobene Zeile ist das einzige Signal,
  wo man gerade steht — sie darf nicht anders aussehen als das, was der Zeiger zeigt.
- **Der Textausschnitt** wird nach zwei Zeilen abgeschnitten.
- **Der Treffer im Text** wird mit derselben Farbe markiert wie `==Hervorhebung==` im Fließtext.
  „Das hast du gesucht" bedeutet auf der ganzen Seite dasselbe.
- **Der Pfad** steht in der Codeschrift, gedämpft und klein — er ist Herkunft, nicht Inhalt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 17 Variablen liest `page-search-results.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 weitere Komponenten |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--textHighlight` | `rgba(226, 189, 92, 0.55)` · dunkel `rgba(140, 184, 218, 0.30)` | Fließtext |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 6 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 weitere Komponenten |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
