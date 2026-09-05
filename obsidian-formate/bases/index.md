---
title: Bases
description: Abfragen über den Vault, als Tabelle, Karten oder Liste.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - bases
translationKey: obsidian-formate/bases/index
---

Eine Base ist eine gespeicherte Abfrage: Sie sammelt Notizen nach Kriterien und zeigt sie in einer
oder mehreren Ansichten. Die Datei ist YAML und endet auf `.base`.

Drei Beispiele in diesem Vault, alle über die Notizen dieser Website selbst:

- [[obsidian-formate/bases/Alle-Ansichten.base|Alle Ansichten]] — **alle fünf Darstellungsformen**
  derselben Daten: Tabelle, Kacheln, Liste, Board und Galerie
- [[obsidian-formate/bases/Formatierungsseiten.base|Formatierungsseiten]] — Tabelle und Kacheln
- [[obsidian-formate/bases/Gestaltungsseiten.base|Gestaltungsseiten]] — Liste, nach Bereich gruppiert

Wie das Format aufgebaut ist: [[obsidian-formate/bases/wie-es-funktioniert|Wie es funktioniert]].

## Die fünf Darstellungsformen

Eine Base kann dieselben Daten auf fünf Arten zeigen; die Umschalter stehen oben auf der Seite.

| Ansicht | Wofür sie taugt |
| --- | --- |
| **Tabelle** | viele Spalten vergleichen, nach einer Spalte sortieren |
| **Kacheln** | wenige Angaben je Eintrag, nebeneinander überfliegen |
| **Liste** | kompakt untereinander, mit Gruppierung |
| **Board** | nach einem Feld in Spalten aufgeteilt, wie ein Kanban |
| **Galerie** | großflächig, für Einträge mit Bild |

Alle fünf sind in dieser Vorlage gestaltet — zu sehen unter
[[obsidian-formate/bases/Alle-Ansichten.base|Alle Ansichten]].

## In dieser Vorlage

Bases-Seiten nutzen den Frame **`index`**, denselben wie Ordner- und Tag-Seiten. Ein
Inhaltsverzeichnis entsteht dort nicht, weil eine Tabelle keine Überschriften hat; die rechte
Spalte bleibt trotzdem stehen, damit die Tabelle dort beginnt, wo sonst der Text beginnt — am
Desktop neben dem Inhalt, darunter in einer eigenen Zeile.

> [!warning] Der Umschalter findet diese Seiten nicht
> Eine `.base`-Datei hat kein Frontmatter und kann deshalb keinen `translationKey` tragen. Der
> Sprachumschalter bietet auf so einer Seite die Startseite der anderen Sprache an statt der
> entsprechenden Base. Siehe [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].

> [!note] Bases sind neu
> Sie kamen mit Obsidian 1.9 als Kernfunktion dazu. Ältere Vaults haben sie nicht; im
> Beispiel-Vault ist die Funktion eingeschaltet.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 28 Variablen liest `page-bases.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 weitere Komponenten |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--ink` | — | nur hier |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 7 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 12 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 8 weitere Komponenten |
| `--tpl-tracking-caps` | `0.06em` | Tokens, Code |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
