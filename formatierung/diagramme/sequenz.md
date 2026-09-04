---
title: Sequenzdiagramme
description: Wer sagt wem was, in welcher Reihenfolge.
section: Formatierung
tags:
  - formatierung
  - diagramme
---

````md
```mermaid
sequenceDiagram
    Nutzer->>App: Vorlage wählen
    App->>Paket: Vorschau (Dry-Run)
    Paket-->>App: zehn Bausteine
    App->>Projekt: Snapshot anlegen
    App->>Projekt: anwenden
    Projekt-->>Nutzer: fertig, ohne Warnungen
```
````

```mermaid
sequenceDiagram
    Nutzer->>App: Vorlage wählen
    App->>Paket: Vorschau (Dry-Run)
    Paket-->>App: zehn Bausteine
    App->>Projekt: Snapshot anlegen
    App->>Projekt: anwenden
    Projekt-->>Nutzer: fertig, ohne Warnungen
```

Der durchgezogene Pfeil `->>` ist ein Aufruf, der gestrichelte `-->>` eine Antwort.
