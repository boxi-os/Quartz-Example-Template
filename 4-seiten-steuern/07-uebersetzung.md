---
title: 4.7 Übersetzung
description: Die Felder, die eine Seite mit ihrer Übersetzung verbinden — translationKey, aliases, lang — und wann man sie braucht.
section: 4 Eine Seite steuern
tags:
  - seiten-steuern
  - mehrsprachigkeit
translationKey: seiten-steuern/uebersetzung
---

Diese Website gibt es auf Deutsch und Englisch. Damit der Umschalter oben rechts von einer Seite zu
ihrer Übersetzung findet, müssen beide sagen, dass sie zusammengehören. Das geschieht im
[[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]] — auf drei Wegen, von denen man meist nur den ersten braucht.

## `translationKey` — der Normalfall

```yaml
---
title: Betonung
translationKey: formatierung/text/betonung
---
```

Zwei Seiten mit demselben Schlüssel sind Übersetzungen voneinander. Der Schlüssel ist frei
wählbar; dieses Handbuch nimmt den deutschen Pfad ohne die Kapitelnummern, weil er eindeutig ist
und man der Zeile ansieht, worauf sie zeigt. So sind alle regulären Seiten hier verbunden.

## `aliases` — der Weg über den Titel

Ein [[7-nachschlagen/01-glossar#Alias|Alias]], der dem Titel oder Dateinamen der Seite in der anderen Sprache entspricht, verbindet die
beiden ebenfalls. Das Obsidian-Plugin *Multilingual* schreibt solche Aliase automatisch. Drei
Seiten dieser Website hängen absichtlich nur daran, um den Weg vorzuführen.

## Gleicher Pfad

Zwei Seiten, deren Pfad ohne den Sprachordner gleich ist, gehören zusammen. Das trifft hier nur
auf die beiden Startseiten zu: `index.md` und `en/index.md`.

## `lang` — die Sprache einer Seite

Die Sprache erkennt das [[7-nachschlagen/01-glossar#Plugin|Plugin]] am Ordner: Was unter `en/` liegt, ist englisch; alles andere fällt
in die Standardsprache Deutsch. Ein Feld `lang` braucht man nur, wenn eine Seite anders liegt, als
sie spricht.

Wie das im Einzelnen funktioniert, mit den gemessenen Zahlen und den Grenzen:
[[6-anpassen/07-zwei-sprachen/index|6.7 Zwei Sprachen]].
