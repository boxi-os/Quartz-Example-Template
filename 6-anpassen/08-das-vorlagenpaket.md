---
title: 6.8 Das Vorlagenpaket
description: Was in einer .qtpl-Datei steckt, was beim Import im Projekt ankommt — und was bewusst nicht mitreist.
section: Anpassen
tags:
  - anpassen
translationKey: anpassen/das-vorlagenpaket
---

Eine Vorlage reist als eine Datei mit der Endung `.qtpl`. QuartzControl schreibt sie unter
*Vorlagen* aus einem Projekt heraus (Export) und liest sie in ein anderes hinein (Import). Die
Datei ist ein Archiv, in dem elf **Bausteine** liegen können — jeder ein abgegrenzter Teil dessen,
was ein Projekt ausmacht. Beim Import wählt man aus, welche davon man übernimmt.

## Die Bausteine

| Baustein | Was er trägt | In dieser Vorlage |
| --- | --- | --- |
| Farben & Schriften | die neun Farbrollen für hell und dunkel, die drei Schriftrollen, woher Schriften geladen werden | gefüllt — [[6-anpassen/02-farben-und-kontrast\|6.2]], [[6-anpassen/03-schriften\|6.3]] |
| CSS-Variablen | eigene Werte für Variablen, getrennt nach hell und dunkel | 53 Variablen — [[6-anpassen/04-variablen\|6.4]] |
| Eigenes CSS | `custom.scss` und alle eigenen Stylesheets samt Ladereihenfolge | 30 Stylesheets — [[5-gestaltung/index\|Kapitel 5]] |
| Schriftdateien | mitgebrachte Schriftdateien und ihre `@font-face`-Regeln | vier Dateien, 157 KB — [[6-anpassen/03-schriften\|6.3]] |
| Layout | welche Komponente wo erscheint, je Seitentyp, und die Umbruchbreiten | gefüllt — [[1-einstieg/04-so-ist-eine-seite-aufgebaut\|1.4]] |
| Eigene Frames | selbst gebaute Seitenraster; werden im Ziel neu registriert, nicht kopiert | drei — [[6-anpassen/05-seitenraster\|6.5]] |
| Plugins | alle Plugin-Einträge mit Optionen, Reihenfolge und Position | gefüllt, darunter fünf Layout-Boxen — [[5-gestaltung/05-layout-boxen/index\|5.5]] |
| Übersetzungen | Texte, die in Quartz' Sprachdateien geändert wurden | gefüllt, mit einer Einschränkung (unten) |
| Theme-Presets | gespeicherte Zusammenstellungen von Farben und Schriften | zwei: hell und dunkel |
| Community-Theme | ein installiertes Theme mit seinen Einstellungen | leer — diese Vorlage ist selbst das Theme |
| Inhalt | die Notizen selbst | leer — der Inhalt liegt im Vault |

Der Import zeigt vorher, welche Bausteine das Paket enthält und was im Projekt dadurch ersetzt
wird, und legt einen Snapshot an — eine Sicherung, zu der man zurückkehren kann.

## Was nicht mitreist

Von den *Dateien* eines Projekts trägt ein Paket nur `quartz/styles/` (Eigenes CSS) und
`quartz/static/fonts/` (Schriftdateien). Alles andere unter `quartz/static/` bleibt zurück:
Bilder, Logos und die Schnipsel-Dateien der Layout-Boxen.

Deshalb holen vier der fünf Layout-Boxen dieser Vorlage ihren Inhalt aus der Konfiguration
(`html:`) und reisen vollständig mit dem Baustein *Plugins*. Auch die Wortmarke ist ein
Inline-SVG und keine Bilddatei. Die fünfte Box — „Über dieses Handbuch“ — liest bewusst aus einer
Datei, um beide Wege zu zeigen. Wer sie behalten will, kopiert `sidebar-note.md` und
`sidebar-note.en.md` von Hand nach `quartz/static/snippets/`. Fehlt die Datei, ist das kein
Fehler: Das Plugin protokolliert eine Warnung und rendert nichts; im Dev-Server erscheint ein
gestrichelter Platzhalter mit dem erwarteten Pfad.

**Der Inhalt** reist nicht mit — mit Absicht. Eine Vorlage ist eine Gestaltung; die eigenen
Notizen kommen aus dem eigenen Vault. Den Baustein *Inhalt* gibt es für den seltenen Fall einer
Vorlage, die sich selbst erklärt; diese hier tut das über den Vault.

## Zwei bekannte Einschränkungen

> [!bug] Nur eine der fünf Layout-Boxen überlebt den Import
> Alle fünf Instanzen tragen denselben abgeleiteten Namen (`quartz-layout-box`), und der Import
> ordnet Plugin-Einträge nach Namen zu. Gemessen: Von den fünf kommt eine an. Die anderen vier legt
> man nach dem Import unter *Plugins* neu an; ihre Einstellungen stehen in
> [[5-gestaltung/05-layout-boxen/die-fuenf-instanzen|Die fünf Instanzen]].

> [!warning] Der Baustein Übersetzungen ändert keine Komponenten-Überschriften
> „Backlinks“, „Graphansicht“, „Zuletzt bearbeitete Seiten“ kommen aus den Plugins selbst, die
> ihre Sprachdateien mitbringen. Was man in QuartzControl unter *Konfiguration → Übersetzungen*
> ändert, erreicht alles, was der Quartz-Kern beschriftet — die Komponenten-Überschriften nicht.
> Gemessen an der gebauten Seite: Alle drei blieben nach der Änderung stehen. Der Mechanismus ist
> richtig, seine Reichweite kleiner, als man erwartet.

## Die Vorlage selbst weitergeben

Wer diese Vorlage verändert hat und das Ergebnis weitergeben will, exportiert unter *Vorlagen* ein
neues Paket — mit den Bausteinen, die sich geändert haben. Der Empfänger importiert es in sein
Projekt und wählt dieselben Bausteine. Was er dabei überschreibt, sagt ihm die App vorher.
