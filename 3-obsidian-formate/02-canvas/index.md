---
title: 3.2 Canvas
description: Eine unendliche Fläche mit Karten und Verbindungen.
section: 3 Obsidian-Formate
tags:
  - obsidian-formate
  - canvas
translationKey: obsidian-formate/canvas/index
---

Ein Canvas ist eine freie Fläche: Man legt Karten darauf, verbindet sie mit Pfeilen und ordnet sie
räumlich statt in einer Reihenfolge. Für Zusammenhänge, die keine Gliederung sind.

Das Beispiel in diesem [[7-nachschlagen/01-glossar#Vault|Vault]]: [[3-obsidian-formate/02-canvas/Aufbau der Vorlage.canvas|Aufbau der Vorlage]] —
die sieben Kapitel dieses Handbuchs und wie sie zusammenhängen.

Wie das Format aufgebaut ist: [[3-obsidian-formate/02-canvas/wie-es-funktioniert|Wie es funktioniert]].

## In dieser Vorlage

Eine Canvas-Seite braucht die **volle Breite** — eine Fläche in der schmalen Textspalte zeigt
nichts. Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] bringt dafür zwar ein eigenes Seitenraster mit, diese Vorlage überschreibt es
aber: In der Konfiguration steht für den Seitentyp `canvas` das mitgelieferte Quartz-Raster
`full-width`. Gemessen an der gebauten Seite ist das Ergebnis Kopfbereich, Fläche und Fußzeile —
keine Seitenleisten, keine [[7-nachschlagen/01-glossar#Brotkrumen|Brotkrumen]].

> [!bug] Links in einem Dateiknoten können ins Leere führen
> Ein Dateiknoten zeigt eine Notiz mit ihrem ganzen Inhalt — und die Links darin bekommen den
> Ordner der eingebetteten Notiz **noch einmal** vorangestellt. Ob das Ziel danach noch stimmt,
> hängt davon ab, wie tief die Notiz liegt. Gemessen am 06.09.2026: Mit den sieben Kapitelseiten
> als Knoten (eine Ordnerebene tief) waren **112 Links** je Sprache kaputt — aus dem Verweis auf das
> Glossar wurde `../../1-einstieg/../../7-nachschlagen/01-glossar`, ein Pfad, der aus der Website
> herausführt. Mit den jetzigen sieben Knoten, alle zwei oder drei Ebenen tief, ist kein Link
> kaputt außer dem auf den Entwurf, der es absichtlich ist. Deshalb liegen hier keine Kapitelseiten.
> Ein Link in einem *Textknoten* wird gar nicht erst aufgelöst — `[[…]]` bleibt dort als Text
> stehen. Und das Label eines Dateiknotens ist der Dateiname, nicht der Titel.
>
> Das ist ein Fehler im Plugin `canvas-page`, nicht in dieser Vorlage — die Links stimmen auf ihren
> eigenen Seiten. Wer sich darauf verlassen will, klickt den Knotentitel an und liest die Notiz
> dort.

> [!note] Zoomen und Verschieben
> Auf der gebauten Seite lässt sich das Canvas mit dem Mausrad zoomen und mit gedrückter Maustaste
> verschieben — es ist keine Momentaufnahme, sondern die Fläche selbst.

## Die Seiten

- [[3-obsidian-formate/02-canvas/Aufbau der Vorlage.canvas|Aufbau der Vorlage]] — ein Canvas
- [[3-obsidian-formate/02-canvas/wie-es-funktioniert|Wie ein Canvas aufgebaut ist]] — JSON mit Knoten und Kanten.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 14 Variablen liest `page-canvas.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
