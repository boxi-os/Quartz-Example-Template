---
title: Number diagrams
description: Pies, curves, flows and quadrant charts.
section: Formatting
tags:
  - formatting
  - diagrams
translationKey: formatierung/diagramme/zahlen
cover: "[[assets/covers/cover-diagramme.svg]]"
---

## Pie chart

````md
```mermaid
pie title Lines per area
    "Notes" : 10900
    "Stylesheets" : 4900
    "Script" : 2100
    "Configuration" : 500
```
````

```mermaid
pie title Lines per area
    "Notes" : 10900
    "Stylesheets" : 4900
    "Script" : 2100
    "Configuration" : 500
```

The numbers are real, rounded to hundreds and measured on 2026-09-05: notes are both languages
together, stylesheets the 34 files under `quartz/styles/custom/`, script the template build in the
app repository. They grow; the diagram does not follow on its own.

## Quadrant chart

````md
```mermaid
quadrantChart
    title Effort and effect
    x-axis Little effort --> Much effort
    y-axis Small effect --> Large effect
    quadrant-1 Do
    quadrant-2 Plan
    quadrant-3 Drop
    quadrant-4 Delegate
    Readable body text: [0.2, 0.9]
    Measure contrast: [0.4, 0.85]
    Frames of your own: [0.8, 0.6]
    Callout colours: [0.3, 0.7]
```
````

```mermaid
quadrantChart
    title Effort and effect
    x-axis Little effort --> Much effort
    y-axis Small effect --> Large effect
    quadrant-1 Do
    quadrant-2 Plan
    quadrant-3 Drop
    quadrant-4 Delegate
    Readable body text: [0.2, 0.9]
    Measure contrast: [0.4, 0.85]
    Frames of your own: [0.8, 0.6]
    Callout colours: [0.3, 0.7]
```

## Flow quantities

````md
```mermaid
sankey-beta
Vault,Notes,100
Vault,Bases,2
Vault,Canvas,1
Notes,Formatting,45
Notes,Design,30
Notes,Handbook,10
```
````

```mermaid
sankey-beta
Vault,Notes,100
Vault,Bases,2
Vault,Canvas,1
Notes,Formatting,45
Notes,Design,30
Notes,Handbook,10
```

## Curves and bars

````md
```mermaid
xychart-beta
    title "Pages per pass"
    x-axis [Start, Rebuild, Bases, Mermaid]
    y-axis "Pages" 0 --> 110
    bar [31, 75, 100, 103]
    line [31, 75, 100, 103]
```
````

```mermaid
xychart-beta
    title "Pages per pass"
    x-axis [Start, Rebuild, Bases, Mermaid]
    y-axis "Pages" 0 --> 110
    bar [31, 75, 100, 103]
    line [31, 75, 100, 103]
```
