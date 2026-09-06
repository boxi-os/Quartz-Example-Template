---
title: 5 Die Gestaltung
description: Was Quartz von Haus aus tut, und was diese Vorlage daran ändert — je Komponente.
section: Gestaltung
tags:
  - gestaltung
translationKey: gestaltung/index
---

Jede Seite in diesem Bereich behandelt **eine** Komponente und hat zwei Absätze:

> **Von Haus aus** — was Quartz ohne Zutun macht.
> **In dieser Vorlage** — was hier anders ist, und warum.

Der Vergleich steht direkt bei dem Element, das man dabei ansieht. Eine gesammelte Liste aller
Unterschiede gäbe es zwar auch, aber sie wäre weit weg von der Sache.

## Die Bereiche

| Bereich | Komponenten |
| --- | --- |
| [[6-anpassen/02-farben-und-kontrast\|Grundlagen]] | Farben, Schriften, Tokens, Frames, Barrierefreiheit, Anpassen |
| [[5-gestaltung/01-navigation/explorer\|Navigation]] | Explorer, Suche, Farbschema, Lesemodus, Kopfbereich, Fußzeile |
| [[5-gestaltung/04-neben-dem-inhalt/inhaltsverzeichnis\|Seitenapparat]] | Inhaltsverzeichnis, Rückverweise, Graph, zuletzt geändert |
| [[5-gestaltung/02-ueber-dem-inhalt/brotkrumen\|Über dem Inhalt]] | Brotkrumen, Titel, Datum, Eigenschaften, Tags |
| [[5-gestaltung/03-im-inhalt/fliesstext\|Im Inhalt]] | Fließtext, Callouts, Code, Tabellen, Medien |
| [[5-gestaltung/06-erzeugte-seiten/ordner-und-tags\|Seitentypen]] | Ordner- und Tag-Listen, Vorschau, Suche, Fehlerseite |
| [[5-gestaltung/05-layout-boxen/index\|Layout-Box]] | Das eigene Plugin in fünf Ausprägungen |
| [[6-anpassen/07-zwei-sprachen/index\|Zwei Sprachen]] | Erkennung, Verknüpfung, Umschalter — und wo es aufhört |

## Die drei Entscheidungen, die alles andere tragen

1. **Die Breite entscheidet das Raster** — der Frame, an einer Stelle, nicht zusätzlich der Absatz.
2. **Farben sind gemessen.** 87 Paare, alle über der WCAG-Schwelle, in beiden Modi.
3. **Farbe und Maß stehen nicht in den Stylesheets**, sondern in 53 Variablen, die in der App
   bearbeitbar bleiben. Was doch literal dasteht, ist benannt und begründet.
