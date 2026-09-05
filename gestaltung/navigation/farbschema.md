---
title: Farbschema-Umschalter
description: Der Knopf zwischen hell und dunkel.
section: Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/farbschema
---

## Von Haus aus

Ein Knopf mit zwei Symbolen, von denen je nach Schema eines sichtbar ist.

## In dieser Vorlage

Er ist Teil der Werkzeugleiste im Kopfbereich und teilt deren Maße: 44 × 44 px, gleicher Rahmen,
gleiche Ecken wie Suche, Lesemodus und Sprachumschalter. Eine Reihe von Bedienelementen mit unterschiedlichen Höhen liest sich als
Fehler.

Beim Überfahren wechselt der Rand auf die Akzentfarbe und die Fläche auf die getönte Variante —
dieselbe Rückmeldung wie bei den beiden Nachbarn.

## Ein Fund beim Bauen

Die erste Fassung dieser Datei gestaltete ein `<input>`/`<label>`-Paar. Das gibt es hier nicht: Die
Komponente ist ein einzelner `<button class="darkmode">` mit zwei SVGs darin. Die Regeln trafen
nichts — sichtbar wurde das erst, als jeder Selektor der Vorlage gegen die gebaute Seite geprüft
wurde.

Daraus die Regel, die überall in dieser Vorlage gilt: **Vor dem Schreiben einer Regel im gebauten
HTML nachsehen.** Klassennamen sind kein Vertrag.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 10 Variablen liest `nav-darkmode.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-icon` | `1.1rem` | Explorer, Lesemodus |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 12 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
