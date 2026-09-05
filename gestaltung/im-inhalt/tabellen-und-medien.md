---
title: Tabellen und Medien
description: Zwei Elemente, die die Spalte sprengen wollen.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
translationKey: gestaltung/im-inhalt/tabellen-und-medien
---

## Tabellen

**Von Haus aus** rahmt Quartz die Tabelle und setzt Innenabstände direkt am Element.

**In dieser Vorlage** gibt es keine senkrechten Linien und keinen Außenrahmen: eine Haarlinie unter
jeder Zeile, eine kräftigere unter dem Kopf, und die letzte Zeile verliert ihre Linie. Der Kopf
steht in der Überschriftenschrift und bricht nicht um.

Das Scrollen liegt auf dem Container, den Quartz um jede Tabelle legt — **nicht auf der Tabelle
selbst.** Der naheliegende erste Versuch (`display: block; overflow-x: auto` auf dem `<table>`)
zerlegt das Tabellenlayout: Beim Bauen rutschten dadurch Schlüssel und Werte der
Eigenschaften-Tabelle übereinander.

## Bilder

Zarter Rahmen und runde Ecken. Ohne Rahmen sieht ein Bild mit weißem Hintergrund auf dem warmen
Grund dieser Seite wie ein Loch aus.

Eine ausdrücklich gesetzte Breite (`![[bild.png|300]]`) bleibt erhalten; die Vorlage begrenzt nur
nach oben.

## Einbettungen

Ein `iframe` bekommt `aspect-ratio: 16/9`. Ohne diese Regel fällt es in einer Grid-Zelle auf null
Höhe zusammen — was genau dann passiert, wenn die Seite ein eigenes Raster verwendet, also in dieser
Vorlage überall.

## Transkludierte Notizen

Gestrichelter Balken und getönte Fläche: Man soll sehen, wo fremder Inhalt anfängt und aufhört.
**Von Haus aus** ist eine Einbettung optisch nicht vom umgebenden Text getrennt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 12 Variablen liest `body-media.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 21 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
