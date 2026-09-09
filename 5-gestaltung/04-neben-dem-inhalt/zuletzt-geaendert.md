---
title: Zuletzt geändert
description: Die jüngsten Notizen in der Seitenleiste.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/neben-dem-inhalt/zuletzt-geaendert
---

## Von Haus aus

Eine Liste der zuletzt bearbeiteten Seiten mit Datum, Beschreibung und Tags.

## In dieser Vorlage

Auf fünf Einträge begrenzt, durch Haarlinien getrennt, und **auf eine Zeile Titel plus Datum
eingedampft**. Nur am Desktop sichtbar — auf einem Telefon steht die Seitenleiste über dem Inhalt,
und dort ist diese Liste im Weg.

Gemessen vor dem Eindampfen: Ein Eintrag war 113 px hoch, fünf davon füllten 700 px einer Leiste,
die auch noch den Baum und die Notiz-Box trägt. Danach: 57 px je Eintrag, 398 px für die Box.

Zwei der drei Zeilen waren ein Versehen. Die Regel für die Überschrift der Box lautete
`.recent-notes h1, h2, h3` — und jeder Eintragstitel *ist* eine `h3`, also wurden alle fünf in
Versalien und Sperrung gesetzt. Der Selektor nennt jetzt das eigene Kind der Box (`> h3`) und nichts
Tieferes. Beschreibung und Tag-Pillen sind ganz weg: Die eine wiederholt den Titel bei halber
Lesbarkeit, die anderen sind höher als der Eintrag, den sie beschriften.

## Ein Fund beim Bauen

Diese Komponente benutzt **dieselben Klassennamen** wie die Ordner- und Tag-Listen: `.section`,
`.meta`, `.desc`, `.tags`. Die Listenregeln der Vorlage waren zunächst nicht eingegrenzt und
landeten deshalb auch hier — in der schmalen Seitenleiste stapelte das dreispaltige Raster Datum
und Titel übereinander.

Seitdem sind alle Listenregeln auf `.page-listing` eingegrenzt. Die Lehre: **Ein Klassenname gehört
nicht der Komponente, in der man ihn zuerst gesehen hat.**

> [!note] Beide Sprachen in einer Liste
> Die Liste entsteht aus jeder Seite des [[7-nachschlagen/01-glossar#Build|Builds]], eine englische Seite kann also in der Leiste einer
> deutschen auftauchen. Wie beim Suchindex trennte das nur ein Build je Sprache — siehe
> [[6-anpassen/07-zwei-sprachen/grenzen|Wo die zwei Sprachen aufhören]].

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 13 Variablen liest `aside-recent-notes.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
