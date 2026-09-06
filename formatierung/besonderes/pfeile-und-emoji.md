---
title: Pfeile, Tags und Emoji
description: Kleinigkeiten, die Obsidian im Vorbeigehen umwandelt.
section: Formatierung
tags:
  - formatierung
  - besonderes
translationKey: formatierung/besonderes/pfeile-und-emoji
cover: "[[assets/covers/cover-besonderes.svg]]"
---

## Pfeile

Obsidian wandelt Zeichenfolgen wie `-->` in echte Pfeile. Die Option dafür heißt `parseArrows` und
steht in dieser Vorlage auf `true`. Die Zeile darunter zeigt, was daraus wird:

```md
--> und <-- und <--> und ==>
```

--> und <-- und <--> und ==>

> [!failure] Auf der Website wird daraus keiner
> Gemessen an der gebauten Seite steht dort `—> und <— und <—> und ==>`. Zwei Dinge gehen dabei
> schief, und zwar unabhängig voneinander:
>
> 1. **`parseArrows` wandelt nichts.** Gegenprobe mit abgeschaltetem *GitHub flavored markdown*:
>    Dann steht dort `--> und <-- und <--> und ==>`, also weiterhin der Rohtext. Die Option ist
>    gesetzt und bleibt wirkungslos.
> 2. **Der Bindestrich-Ersatz kommt trotzdem.** *GitHub flavored markdown* macht aus jedem `--`
>    einen Geviertstrich, bevor irgendjemand nach einem Pfeil sucht. Aus `-->` wird `—>`.
>
> In Obsidian sieht man Pfeile, auf der Website nicht. Wer einen Pfeil meint, schreibt ihn:
> → ← ↔ ⇒ — die Schriften dieser Vorlage zeichnen alle vier. Siehe
> [[formatierung/text/sonderzeichen|Sonderzeichen]].

## Tags im Text

```md
Ein Satz mit einem #inline-tag mittendrin.
```

Ein Satz mit einem #inline-tag mittendrin.

Ein Tag im Fließtext zählt genauso wie eines im Frontmatter: Es erscheint auf der Tag-Seite und in
der Tag-Liste.

> [!bug] Der Link daran ist kaputt
> Gemessen an der gebauten Seite trägt das Tag oben im Absatz das Ziel `../.././../tags/inline-tag`
> — ein `../` zu viel, der Pfad führt aus der Website heraus. Dasselbe Tag in der Liste unter dem
> Titel verlinkt daneben völlig richtig auf `../../tags/inline-tag`. Beide Links entstehen im
> selben Bau, nur an verschiedenen Stellen: `parseTags` im *Obsidian flavored markdown* rechnet den
> Weg zur Wurzel für ein Tag im Fließtext falsch. Ein Fehler in Quartz, nicht in dieser Vorlage.

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
