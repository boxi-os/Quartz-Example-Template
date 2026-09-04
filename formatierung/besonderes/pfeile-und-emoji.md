---
title: Pfeile, Tags und Emoji
description: Kleinigkeiten, die Obsidian im Vorbeigehen umwandelt.
section: Formatierung
tags:
  - formatierung
  - besonderes
---

## Pfeile

Das Plugin *Obsidian flavored markdown* wandelt Zeichenfolgen in echte Pfeile:

```md
--> und <-- und <--> und ==>
```

--> und <-- und <--> und ==>

## Tags im Text

```md
Ein Satz mit einem #inline-tag mittendrin.
```

Ein Satz mit einem #inline-tag mittendrin.

Ein Tag im Fließtext zählt genauso wie eines im Frontmatter: Es erscheint auf der Tag-Seite und in
der Tag-Liste.

**In dieser Vorlage** verliert ein Tag im Absatz seine Pillenform und behält nur die Farbe — ein
Absatz voller Pillen ist nicht lesbar. Unter dem Titel, wo die Tags gesammelt stehen, behalten sie
die Pille.

### Tags mit Ebenen

Ein Schrägstrich staffelt Tags:

```md
#bereich/unterbereich
```

Jede Ebene bekommt eine eigene Tag-Seite, und die übergeordnete sammelt die untergeordneten mit
ein. Gut für ein Vokabular, das wachsen soll — `#quelle/buch` und `#quelle/artikel` liegen dann
beide unter `#quelle`.

## Emoji

```md
Direkt eingefügt: 📐 ✓ ⚠️
```

Direkt eingefügt: 📐 ✓ ⚠️

> [!tip] Emoji sind kein Ersatz für Text
> Ein Screenreader liest „Warnschild" vor, nicht „Achtung". Als Schmuck neben einem Wort in
> Ordnung, als alleiniger Träger einer Information nicht.
