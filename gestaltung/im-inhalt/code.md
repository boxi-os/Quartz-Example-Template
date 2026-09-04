---
title: Code
description: Inline, Blöcke, Sprachlabel und der Kopierknopf.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
  - code
---

## Inline

**Von Haus aus** ein Kasten mit Rahmen. **In dieser Vorlage** eine Tönung ohne Rahmen — genug zur
Trennung, zu wenig zur Unterbrechung. Etwas kleiner gesetzt (0.9em), weil JetBrains Mono neben
Inter sonst zu groß wirkt.

## Blöcke

Die Fläche kommt von der Vorlage, nicht vom Syntax-Thema: `keepBackground: false` sorgt dafür, dass
shiki nur die Zeichenfarben setzt. Nur so passt der Block in beiden Farbschemata.

Der Block ist vom Lesemaß ausgenommen und scrollt bei langen Zeilen in sich selbst.

## Das Sprachlabel

Oben links steht die Sprache — als `::after` im Stylesheet, nicht als Element. Es landet damit
nicht in einer Kopie und nicht in der Vorlesereihenfolge.

## Der Kopierknopf

**Von Haus aus** erscheint er nur beim Überfahren mit dem Zeiger — auf einem Telefon ist er damit
unerreichbar.

**In dieser Vorlage** erscheint er bei Hover, **bei Fokus** und **dauerhaft auf Geräten ohne
Zeiger** (`@media (hover: none)`). Er misst 44 px, während das Symbol darin klein bleibt. Versteckt
wird er über `opacity`, nie über `display` — sonst wäre er für die Tastatur gar nicht da.

## Hervorgehobene Zeilen

Fläche **und** Balken links. Eine Tönung allein ist auf einem ohnehin getönten Block zu schwach.
