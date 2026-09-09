---
title: Eigenschaften
description: Die Frontmatter-Tabelle unter dem Titel.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - ueber-dem-inhalt
translationKey: gestaltung/ueber-dem-inhalt/eigenschaften
---

## Von Haus aus

Eine schlichte Tabelle in Textfarbe, klappbar.

## In dieser Vorlage

- auf einer **getönten Fläche** mit Rahmen und runden Ecken
- die **Kopfzeile** versal, klein und gedämpft — sie ist Beschriftung, nicht Inhalt, und trägt
  seit dem 05.09.2026 keine Linie mehr unter sich: Eine zweite Waagerechte so dicht an der eigenen
  Kante der Box liest sich als Naht
- der **Schlüssel** gedämpft und so breit wie sein Text, der **Wert** nimmt den Rest
- **Werttypen** werden unterschieden: eine Zahl in Ziffernbreite, ein Wahrheitswert als
  eingefärbtes Wort, eine Liste als Reihe von Marken, ein leeres Feld kursiv

Zu sehen unter [[2-formatierung/11-eigenschaften/datentypen|Datentypen]], wo eine Seite alle vier Typen
mitbringt.

## Der Fund mit der Zellenbreite

Die naheliegende Lösung für „der Schlüssel ist so breit wie sein Inhalt" ist `width: 1%` auf der
Schlüsselzelle. Gemessen: Die Zelle wurde 7,94 px breit — exakt 1 % der Tabelle — und der Schlüssel
lag über dem Wert.

Der Weg, der funktioniert, ist der umgekehrte: **`width: 100%` auf die Wertzelle.** Sie beansprucht
alles, was übrig ist, und lässt dem Schlüssel seine Inhaltsbreite.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 16 Variablen liest `meta-note-properties.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 weitere Komponenten |
| `--tpl-positive` | `#136B34` · dunkel `#6DD68F` | nur hier |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
