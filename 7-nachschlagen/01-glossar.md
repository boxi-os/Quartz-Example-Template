---
title: 7.1 Glossar
description: Jeder Begriff dieses Handbuchs in zwei, drei Sätzen — alphabetisch, mit dem Verweis auf die Seite, die ihn ausführt.
section: Nachschlagen
tags:
  - nachschlagen
  - referenz
translationKey: nachschlagen/glossar
---

Jeder Eintrag ist eine Überschrift und damit verlinkbar: `[[7-nachschlagen/01-glossar#Symlink]]`
springt direkt zum Begriff.

### Alias

Ein zweiter Name für eine Seite, eingetragen im Frontmatter unter `aliases`. Obsidian findet die
Notiz auch darunter; auf der Website baut ein Plugin für jeden Alias eine Weiterleitung. →
[[4-seiten-steuern/03-aliase|4.3 Aliase]]

### Barrierefreiheit

Eine Website so bauen, dass sie auch ohne Maus, ohne Farbsehen, mit Screenreader oder mit
Systemeinstellungen wie „weniger Bewegung“ benutzbar bleibt. Die Regeln dafür heißen WCAG. →
[[6-anpassen/06-barrierefreiheit|6.6 Barrierefreiheit]]

### Base

Eine gespeicherte Abfrage über den Vault in Obsidian: Sie sammelt Notizen nach Kriterien und
zeigt sie als Tabelle, Liste, Kacheln, Board oder Galerie. Die Datei endet auf `.base`. →
[[3-obsidian-formate/01-bases/index|3.1 Bases]]

### Baustein

Das Wort hat in QuartzControl zwei Bedeutungen. Im Layout-Editor ist ein Baustein eine
*Komponente* — Suche, Inhaltsverzeichnis, Explorer —, die man an einen Ort der Seite setzt. In einem
Vorlagenpaket ist ein Baustein ein *Teil des Pakets* — Farben, Stylesheets, Plugins —, den man
einzeln übernehmen kann. → [[6-anpassen/08-das-vorlagenpaket|6.8 Das Vorlagenpaket]]

### Breakpoint

Die Fensterbreite, ab der eine Seite anders umbricht. Diese Vorlage hat zwei: 1100 px (Desktop zu
Tablet) und 800 px (Tablet zu Telefon). → [[6-anpassen/05-seitenraster|6.5 Seitenraster]]

### Brotkrumen

Die Zeile über dem Titel, die den Weg von der Startseite bis zur aktuellen Seite zeigt: „2
Formatierung › 2.5 Callouts › Grundform“. → [[5-gestaltung/02-ueber-dem-inhalt/brotkrumen|Brotkrumen]]

### Build

Der Vorgang, in dem Quartz aus den Notizen die fertige Website erzeugt: Markdown lesen, Plugins
anwenden, HTML-Dateien in den Ausgabeordner `public/` schreiben. In QuartzControl unter
*Vorschau & Build*. → [[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]]

### Callout

Ein hervorgehobener Kasten im Text, in Obsidian geschrieben als `> [!note]`. Es gibt dreizehn Typen
mit eigener Farbe und eigenem Symbol; diese Vorlage setzt alle Farben neu. →
[[2-formatierung/05-callouts/index|2.5 Callouts]]

### Canvas

Eine freie Fläche in Obsidian, auf der man Karten anordnet und mit Pfeilen verbindet. Die Datei
endet auf `.canvas`; Quartz macht daraus eine zoombare Seite. →
[[3-obsidian-formate/02-canvas/index|3.2 Canvas]]

### Commit

Ein gespeicherter Stand in git, mit Datum, Urheber und Beschreibung. Man kann zu jedem Commit
zurückkehren. → [[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### CSS und SCSS

CSS ist die Sprache, in der das Aussehen einer Website beschrieben wird — Farben, Abstände,
Schriften, Anordnung. SCSS ist eine Erweiterung davon mit Variablen und Verschachtelung, die beim
Bauen zu CSS übersetzt wird. Quartz und diese Vorlage schreiben SCSS. →
[[6-anpassen/01-etwas-aendern|6.1 Etwas ändern]]

### Dev-Server

Ein kleiner Webserver auf dem eigenen Rechner, den QuartzControl unter *Vorschau & Build* startet.
Er baut die Website bei jeder Änderung neu und zeigt sie unter `localhost:8080` — nur für einen
selbst sichtbar. → [[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]]

### Diff

Der Vergleich zweier Stände einer Datei, Zeile für Zeile: was dazukam, was wegfiel. git zeigt so,
was ein Commit geändert hat. → [[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Entwurf

Eine Seite mit `draft: true` im Frontmatter. Sie bleibt im Vault, wird aber nicht gebaut. →
[[4-seiten-steuern/02-entwurf-und-ungelistet|4.2 Entwurf und ungelistet]]

### Excalidraw

Ein Zeichenwerkzeug für Skizzen und Diagramme, als Plugin in Obsidian. Die Zeichnung liegt in
einer `.excalidraw.md`-Datei; auf der Website bleibt sie zoombar. →
[[3-obsidian-formate/03-excalidraw/index|3.3 Excalidraw]]

### Explorer

Der Ordnerbaum aller Seiten in der linken Spalte. Er sortiert nach dem Titel der Seiten, nicht
nach dem Dateinamen. → [[5-gestaltung/01-navigation/explorer|Explorer]]

### Farbschema

Hell oder dunkel. Die Website folgt der Systemeinstellung und hat einen Schalter im Kopfbereich;
jede Farbe der Vorlage ist für beide Schemata gesetzt und gemessen. →
[[5-gestaltung/01-navigation/farbschema|Farbschema-Umschalter]]

### Frame

Das Seitenraster: welche Bereiche eine Seite hat, wo sie liegen, wie breit sie sind — je
Bildschirmbreite. Quartz bringt drei feste mit; diese Vorlage baut drei eigene (`editorial`,
`index`, `drawing`) im Frame-Editor von QuartzControl. → [[6-anpassen/05-seitenraster|6.5 Seitenraster]]

### Frame-Box

Breite, Ausrichtung und Innenabstand eines Frames, je Breakpoint einzeln gesetzt. Sie entscheidet,
wie breit der Text wird. → [[6-anpassen/05-seitenraster|6.5 Seitenraster]]

### Frontmatter

Der Block ganz oben in einer Notiz zwischen zwei Zeilen aus `---`, in dem Angaben über die Seite
stehen: Titel, Beschreibung, Tags, Datum. Obsidian nennt ihn „Eigenschaften“. →
[[4-seiten-steuern/index|4 Eine Seite steuern]]

### git

Ein Programm, das die Geschichte von Dateien aufzeichnet: jeden gespeicherten Stand, mit Datum und
Beschreibung. Man muss es für diese Vorlage nicht bedienen können; QuartzControl bringt es mit. →
[[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Graph

Die Darstellung der Seiten als Punkte und ihrer Links als Linien, in der rechten Spalte. →
[[5-gestaltung/04-neben-dem-inhalt/graph|Graph]]

### Hover

Der Zustand eines Elements, während der Mauszeiger darüber steht. Ein Link wechselt dann die
Farbe; auf einem Touchscreen gibt es diesen Zustand nicht, weshalb nichts *nur* im Hover sichtbar
sein darf. → [[6-anpassen/06-barrierefreiheit|6.6 Barrierefreiheit]]

### HTML

Die Sprache, in der Webseiten geschrieben sind und die ein Browser liest. Quartz übersetzt
Markdown in HTML. Man kann HTML auch direkt in eine Notiz schreiben. →
[[2-formatierung/13-besonderes/html|HTML]]

### Kontrast

Das Helligkeitsverhältnis zwischen Text und Grund, geschrieben als 4,5:1. WCAG verlangt für
normalen Text mindestens 4,5:1, für große Schrift 3:1. Diese Vorlage misst 89 Paare bei jedem
Lauf. → [[6-anpassen/02-farben-und-kontrast|6.2 Farben und Kontrast]]

### Layout

Welche Komponente an welchem Ort der Seite erscheint — Kopfbereich, linke und rechte Spalte, vor und
nach dem Inhalt, Fußzeile —, je Seitentyp. In QuartzControl unter *Layout*. →
[[1-einstieg/04-so-ist-eine-seite-aufgebaut|1.4 So ist eine Seite aufgebaut]]

### Layout-Box

Ein Plugin, das einen eigenen Kasten mit HTML oder Markdown an eine Stelle des Layouts setzt. Diese
Vorlage nutzt es fünfmal: Wortmarke, Seitenleisten-Box, mobiler Hinweis, „Weiterlesen“, Impressum. →
[[5-gestaltung/05-layout-boxen/index|5.5 Layout-Boxen]]

### Markdown

Die Schreibweise der Notizen: Text mit wenigen Zeichen, die Bedeutung tragen — `**fett**`,
`# Überschrift`, `[[Link]]`. Obsidian schreibt sie, Quartz liest sie. →
[[2-formatierung/index|2 Formatierung]]

### Media-Query

Eine Bedingung in CSS, die Regeln nur bei bestimmter Fensterbreite anwendet — so entstehen die
Breakpoints. Eine Media-Query kann keine Variable lesen; deshalb stehen die Breakpoints als Zahl
in den Stylesheets. → [[6-anpassen/04-variablen|6.4 Variablen]]

### Mermaid

Eine Textschreibweise für Diagramme — Flussdiagramme, Sequenzen, Zeitleisten —, die Quartz in
eine Grafik übersetzt. → [[2-formatierung/09-diagramme/index|2.9 Diagramme]]

### Obsidian

Das Programm, in dem die Notizen geschrieben werden. Es speichert Markdown-Dateien in einem Vault. →
[[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Plugin

Ein Baustein von Quartz mit einer Aufgabe: einer baut den Explorer, einer die Suche, einer liest
das Datum. Quartz bringt viele mit; weitere kommen aus dem Marktplatz in QuartzControl. Obsidian
hat eigene Plugins, die nichts mit denen von Quartz zu tun haben. →
[[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Projekt

Ein Ordner mit einer Quartz-Installation, seiner Konfiguration und dem Inhalt. QuartzControl
verwaltet mehrere davon. → [[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Quartz

Der Static-Site-Generator, der aus Markdown-Notizen eine Website baut und Obsidians Schreibweise
versteht. → [[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### QuartzControl

Die App, mit der man Quartz bedient: Projekte, Plugins, Farben, Schriften, Layout, Vorschau,
Build, Veröffentlichung. Diese Vorlage ist für sie gemacht. →
[[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Repository

Ein Ordner, dessen Geschichte git führt. Der Vault dieser Website ist eines; das Quartz-Projekt
ist ein zweites. → [[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Rückverweise

Die Liste der Seiten, die auf die aktuelle Seite verlinken, in der rechten Spalte. Quartz nennt sie
„Backlinks“. → [[5-gestaltung/04-neben-dem-inhalt/rueckverweise|Rückverweise]]

### Slug

Der Teil der Adresse, der eine Seite benennt: aus `2-formatierung/05-callouts/grundform.md` wird
`/2-formatierung/05-callouts/grundform`. Quartz leitet ihn aus dem Dateipfad ab; Leerzeichen
werden Bindestriche. → [[2-formatierung/04-links/wikilinks|Wikilinks]]

### Snapshot

Eine Sicherung des Projekts, die QuartzControl vor größeren Eingriffen anlegt — vor einem Import,
einem Update, einem Plugin-Wechsel — und zu der man zurückkehren kann. Der Inhalt ist nicht
enthalten, wenn `content/` ein Symlink ist. →
[[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]]

### Static-Site-Generator

Ein Programm, das aus Textdateien fertige HTML-Seiten erzeugt, die ohne Datenbank und ohne
laufendes Programm auf jedem Webspace liegen können. Quartz ist einer. →
[[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Stylesheet

Eine Datei mit CSS oder SCSS, die das Aussehen beschreibt. Diese Vorlage hat 30, eins je
Komponente, unter *Stile → Eigenes CSS*. → [[5-gestaltung/index|5 Die Gestaltung]]

### Symlink

Eine Verknüpfung im Dateisystem, die einen Ordner an einer zweiten Stelle erscheinen lässt, ohne
ihn zu kopieren. Der Ordner `content/` dieses Projekts ist ein Symlink auf den Vault. →
[[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]]

### Tag

Ein Schlagwort, im Frontmatter unter `tags` oder im Text als `#wort`. Quartz baut für jedes Tag eine
Seite mit allen Notizen, die es tragen. → [[5-gestaltung/02-ueber-dem-inhalt/tags|Tags]]

### Token

Eine benannte Variable, aus der die Gestaltung besteht — `--tpl-space-md` für den Grundabstand,
`--tpl-radius-md` für die Ecken. Ändert man das Token, ändert sich jede Stelle, die es liest. In
QuartzControl heißen sie schlicht *Variablen*. → [[6-anpassen/04-variablen|6.4 Variablen]]

### Ungelistet

Eine Seite mit `unlisted: true`: gebaut und über ihre Adresse erreichbar, aber in keiner Liste. →
[[4-seiten-steuern/02-entwurf-und-ungelistet|4.2 Entwurf und ungelistet]]

### Vault

Obsidians Wort für den Ordner, in dem die Notizen liegen. Diese Website hat einen eigenen. →
[[1-einstieg/02-die-werkzeuge|1.2 Die Werkzeuge]]

### Veröffentlichen

Die gebaute Website an ihr Ziel bringen: einen Ordner, einen Server, ein git-Repository. In
QuartzControl unter *Veröffentlichen*. →
[[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]]

### Vorlage

Eine Gestaltung für QuartzControl, verpackt in einer `.qtpl`-Datei, die man in ein Projekt
importiert. Diese Website ist das Handbuch der Vorlage *Example*. →
[[1-einstieg/01-was-diese-vorlage-ist|1.1 Was diese Vorlage ist]]

### Wikilink

Ein Verweis auf eine andere Notiz in doppelten eckigen Klammern: `[[Seite]]` oder
`[[Seite|angezeigter Text]]`. Die Schreibweise stammt aus Obsidian; Quartz löst sie beim Bauen auf. →
[[2-formatierung/04-links/wikilinks|Wikilinks]]

### YAML

Die Schreibweise des Frontmatters und der Quartz-Konfiguration: `schlüssel: wert`, Listen mit
einem Bindestrich je Zeile, Einrückung mit Leerzeichen. →
[[2-formatierung/11-eigenschaften/frontmatter|Frontmatter]]
