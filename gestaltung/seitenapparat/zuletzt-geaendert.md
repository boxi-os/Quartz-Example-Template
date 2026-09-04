---
title: Zuletzt geändert
description: Die jüngsten Notizen in der Seitenleiste.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/seitenapparat/zuletzt-geaendert
---

## Von Haus aus

Eine Liste der zuletzt bearbeiteten Seiten mit Datum, Beschreibung und Tags.

## In dieser Vorlage

Auf fünf Einträge begrenzt, durch Haarlinien getrennt, und **auf eine Zeile Titel plus Datum
eingedampft**. Nur am Desktop sichtbar — auf einem Telefon steht die Seitenleiste über dem Inhalt,
und dort ist diese Liste im Weg.

Gemessen vor dem Eindampfen: Ein Eintrag war 113 px hoch, fünf davon füllten 700 px einer Leiste,
die auch noch den Baum und die Notiz-Box trägt. Danach: 57 px je Eintrag, 398 px für die Box.

Zwei der drei Zeilen waren ein Versehen. Die Regel für die Überschrift der Box lautete
`.recent-notes h1, h2, h3` — und jeder Eintragstitel *ist* eine `h3`, also wurden alle fünf in
Versalien und Sperrung gesetzt. Der Selektor nennt jetzt das eigene Kind der Box (`> h3`) und nichts
Tieferes. Beschreibung und Tag-Pillen sind ganz weg: Die eine wiederholt den Titel bei halber
Lesbarkeit, die anderen sind höher als der Eintrag, den sie beschriften.

## Ein Fund beim Bauen

Diese Komponente benutzt **dieselben Klassennamen** wie die Ordner- und Tag-Listen: `.section`,
`.meta`, `.desc`, `.tags`. Die Listenregeln der Vorlage waren zunächst nicht eingegrenzt und
landeten deshalb auch hier — in der schmalen Seitenleiste stapelte das dreispaltige Raster Datum
und Titel übereinander.

Seitdem sind alle Listenregeln auf `.page-listing` eingegrenzt. Die Lehre: **Ein Klassenname gehört
nicht der Komponente, in der man ihn zuerst gesehen hat.**

> [!note] Beide Sprachen in einer Liste
> Die Liste entsteht aus jeder Seite des Builds, eine englische Seite kann also in der Leiste einer
> deutschen auftauchen. Wie beim Suchindex trennte das nur ein Build je Sprache — siehe
> [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].
