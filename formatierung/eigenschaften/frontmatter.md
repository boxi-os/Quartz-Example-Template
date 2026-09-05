---
title: Frontmatter
description: Die Felder ganz oben in der Datei und was Quartz damit macht.
section: Formatierung
tags:
  - formatierung
  - frontmatter
translationKey: formatierung/eigenschaften/frontmatter
---

Zwischen zwei Zeilen aus drei Bindestrichen, ganz am Anfang der Datei:

````md
---
title: Frontmatter
description: Eine kurze Beschreibung für Vorschau und Suchergebnis.
tags:
  - formatierung
  - frontmatter
date: 2026-09-01
lastmod: 2026-09-04
aliases:
  - Properties
draft: false
---
````

## Was Quartz auswertet

| Feld | Wirkung |
| ---- | ------- |
| `title` | Seitentitel, Browsertitel, Beschriftung in Listen und Suche |
| `description` | Vorschautext in Suche, Listen und beim Teilen |
| `tags` | Tag-Liste unter dem Titel, Tag-Seiten, Verweise |
| `date` / `lastmod` | Datum unter dem Titel, Sortierung in „Zuletzt geändert" |
| `aliases` | Weiterleitungen von anderen Pfaden — siehe [[formatierung/links/aliase\|Aliase]] |
| `draft: true` | Die Seite wird gar nicht erst gebaut |
| `unlisted: true` | Die Seite wird gebaut, taucht aber in keiner Liste auf |
| `translationKey` | Bindet die Seite an ihre Übersetzung — siehe [[gestaltung/mehrsprachigkeit/verknuepfung\|Wie die Sprachen sich finden]] |

## Woher das Datum kommt

Ohne `date` im Frontmatter nimmt Quartz das Datum aus git — und ohne git aus dem Dateisystem.
Eingestellt wird die Reihenfolge beim Plugin *Created modified date*; diese Vorlage nutzt
`frontmatter → filesystem` und lässt git aus, weil es hier nichts beantworten kann — warum, steht
unter [[gestaltung/ueber-dem-inhalt/titel-und-datum|Titel und Datum]].

> [!tip] Eigene Felder sind erlaubt
> Ein Feld, das Quartz nicht kennt, stört nicht. Diese Vorlage nutzt zum Beispiel `section` — für
> die Anzeige in den Eigenschaften und für einen Platzhalter in der Layout-Box.
