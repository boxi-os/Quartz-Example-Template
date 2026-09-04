---
title: Code
description: Inline, Blöcke, Sprachlabel und der Kopierknopf.
section: Gestaltung
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

Sie ist seit dem 05.09.2026 **heller als die übrige Tönung** und hat dafür einen eigenen Token
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

> [!warning] Eine Farbe des Syntax-Themas bleibt unter der Schwelle
> Das Orange von `github-light`, mit dem CSS-Variablennamen gesetzt werden, erreicht auch auf der
> helleren Fläche nur 3,04 : 1 statt der 4,5 : 1, die WCAG für Text verlangt. Das ist keine Folge
> dieser Änderung — vorher waren es 2,54 : 1 —, aber es ist die eine Stelle dieser Vorlage, an der
> eine sichtbare Farbe nicht gemessen bestanden hat. Heilen ließe sie sich nur, indem man das
> Syntax-Thema wechselt oder diesen einen Token überschreibt.

Lange Zeilen brechen nicht um, sondern scrollen im Block.

## Das Sprachlabel

Oben links steht die Sprache — als `::after` im Stylesheet, nicht als Element. Es landet damit
nicht in einer Kopie und nicht in der Vorlesereihenfolge.

## Der Kopierknopf

**Von Haus aus** erscheint er nur beim Überfahren mit dem Zeiger — auf einem Telefon ist er damit
unerreichbar.

**In dieser Vorlage** erscheint er bei Hover, **bei Fokus** und **dauerhaft auf Geräten ohne
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
