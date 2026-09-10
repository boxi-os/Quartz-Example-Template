---
title: Graph
description: Die Umgebung einer Notiz als Netz.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/neben-dem-inhalt/graph
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
selbst auf, und ein [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]], das dagegen arbeitet, trifft immer nur die Hälfte.

**Auf schmalen Bildschirmen wird er ausgeblendet** (`display: desktop-only`) — ein Netz aus Punkten
in einer 390 px breiten Spalte zeigt nichts.

## Was auf Ordnerseiten fehlt

Auf einer **Ordner- oder Kapitelseite** steht im Kasten nur ein einzelner Punkt, auch wenn die Seite
verlinkt ist. Das ist ein Fehler im Plugin und von einer Vorlage aus nicht zu beheben.

Das Skript rechnet Adressen an zwei Stellen um und an jeder anders. Seinen Datensatz schlüsselt es
mit `simplifySlug`: Das schneidet ein `index` am Ende ab und läßt den Schrägstrich davor stehen, aus
`2-formatierung/01-text/index` wird also `2-formatierung/01-text/`. Die Mitte des Graphen holt es
dagegen aus der Adresszeile und schneidet den Schrägstrich dort **ab**. Für jede Seite, deren
Adresse auf einen Schrägstrich endet — und das sind genau die Ordnerseiten — sucht es damit einen
Knoten, den es selbst nie angelegt hat: keine Kanten, ein Punkt.

Dieselbe Seite über `…/01-text/index` aufgerufen zeigt neun Knoten und acht Kanten. Ein Zeichen
Unterschied.

Ausblenden läßt der Kasten sich dort nicht: Quartz' Bedingung `not-index` meint nur die Startseite,
und alles Feinere braucht Code statt Konfiguration. Was die Verbindungen einer Ordnerseite
trotzdem zeigt, sind die [[7-nachschlagen/01-glossar#Rückverweise|Rückverweise]] und die Liste im Text darüber.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 17 Variablen liest `aside-graph.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--tpl-radius-lg` | `14px` | 3 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 10 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DDDDDD` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
