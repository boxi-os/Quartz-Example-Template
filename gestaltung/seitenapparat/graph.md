---
title: Graph
description: Die Umgebung einer Notiz als Netz.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/seitenapparat/graph
---

## Von Haus aus

Ein Kasten mit der lokalen Umgebung, dazu ein Symbol zum Öffnen der Gesamtansicht.

## In dieser Vorlage

Der Graph zeichnet sich selbst und holt seine Farben zur Laufzeit aus den CSS-Variablen. Die
Vorlage gestaltet deshalb **nur den Kasten darum**, nicht die Zeichnung:

- ein **quadratisches Feld** (`aspect-ratio: 1`) — der lokale Graph ist rund, ein breiter Kasten
  verschenkt die Seitenleiste
- Rahmen und getönte Fläche wie bei den anderen Panels
- das **Symbol für die Gesamtansicht** ist 44 px groß und sitzt rechts in der Überschriftenzeile
- die **Gesamtansicht** bekommt denselben Schatten wie die Suche — beide schweben wirklich

Ein halb umgefärbter Graph wäre schlechter als ein fremdfarbiger: Die Zeichnung löst ihre Farben
selbst auf, und ein Stylesheet, das dagegen arbeitet, trifft immer nur die Hälfte.

**Auf schmalen Bildschirmen wird er ausgeblendet** (`display: desktop-only`) — ein Netz aus Punkten
in einer 390 px breiten Spalte zeigt nichts.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 17 Variablen liest `aside-graph.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--tpl-radius-lg` | `14px` | Suche, Link-Vorschau |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 12 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
