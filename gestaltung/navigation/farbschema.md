---
title: Farbschema-Umschalter
description: Der Knopf zwischen hell und dunkel.
section: Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/farbschema
---

## Von Haus aus

Ein Knopf mit zwei Symbolen, von denen je nach Schema eines sichtbar ist.

## In dieser Vorlage

Er ist Teil der Werkzeugleiste im Kopfbereich und teilt deren Maße: 44 × 44 px, gleicher Rahmen,
gleiche Ecken wie Suche, Lesemodus und Sprachumschalter. Eine Reihe von Bedienelementen mit unterschiedlichen Höhen liest sich als
Fehler.

Beim Überfahren wechselt der Rand auf die Akzentfarbe und die Fläche auf die getönte Variante —
dieselbe Rückmeldung wie bei den beiden Nachbarn.

## Ein Fund beim Bauen

Die erste Fassung dieser Datei gestaltete ein `<input>`/`<label>`-Paar. Das gibt es hier nicht: Die
Komponente ist ein einzelner `<button class="darkmode">` mit zwei SVGs darin. Die Regeln trafen
nichts — sichtbar wurde das erst, als jeder Selektor der Vorlage gegen die gebaute Seite geprüft
wurde.

Daraus die Regel, die überall in dieser Vorlage gilt: **Vor dem Schreiben einer Regel im gebauten
HTML nachsehen.** Klassennamen sind kein Vertrag.
