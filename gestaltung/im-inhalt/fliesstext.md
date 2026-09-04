---
title: Fließtext
description: Das Lesemaß, die Überschriftenskala und die Links darin.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
---

## Das Lesemaß

**In dieser Vorlage** ist Fließtext auf **68 Zeichen** begrenzt. Tabellen, Codeblöcke, Diagramme,
Bilder und Formeln sind ausgenommen und dürfen die volle Spalte nehmen.

**Von Haus aus** begrenzt Quartz nicht den Text, sondern die Seite auf eine Pixelbreite. Bei einem
breiten Fenster wächst dadurch die Zeilenlänge.

> [!example] Der Fund dahinter
> Die Regel griff in der ersten Fassung **überhaupt nicht.** Gerendertes Markdown ist kein direktes
> Kind von `<article>`, sondern liegt in einem `<div class="markdown-preview-view">`. `article > p`
> traf damit nichts — und der Text sah trotzdem gut aus, weil die Spalte des Frames zufällig ungefähr
> passte. Gemessen: `max-width` war `none`, der Absatz 786 px breit. Jetzt sind es 686 px.

## Überschriften

Sechs Ebenen, aber nur vier Größen. Ebene 5 und 6 wechseln zu Versalien und Sperrung, weil ein
Unterschied von einem Pixel keine Information ist. Der Abstand liegt **über** der Überschrift, nie
darunter — die Lücke sagt, was zur Überschrift gehört.

## Links

Farbe **und** Unterstreichung. Die Unterstreichung ist halbtransparent und tief gesetzt, damit sie
die Unterlängen nicht zerschneidet; beim Überfahren wird sie deckend. Externe Links tragen einen
Pfeil.

## Zitate

Balken in der Akzentfarbe, getönte Fläche, aufrechter Text. **Von Haus aus** ist der Text kursiv —
über mehrere Zeilen liest sich das schlechter, und ein Zitat ist eine andere Stimme, kein anderer
Tonfall.

## Hervorhebung

`==markiert==` nimmt `textHighlight` — im hellen Modus ein warmes Gelb, im dunklen der Akzent mit
Transparenz. Beide sind gegen die Textfarbe gemessen.
