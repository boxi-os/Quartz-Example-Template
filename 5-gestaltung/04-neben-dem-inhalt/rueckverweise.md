---
title: Rückverweise
description: Was auf diese Seite zeigt.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/neben-dem-inhalt/rueckverweise
---

Unter dem Inhaltsverzeichnis steht, welche anderen Notizen auf die aktuelle verweisen.

## Von Haus aus

Eine Liste von Titeln. Der Leerzustand lautet „Keine Backlinks gefunden".

## In dieser Vorlage

- Die Einträge sind durch **Haarlinien** getrennt statt durch Abstand — in einer schmalen Spalte
  spart das Platz und liest sich ruhiger.
- Ein langer Titel wird nach **zwei Zeilen abgeschnitten**. Eine Liste voller dreizeiliger Titel
  ist eine Wand.
- Der **Leerzustand** ist kursiv und gedämpft gesetzt: Er soll wie eine Antwort aussehen, nicht wie
  ein Fehler.

## Zur Formulierung

Die Vorlage benennt die Komponente in ihrer Sprachdatei um — „Verweise hierher" statt „Backlinks".
Das ist ein Wort aus dem Werkzeug, nicht aus der Sprache.

> [!warning] Diese Umbenennung wirkt nicht
> Gemessen: Jede sichtbare Überschrift auf einer Quartz-5-Seite kommt aus einem
> Komponenten-**Plugin**, und jedes dieser npm-Pakete bringt seine eigenen kompilierten
> Übersetzungen mit. Die Sprachdatei des Projekts erreicht sie nicht. Der Eintrag steht trotzdem
> in der Vorlage — der Mechanismus ist richtig, nur seine Reichweite ist heute klein.

> [!note] Rückverweise überschreiten die Sprachgrenze nicht
> Eine deutsche Seite verlinkt auf deutsche Seiten, eine englische auf englische; damit bleiben die
> beiden Listen getrennt. Das tut nicht das Plugin — es folgt daraus, dass jede Seite nur innerhalb
> ihres eigenen Baums verlinkt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 9 Variablen liest `aside-backlinks.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
