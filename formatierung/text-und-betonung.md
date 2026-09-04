---
title: Text und Betonung
description: Fett, kursiv, durchgestrichen, hervorgehoben — und was davon in Quartz ankommt.
section: Formatierung
tags:
  - referenz
  - formatierung
---

## Betonung

```md
*kursiv* oder _kursiv_
**fett** oder __fett__
***fett und kursiv***
~~durchgestrichen~~
==hervorgehoben==
```

*kursiv* oder _kursiv_
**fett** oder __fett__
***fett und kursiv***
~~durchgestrichen~~
==hervorgehoben==

> [!note] Zwei Plugins, ein Ergebnis
> `~~durchgestrichen~~` kommt aus GitHub Flavored Markdown, `==hervorgehoben==` aus Obsidian
> Flavored Markdown. Beide sind in dieser Vorlage aktiv; wäre eines aus, bliebe die Auszeichnung
> als Rohtext stehen.

## Innerhalb eines Wortes

```md
Ein Wort mit **innen**liegender Betonung, und ein Unter_strich_ mitten im Wort.
```

Ein Wort mit **innen**liegender Betonung, und ein Unter_strich_ mitten im Wort.

## Hoch- und tiefgestellt

Markdown selbst kennt beides nicht; Quartz lässt HTML durch.

```md
H<sub>2</sub>O und E = mc<sup>2</sup>
```

H<sub>2</sub>O und E = mc<sup>2</sup>

## Anführungszeichen und Gedankenstriche

```md
„Deutsche Anführungszeichen“ und »französische«, ein Gedankenstrich — so —
sowie drei Punkte …
```

„Deutsche Anführungszeichen“ und »französische«, ein Gedankenstrich — so —
sowie drei Punkte …

## Zeilenumbruch innerhalb eines Absatzes

Das Plugin *Hard line breaks* ist aktiv: ein einfacher Zeilenumbruch im Quelltext wird zu einem
Umbruch in der Ausgabe. Ohne dieses Plugin bräuchte es zwei Leerzeichen am Zeilenende.

```md
Erste Zeile
Zweite Zeile
```

Erste Zeile
Zweite Zeile
