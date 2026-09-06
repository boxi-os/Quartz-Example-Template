---
title: 4.4 Eigene Felder
description: Frontmatter-Felder, die Quartz nicht kennt — und wie die Eigenschaften-Tabelle sie zeigt.
section: 4 Eine Seite steuern
date: 2026-07-02
lastmod: 2026-09-01
tags:
  - seiten-steuern
  - frontmatter
aliases:
  - Frontmatter-Demo
zahl: 42
wahr: true
falsch: false
liste:
  - eins
  - zwei
  - drei
leer:
translationKey: seiten-steuern/eigene-felder
---

Ein [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]] darf Felder enthalten, die Quartz nicht kennt. Sie stören nicht, und sie sind
nützlich: Obsidian kann nach ihnen suchen und sortieren, eine [[7-nachschlagen/01-glossar#Base|Base]] kann nach ihnen filtern, und das
[[7-nachschlagen/01-glossar#Plugin|Plugin]] *Note properties* zeigt sie in einer Tabelle unter dem Titel — so wie oben auf dieser Seite.

## Was diese Seite trägt

Sie hat mehr Frontmatter, als angezeigt wird. Die Vorlage listet beim Plugin unter
`includedProperties` dreizehn Felder: `description`, `tags` und `section`, die jede Seite haben
kann, dazu die fünf Demofelder — `zahl`, `wahr`, `falsch`, `liste`, `leer` — und noch einmal
dieselben fünf mit englischen Namen, weil die englische Fassung dieser Seite sie so nennt. Ein
Feld, das eine Seite nicht hat, bekommt keine Zeile; die Tabelle oben zählt deshalb acht.

Die fünf Demofelder gibt es, damit jede Art von Wert einmal vorkommt: eine Zahl, ein Ja, ein Nein,
eine Liste, ein leeres Feld. Wie die Tabelle jede davon anders darstellt, steht in
[[5-gestaltung/02-ueber-dem-inhalt/eigenschaften|Eigenschaften]].

Nicht angezeigt werden `aliases` und `translationKey`: Beide sind Technik und stünden auf fast
jeder Seite.

## `section` — das eigene Feld dieser Website

Jede Seite hier trägt `section` mit dem Namen ihres Kapitels. Quartz kennt das Feld nicht. Es
erscheint in der Eigenschaften-Tabelle, die Base [[7-nachschlagen/Alle Seiten.base|Alle Seiten]] gruppiert
danach, und eine [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]] könnte es als Platzhalter `{{frontmatter.section}}` einsetzen.

## Alle Felder zeigen

Wer alle Felder sehen will, stellt in QuartzControl unter *Plugins → Note properties* die Option
`includeAll` auf wahr. Dann erscheinen auch [[7-nachschlagen/01-glossar#Alias|Aliase]] und Übersetzungsschlüssel.

Wie man Felder *schreibt* und welche Datentypen es gibt:
[[2-formatierung/11-eigenschaften/index|2.11 Eigenschaften]].
