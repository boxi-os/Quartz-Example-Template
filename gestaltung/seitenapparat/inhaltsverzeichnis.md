---
title: Inhaltsverzeichnis
description: Die Gliederung rechts — alle Ebenen, nicht nur drei.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/seitenapparat/inhaltsverzeichnis
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
  einer drei Spalten breiten Leiste lassen kein Wort mehr übrig.
- **Der aktuelle Abschnitt** bekommt Farbe, Halbfett *und* einen Balken an der Führungslinie. Beim
  Scrollen ist der Balken das, was man findet.
- **Es zeigt sich ganz.** Quartz deckelt diese Komponente gleich dreifach — `flex: 0 0.5 auto` mit
  `overflow-y: hidden`, dazu `max-height: calc(100% - 2rem)` auf der Liste und noch eine Regel in
  seinem Basis-Stylesheet. Zusammen machen die drei aus einer langen Gliederung einen kurzen Stummel
  mit eigener Rollleiste, mitten in einer Spalte, die selbst schon rollte. Alle drei sind hier
  aufgehoben.
- **Gerollt wird eine Ebene höher**, in der rechten Spalte als Ganzem — mit derselben weichen Kante
  wie im Explorer und mit nur einer Rollleiste statt zweier ineinander. In Chromium ist dabei immer
  nur die Seite weich, hinter der noch etwas liegt: Am Anfang der Liste ist der erste Eintrag
  scharf, am Ende der letzte. Ein Browser ohne scroll-getriebene Animationen bekommt die Kante an
  beiden Enden.
- **Kein Ausblenden per Deckkraft.** Quartz dimmt einen Eintrag, der gerade nicht im Bild ist, auf
  `opacity: 0.35`; das misst sich auf diesem Grund unter 3:1. Der Zustand bleibt, gesagt wird er in
  Farbe, Gewicht und Balken — drei Signalen, die alle gemessen sind.

## Die rechte Spalte steht

Ein Inhaltsverzeichnis, das mit dem Text nach oben wegrollt, ist eine Liste von Stellen, zu denen
man nicht mehr springen kann. Ab Tablet-Breite bleibt die rechte Spalte deshalb stehen
(`position: sticky`) und rollt nur in sich selbst, wenn ihr Inhalt höher wird als das Fenster.

Drei Dinge gehören dafür zusammen, und ohne eines davon passiert gar nichts: `align-self: start` —
ein Raster-Element füllt sonst seine Zeile, und was schon ganz oben *und* ganz unten ist, kann
nirgends kleben —, ein `top`, und eine Maximalhöhe.

Das `top` ist seit dem 05.09.2026 keine feste Zahl mehr, sondern `--tpl-header-h` plus einen
Abstand: Der Kopfbereich klebt selbst und schrumpft dabei, und die Spalte wandert mit ihm nach
oben, statt eine Lücke zu lassen, die bei jedem Scrollen wächst.

> [!note] Die Tiefenzahlen sind relativ
> `depth-0` ist nicht `h1`, sondern die flachste Überschrift der Seite. Auf einer normalen Seite ist
> das `h2`, also landet `h6` auf `depth-4`.
