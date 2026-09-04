---
title: Weitere Diagrammarten
description: Gantt, Klassen, Zustände und Torten.
section: Formatierung
tags:
  - formatierung
  - diagramme
---

## Gantt

```mermaid
gantt
    title Aufbau der Vorlage
    dateFormat YYYY-MM-DD
    section Gestaltung
    Palette messen      :a1, 2026-09-03, 1d
    Komponenten stylen  :a2, after a1, 2d
    section Prüfung
    Bauen und messen    :b1, after a2, 1d
    Gegenprobe          :b2, after b1, 1d
```

## Klassen

```mermaid
classDiagram
    class Vorlagenpaket {
        +manifest.json
        +parts/
        +files/
    }
    class Baustein {
        +collect()
        +plan()
        +apply()
    }
    Vorlagenpaket "1" --> "10" Baustein
```

## Zustände

```mermaid
stateDiagram-v2
    [*] --> Entwurf
    Entwurf --> Geprüft: Kontrast gemessen
    Geprüft --> Exportiert: alle zehn Bausteine
    Exportiert --> [*]
```

## In dieser Vorlage

Die Diagramme bringen ihre eigenen Farben mit; die Vorlage gestaltet nur den Kasten darum — Fläche,
Rahmen, Ecken, Scrollverhalten. Ein halb umgefärbtes Diagramm ist schlechter als ein fremdfarbiges,
weil Mermaid seine Farben zur Laufzeit auflöst und ein Stylesheet dabei immer nur die Hälfte trifft.
