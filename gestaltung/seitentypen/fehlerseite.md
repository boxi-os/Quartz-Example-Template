---
title: Fehlerseite
description: Was bei einer nicht vorhandenen Adresse erscheint.
section: Gestaltung
tags:
  - gestaltung
  - seitentypen
---

## Von Haus aus

Die 404-Seite nutzt dasselbe Raster wie jede andere Seite — mit Explorer, Graph und Rückverweisen
um eine Fehlermeldung herum.

## In dieser Vorlage

Sie nutzt den Frame **`focus`**. Der steht auf demselben Zwölf-Spalten-Raster wie alles andere und
setzt die Meldung in dieselben sechs Spalten, in denen sonst der Artikel steht — beide Randspalten
bleiben reserviert und leer. Das ist der Punkt: Eine Fehlerseite, die ihren Text irgendwo anders
hinsetzt als der Rest der Site, wirkt wie eine fremde Seite und nicht wie eine fehlende.

Die Randspalten sind leer, weil die Konfiguration ihre Komponentenlisten leert
(`positions: { left: [], right: [], … }`) — sie werden gar nicht erst gebaut. Kein Explorer, kein
Graph, kein Inhaltsverzeichnis. Kopfbereich und Fußzeile bleiben, und mit dem Kopf seit dem Umzug
der Werkzeugleiste auch Suche und Farbschema-Umschalter — vorher gab es auf der Fehlerseite beides
nicht.

Die Luft nach oben setzt das Stylesheet der Seite, nicht der Frame: Der Innenabstand eines Frames
verschiebt auch den Kopfbereich, und eine Site, deren Wortmarke auf der Fehlerseite sechzig Pixel
tiefer sitzt, sieht kaputt aus statt ruhig.

> [!tip] Warum das eine eigene Entscheidung ist
> Wer auf einer Fehlerseite landet, sucht einen Weg zurück — nicht eine Umgebungsanzeige seiner
> nicht existierenden Notiz. Alles, was nicht dabei hilft, ist Dekoration auf einem Fehler.

Ausprobieren: eine beliebige nicht existierende Adresse aufrufen.
