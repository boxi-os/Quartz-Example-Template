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
`includedProperties` sieben Felder: `description`, `tags` und `section`, die jede Seite haben kann,
dazu `zahl`, `wahr`, `liste` und `leer` — die vier, die es nur hier und auf
[[formatierung/eigenschaften/datentypen|Datentypen]] gibt und die die vier Werttypen vorführen. Die
Tabelle oben zählt deshalb sieben.

Nicht angezeigt werden `falsch`, `aliases` und `translationKey`: Das erste ist im Frontmatter, aber
nicht in der Liste, die beiden anderen sind Technik und stünden auf fast jeder Seite.

Wer alle Felder sehen will, stellt in der App unter *Plugins → Note properties* die Option
`includeAll` auf wahr.

Siehe auch [[formatierung/eigenschaften/frontmatter|Eigenschaften]] in der Formatierungsreferenz.
