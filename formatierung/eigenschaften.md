---
title: Eigenschaften
description: Frontmatter — welche Felder Quartz auswertet und wie sie angezeigt werden.
section: Formatierung
tags:
  - referenz
  - formatierung
  - frontmatter
---

Das Frontmatter steht ganz oben in der Datei, zwischen zwei Zeilen aus drei Bindestrichen.

````md
---
title: Eigenschaften
description: Eine kurze Beschreibung für Vorschau und Suchergebnis.
tags:
  - referenz
  - formatierung
date: 2026-09-01
lastmod: 2026-09-04
aliases:
  - Frontmatter
  - Properties
draft: false
---
````

## Was Quartz damit macht

| Feld | Wirkung |
| ---- | ------- |
| `title` | Seitentitel, Browsertitel, Beschriftung in Listen und Suche |
| `description` | Vorschautext in Suche, Listen und beim Teilen |
| `tags` | Tag-Liste unter dem Titel, Tag-Seiten, Verweise |
| `date` / `lastmod` | Datum unter dem Titel und Sortierung in „Zuletzt geändert“ |
| `aliases` | Weiterleitungen von anderen Pfaden auf diese Seite |
| `draft: true` | Die Seite wird nicht gebaut |
| `unlisted: true` | Die Seite wird gebaut, taucht aber in keiner Liste auf |

## Anzeige

Die Eigenschaften-Tabelle unter dem Titel zeigt in dieser Vorlage nur drei Felder: `description`,
`tags` und `section`. Alles andere wäre auf jeder Seite dieselbe Wiederholung dessen, was ohnehin
darüber steht.

Eingestellt wird das an der Option `includedProperties` des Plugins *Note properties*.

## Datentypen

Die Anzeige unterscheidet Typen: eine Zahl steht in Ziffernbreite, ein Wahrheitswert als Wort,
eine Liste als Reihe von Marken, ein leeres Feld kursiv.

````md
---
zahl: 42
wahr: true
falsch: false
liste:
  - eins
  - zwei
leer:
---
````

## Tags im Text

Tags müssen nicht im Frontmatter stehen:

```md
Ein Satz mit einem #inline-tag mittendrin.
```

Ein Satz mit einem #inline-tag mittendrin.

Im Fließtext verliert ein Tag seine Pillenform und behält nur die Farbe — ein Absatz voller Pillen
ist nicht lesbar.
