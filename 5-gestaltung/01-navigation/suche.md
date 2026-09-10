---
title: Suche
description: Das Feld in der Leiste und die Überlagerung dahinter.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/suche
---

## Von Haus aus

Ein Knopf mit Lupe, der eine Überlagerung öffnet. Der Rand kommt aus `lightgray`.

## In dieser Vorlage

- Der Rand kommt aus **`gray`**, nicht aus `lightgray`. Das ist die Umsetzung der Kontrastregel:
  `lightgray` misst 1,34:1 gegen den Grund und darf deshalb nichts umranden, das man bedient.
- Der Knopf steht **im Kopfbereich**, ganz rechts, zusammen mit den drei anderen Bedienelementen.
  Er ist 44 px hoch wie seine Nachbarn und 15 rem breit — breit genug, um als Feld gelesen zu
  werden, schmal genug, dass der Kopf weiter dem Seitentitel gehört. Am Telefon wird er ein Quadrat
  ohne Beschriftung.
- Die **Überlagerung** trägt einen echten Schatten. Den bekommt in dieser Vorlage nur, was
  wirklich über der Seite schwebt statt in ihr zu liegen: diese Überlagerung, die Linkvorschau,
  das Sprachmenü, die Schublade am Telefon und der große [[7-nachschlagen/01-glossar#Graph|Graph]]. Fünf Stellen, und die Regel zählt,
  nicht die Zahl.
- Das **Eingabefeld** bekommt keinen Fokusring, sondern eine kräftigere Unterkante — ein Ring
  innerhalb eines abgerundeten Kastens sieht aus wie ein Fehler.
- **Ergebnisse**: Der Tastatur-Cursor und der Zeiger-Hover sehen gleich aus. Die Pfeiltasten
  bewegen sich durch die Liste, und die hervorgehobene Zeile ist das einzige Signal, wo man steht.
- Der **Treffer im Text** wird mit derselben Farbe markiert wie `==Hervorhebung==` im Fließtext.
  „Das hast du gesucht" heißt auf der ganzen Seite dasselbe.

Bei `prefers-reduced-transparency` wird die durchscheinende Fläche durch eine deckende ersetzt.

> [!example] Die Breite ist zweimal umgezogen
> Sie stand zuerst als `flex: 0 1 15rem` an `.search` — und wirkte nicht: Gemessen waren es
> **110 px**, bei 1728, 1440, 1100 und 900 px gleichermaßen, obwohl die Werkzeugleiste dort nur 322
> von 1400 px belegte. Quartz legt um jede Komponente einer Gruppe einen eigenen `div` ohne Klasse
> und schreibt dessen Flex-Werte als **Inline-Stil** aus der Konfiguration. Das Flex-Element ist
> also der Wrapper, nicht `.search`, und ein Inline-Stil schlägt jedes [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]].
>
> Also zog sie am 05.09.2026 in die Konfiguration, als `layout.groupOptions.basis`. Das war in
> Chromium richtig und in den zwei anderen Engines falsch: Gecko und WebKit rechnen eine
> `flex-basis` **nicht** in die Maximalbreite der Gruppe ein, sondern nehmen dafür die
> Inhaltsbreite des Elements — 110 px statt 240. Die Gruppe kam damit auf 322 px statt 452, und ihre
> eigenen Kinder hingen in Firefox und Safari 130 px aus dem Fenster.
>
> Seit dem 06.09.2026 ist es wieder eine `width: 15rem` an `.search` in `nav-header.scss`, und dabei
> bleibt es: Eine Breite am Element selbst macht dessen Inhaltsbreite zu 240 px, und darüber sind
> sich alle drei Engines einig. In der Konfiguration blieb `shrink: false` — ohne das gibt das Feld
> seine Breite an die zwei Icon-Knöpfe ab, lange bevor die Leiste voll ist. Am Telefon nimmt
> dasselbe Stylesheet die Breite wieder weg.

> [!note] Der Index umfasst beide Sprachen
> Es gibt einen Suchindex für die ganze Website, eine englische Seite kann also in einem deutschen
> Suchergebnis auftauchen. Trennen ließe sich das nur mit einem [[7-nachschlagen/01-glossar#Build|Build]] je Sprache — siehe
> [[6-anpassen/07-zwei-sprachen/grenzen|Wo die zwei Sprachen aufhören]].

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 18 Variablen liest `nav-search.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-lg` | `14px` | 3 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 10 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-lg` | `1.15rem` | 6.4 – Variablen, Link-Vorschau |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
