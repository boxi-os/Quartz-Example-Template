---
title: Wikilinks
description: Die Obsidian-Schreibweise für interne Verweise.
section: 2 – Formatierung
tags:
  - formatierung
  - links
translationKey: formatierung/links/wikilinks
cover: "[[assets/covers/cover-links.svg]]"
---

```md
[[2-formatierung/02-struktur/ueberschriften]]
[[2-formatierung/02-struktur/ueberschriften|mit eigenem Text]]
```

[[2-formatierung/02-struktur/ueberschriften]]
[[2-formatierung/02-struktur/ueberschriften|mit eigenem Text]]

## Kurzform

Solange der Dateiname im [[7-nachschlagen/01-glossar#Vault|Vault]] eindeutig ist, reicht er allein:

```md
[[ueberschriften]]
```

[[ueberschriften]]

Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Crawl links* löst den Pfad beim Bauen auf. Diese Vorlage steht auf
`markdownLinkResolution: shortest` — die kürzeste eindeutige Schreibweise gewinnt.

> [!note] Zwei Sprachen, zwei Dateinamen
> Das ist einer der Gründe, warum die englischen Seiten englische Dateinamen tragen: `headings`
> findet die englische Seite, `ueberschriften` die deutsche. Hätten beide Sprachen dieselben Namen,
> wäre die Kurzform mehrdeutig geworden — siehe
> [[6-anpassen/07-zwei-sprachen/index|Zwei Sprachen]].

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
