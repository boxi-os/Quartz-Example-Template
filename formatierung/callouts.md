---
title: Callouts
description: Alle dreizehn Typen, faltbar und verschachtelt — mit gemessenen Farben.
section: Formatierung
tags:
  - referenz
  - formatierung
  - callouts
---

## Aufbau

````md
> [!note] Ein eigener Titel
> Der Inhalt des Callouts.
````

> [!note] Ein eigener Titel
> Der Inhalt des Callouts.

Ohne Titel steht der Typ als Titel:

````md
> [!warning]
> Ohne eigenen Titel.
````

> [!warning]
> Ohne eigenen Titel.

## Alle Typen

> [!note] note
> Der Standardtyp.

> [!abstract] abstract
> Auch: `summary`, `tldr`.

> [!info] info
> Sachliche Ergänzung.

> [!todo] todo
> Was noch zu tun ist.

> [!tip] tip
> Auch: `hint`, `important`.

> [!success] success
> Auch: `check`, `done`.

> [!question] question
> Auch: `help`, `faq`.

> [!warning] warning
> Auch: `caution`, `attention`.

> [!failure] failure
> Auch: `fail`, `missing`.

> [!danger] danger
> Auch: `error`.

> [!bug] bug
> Ein Fehler im Programm.

> [!example] example
> Ein Beispiel.

> [!quote] quote
> Auch: `cite`. Nimmt die Akzentfarbe der Seite statt einer eigenen.

## Gemessene Farben

Quartz liefert für diese Typen zwölf Farben mit, von denen elf auf hellem Grund unter der
WCAG-Schwelle von 4,5:1 liegen — `note` erreicht 3,23:1, `question` 2,14:1. Das Rot von `danger`,
`failure` und `bug` scheitert in **beiden** Modi. Diese Vorlage setzt deshalb alle zwölf neu, je
Modus, und misst sie: gegen den Seitengrund und gegen die eigene getönte Fläche. Der Farbton bleibt
erhalten — Blau bleibt Blau —, damit der Typ weiterhin an der Farbe erkennbar ist.

## Faltbar

````md
> [!question]- Zugeklappt (Minus)
> Erscheint erst beim Aufklappen.

> [!question]+ Aufgeklappt (Plus)
> Beginnt offen, lässt sich zuklappen.
````

> [!question]- Zugeklappt (Minus)
> Erscheint erst beim Aufklappen.

> [!question]+ Aufgeklappt (Plus)
> Beginnt offen, lässt sich zuklappen.

## Verschachtelt

````md
> [!info] Außen
> Text im äußeren Callout.
>
> > [!tip] Innen
> > Der innere verliert seinen Rahmen, behält aber den Farbbalken.
````

> [!info] Außen
> Text im äußeren Callout.
>
> > [!tip] Innen
> > Der innere verliert seinen Rahmen, behält aber den Farbbalken.

## Mit weiterem Inhalt

````md
> [!example] Ein Callout kann alles enthalten
>
> 1. Eine Liste
> 2. Mit mehreren Punkten
>
> | Und | eine Tabelle |
> | --- | ------------ |
> | a   | b            |
>
> ```js
> const auch = "Code"
> ```
````

> [!example] Ein Callout kann alles enthalten
>
> 1. Eine Liste
> 2. Mit mehreren Punkten
>
> | Und | eine Tabelle |
> | --- | ------------ |
> | a   | b            |
>
> ```js
> const auch = "Code"
> ```
