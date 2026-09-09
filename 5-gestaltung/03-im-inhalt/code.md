---
title: Code
description: Inline, Blöcke, Sprachlabel und der Kopierknopf.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - im-inhalt
  - code
translationKey: gestaltung/im-inhalt/code
---

## Inline

**Von Haus aus** ein Kasten mit Rahmen. **In dieser Vorlage** eine Tönung ohne Rahmen — genug zur
Trennung, zu wenig zur Unterbrechung. Etwas kleiner gesetzt (0.9em), weil JetBrains Mono neben
Inter sonst zu groß wirkt.

## Blöcke

Die Fläche kommt von der Vorlage, nicht vom Syntax-Thema: `keepBackground: false` sorgt dafür, dass
shiki nur die Zeichenfarben setzt. Nur so passt der Block in beiden Farbschemata.

Sie ist seit dem 05.09.2026 **heller als die übrige Tönung** und hat dafür einen eigenen [[7-nachschlagen/01-glossar#Token|Token]]
(`--tpl-surface-code`, hell `#F1EFE9`, dunkel weiter `lightgray`). Ein Block ist eine große Fläche,
und die Tönung, die für ein Wort Inline-Code richtig ist, macht aus zwanzig Zeilen eine graue
Platte. Gemessen, was das bringt:

| Farbe | auf der alten Fläche | auf der neuen |
| --- | --- | --- |
| Text (`#24292E`) | 10,69 : 1 | 12,76 : 1 |
| Blau (`#005CC5`) | 4,59 : 1 | 5,47 : 1 |
| Violett (`#6F42C1`) | 4,75 : 1 | 5,66 : 1 |
| Orange (`#E36209`) | 2,54 : 1 | 3,04 : 1 |

Bezahlt wird das mit Trennung: Die Fläche steht jetzt nur noch 1,12 : 1 gegen den Seitengrund statt
1,34 : 1. Deshalb bekommt der Block seinen Rahmen aus `--tpl-rule` — genau der Farbe, die vorher
seine Füllung war.

## Fünf Farben des Syntax-Themas sind korrigiert

Der hellere Grund reichte nicht. Gezählt wurde deshalb über die **ganze gebaute Site**: jeder
`--shiki-light`- und `--shiki-dark`-Wert auf allen 333 Seiten, mit seiner Häufigkeit und seinem
[[7-nachschlagen/01-glossar#Kontrast|Kontrast]] gegen die Codefläche. Fünf Paare fielen durch:

| Farbe | wofür | vorher | jetzt |
| --- | --- | --- | --- |
| `#22863A` hell | Zeichenketten, Tags (206×) | 4,02 : 1 | `#1F7A35` — 4,69 : 1 |
| `#D73A49` hell | Schlüsselwörter (112×) | 3,98 : 1 | `#CA2938` — 4,70 : 1 |
| `#E36209` hell | Konstanten, CSS-Variablen (82×) | 3,04 : 1 | `#B04C07` — 4,70 : 1 |
| `#6A737D` hell | Kommentare (4×) | 4,19 : 1 | `#636B74` — 4,70 : 1 |
| `#6A737D` dunkel | Kommentare (4×) | 2,74 : 1 | `#949CA4` — 4,74 : 1 |

Jede Korrektur behält Farbton und Sättigung und ändert nur die Helligkeit — `github-light` liest
sich weiterhin als `github-light`. Es ist dasselbe, was diese Vorlage mit Quartz' Callout-Farben
tut.

Geprüft werden sie seitdem bei jedem Lauf: `--check-contrast` liest die fünf Werte aus
`body-code.scss` und misst sie gegen `--tpl-surface-code`. Aus 78 Paaren sind 83 geworden; mit dem dreizehnten [[7-nachschlagen/01-glossar#Callout|Callout]], der seit dem 05.09.2026 nicht mehr übersprungen wird, sind es 87.

> [!note] Wie das technisch geht
> shiki schreibt die Farbe **inline an jedes einzelne `<span>`**
> (`style="--shiki-light:#E36209;--shiki-dark:#FFAB70;"`), und eine Inline-Deklaration schlägt jede
> Autorenregel, die nicht `!important` ist. Überschrieben wird deshalb die *Variable*, nicht
> `color` — dann macht Quartz' eigene Hell-Dunkel-Umschaltung weiter, was sie soll.
>
> Was das nicht abdeckt: eine Sprache, deren Tokens eine zehnte Farbe erzeugen, käme ungemessen
> herein. Die Zählung ist wiederholbar — `--shiki-light:` aus `public/` greppen.

Lange Zeilen brechen nicht um, sondern scrollen im Block.

## Das Sprachlabel

Oben links steht die Sprache — als `::after` im [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]], nicht als Element. Es landet damit
nicht in einer Kopie und nicht in der Vorlesereihenfolge.

## Der Kopierknopf

**Von Haus aus** erscheint er nur beim Überfahren mit dem Zeiger — auf einem Telefon ist er damit
unerreichbar.

**In dieser Vorlage** erscheint er bei [[7-nachschlagen/01-glossar#Hover|Hover]], **bei Fokus** und **dauerhaft auf Geräten ohne
Zeiger** (`@media (hover: none)`). Er misst 44 px, während das Symbol darin klein bleibt. Versteckt
wird er über `opacity`, nie über `display` — sonst wäre er für die Tastatur gar nicht da.

Und er ist **nur das Symbol**: kein Rahmen, keine Fläche. Sein Zustand ist die Farbe des Symbols,
von `gray` auf `dark`.

> [!bug] Die Ausnahme von der Schichtungsregel
> „Alles in `custom.scss` steht ungeschichtet und gewinnt deshalb gegen die Plugin-Stile" — für
> Komponenten-CSS stimmt das, für **Ressourcen-Stylesheets** nicht. Quartz liefert die Gestaltung
> dieses Knopfes in `static/resource-style-….css` aus, ungeschichtet und *nach* `index.css`
> verlinkt. Bei gleicher Spezifität gewinnt damit die spätere Regel:
>
> ```css
> .clipboard-button { float: right; border: 1px solid; border-color: var(--dark);
>                     background-color: var(--light); margin: .3rem; padding: .4rem }
> ```
>
> Gemessen an der gebauten Seite: Der Knopf meldete weiterhin einen 1-px-Rahmen und `--light`
> dahinter, obwohl jede Regel dieser Vorlage `border: none` und `background: transparent` sagte.
> Ein Nachfahre im Selektor (`pre .clipboard-button`) entscheidet es.

## Hervorgehobene Zeilen

Fläche **und** Balken links. Eine Tönung allein ist auf einem ohnehin getönten Block zu schwach.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 22 Variablen liest `body-code.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 weitere Komponenten |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 weitere Komponenten |
| `--tpl-surface-code` | `color-mix(in srgb, var(--lightgray) 40%, …` · dunkel `var(--lightgray)` | nur hier |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-caps` | `0.06em` | 6.4 Variablen, 3.1 Bases |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
