---
title: 1.1 Was diese Vorlage ist
description: Eine Gestaltung für Quartz-Websites, die man in QuartzControl importiert — und die drei Entscheidungen, aus denen sie besteht.
section: Einstieg
tags:
  - einstieg
translationKey: einstieg/was-diese-vorlage-ist
---

**Example** ist eine Vorlage für QuartzControl. Eine Vorlage ist hier eine *Gestaltung*: Farben,
Schriften, Abstände, das Seitenraster, die Anordnung der [[7-nachschlagen/01-glossar#Baustein|Bausteine]], die Einstellungen der [[7-nachschlagen/01-glossar#Plugin|Plugins]] —
alles, was eine Website ausmacht, außer ihrem Inhalt. Sie wird als eine Datei mit der Endung
`.qtpl` weitergegeben und in der App unter *Vorlagen* in ein eigenes Projekt importiert. Danach
sieht die eigene Website aus wie diese hier, mit den eigenen Notizen darin.

Die Vorlage ist zum Benutzen gedacht **und** zum Umbauen. Nichts an ihr ist versteckt: Jede Farbe
und jedes Maß ist eine Variable, die man in der App ändern kann. Jedes [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]] — die Datei, in
der das Aussehen einer Komponente beschrieben ist — gehört zu genau einer Komponente und ist nach
ihr benannt.

## Warum es diese Website gibt

Eine Gestaltung kann man nicht abstrakt ansehen. Ein [[7-nachschlagen/01-glossar#Explorer|Explorer]] braucht Ordner, ein
Inhaltsverzeichnis braucht Überschriften, ein [[7-nachschlagen/01-glossar#Graph|Graph]] braucht Verweise, eine Tabelle braucht Zeilen.
Diese Website liefert das alles: Sie ist das Handbuch der Vorlage und zugleich ihr Vorführmodell.
Jedes Element, das Obsidian schreiben kann, kommt hier mindestens einmal vor — und wer eine eigene
Anpassung prüfen will, findet hier die Seite, an der man den Unterschied sieht.

## Die drei Entscheidungen

Alles Weitere folgt aus diesen dreien.

### 1. Die Breite entscheidet das Raster

Das Seitenraster — in Quartz *[[7-nachschlagen/01-glossar#Frame|Frame]]* genannt — teilt die Seite in zwölf gleich breite Spalten und
gibt dem Text sechs davon. Wie breit eine Textzeile wird, ist damit entschieden, und zwar an genau
einer Stelle. Es gibt keine zweite Begrenzung am Absatz, die mit der ersten in Streit geraten
könnte. Was das für Tablet und Telefon heißt, steht unter [[6-anpassen/05-seitenraster|6.5
Seitenraster]].

### 2. Farben sind gemessen

[[7-nachschlagen/01-glossar#Kontrast|Kontrast]] ist das Helligkeitsverhältnis zwischen Text und Grund. Die Richtlinie für barrierefreie
Websites, [[7-nachschlagen/01-glossar#WCAG|WCAG]], verlangt für normalen Text mindestens 4,5:1. Diese Vorlage misst bei jedem Lauf
89 Farbpaare in hell und dunkel — jede Text-auf-Grund-Kombination, die dreizehn Callout-Farben,
die Farben des Code-Syntaxthemas — und bricht ab, wenn eines darunter liegt. Quartz' eigene Farben
bestehen diese Prüfung nicht: elf der zwölf Callout-Farben scheitern im hellen Modus. Deshalb sind
sie hier neu gesetzt. Mehr unter [[6-anpassen/02-farben-und-kontrast|6.2 Farben und Kontrast]].

### 3. Kein Stylesheet setzt eine Farbe oder ein Maß selbst

Farben und Maße stehen in 53 Variablen, nicht in den Stylesheets. Das ist keine Kosmetik: Nach dem
Import bleiben Variablen in der App unter *Stile → Variablen* bearbeitbar; ein Wert, der in einer
Stylesheet-Datei steht, nicht. Was trotzdem als Zahl in einer Datei steht, ist benannt und
begründet — die Callout- und Syntaxfarben, weil sie einen Status bedeuten und keine Palette sind;
die Haarlinien; und die Umbruchbreiten, weil eine [[7-nachschlagen/01-glossar#Media-Query|Media-Query]] keine Variable lesen kann. Mehr unter
[[6-anpassen/04-variablen|6.4 Variablen]].

## Was die Vorlage nicht enthält

**Keinen Inhalt.** Die Notizen dieser Website reisen nicht mit der Vorlage; sie liegen in einem
eigenen Obsidian-Vault. Wer die Vorlage importiert, bekommt die Gestaltung und schreibt seine
eigenen Seiten hinein.

**Keine Bilder und keine Schnipsel-Dateien.** Ein Vorlagenpaket trägt Stylesheets und
Schriftdateien, sonst keine Dateien. Was das für die eine [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]] bedeutet, die aus einer Datei
liest, steht unter [[6-anpassen/08-das-vorlagenpaket|6.8 Das Vorlagenpaket]].
