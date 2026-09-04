---
title: Fußnoten — Grundform
description: Ein Verweis im Text, der Text am Seitenende.
section: Formatierung
tags:
  - formatierung
  - fussnoten
---

```md
Ein Satz mit einer Fußnote.[^1]

[^1]: Der Text der Fußnote, ganz unten auf der Seite.
```

Ein Satz mit einer Fußnote.[^1]

[^1]: Der Text der Fußnote, ganz unten auf der Seite.

## Was dabei passiert

Die hochgestellte Zahl im Text ist ein Sprunglink nach unten. Am Seitenende steht der Text, und
dahinter ein Pfeil, der zurück an die Stelle im Text führt. Beide Richtungen entstehen automatisch.

Die Definition darf überall in der Datei stehen — üblich ist direkt unter dem Absatz oder gesammelt
am Ende. Die Nummerierung in der Ausgabe folgt der Reihenfolge **im Text**, nicht der der
Definitionen.

## In dieser Vorlage

Der Fußnotenbereich ist durch eine Linie abgesetzt, kleiner gesetzt und gedämpft — er ist Apparat,
nicht Text. Eine angesprungene Fußnote wird kurz hervorgehoben, damit man beim Landen sieht, welche
gemeint war.

**Von Haus aus** steht der Bereich in derselben Größe wie der Fließtext und ohne Trennung.
