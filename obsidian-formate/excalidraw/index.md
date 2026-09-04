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
Freihandstriche werden nachgezeichnet, Farben passen sich dem Farbschema an — das Plugin bringt für
alle 65 Excalidraw-Farben eine dunkle Entsprechung mit.

Eingebettete Notizen (`[[notiz]]` in der Zeichnung) werden aufgelöst und mit ihrem Inhalt
dargestellt.

## Zwei Dinge, die man wissen sollte

**Zum Bearbeiten braucht der Vault das Plugin.** In diesem Vault ist es installiert. Ohne das
Plugin zeigt Obsidian nur den Warnhinweis oben in der Datei.

**Das Plugin ist kein Kernbestandteil von Quartz.** Es muss über die Plugin-Verwaltung installiert
werden — anders als Bases und Canvas, die schon dabei sind.
