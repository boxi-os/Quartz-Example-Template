---
title: Tabellen und Medien
description: Zwei Elemente, die die Spalte sprengen wollen.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
translationKey: gestaltung/im-inhalt/tabellen-und-medien
---

## Tabellen

**Von Haus aus** rahmt Quartz die Tabelle und setzt Innenabstände direkt am Element.

**In dieser Vorlage** gibt es keine senkrechten Linien und keinen Außenrahmen: eine Haarlinie unter
jeder Zeile, eine kräftigere unter dem Kopf, und die letzte Zeile verliert ihre Linie. Der Kopf
steht in der Überschriftenschrift und bricht nicht um.

Das Scrollen liegt auf dem Container, den Quartz um jede Tabelle legt — **nicht auf der Tabelle
selbst.** Der naheliegende erste Versuch (`display: block; overflow-x: auto` auf dem `<table>`)
zerlegt das Tabellenlayout: Beim Bauen rutschten dadurch Schlüssel und Werte der
Eigenschaften-Tabelle übereinander.

## Bilder

Zarter Rahmen und runde Ecken. Ohne Rahmen sieht ein Bild mit weißem Hintergrund auf dem warmen
Grund dieser Seite wie ein Loch aus.

Eine ausdrücklich gesetzte Breite (`![[bild.png|300]]`) bleibt erhalten; die Vorlage begrenzt nur
nach oben.

## Einbettungen

Ein `iframe` bekommt `aspect-ratio: 16/9`. Ohne diese Regel fällt es in einer Grid-Zelle auf null
Höhe zusammen — was genau dann passiert, wenn die Seite ein eigenes Raster verwendet, also in dieser
Vorlage überall.

## Transkludierte Notizen

Gestrichelter Balken und getönte Fläche: Man soll sehen, wo fremder Inhalt anfängt und aufhört.
**Von Haus aus** ist eine Einbettung optisch nicht vom umgebenden Text getrennt.
