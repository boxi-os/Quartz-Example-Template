---
title: Betonung
description: Fett, kursiv, durchgestrichen, hervorgehoben — und welches Plugin welches davon liefert.
section: 2 Formatierung
tags:
  - formatierung
  - text
translationKey: formatierung/text/betonung
cover: "[[assets/covers/cover-text.svg]]"
---

## Die fünf Auszeichnungen

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

## Wer was liefert

Zwei der fünf kommen nicht aus [[7-nachschlagen/01-glossar#Markdown|Markdown]] selbst:

| Auszeichnung | Kommt von | Ohne das [[7-nachschlagen/01-glossar#Plugin\|Plugin]] |
| --- | --- | --- |
| `~~durchgestrichen~~` | GitHub Flavored Markdown | bleibt als Rohtext stehen |
| `==hervorgehoben==` | Obsidian Flavored Markdown | bleibt als Rohtext stehen |

Beide sind in dieser Vorlage aktiv. Die Hervorhebung nimmt dabei die Farbe `textHighlight` aus der
Palette — nachzulesen unter [[5-gestaltung/03-im-inhalt/fliesstext|Fließtext]].

## Innerhalb eines Wortes

```md
Ein Wort mit **innen**liegender Betonung, und ein Unter_strich_ mitten im Wort.
```

Ein Wort mit **innen**liegender Betonung, und ein Unter_strich_ mitten im Wort.

Der Unterstrich mitten im Wort wird bewusst *nicht* als Kursivsetzung gelesen — sonst würden
`snake_case_namen` ständig zerfallen.

## Hoch- und tiefgestellt

Markdown kennt beides nicht; Quartz lässt [[7-nachschlagen/01-glossar#HTML|HTML]] durch:

```md
H<sub>2</sub>O und E = mc<sup>2</sup>
```

H<sub>2</sub>O und E = mc<sup>2</sup>
