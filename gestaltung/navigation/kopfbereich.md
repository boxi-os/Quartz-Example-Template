---
title: Kopfbereich
description: Wortmarke, Seitentitel und die vier Bedienelemente in einer Zeile.
section: Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/kopfbereich
---

Oben steht die Wortmarke, daneben der Seitentitel, am rechten Ende Suche, Farbschema-Umschalter,
Lesemodus und der Sprachumschalter. Darunter eine Trennlinie.

## Von Haus aus

Der Kopfbereich enthält nur den Seitentitel. Eine Marke gibt es nicht — dafür müsste man eine
eigene Komponente bauen. Suche und die beiden Umschalter sitzen in der linken Seitenleiste.

## In dieser Vorlage

Die Marke kommt aus einer **Layout-Box-Instanz** mit Inline-SVG, einmal hell und einmal dunkel. Sie
ist zugleich der Link zur Startseite.

Zwei Feinheiten:

- Der **Text der Marke ist visuell versteckt**, aber im Dokument vorhanden. Der Link enthält sonst
  nur ein SVG und hätte keinen zugänglichen Namen. `display: none` wäre hier falsch gewesen — genau
  dieser Fehler steckte in der ersten Fassung.
- Die vier Bedienelemente stehen **im Kopf, nicht in der Leiste**. Dort sucht man sie, und es ist
  der einzige Bereich, den jeder Frame hat — auf der Fehlerseite gab es vorher weder Suche noch
  Farbschema-Umschalter, weil sie keine Seitenleisten hat.
- Sie bilden eine **Gruppe** (`toolbar`) mit `wrap`, damit vier Bedienelemente und der Seitenname
  auch auf einem 360 px breiten Telefon nebeneinander passen.
- Am Telefon wird der Kopf zur **App-Leiste**: Er bleibt beim Scrollen oben stehen, läuft über die
  volle Breite und nimmt den Schubladen-Knopf des Explorers mit auf. Die Suche gibt dort ihr Wort
  auf und wird ein Quadrat wie die beiden anderen; ihre 44 px behält sie.

## Er bleibt stehen und wird kleiner

Seit dem 05.09.2026 klebt der Kopf auf jeder Breite oben am Fenster, nicht mehr nur am Telefon: Die
vier Bedienelemente und der Weg zurück zur Startseite sind das, wonach man mitten in einem langen
Artikel greift, und mehrere Seiten hier sind drei Bildschirme hoch.

Beim Scrollen schrumpft er. Was dabei kleiner wird, ist der **Innenabstand** und der Seitentitel —
nicht die Bedienelemente: Ein Ziel, das seine Größe ändert, während man danach greift, ist
schlimmer als eine hohe Leiste. Gemessen: 61 px in Ruhe, 49 px ab 4 rem Scrollweg.

Getragen wird das von zwei registrierten Längen (`--tpl-header-pad`, `--tpl-header-title`), die an
`scroll(root block)` hängen. Nichts davon bewegt sich von selbst — die Höhe ist eine Funktion der
Scrollposition, nicht der Zeit —, deshalb gibt es bei `prefers-reduced-motion` auch nichts zu
unterdrücken.

Zwei Dinge hängen daran und stehen deshalb in derselben Rechnung:

- Die **rechte Spalte** klebt unter dem Kopf, nicht darunter verborgen: Ihr `top` liest
  `--tpl-header-h` und wandert mit nach oben, während der Kopf schrumpft.
- **Sprungziele** halten die Höhe der kleinen Leiste über sich frei (`scroll-margin-block-start`),
  sonst landete jede Überschrift aus dem Inhaltsverzeichnis hinter dem Kopf.

## Ein Fund beim Bauen

Das Plugin setzt `width: 100%` auf jede Layout-Box. In einer Flex-Zeile machte das die Marke
1376 px breit und schob den Titel in die nächste Zeile. `flex` hebt eine gesetzte Breite nicht auf —
sie musste ausdrücklich zurückgenommen werden.
