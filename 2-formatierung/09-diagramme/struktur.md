---
title: Struktur-Diagramme
description: Klassen, Entitäten und Mindmaps.
section: 2 Formatierung
tags:
  - formatierung
  - diagramme
translationKey: formatierung/diagramme/struktur
cover: "[[assets/covers/cover-diagramme.svg]]"
---

## Klassendiagramm

````md
```mermaid
classDiagram
    class Vorlagenpaket {
        +manifest.json
        +parts/
        +files/
        +lesen()
    }
    class Baustein {
        +collect()
        +plan()
        +apply()
    }
    class Frame {
        +id
        +breakpoints
    }
    Vorlagenpaket "1" --> "10" Baustein
    Baustein <|-- Frame
```
````

```mermaid
classDiagram
    class Vorlagenpaket {
        +manifest.json
        +parts/
        +files/
        +lesen()
    }
    class Baustein {
        +collect()
        +plan()
        +apply()
    }
    class Frame {
        +id
        +breakpoints
    }
    Vorlagenpaket "1" --> "10" Baustein
    Baustein <|-- Frame
```

> [!warning] Annotationen mit spitzen Klammern gehen hier nicht
> [[7-nachschlagen/01-glossar#Mermaid|Mermaid]] kennt für Klassen eine Annotation in der Form `<` `<Schnittstelle>` `>`. In Quartz
> überlebt sie nicht: Der Inhalt eines Mermaid-Blocks läuft durch dieselbe HTML-Verarbeitung wie
> der übrige Text, und die doppelten spitzen Klammern werden als Tag gelesen und entfernt. Übrig
> bleibt ein einzelnes `>` — und das Diagramm scheitert mit *Syntax error in text*.
>
> Gemessen an dieser Seite: Der Quelltext parst in Mermaid selbst fehlerfrei, im gebauten [[7-nachschlagen/01-glossar#HTML|HTML]] fehlt
> der Anfang des Blocks. Wer eine Schnittstelle kennzeichnen will, nimmt eine Anmerkung
> (`note for Baustein "Schnittstelle"`) oder schreibt es in den Klassennamen.

## Entity-Relationship

````md
```mermaid
erDiagram
    VAULT ||--o{ NOTIZ : enthaelt
    NOTIZ ||--o{ TAG : traegt
    NOTIZ }o--o{ NOTIZ : verweist-auf
    VAULT {
        string pfad
        int notizen
    }
    NOTIZ {
        string titel
        date geaendert
    }
```
````

```mermaid
erDiagram
    VAULT ||--o{ NOTIZ : enthaelt
    NOTIZ ||--o{ TAG : traegt
    NOTIZ }o--o{ NOTIZ : verweist-auf
    VAULT {
        string pfad
        int notizen
    }
    NOTIZ {
        string titel
        date geaendert
    }
```

## Mindmap

````md
```mermaid
mindmap
  root((Vorlage))
    Gestaltung
      Farben
      Schriften
      Tokens
    Struktur
      Frames
      Layout
    Inhalt
      Notizen
      Bases
      Canvas
```
````

```mermaid
mindmap
  root((Vorlage))
    Gestaltung
      Farben
      Schriften
      Tokens
    Struktur
      Frames
      Layout
    Inhalt
      Notizen
      Bases
      Canvas
```
