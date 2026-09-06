---
title: Lesemodus
description: Die Leisten ausblenden — und sehen, dass es an ist.
section: 5 Die Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/lesemodus
---

Der Lesemodus blendet die Seitenleisten aus, solange man auf der Seite bleibt.

## Von Haus aus

Ein Knopf, der den Modus umschaltet. Die einzige Rückmeldung ist, dass die Seite anders aussieht.

## In dieser Vorlage

Der Knopf **zeigt seinen Zustand**: Bei eingeschaltetem Lesemodus wechseln Rand, Fläche und Symbol
auf die Akzentfarbe. Wer ihn versehentlich getroffen hat, sieht woran es liegt — sonst ist die
einzige Rückmeldung, dass plötzlich die halbe Seite fehlt.

Maße wie bei den Nachbarn: 44 × 44 px, gleicher Rahmen.

> [!tip] Was der Lesemodus nicht ist
> Er ändert nichts am Inhalt und nichts am Ausdruck. Für den Druck entfernt diese Vorlage die
> Leisten ohnehin — siehe [[6-anpassen/06-barrierefreiheit|Barrierefreiheit]].

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 10 Variablen liest `nav-reader-mode.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-icon` | `1.1rem` | Farbschema-Umschalter, Explorer |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
