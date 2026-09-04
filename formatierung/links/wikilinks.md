---
title: Wikilinks
description: Die Obsidian-Schreibweise für interne Verweise.
section: Formatierung
tags:
  - formatierung
  - links
translationKey: formatierung/links/wikilinks
---

```md
[[formatierung/struktur/ueberschriften]]
[[formatierung/struktur/ueberschriften|mit eigenem Text]]
```

[[formatierung/struktur/ueberschriften]]
[[formatierung/struktur/ueberschriften|mit eigenem Text]]

## Kurzform

Solange der Dateiname im Vault eindeutig ist, reicht er allein:

```md
[[ueberschriften]]
```

[[ueberschriften]]

Das Plugin *Crawl links* löst den Pfad beim Bauen auf. Diese Vorlage steht auf
`markdownLinkResolution: shortest` — die kürzeste eindeutige Schreibweise gewinnt.

> [!note] Zwei Sprachen, zwei Dateinamen
> Das ist einer der Gründe, warum die englischen Seiten englische Dateinamen tragen: `headings`
> findet die englische Seite, `ueberschriften` die deutsche. Hätten beide Sprachen dieselben Namen,
> wäre die Kurzform mehrdeutig geworden — siehe
> [[gestaltung/mehrsprachigkeit/index|Zwei Sprachen]].

## Ein Link ins Leere

```md
[[gibt-es-nicht]]
```

[[gibt-es-nicht]]

Ein Wikilink auf eine Seite, die es nicht gibt, bleibt ein Link. In Obsidian erkennt man ihn an der
blassen Farbe; auf der gebauten Website führt er ins Nichts. Vor dem Veröffentlichen lohnt sich in
Obsidian der Blick in die Liste der nicht aufgelösten Links.

## In dieser Vorlage

**Von Haus aus** färbt Quartz interne Links in der Sekundärfarbe, ohne Unterstreichung.

**In dieser Vorlage** sind sie zusätzlich unterstrichen — eine Farbe allein ist für einen Teil der
Leser kein Hinweis darauf, dass etwas anklickbar ist. Die Unterstreichung sitzt tiefer als üblich
(`text-underline-offset`) und ist halbtransparent, damit sie die Unterlängen nicht zerschneidet.
