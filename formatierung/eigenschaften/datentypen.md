---
title: Datentypen
description: Text, Zahl, Wahrheitswert, Liste — und wie sie angezeigt werden.
section: Formatierung
tags:
  - formatierung
  - frontmatter
zahl: 42
wahr: true
falsch: false
liste:
  - eins
  - zwei
  - drei
leer:
translationKey: formatierung/eigenschaften/datentypen
---

Diese Seite trägt selbst fünf Beispielfelder. Die Eigenschaften-Tabelle über diesem Text zeigt sie.

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

| Typ | Schreibweise | Anzeige in dieser Vorlage |
| --- | --- | --- |
| Text | `feld: Wert` | wie er ist |
| Zahl | `zahl: 42` | in Ziffernbreite (`tabular-nums`) |
| Wahrheitswert | `wahr: true` / `falsch: false` | als Wort — wahr in der Positiv-Farbe, falsch gedämpft |
| Liste | Einträge mit `-` | als Reihe von Marken |
| Leer | `leer:` | kursiv und gedämpft |
| Datum | `date: 2026-09-01` | nach Gebietsschema formatiert |

## Was angezeigt wird, entscheidet die Konfiguration

Das Plugin *Note properties* zeigt standardmäßig nicht alles, sondern nur die Felder aus
`includedProperties`. Diese Vorlage listet dort `description`, `tags`, `section` und die fünf
Demofelder dieser Seite — in beiden Sprachen, weil die englische Fassung sie englisch benennt. Ein Feld, das eine Seite nicht hat, bekommt keine Zeile.
