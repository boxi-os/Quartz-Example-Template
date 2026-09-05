---
title: Link-Vorschau
description: Was beim Überfahren eines internen Links erscheint.
section: Gestaltung
tags:
  - gestaltung
  - seitentypen
translationKey: gestaltung/seitentypen/vorschau
---

## Von Haus aus

Ein Kasten mit dem Anfang der Zielseite.

## In dieser Vorlage

Sie trägt einen echten Schatten — eine der fünf Stellen, die wirklich über der Seite schweben.
Deckende Fläche, denn eine durchscheinende Vorschau über Fließtext ist unlesbar.

Der Inhalt ist auf **20 rem gekappt**, und am Schnitt liegt ein weicher Verlauf: Eine abgeschnittene
Vorschau soll geschnitten aussehen, nicht kaputt.

Weggelassen wird darin, was in einer Vorschau nur stört: Callouts, Tags und Codeblöcke. Eine
Vorschau soll die Frage beantworten, ob sich der Klick lohnt — mehr nicht.

## Nur mit Zeiger

Bei `@media (hover: none)` wird sie ganz abgeschaltet. Daraus folgt eine Regel für den Inhalt:
**Keine Information darf ausschließlich in einer Vorschau stehen**, denn auf einem Telefon gibt es
sie nicht.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 13 Variablen liest `page-popover.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--tpl-radius-lg` | `14px` | Graph, Suche |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-lg` | `1.15rem` | Tokens, Suche |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
