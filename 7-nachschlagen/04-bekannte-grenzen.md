---
title: 7.4 – Bekannte Grenzen
description: Was nicht geht, warum nicht, und was die Vorlage stattdessen tut — gesammelt aus allen Kapiteln, je mit dem Verweis auf die Seite, die es ausführt.
section: 7 – Nachschlagen
tags:
  - nachschlagen
  - referenz
translationKey: nachschlagen/bekannte-grenzen
---

Alles hier ist an der gebauten Website gemessen, nicht vermutet. Die meisten Punkte sind Grenzen
von Quartz oder eines [[7-nachschlagen/01-glossar#Plugin|Plugins]], die eine Vorlage nicht beheben, nur umgehen kann; ein paar sind
Grenzen von QuartzControl, und die sind gemeldet. Die verlinkte Seite hat jeweils die Einzelheiten.

## Beim Schreiben

| Grenze | Was stattdessen | Wo |
| --- | --- | --- |
| Aufgaben kennen auf der Website nur offen und erledigt; `[/]`, `[-]`, `[?]` werden leere Kästchen | den Zustand in den Text schreiben | [[2-formatierung/03-listen/aufgaben\|Aufgaben]] |
| Inline-Fußnoten `^[…]` bleiben Rohtext | die Fußnote mit `[^1]` schreiben | [[2-formatierung/10-fussnoten/varianten\|Varianten]] |
| Pfeile wie `-->` werden nicht zu → | das Zeichen → direkt schreiben | [[2-formatierung/13-besonderes/pfeile-und-emoji\|Pfeile und Emoji]] |
| Ein Tag im Fließtext hat einen kaputten Link — ein Fehler in Quartz | Tags ins [[7-nachschlagen/01-glossar#Frontmatter\|Frontmatter]] | [[2-formatierung/13-besonderes/pfeile-und-emoji\|Pfeile und Emoji]] |
| Ein Bild hat entweder eine Größe oder einen Alternativtext, nicht beides | Größe über [[7-nachschlagen/01-glossar#HTML\|HTML]] setzen, wenn beides nötig ist | [[2-formatierung/12-medien/bilder\|Bilder]] |
| Ein eingebettetes PDF beginnt immer auf Seite 1 | den Seitenanker nur im Link nutzen | [[2-formatierung/12-medien/dokumente\|Dokumente]] |
| Definitionslisten gibt es nicht | eine HTML-Liste `<dl>` | [[2-formatierung/13-besonderes/html\|HTML]] |
| [[7-nachschlagen/01-glossar#Mermaid\|Mermaid]] ignoriert fast alle Farben der Vorlage; jede eigene Regel braucht `!important` | das mitgelieferte [[7-nachschlagen/01-glossar#Stylesheet\|Stylesheet]], das genau das tut | [[6-anpassen/01-etwas-aendern\|6.1 – Etwas ändern]] |

## Bases, Canvas, Zeichnungen

| Grenze | Was stattdessen | Wo |
| --- | --- | --- |
| [[7-nachschlagen/01-glossar#Base\|Bases]] sprechen Englisch: „Showing 45 of 45 entries“ und englische Spaltenköpfe kommen aus dem Plugin und lassen sich nicht übersetzen | die Zeile ist leise gesetzt statt entfernt | [[3-obsidian-formate/01-bases/index\|3.1 – Bases]] |
| Eine Base kann nicht nach einer Formel gruppieren | nach einem Frontmatter-Feld gruppieren | [[3-obsidian-formate/01-bases/wie-es-funktioniert\|Wie eine Base aufgebaut ist]] |
| Links in einem Canvas-Dateiknoten bekommen den Ordner noch einmal vorangestellt und führen je nach Tiefe der Notiz ins Leere — ein Fehler im Plugin | Knoten aus zweiter oder dritter Ebene wählen; sonst den Knotentitel anklicken | [[3-obsidian-formate/02-canvas/index\|3.2 – Canvas]] |
| Eine `.base`- oder `.canvas`-Datei hat kein Frontmatter und kann keine Übersetzung verknüpfen | der Umschalter bietet die Startseite der anderen Sprache | [[6-anpassen/07-zwei-sprachen/grenzen\|Wo die zwei Sprachen aufhören]] |
| Eine Excalidraw-Seite hat weder Seitenleisten noch Sprachumschalter | — | [[3-obsidian-formate/03-excalidraw/index\|3.3 – Excalidraw]] |

## Navigation und Seiten

| Grenze | Was stattdessen | Wo |
| --- | --- | --- |
| Der [[7-nachschlagen/01-glossar#Explorer\|Explorer]] startet zugeklappt; die Option `folderDefaultState: open` wird vom Plugin nicht gelesen | offen sind die Ordner auf dem Weg zur aktuellen Seite | [[5-gestaltung/01-navigation/explorer\|Explorer]] |
| Der Explorer sortiert nach Titel, nicht nach Dateiname, und die Sortierung ist aus der Konfiguration nicht änderbar | Nummern im Titel | [[5-gestaltung/01-navigation/explorer\|Explorer]] |
| Der Explorer lässt sich nicht aus der Konfiguration nach Sprache filtern | ein Stylesheet blendet den fremdsprachigen Ast aus | [[6-anpassen/07-zwei-sprachen/grenzen\|Wo die zwei Sprachen aufhören]] |
| Die Oberfläche — Explorer, Suche, [[7-nachschlagen/01-glossar#Rückverweise\|Rückverweise]], [[7-nachschlagen/01-glossar#Graph\|Graph]] — spricht site-weit eine Sprache; Suche, Graph und „Zuletzt geändert“ mischen beide Sprachen; es gibt eine Fehlerseite für beide | die [[7-nachschlagen/01-glossar#Layout-Box\|Layout-Boxen]] sprechen beide Sprachen; ein [[7-nachschlagen/01-glossar#Build\|Build]] je Sprache würde den Rest lösen | [[6-anpassen/07-zwei-sprachen/grenzen\|Wo die zwei Sprachen aufhören]] |
| Quartz rendert keinen Skip-Link; per Tastatur kostet der Weg zum Text einen Tabstopp je Baumzeile | die Gestaltung dafür liegt bereit | [[6-anpassen/06-barrierefreiheit\|6.6 – Barrierefreiheit]] |
| Das Datum einer Seite kommt nicht aus [[7-nachschlagen/01-glossar#git\|git]], weil `content/` ein [[7-nachschlagen/01-glossar#Symlink\|Symlink]] ist — ein Fehler im Plugin | Datum im Frontmatter | [[4-seiten-steuern/01-titel-beschreibung-datum\|4.1 – Titel, Beschreibung, Datum]] |

## In QuartzControl

| Grenze | Was stattdessen | Wo |
| --- | --- | --- |
| Nur eine der fünf Layout-Boxen überlebt den Import einer Vorlage | die anderen vier neu anlegen | [[6-anpassen/08-das-vorlagenpaket\|6.8 – Das Vorlagenpaket]] |
| Ein Vorlagenpaket trägt keine Bilder und keine Schnipsel-Dateien | Inline-HTML und Inline-SVG; eine Datei von Hand kopieren | [[6-anpassen/08-das-vorlagenpaket\|6.8 – Das Vorlagenpaket]] |
| Der [[7-nachschlagen/01-glossar#Baustein\|Baustein]] Übersetzungen erreicht die Überschriften der Komponenten nicht | — | [[6-anpassen/08-das-vorlagenpaket\|6.8 – Das Vorlagenpaket]] |
| [[7-nachschlagen/01-glossar#Snapshot\|Snapshots]] enthalten den Inhalt nicht, wenn `content/` ein Symlink ist | der [[7-nachschlagen/01-glossar#Vault\|Vault]] sichert sich über sein eigenes git | [[1-einstieg/03-von-der-notiz-zur-website\|1.3 – Von der Notiz zur Website]] |
| Die App schreibt `@font-face`-Regeln ohne Gewicht und Stil | die Regeln sind von Hand korrigiert | [[6-anpassen/03-schriften\|6.3 – Schriften]] |
| Im Frame-Editor darf ein Wert kein Komma enthalten, und Längen stehen als Zahl, nicht als Variable | `calc()` ohne Komma; Zahlen | [[6-anpassen/05-seitenraster\|6.5 – Seitenraster]] |
| Drei Blöcke in `custom.scss` schreibt die App bei jedem Speichern neu | eigene Regeln außerhalb der Markierungen oder in eine eigene Datei | [[6-anpassen/01-etwas-aendern\|6.1 – Etwas ändern]] |
