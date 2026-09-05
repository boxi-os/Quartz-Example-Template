---
title: Excalidraw
description: Handgezeichnet wirkende Diagramme, die auf der Website interaktiv bleiben.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - excalidraw
translationKey: obsidian-formate/excalidraw/index
---

Excalidraw ist ein Zeichenwerkzeug für Skizzen, Diagramme und Abläufe. Als Obsidian-Plugin
speichert es die Zeichnung in einer `.excalidraw.md` — einer Markdown-Datei mit eingebettetem JSON.

Die Zeichnung in diesem Vault:
[[obsidian-formate/excalidraw/Aufbau des editorial-Frames.excalidraw|Aufbau des editorial-Frames]]

Wie das Format aufgebaut ist: [[obsidian-formate/excalidraw/wie-es-funktioniert|Wie es funktioniert]].

## Was das Quartz-Plugin daraus macht

Kein Bild, sondern **interaktives SVG**: Man kann zoomen und verschieben. Formen, Text, Pfeile und
Freihandstriche werden nachgezeichnet, Farben passen sich dem Farbschema an — das Plugin führt dafür
eine Tabelle mit 63 Paaren, je einer hellen Excalidraw-Farbe und ihrer dunklen Entsprechung.

Eingebettete Notizen (`[[notiz]]` in der Zeichnung) werden aufgelöst und mit ihrem Inhalt
dargestellt.

## Zwei Dinge, die man wissen sollte

**Zum Bearbeiten braucht der Vault das Plugin.** In diesem Vault ist es installiert. Ohne das
Plugin zeigt Obsidian nur den Warnhinweis oben in der Datei.

**Das Plugin ist kein Kernbestandteil von Quartz.** Es muss über die Plugin-Verwaltung installiert
werden — anders als Bases und Canvas, die schon dabei sind.

> [!warning] Die Zeichnungsseite steht für sich
> Anders als bei Canvas bringt hier das Plugin sein eigenes Seitenraster mit, und diese Vorlage
> überschreibt es nicht. Auf einer Zeichnungsseite gibt es deshalb weder Explorer noch
> Seitenapparat — und, gemessen am gebauten Markup, auch **keinen Sprachumschalter**: Die beiden
> Zeichnungen sind das einzige Seitenpaar dieser Website, das gar nicht verknüpft ist. Siehe
> [[gestaltung/mehrsprachigkeit/verknuepfung|Wie die Sprachen sich finden]].
