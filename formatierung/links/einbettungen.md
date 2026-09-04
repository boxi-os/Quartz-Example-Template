---
title: Einbettungen
description: Eine andere Seite mitten in dieser anzeigen.
section: Formatierung
tags:
  - formatierung
  - links
---

Ein Ausrufezeichen vor dem Wikilink bettet den Inhalt ein, statt darauf zu verweisen.

```md
![[formatierung/struktur/trennlinien]]
```

![[formatierung/struktur/trennlinien]]

## Nur einen Abschnitt

```md
![[formatierung/links/wikilinks#Kurzform]]
```

![[formatierung/links/wikilinks#Kurzform]]

## In dieser Vorlage

Eine eingebettete Seite bekommt einen gestrichelten Balken links und eine getönte Fläche — man soll
sehen, wo fremder Inhalt anfängt und aufhört. **Von Haus aus** ist die Einbettung optisch nicht vom
umgebenden Text getrennt.

> [!warning] Vorsicht mit Ketten
> Bettet die eingebettete Seite ihrerseits etwas ein, wird die Seite schnell unübersichtlich — und
> ein Kreis (A bettet B ein, B bettet A ein) ist ein Fehler, den erst der Build zeigt.
