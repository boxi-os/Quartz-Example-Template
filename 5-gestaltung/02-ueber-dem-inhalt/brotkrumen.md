---
title: Brotkrumen
description: Der Weg von der Startseite bis hierher.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - ueber-dem-inhalt
translationKey: gestaltung/ueber-dem-inhalt/brotkrumen
---

## Von Haus aus

Eine Zeile mit den Ordnern des Pfades, durch Zeichen getrennt.

## In dieser Vorlage

- Die **letzte Krume ist die aktuelle Seite**: kräftiger gesetzt und nicht anklickbar. Ein Link auf
  die Seite, auf der man steht, ist eine Sackgasse.
- Das **Trennzeichen** ist gedämpft und nicht auswählbar — es soll nicht in einer Kopie landen.
- Die Zeile **bricht um** statt zu überlaufen. Drei Ordner tief ist der Pfad auf einem Telefon
  länger als der Bildschirm.
- Jede Krume hat **Innenabstand nach oben und unten**, damit sie auf einem Touchscreen zu treffen
  ist.

Ein tiefes Beispiel: [[2-formatierung/05-callouts/grundform|Callouts — Grundform]] — dort steht
der ganze Weg über vier Stationen.

> [!note] Nicht auf der Startseite
> Die Komponente ist mit `condition: not-index` konfiguriert; auf einer Ordner-Startseite wäre die
> letzte Krume identisch mit dem Titel darunter.

> [!note] Der Sprachordner ist auch eine Krume
> Auf einer englischen Seite beginnt der Pfad mit `en` — er ist ein Ordner wie jeder andere, und
> Quartz hat keinen Grund, ihn anders zu behandeln.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 7 Variablen liest `meta-breadcrumbs.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 6 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
