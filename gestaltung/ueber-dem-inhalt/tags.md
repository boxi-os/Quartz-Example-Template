---
title: Tags
description: Marken unter dem Titel und im Fließtext.
section: Gestaltung
tags:
  - gestaltung
  - ueber-dem-inhalt
translationKey: gestaltung/ueber-dem-inhalt/tags
---

## Von Haus aus

Tags erscheinen als Links unter dem Titel, mit Hintergrund und Rahmen.

## In dieser Vorlage

**Eine Regel für alle Orte.** Ein Tag sieht in der Tag-Liste, in den Eigenschaften, in „zuletzt
geändert" und in einer Ordnerliste gleich aus: eine Pille mit dem Rautenzeichen davor, in der
Akzentfarbe auf getönter Fläche. Ein Ding, das an vier Stellen anders aussieht, sind vier Dinge zum
Lernen.

**Mit einer Ausnahme:** Im Fließtext verliert das Tag seine Pille und behält nur die Farbe. Ein
Absatz voller Pillen ist nicht lesbar. Zu sehen unter
[[formatierung/besonderes/pfeile-und-emoji|Pfeile, Tags und Emoji]].

Das Rautenzeichen steht als `::before` im Stylesheet und ist leicht transparent — es gehört zum
Tag, aber es ist nicht sein Name.

Beim Überfahren wechselt die Fläche und der Rand erscheint in der Akzentfarbe; die Pille springt
dabei nicht, weil der Rand vorher transparent da war.

> [!note] Englische Tags, englische Tag-Seiten
> Die englischen Seiten tragen englische Tags (`formatting` statt `formatierung`), jede Sprache
> bekommt damit eigene Tag-Seiten. Ein gemeinsamer Tag hätte beide Sprachen in eine Liste geworfen.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 11 Variablen liest `meta-tag-list.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tag-background` | — | nur hier |
| `--tag-background-hover` | — | nur hier |
| `--tag-color` | — | nur hier |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 8 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
