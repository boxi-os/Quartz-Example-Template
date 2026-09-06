---
title: 4.1 Titel, Beschreibung, Datum
description: Die drei Angaben, die jede Seite haben sollte — und woher das Datum kommt, wenn keines dasteht.
section: 4 Eine Seite steuern
tags:
  - seiten-steuern
date: 2026-09-06
translationKey: seiten-steuern/titel-beschreibung-datum
---

## `title`

Der Titel steht als Überschrift über der Seite, im Browser-Tab, im [[7-nachschlagen/01-glossar#Explorer|Explorer]], in jeder Liste und in
jedem Suchergebnis. Fehlt er, nimmt Quartz den Dateinamen. Diese Website setzt ihn auf jeder Seite,
weil ein Dateiname wie `ueberschriften` kein Titel ist.

Der Explorer sortiert nach dem Titel, nicht nach dem Dateinamen — deshalb tragen die Kapitel und
Abschnitte dieses Handbuchs ihre Nummer im Titel. Siehe
[[5-gestaltung/01-navigation/explorer|Explorer]].

## `description`

Ein Satz, der die Seite beschreibt. Er erscheint in Suchergebnissen, in Ordner- und Tag-Listen, in
der Vorschau beim Überfahren eines Links und beim Teilen der Adresse in sozialen Netzen. Ohne ihn
nimmt Quartz die ersten Wörter des Textes.

## `date` und `lastmod`

`date` ist das Erstellungsdatum, `lastmod` das der letzten Änderung. Unter dem Titel zeigt diese
Vorlage das Änderungsdatum; danach sortiert auch die Liste „Zuletzt geändert“ in der linken Spalte.
Das Format folgt der Sprache der Seite: Auf einer englischen Seite steht ein englisches Datum.

### Woher das Datum kommt, wenn keines dasteht

Quartz fragt der Reihe nach: das [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]], dann [[7-nachschlagen/01-glossar#git|git]], dann das Dateisystem. Eingestellt wird die
Reihenfolge beim [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Created modified date*, in QuartzControl unter *Plugins*. Diese Vorlage
lässt git aus — `frontmatter → filesystem` — und das hat einen gemessenen Grund.

> [!warning] Ein Symlink nimmt Quartz die git-Daten
> git — das Programm, das die Geschichte von Dateien aufzeichnet — wäre die bessere Quelle: Ein
> Commit-Datum überlebt ein Kopieren, ein Wiederherstellen und ein frisches Auschecken, die
> Änderungszeit einer Datei nicht. Hier fehlt es trotzdem. Der Inhalt liegt in einem
> Obsidian-Vault, auf den `content/` per [[7-nachschlagen/01-glossar#Symlink|Symlink]] zeigt; das Plugin folgt dem Link und findet auch
> das git des [[7-nachschlagen/01-glossar#Vault|Vaults]], rechnet den Dateipfad danach aber gegen das Projektverzeichnis — und fragt so
> nach einem Pfad, der aus dem Vault wieder herausführt. Jede Abfrage scheitert. Für **250 der 254
> Seiten** stand deshalb *„isn't yet tracked by git, dates will be inaccurate“* im Bauprotokoll;
> stumm blieben nur die vier, die ein `lastmod` tragen und git gar nicht erst fragen. Der Fehler
> ist gemeldet; sobald er behoben ist, gehört `git` wieder in die Liste.

Was das Dateisystem liefert, ist die Änderungszeit der Datei — und die ändert sich bei jedem
Kopieren. Wer ein Datum will, das bleibt, schreibt es ins Frontmatter. Diese Seite tut das.

Wie Titel und Datum *aussehen*, steht in
[[5-gestaltung/02-ueber-dem-inhalt/titel-und-datum|Titel und Datum]].
