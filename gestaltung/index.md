---
title: Gestaltung
description: Was Quartz von Haus aus tut, und was diese Vorlage daran ändert — je Komponente.
section: Gestaltung
tags:
  - gestaltung
---

Jede Seite in diesem Bereich behandelt **eine** Komponente und hat zwei Absätze:

> **Von Haus aus** — was Quartz ohne Zutun macht.
> **In dieser Vorlage** — was hier anders ist, und warum.

Der Vergleich steht direkt bei dem Element, das man dabei ansieht. Eine gesammelte Liste aller
Unterschiede gäbe es zwar auch, aber sie wäre weit weg von der Sache.

## Die Bereiche

| Bereich | Komponenten |
| --- | --- |
| [[gestaltung/grundlagen/farben-und-kontrast\|Grundlagen]] | Farben, Schriften, Tokens, Frames, Barrierefreiheit |
| [[gestaltung/navigation/explorer\|Navigation]] | Explorer, Suche, Farbschema, Lesemodus, Kopfbereich |
| [[gestaltung/seitenapparat/inhaltsverzeichnis\|Seitenapparat]] | Inhaltsverzeichnis, Rückverweise, Graph, zuletzt geändert |
| [[gestaltung/ueber-dem-inhalt/brotkrumen\|Über dem Inhalt]] | Brotkrumen, Titel, Datum, Eigenschaften, Tags |
| [[gestaltung/im-inhalt/fliesstext\|Im Inhalt]] | Fließtext, Callouts, Code, Tabellen, Medien |
| [[gestaltung/seitentypen/ordner-und-tags\|Seitentypen]] | Ordner- und Tag-Listen, Vorschau, Suche, Fehlerseite |
| [[gestaltung/layout-box/index\|Layout-Box]] | Das eigene Plugin in fünf Ausprägungen |

## Die drei Entscheidungen, die alles andere tragen

1. **Die Breite entscheidet das Raster** — der Frame, an einer Stelle, nicht zusätzlich der Absatz.
2. **Farben sind gemessen.** 78 Paare, alle über der WCAG-Schwelle, in beiden Modi.
3. **Kein Stylesheet enthält eine Zahl.** Alles liest Variablen, die in der App bearbeitbar bleiben.
