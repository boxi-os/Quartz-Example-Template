---
title: Diagramme
description: Mermaid — Flussdiagramm, Sequenz, Gantt, Klassen.
section: Formatierung
tags:
  - referenz
  - formatierung
---

Mermaid ist Teil des Obsidian-Flavored-Markdown-Plugins und in dieser Vorlage aktiv. Die Diagramme
bringen ihre eigenen Farben mit; die Vorlage gestaltet den Kasten darum und lässt die Zeichnung in
Ruhe — ein halb umgefärbtes Diagramm ist schlechter als ein fremdfarbiges.

## Flussdiagramm

````md
```mermaid
flowchart TD
    A[Vorlage exportieren] --> B{Alle zehn Bausteine?}
    B -->|ja| C[.qtpl schreiben]
    B -->|nein| D[Fehlende ergänzen]
    D --> B
    C --> E[In anderes Projekt importieren]
```
````

```mermaid
flowchart TD
    A[Vorlage exportieren] --> B{Alle zehn Bausteine?}
    B -->|ja| C[.qtpl schreiben]
    B -->|nein| D[Fehlende ergänzen]
    D --> B
    C --> E[In anderes Projekt importieren]
```

## Sequenzdiagramm

````md
```mermaid
sequenceDiagram
    Nutzer->>App: Vorlage wählen
    App->>Paket: Vorschau (Dry-Run)
    Paket-->>App: zehn Bausteine
    App->>Projekt: Snapshot anlegen
    App->>Projekt: anwenden
```
````

```mermaid
sequenceDiagram
    Nutzer->>App: Vorlage wählen
    App->>Paket: Vorschau (Dry-Run)
    Paket-->>App: zehn Bausteine
    App->>Projekt: Snapshot anlegen
    App->>Projekt: anwenden
```

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

## Klassendiagramm

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
