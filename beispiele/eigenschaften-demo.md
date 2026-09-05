---
title: Viele Eigenschaften
description: Eine Seite mit vollem Frontmatter, um die Eigenschaften-Tabelle zu zeigen.
section: Beispiele
date: 2026-07-02
lastmod: 2026-09-01
tags:
  - beispiele
  - frontmatter
  - referenz
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
translationKey: beispiele/eigenschaften-demo
---

Diese Seite trägt mehr Frontmatter, als angezeigt wird. Die Vorlage listet in
`includedProperties` dreizehn Felder: `description`, `tags` und `section`, die jede Seite haben
kann, dazu die fünf Demofelder — `zahl`, `wahr`, `falsch`, `liste`, `leer` — und noch einmal
dieselben fünf mit englischen Namen, weil die englische Fassung dieser Seite sie so nennt. Ein Feld,
das eine Seite nicht hat, bekommt keine Zeile; die Tabelle oben zählt deshalb acht.

Nicht angezeigt werden `aliases` und `translationKey`: Beide sind Technik und stünden auf fast jeder
Seite.

Wer alle Felder sehen will, stellt in der App unter *Plugins → Note properties* die Option
`includeAll` auf wahr.

Siehe auch [[formatierung/eigenschaften/frontmatter|Eigenschaften]] in der Formatierungsreferenz.
