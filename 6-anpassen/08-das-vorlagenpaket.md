---
title: 6.8 – Das Vorlagenpaket
description: Was in einer .qtpl-Datei steckt, was beim Import im Projekt ankommt — und was bewusst nicht mitreist.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/das-vorlagenpaket
---

Eine Vorlage reist als eine Datei mit der Endung `.qtpl`. QuartzControl schreibt sie unter
*Vorlagen* aus einem Projekt heraus (Export) und liest sie in ein anderes hinein (Import). Die
Datei ist ein Archiv, in dem zwölf **Bausteine** liegen können — jeder ein abgegrenzter Teil dessen,
was ein Projekt ausmacht. Beim Import wählt man aus, welche davon man übernimmt.

## Die Bausteine

| Baustein | Was er trägt | In dieser Vorlage |
| --- | --- | --- |
| Farben & Schriften | die neun Farbrollen für hell und dunkel, die drei Schriftrollen, woher Schriften geladen werden | gefüllt — [[6-anpassen/02-farben-und-kontrast\|6.2]], [[6-anpassen/03-schriften\|6.3]] |
| CSS-Variablen | eigene Werte für Variablen, getrennt nach hell und dunkel | 50 Variablen — [[6-anpassen/04-variablen\|6.4]] |
| Eigenes [[7-nachschlagen/01-glossar#CSS und SCSS\|CSS]] | `custom.scss` und alle eigenen [[7-nachschlagen/01-glossar#Stylesheet\|Stylesheets]] samt Ladereihenfolge | 30 Stylesheets — [[5-gestaltung/index\|Kapitel 5]] |
| Schriftdateien | mitgebrachte Schriftdateien und ihre `@font-face`-Regeln | vier Dateien, 157 KB — [[6-anpassen/03-schriften\|6.3]] |
| Statische Dateien | alles unter `quartz/static/` außer den Schriften: Logos, Bilder, Textschnipsel | zwei Schnipsel — [[5-gestaltung/05-layout-boxen/die-instanzen\|Die Instanzen]] |
| Layout | welche Komponente wo erscheint, je Seitentyp, und die Umbruchbreiten | gefüllt — [[1-einstieg/04-so-ist-eine-seite-aufgebaut\|1.4]] |
| Eigene [[7-nachschlagen/01-glossar#Frame\|Frames]] | selbst gebaute Seitenraster; werden im Ziel neu registriert, nicht kopiert | vier — [[6-anpassen/05-seitenraster\|6.5]] |
| [[7-nachschlagen/01-glossar#Plugin\|Plugins]] | alle Plugin-Einträge mit Optionen, Reihenfolge und Position | gefüllt, darunter sieben [[7-nachschlagen/01-glossar#Layout-Box\|Layout-Boxen]] — [[5-gestaltung/05-layout-boxen/index\|5.5]] |
| Übersetzungen | Texte, die in Quartz' Sprachdateien geändert wurden | gefüllt, mit einer Einschränkung (unten) |
| Theme-Presets | gespeicherte Zusammenstellungen von Farben und Schriften | zwei: hell und dunkel |
| Community-Theme | ein installiertes Theme mit seinen Einstellungen | leer — diese Vorlage ist selbst das Theme |
| Inhalt | die Notizen selbst | leer — der Inhalt liegt im [[7-nachschlagen/01-glossar#Vault\|Vault]] |

Der Import zeigt vorher, welche Bausteine das Paket enthält und was im Projekt dadurch ersetzt
wird, und legt einen [[7-nachschlagen/01-glossar#Snapshot|Snapshot]] an — eine Sicherung, zu der man zurückkehren kann.

## Was mitreist und was nicht

Von den *Dateien* eines Projekts trägt ein Paket alles unter `quartz/styles/` (Eigenes CSS) und
alles unter `quartz/static/` — die Schriftdateien in ihrem eigenen Baustein, Logos, Bilder und
Schnipsel-Dateien im Baustein *Statische Dateien*.

Dass letzterer existiert, ist neu: Bis zum 06.09.2026 blieb alles außer den Schriften zurück, und
eine Layout-Box mit `file:` kam im Zielprojekt mit einem Verweis ins Leere an — gemessen erschien
`layout-box-note` auf 0 von 334 Seiten. Seitdem kommen die zwei Schnipsel-Dateien mit, und im
Zielprojekt rendern alle Boxen.

Der Baustein rechnet dabei mit, was Quartz selbst mitbringt: Von den sechs Dateien unter
`quartz/static/` sind vier byteweise Quartz' eigenes Gerüst (`icon.png`, `og-image.png`, zwei
giscus-Stylesheets) und nur die zwei Schnipsel gehören der Vorlage. Die Vorschau meldet deshalb
zwei Ergänzungen statt sechs Konflikten, und ein Zielprojekt bekommt nie das Gerüst eines anderen
übergestülpt.

Sechs der sieben Layout-Boxen holen ihren Inhalt trotzdem aus der Konfiguration (`html:`) und die
Wortmarke ist ein Inline-SVG. Das ist seit dem 06.09.2026 keine Notwendigkeit mehr, sondern eine
Entscheidung: Markup im Konfigurationseintrag kann ohne diesen Eintrag gar nicht erst ankommen. Die
eine `file:`-Box — „Über dieses Handbuch“ — zeigt den anderen Weg. Fehlt ihre Datei doch einmal,
ist das kein Fehler: Das Plugin protokolliert eine Warnung und rendert nichts; im [[7-nachschlagen/01-glossar#Dev-Server|Dev-Server]]
erscheint ein gestrichelter Platzhalter mit dem erwarteten Pfad.

**Der Inhalt** reist nicht mit — mit Absicht. Eine Vorlage ist eine Gestaltung; die eigenen
Notizen kommen aus dem eigenen Vault. Den Baustein *Inhalt* gibt es für den seltenen Fall einer
Vorlage, die sich selbst erklärt; diese hier tut das über den Vault.

## Eine bekannte Einschränkung

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
