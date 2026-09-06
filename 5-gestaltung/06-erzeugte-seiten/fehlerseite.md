---
title: Fehlerseite
description: Was bei einer nicht vorhandenen Adresse erscheint.
section: Gestaltung
tags:
  - gestaltung
  - seitentypen
translationKey: gestaltung/erzeugte-seiten/fehlerseite
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

> [!note] Die Fehlerseite hat keine Sprache
> Quartz schreibt eine `404.html` für die ganze Website, sie bleibt also in der Sprache der Site.
> Wer sich in einer englischen Adresse vertippt, landet auf der deutschen Fehlerseite.

Ausprobieren: eine beliebige nicht existierende Adresse aufrufen.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 6 Variablen liest `page-404.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-space-2xl` | `4rem` | 6.4 Variablen |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 4 weitere Komponenten |
| `--tpl-text-3xl` | `2.25rem` | 6.4 Variablen, Titel und Datum |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
