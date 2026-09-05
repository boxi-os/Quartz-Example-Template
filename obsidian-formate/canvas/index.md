---
title: Canvas
description: Eine unendliche Fläche mit Karten und Verbindungen.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - canvas
translationKey: obsidian-formate/canvas/index
---

Ein Canvas ist eine freie Fläche: Man legt Karten darauf, verbindet sie mit Pfeilen und ordnet sie
räumlich statt in einer Reihenfolge. Für Zusammenhänge, die keine Gliederung sind.

Das Beispiel in diesem Vault: [[obsidian-formate/canvas/Aufbau der Vorlage.canvas|Aufbau der Vorlage]] —
die vier Bereiche dieser Website und wie sie zusammenhängen.

Wie das Format aufgebaut ist: [[obsidian-formate/canvas/wie-es-funktioniert|Wie es funktioniert]].

## In dieser Vorlage

Eine Canvas-Seite braucht die **volle Breite** — eine Fläche in der schmalen Textspalte zeigt
nichts. Das Plugin bringt dafür zwar ein eigenes Seitenraster mit, diese Vorlage überschreibt es
aber: In der Konfiguration steht für den Seitentyp `canvas` das mitgelieferte Quartz-Raster
`full-width`. Gemessen an der gebauten Seite ist das Ergebnis Kopfbereich, Fläche und Fußzeile —
keine Seitenleisten, keine Brotkrumen.

> [!bug] Links in einem Dateiknoten führen ins Leere
> Ein Dateiknoten zeigt eine Notiz mit ihrem ganzen Inhalt — und die Links darin bekommen den
> Ordner der eingebetteten Notiz **zweimal** vorangestellt. Aus dem Verweis auf
> `gestaltung/grundlagen/frames` in der Bases-Übersicht wird auf dieser Seite
> `../../obsidian-formate/bases/../../../obsidian-formate/bases/alle-ansichten.base` — ein Pfad, der
> aus der Website herausführt. Gemessen: **sechs je Sprache**, alle in demselben Dateiknoten, und die
> Zahl wächst mit jedem Link, der in einer eingebetteten Notiz dazukommt.
>
> Das ist ein Fehler im Plugin `canvas-page`, nicht in dieser Vorlage — die Links stimmen auf ihren
> eigenen Seiten. Wer sich darauf verlassen will, klickt den Knotentitel an und liest die Notiz
> dort.

> [!note] Zoomen und Verschieben
> Auf der gebauten Seite lässt sich das Canvas mit dem Mausrad zoomen und mit gedrückter Maustaste
> verschieben — es ist keine Momentaufnahme, sondern die Fläche selbst.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 13 Variablen liest `page-canvas.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 12 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
