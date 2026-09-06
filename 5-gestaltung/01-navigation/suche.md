---
title: Suche
description: Das Feld in der Leiste und die Überlagerung dahinter.
section: Gestaltung
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
  das Sprachmenü, die Schublade am Telefon und der große Graph. Fünf Stellen, und die Regel zählt,
  nicht die Zahl.
- Das **Eingabefeld** bekommt keinen Fokusring, sondern eine kräftigere Unterkante — ein Ring
  innerhalb eines abgerundeten Kastens sieht aus wie ein Fehler.
- **Ergebnisse**: Der Tastatur-Cursor und der Zeiger-Hover sehen gleich aus. Die Pfeiltasten
  bewegen sich durch die Liste, und die hervorgehobene Zeile ist das einzige Signal, wo man steht.
- Der **Treffer im Text** wird mit derselben Farbe markiert wie `==Hervorhebung==` im Fließtext.
  „Das hast du gesucht" heißt auf der ganzen Seite dasselbe.

Bei `prefers-reduced-transparency` wird die durchscheinende Fläche durch eine deckende ersetzt.

> [!example] Warum die Breite in der Konfiguration steht und nicht im Stylesheet
> Sie stand einmal dort, als `flex: 0 1 15rem` an `.search` — und wirkte nicht: Gemessen waren es
> **110 px**, bei 1728, 1440, 1100 und 900 px gleichermaßen, obwohl die Werkzeugleiste dort nur 322
> von 1400 px belegte. Quartz legt um jede Komponente einer Gruppe einen eigenen `div` ohne Klasse
> und schreibt dessen Flex-Werte als **Inline-Stil** aus der Konfiguration. Das Flex-Element ist
> also der Wrapper, nicht `.search`, und ein Inline-Stil schlägt jedes Stylesheet.
>
> Die 15 rem stehen deshalb seit dem 05.09.2026 in `layout.groupOptions.basis` der Suche, zusammen
> mit `shrink: false`. Das zweite gehört dazu: Ein schrumpfbares Element steuert nur seine
> Inhaltsbreite zur Größe der Gruppe bei, die Gruppe blieb bei 322 px, während ihre Kinder 452
> wollten — und die Leiste brach auf zwei Zeilen um, der Kopf wuchs von 61 auf 101 px. Am Telefon
> nimmt `nav-header.scss` die Breite wieder weg, mit `!important`, weil nur das gegen einen
> Inline-Stil ankommt.

> [!note] Der Index umfasst beide Sprachen
> Es gibt einen Suchindex für die ganze Website, eine englische Seite kann also in einem deutschen
> Suchergebnis auftauchen. Trennen ließe sich das nur mit einem Build je Sprache — siehe
> [[6-anpassen/07-zwei-sprachen/grenzen|Wo die zwei Sprachen aufhören]].

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 18 Variablen liest `nav-search.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-lg` | `14px` | 3 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-lg` | `1.15rem` | 6.4 Variablen, Link-Vorschau |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
