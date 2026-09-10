---
title: Rückverweise
description: Was auf diese Seite zeigt.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/neben-dem-inhalt/rueckverweise
---

Direkt unter dem Text steht, welche anderen Notizen auf die aktuelle verweisen — als Kasten neben
dem der [[5-gestaltung/04-neben-dem-inhalt/zuletzt-geaendert|zuletzt geänderten Seiten]].

## Von Haus aus

Eine Liste von Titeln. Der Leerzustand lautet „Keine Backlinks gefunden".

## In dieser Vorlage

- Die Einträge sind durch **Haarlinien** getrennt statt durch Abstand — in einer schmalen Spalte
  spart das Platz und liest sich ruhiger.
- Ein langer Titel wird nach **zwei Zeilen abgeschnitten**. Eine Liste voller dreizeiliger Titel
  ist eine Wand.
- Der **Leerzustand** ist kursiv und gedämpft gesetzt: Er soll wie eine Antwort aussehen, nicht wie
  ein Fehler.

## Wo er steht

Bis zum 10.09.2026 stand dieser Kasten in der rechten Spalte, unter dem Inhaltsverzeichnis. Er steht
jetzt unter dem Text, weil er dorthin gehört: Was auf eine Seite zeigt, ist eine Frage, die man
*nach* dem Lesen stellt, nicht daneben — und in der rechten Spalte teilte er sich den Platz mit
einer Gliederung, die beim Lesen gebraucht wird.

Er teilt seine Zeile mit dem Kasten „Zuletzt bearbeitete Seiten“ und ist dabei der rechte von
beiden. Die zwei stehen oberhalb der Telefonbreite immer nebeneinander, auch wenn einer von ihnen
leer bleibt — dann nimmt der andere die ganze Breite.

## Zur Formulierung

Die Vorlage benennt die Komponente in ihrer Sprachdatei um — „Verweise hierher" statt „Backlinks".
Das ist ein Wort aus dem Werkzeug, nicht aus der Sprache.

> [!warning] Diese Umbenennung wirkt nicht
> Gemessen: Jede sichtbare Überschrift auf einer Quartz-5-Seite kommt aus einem
> Komponenten-**[[7-nachschlagen/01-glossar#Plugin|Plugin]]**, und jedes dieser npm-Pakete bringt seine eigenen kompilierten
> Übersetzungen mit. Die Sprachdatei des Projekts erreicht sie nicht. Der Eintrag steht trotzdem
> in der Vorlage — der Mechanismus ist richtig, nur seine Reichweite ist heute klein.

> [!note] Rückverweise überschreiten die Sprachgrenze nicht
> Eine deutsche Seite verlinkt auf deutsche Seiten, eine englische auf englische; damit bleiben die
> beiden Listen getrennt. Das tut nicht das Plugin — es folgt daraus, dass jede Seite nur innerhalb
> ihres eigenen Baums verlinkt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 11 Variablen liest `aside-backlinks.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--icon-arrow-up-right` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 15 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
