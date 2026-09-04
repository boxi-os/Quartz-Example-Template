---
title: Inhaltsverzeichnis
description: Die Gliederung rechts — alle Ebenen, nicht nur drei.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
---

## Von Haus aus

Quartz zeigt die Überschriften einer Seite als flache Liste mit Einzug. **Die Voreinstellung ist
`maxDepth: 3`** — alles ab der vierten Überschriftenebene fehlt, und im Markup tauchen nur die
Tiefen 0 und 1 auf.

## In dieser Vorlage

`maxDepth` steht auf **6**. Damit erscheint jede Ebene bis `h6`; auf einer normalen Seite sind das
die Tiefen 0 bis 4. Zu sehen ist das unter
[[beispiele/langer-artikel|Ein langer Artikel]].

Gestaltet ist jede Stufe einzeln:

- **Einzug** steigt bis Tiefe 4 um je ein `--tpl-indent` — dasselbe Maß wie im Explorer, damit die
  beiden Leisten miteinander fluchten.
- **Größe und Gewicht** sinken mit der Tiefe; ab Tiefe 3 wird kleiner gesetzt.
- **Ab Tiefe 5** wird nicht weiter eingerückt, sondern mit einem Punkt markiert. Fünf Einzüge in
  einer 260 px breiten Spalte lassen kein Wort mehr übrig.
- **Der aktuelle Abschnitt** bekommt Farbe, Halbfett *und* einen Balken an der Führungslinie. Beim
  Scrollen ist der Balken das, was man findet.
- **Ein langes Verzeichnis scrollt in sich selbst** (55 % der Fensterhöhe).

> [!note] Die Tiefenzahlen sind relativ
> `depth-0` ist nicht `h1`, sondern die flachste Überschrift der Seite. Auf einer normalen Seite ist
> das `h2`, also landet `h6` auf `depth-4`.
