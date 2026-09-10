---
title: Zuletzt geändert
description: Die jüngsten Notizen als Kasten unter dem Text.
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
eingedampft**.

Gemessen vor dem Eindampfen: Ein Eintrag war 113 px hoch, fünf davon füllten 700 px einer Leiste,
die auch noch den Baum und die Notiz-Box trug. Heute sind es 54 px je Eintrag und 320 px für den
ganzen Kasten.

Zwei der drei Zeilen waren ein Versehen. Die Regel für die Überschrift der Box lautete
`.recent-notes h1, h2, h3` — und jeder Eintragstitel *ist* eine `h3`, also wurden alle fünf in
Versalien und Sperrung gesetzt. Der Selektor nennt jetzt das eigene Kind der Box (`> h3`) und nichts
Tieferes. Beschreibung und Tag-Pillen sind ganz weg: Die eine wiederholt den Titel bei halber
Lesbarkeit, die anderen sind höher als der Eintrag, den sie beschriften.

Ein dritter Abstand kam vom `li` selbst. Quartz gibt jedem Listeneintrag 1 rem oben und unten, die
[[7-nachschlagen/01-glossar#Rückverweise|Rückverweise]] nehmen ihn zurück, dieser Kasten tat es nicht — 32 px je Eintrag, die niemand
bestellt hatte, 160 von 408 px insgesamt. Deshalb stand er kopfhoch neben dem Kasten daneben, und
der Abstand unter der Überschrift las sich wie ein Einzug.

## Wo er steht

**Unter dem Text**, nicht in der Seitenleiste, und dort in einer Reihe mit den Rückverweisen — zwei
Kästen nebeneinander, oberhalb der Telefonbreite immer zweispaltig, darunter untereinander. Bis zum
10.09.2026 stand er links oben in der Seitenleiste unter dem [[7-nachschlagen/01-glossar#Explorer|Explorer]]; dort war er eine dritte
Liste in einer Spalte, die schon zwei trug.

Er ist damit auch nicht mehr auf den Desktop beschränkt. Ein Kasten unter dem Artikel ist auf einem
Telefon kein Hindernis mehr, sondern das, was nach dem Lesen kommt.

## Ordnerseiten stehen nicht drin

`hideFolderPages: true` nimmt jede `…/index`-Seite aus der Liste, die zwei Startseiten
eingeschlossen. Ohne diese Option war der Kasten die Spitze der Gliederung statt einer Liste von
Notizen: vier Ordner- und Startseiten von fünf, und auf der Startseite führte er sie selbst auf,
zweimal, weil beide Sprachen „Example“ heißen.

Das ist die Folge davon, dass die Dateizeiten dieses Vaults der Gliederung folgen — sie sind
gestaffelt, damit die Liste überhaupt eine Reihenfolge hat, und oben steht dann eben das
Inhaltsverzeichnis. Ein Kasten, der „zuletzt bearbeitet“ heißt, soll Notizen zeigen.

## Ein Fund beim Bauen

Diese Komponente benutzt **dieselben Klassennamen** wie die Ordner- und Tag-Listen: `.section`,
`.meta`, `.desc`, `.tags`. Die Listenregeln der Vorlage waren zunächst nicht eingegrenzt und
landeten deshalb auch hier — in der damals noch schmalen Seitenleiste stapelte das dreispaltige
Raster Datum und Titel übereinander.

Seitdem sind alle Listenregeln auf `.page-listing` eingegrenzt. Die Lehre: **Ein Klassenname gehört
nicht der Komponente, in der man ihn zuerst gesehen hat.**

> [!note] Beide Sprachen in einer Liste
> Die Liste entsteht aus jeder Seite des [[7-nachschlagen/01-glossar#Build|Builds]], eine englische Seite kann also im Kasten einer
> deutschen auftauchen. Einen Sprachfilter gibt es nicht — die Option dafür ist eine Funktion und
> lässt sich in einer YAML-Konfiguration nicht schreiben. Wie beim Suchindex trennte das nur ein
> Build je Sprache — siehe [[6-anpassen/07-zwei-sprachen/grenzen|Wo die zwei Sprachen aufhören]].

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 13 Variablen liest `aside-recent-notes.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 15 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
