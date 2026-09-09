---
title: 3.3 – Excalidraw
description: Handgezeichnet wirkende Diagramme, die auf der Website interaktiv bleiben.
section: 3 – Obsidian-Formate
tags:
  - obsidian-formate
  - excalidraw
translationKey: obsidian-formate/excalidraw/index
---

Excalidraw ist ein Zeichenwerkzeug für Skizzen, Diagramme und Abläufe. Als Obsidian-Plugin
speichert es die Zeichnung in einer `.excalidraw.md` — einer Markdown-Datei mit eingebettetem JSON.

Die Zeichnung in diesem [[7-nachschlagen/01-glossar#Vault|Vault]]:
[[3-obsidian-formate/03-excalidraw/Aufbau des editorial-Frames.excalidraw|Aufbau des editorial-Frames]]

Wie das Format aufgebaut ist: [[3-obsidian-formate/03-excalidraw/wie-es-funktioniert|Wie es funktioniert]].

## Was das Quartz-Plugin daraus macht

Kein Bild, sondern **interaktives SVG**: Man kann zoomen und verschieben. Formen, Text, Pfeile und
Freihandstriche werden nachgezeichnet, Farben passen sich dem [[7-nachschlagen/01-glossar#Farbschema|Farbschema]] an — das [[7-nachschlagen/01-glossar#Plugin|Plugin]] führt dafür
eine Tabelle mit 63 Paaren, je einer hellen Excalidraw-Farbe und ihrer dunklen Entsprechung.

Eingebettete Notizen (`[[notiz]]` in der Zeichnung) werden aufgelöst und mit ihrem Inhalt
dargestellt.

## Zwei Dinge, die man wissen sollte

**Zum Bearbeiten braucht der Vault das Plugin.** In diesem Vault ist es installiert. Ohne das
Plugin zeigt Obsidian nur den Warnhinweis oben in der Datei.

**Das Plugin ist kein Kernbestandteil von Quartz.** Es muss über die Plugin-Verwaltung installiert
werden — anders als [[7-nachschlagen/01-glossar#Base|Bases]] und [[7-nachschlagen/01-glossar#Canvas|Canvas]], die schon dabei sind.

> [!warning] Die Zeichnungsseite steht für sich
> Anders als bei Canvas bringt hier das Plugin sein eigenes Seitenraster mit, und diese Vorlage
> überschreibt es nicht. Auf einer Zeichnungsseite gibt es deshalb weder [[7-nachschlagen/01-glossar#Explorer|Explorer]] noch
> Seitenapparat — und, gemessen am gebauten Markup, auch **keinen Sprachumschalter**: Die beiden
> Zeichnungen sind das einzige Seitenpaar dieser Website, das gar nicht verknüpft ist. Siehe
> [[6-anpassen/07-zwei-sprachen/verknuepfung|Wie die Sprachen sich finden]].

## Die Seiten

- [[3-obsidian-formate/03-excalidraw/Aufbau des editorial-Frames.excalidraw|Aufbau des editorial-Frames.excalidraw]]
- [[3-obsidian-formate/03-excalidraw/wie-es-funktioniert|Wie eine Excalidraw-Datei aufgebaut ist]] — [[7-nachschlagen/01-glossar#Markdown|Markdown]] außen, Zeichendaten innen — und der zweite, einfachere Weg.
