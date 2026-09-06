---
title: Structure diagrams
description: Classes, entities and mind maps.
section: Formatting
tags:
  - formatting
  - diagrams
translationKey: formatierung/diagramme/struktur
cover: "[[assets/covers/cover-diagramme.svg]]"
---

## Class diagram

````md
```mermaid
classDiagram
    class TemplatePackage {
        +manifest.json
        +parts/
        +files/
        +read()
    }
    class Part {
        +collect()
        +plan()
        +apply()
    }
    class Frame {
        +id
        +breakpoints
    }
    TemplatePackage "1" --> "10" Part
    Part <|-- Frame
```
````

```mermaid
classDiagram
    class TemplatePackage {
        +manifest.json
        +parts/
        +files/
        +read()
    }
    class Part {
        +collect()
        +plan()
        +apply()
    }
    class Frame {
        +id
        +breakpoints
    }
    TemplatePackage "1" --> "10" Part
    Part <|-- Frame
```

> [!warning] Annotations with angle brackets do not work here
> For classes [[en/7-reference/01-glossary#Mermaid|Mermaid]] knows an annotation of the form `<` `<interface>` `>`. In Quartz it does not
> survive: the content of a Mermaid block runs through the same [[en/7-reference/01-glossary#HTML|HTML]] processing as the rest of the
> text, and the double angle brackets are read as a tag and removed. What is left is a single `>` —
> and the diagram fails with *Syntax error in text*.
>
> Measured on this page: the source parses without error in Mermaid itself; in the built HTML the
> start of the block is missing. Anyone wanting to mark an interface uses a note
> (`note for Part "Interface"`) or writes it into the class name.

## Entity relationship

````md
```mermaid
erDiagram
    VAULT ||--o{ NOTE : contains
    NOTE ||--o{ TAG : carries
    NOTE }o--o{ NOTE : links-to
    VAULT {
        string path
        int notes
    }
    NOTE {
        string title
        date changed
    }
```
````

```mermaid
erDiagram
    VAULT ||--o{ NOTE : contains
    NOTE ||--o{ TAG : carries
    NOTE }o--o{ NOTE : links-to
    VAULT {
        string path
        int notes
    }
    NOTE {
        string title
        date changed
    }
```

## Mind map

````md
```mermaid
mindmap
  root((Template))
    Design
      Colours
      Typefaces
      Tokens
    Structure
      Frames
      Layout
    Content
      Notes
      Bases
      Canvas
```
````

```mermaid
mindmap
  root((Template))
    Design
      Colours
      Typefaces
      Tokens
    Structure
      Frames
      Layout
    Content
      Notes
      Bases
      Canvas
```
