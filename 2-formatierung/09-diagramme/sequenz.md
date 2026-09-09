---
title: Sequenzdiagramme
description: Wer sagt wem was, in welcher Reihenfolge.
section: 2 – Formatierung
tags:
  - formatierung
  - diagramme
translationKey: formatierung/diagramme/sequenz
cover: "[[assets/covers/cover-diagramme.svg]]"
---

````md
```mermaid
sequenceDiagram
    Nutzer->>App: Vorlage wählen
    App->>Paket: Vorschau (Dry-Run)
    Paket-->>App: zwölf Bausteine
    App->>Projekt: Snapshot anlegen
    App->>Projekt: anwenden
    Projekt-->>Nutzer: fertig, ohne Warnungen
```
````

```mermaid
sequenceDiagram
    Nutzer->>App: Vorlage wählen
    App->>Paket: Vorschau (Dry-Run)
    Paket-->>App: zwölf Bausteine
    App->>Projekt: Snapshot anlegen
    App->>Projekt: anwenden
    Projekt-->>Nutzer: fertig, ohne Warnungen
```

Der durchgezogene Pfeil `->>` ist ein Aufruf, der gestrichelte `-->>` eine Antwort.
