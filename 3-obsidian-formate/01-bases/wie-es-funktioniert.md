---
title: Wie eine Base aufgebaut ist
description: Filter, Formeln und Ansichten — das YAML-Format erklärt.
section: 3 Obsidian-Formate
tags:
  - obsidian-formate
  - bases
aliases:
  - How a base is built
---

Eine `.base`-Datei hat bis zu drei Abschnitte:

```yaml
filters:
  and:
    - file.hasTag("formatierung")
    - file.ext == "md"

formulas:
  Bereich: file.folder

views:
  - type: table
    name: Alle Formatierungsseiten
    order:
      - file.name
      - description
      - formula.Bereich
    sort:
      - property: file.name
        direction: ASC
```

## filters

Welche Notizen aufgenommen werden. Verknüpft mit `and`, `or` und `not`. Häufige Ausdrücke:

| Ausdruck | Bedeutung |
| --- | --- |
| `file.hasTag("x")` | trägt diesen Tag |
| `file.inFolder("x")` | liegt in diesem Ordner |
| `file.ext == "md"` | ist eine Markdown-Datei |
| `eigenschaft != null` | Feld ist gesetzt |

## formulas

Berechnete Spalten. Sie stehen danach als `formula.Name` zur Verfügung — praktisch, um zwei Felder
zusammenzuziehen oder einen Pfad zu kürzen.

## views

Eine Base kann mehrere Ansichten derselben Daten haben. Das Quartz-Plugin kennt `table`, `list`,
`cards`, `board` und `gallery`; die Voreinstellung ist `table`.

| Schlüssel | Wirkung |
| --- | --- |
| `type` | Ansichtsart |
| `name` | Beschriftung der Ansicht |
| `order` | welche Spalten, in welcher Reihenfolge |
| `sort` | Sortierung, mit `property` und `direction` |
| `groupBy` | Gruppierung nach einem Feld |
| `limit` | Höchstzahl der Einträge |

## Wo man das bearbeitet

In Obsidian gibt es dafür eine Oberfläche — die YAML-Datei ist nur die Ablage. Wer sie von Hand
schreibt, sollte sie danach in Obsidian öffnen und prüfen.


## Verlinken

Ein [[7-nachschlagen/01-glossar#Wikilink|Wikilink]] auf eine solche Datei braucht die **Endung**:

```md
[[3-obsidian-formate/01-bases/Formatierungsseiten.base|Formatierungsseiten]]
[[3-obsidian-formate/02-canvas/Aufbau der Vorlage.canvas|Aufbau der Vorlage]]
```

Quartz behält die Endung im Adressteil der Seite (`…/formatierungsseiten.base`), anders als bei
Markdown-Dateien. Ohne sie geht der Link ins Leere — und das fällt nicht auf, weil ein
unaufgelöster Wikilink hier keine besondere Auszeichnung bekommt.
