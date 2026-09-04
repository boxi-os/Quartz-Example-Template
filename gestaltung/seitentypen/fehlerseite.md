---
title: Fehlerseite
description: Was bei einer nicht vorhandenen Adresse erscheint.
section: Gestaltung
tags:
  - gestaltung
  - seitentypen
---

## Von Haus aus

Die 404-Seite nutzt dasselbe dreispaltige Raster wie jede andere Seite — mit Explorer, Graph und
Rückverweisen um eine Fehlermeldung herum.

## In dieser Vorlage

Sie nutzt den Frame **`focus`**: eine Spalte, 680 px, zentriert, mit viel Luft nach oben. Kein
Explorer, kein Graph, kein Inhaltsverzeichnis.

Doppelt abgesichert: Der Frame blendet die Bereiche geometrisch aus, und die Konfiguration leert
die Positionen zusätzlich (`positions: { left: [], right: [], … }`) — so werden die Komponenten
gar nicht erst gebaut.

Der Text steht zentriert, die Überschrift groß, darunter ein Satz in gedämpfter Farbe.

> [!tip] Warum das eine eigene Entscheidung ist
> Wer auf einer Fehlerseite landet, sucht einen Weg zurück — nicht eine Umgebungsanzeige seiner
> nicht existierenden Notiz. Alles, was nicht dabei hilft, ist Dekoration auf einem Fehler.

Ausprobieren: eine beliebige nicht existierende Adresse aufrufen.
