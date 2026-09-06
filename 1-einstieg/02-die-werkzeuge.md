---
title: 1.2 Die Werkzeuge
description: Obsidian, Quartz, QuartzControl und git — vier Programme, jedes mit einer Aufgabe, und wie sie zusammenhängen.
section: Einstieg
tags:
  - einstieg
translationKey: einstieg/die-werkzeuge
---

Wer diese Vorlage benutzt, hat mit vier Programmen zu tun. Man muss nicht alle vier bedienen
können — QuartzControl nimmt einem zwei davon ab —, aber man sollte wissen, was jedes tut.

## Obsidian — hier wird geschrieben

Obsidian ist ein Programm für Notizen. Es speichert jede Notiz als gewöhnliche Textdatei mit der
Endung `.md`, geschrieben in **Markdown**: einer einfachen Schreibweise, in der `**fett**` fett
wird und `# Überschrift` eine Überschrift. Ein Ordner voller solcher Dateien heißt in Obsidian
**Vault** (englisch für Tresor). Alle Notizen dieser Website liegen in einem Vault; Kapitel 2
zeigt, was man darin schreiben kann.

## Quartz — hieraus wird eine Website

Quartz ist ein **Static-Site-Generator**: ein Programm, das aus einem Ordner voller
Markdown-Dateien einen Ordner voller HTML-Seiten macht — [[7-nachschlagen/01-glossar#HTML|HTML]] ist die Sprache, die ein Browser
versteht. Diesen Vorgang nennt man **[[7-nachschlagen/01-glossar#Build|Build]]** (Bau). Das Ergebnis ist eine fertige Website ohne
Datenbank und ohne Programm dahinter, die man auf jeden Webspace legen kann. Quartz kennt
Obsidians Schreibweise: [[7-nachschlagen/01-glossar#Wikilink|Wikilinks]], [[7-nachschlagen/01-glossar#Callout|Callouts]] und eingebettete Bilder werden richtig übersetzt.

Quartz besteht aus **Plugins** — [[7-nachschlagen/01-glossar#Baustein|Bausteinen]], von denen jeder eine Aufgabe hat: Einer baut den
[[7-nachschlagen/01-glossar#Explorer|Explorer]] links, einer das Inhaltsverzeichnis rechts, einer die Suche, einer liest das Datum einer
Datei. Welche Plugins es gibt und wie sie eingestellt sind, steht in einer Konfigurationsdatei
namens `quartz.config.yaml` im Projekt.

## QuartzControl — hier wird bedient

QuartzControl ist die Oberfläche für Quartz. Ohne sie bedient man Quartz über die Kommandozeile
und bearbeitet die Konfiguration im Texteditor; mit ihr klickt man. Die App legt Projekte an,
verknüpft den Inhalt mit einem Vault, installiert Plugins, ändert Farben und Schriften, baut
Seitenraster in einem Editor, startet die Vorschau, baut die Website und veröffentlicht sie. Ein
**Projekt** ist dabei ein Ordner mit einer Quartz-Installation; QuartzControl kann mehrere davon
verwalten.

Diese Vorlage ist mit QuartzControl gebaut und für QuartzControl gemacht: Alles, was sie
einstellt, ist in der App sichtbar und änderbar.

## git — hier wird die Geschichte geführt

git ist ein Programm, das die Geschichte von Dateien aufzeichnet. Jeder gespeicherte Stand heißt
**Commit** und trägt Datum, Urheber und eine Beschreibung; man kann jeden früheren Stand
wiederherstellen und zwei Stände vergleichen. So ein Vergleich heißt **Diff** und zeigt Zeile für
Zeile, was sich geändert hat. Ein Ordner, dessen Geschichte git führt, heißt **Repository**.

Man muss git nicht bedienen können, um diese Vorlage zu benutzen. Es kommt trotzdem an drei
Stellen vor: QuartzControl braucht es für neue Projekte, für Plugins aus einer git-Quelle und für
seine [[7-nachschlagen/01-glossar#Snapshot|Snapshots]] — und nimmt das git des Rechners oder bringt ein eigenes mit. Das Datum einer Seite
kann Quartz aus git lesen (hier nicht; warum, steht unter
[[4-seiten-steuern/01-titel-beschreibung-datum|4.1 Titel, Beschreibung, Datum]]). Und wer seine
Website über ein git-Repository veröffentlicht, etwa bei GitHub Pages, schickt sie mit git dorthin.

## Wie sie zusammenhängen

```
Obsidian ─schreibt─▶ Vault ◀─Symlink─ Projekt ─Quartz baut─▶ Website ─▶ Webspace
                                         ▲                       ▲
                                         └───── QuartzControl ───┘
```

Der Vault ist die Quelle. Das Projekt zeigt mit einem **[[7-nachschlagen/01-glossar#Symlink|Symlink]]** darauf — einer Verknüpfung im
Dateisystem, die einen Ordner an einer zweiten Stelle erscheinen lässt, ohne ihn zu kopieren.
Quartz liest den Inhalt durch diesen Link, baut daraus die Website, und QuartzControl steuert
beides. Wie das im Einzelnen abläuft:
[[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]].
