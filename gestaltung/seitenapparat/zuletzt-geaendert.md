---
title: Zuletzt geändert
description: Die jüngsten Notizen in der Seitenleiste.
section: Gestaltung
tags:
  - gestaltung
  - seitenapparat
---

## Von Haus aus

Eine Liste der zuletzt bearbeiteten Seiten mit Datum, Beschreibung und Tags.

## In dieser Vorlage

Auf fünf Einträge begrenzt, durch Haarlinien getrennt, Beschreibung nach zwei Zeilen abgeschnitten.
Nur am Desktop sichtbar — auf einem Telefon steht die Seitenleiste über dem Inhalt, und dort ist
diese Liste im Weg.

## Ein Fund beim Bauen

Diese Komponente benutzt **dieselben Klassennamen** wie die Ordner- und Tag-Listen: `.section`,
`.meta`, `.desc`, `.tags`. Die Listenregeln der Vorlage waren zunächst nicht eingegrenzt und
landeten deshalb auch hier — in der schmalen Seitenleiste stapelte das dreispaltige Raster Datum
und Titel übereinander.

Seitdem sind alle Listenregeln auf `.page-listing` eingegrenzt. Die Lehre: **Ein Klassenname gehört
nicht der Komponente, in der man ihn zuerst gesehen hat.**
