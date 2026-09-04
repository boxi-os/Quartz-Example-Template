---
title: Flowcharts
description: Mermaid — processes and decisions.
section: Formatting
tags:
  - formatting
  - diagrams
translationKey: formatierung/diagramme/fluss
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

````md
```mermaid
flowchart TD
    A[Export template] --> B{All ten parts?}
    B -->|yes| C[Write .qtpl]
    B -->|no| D[Add the missing ones]
    D --> B
    C --> E[Import into another project]
```
````

```mermaid
flowchart TD
    A[Export template] --> B{All ten parts?}
    B -->|yes| C[Write .qtpl]
    B -->|no| D[Add the missing ones]
    D --> B
    C --> E[Import into another project]
```

## Direction and shapes

`TD` means top down, `LR` left to right.

````md
```mermaid
flowchart LR
    A[Rectangle] --> B(Rounded corners)
    B --> C{Rhombus}
    C --> D([Stadium])
    C --> E[(Database)]
```
````

```mermaid
flowchart LR
    A[Rectangle] --> B(Rounded corners)
    B --> C{Rhombus}
    C --> D([Stadium])
    C --> E[(Database)]
```
