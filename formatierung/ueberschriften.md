---
title: Überschriften
description: Sechs Ebenen — und warum das Inhaltsverzeichnis rechts alle sechs kennt.
section: Formatierung
tags:
  - referenz
  - formatierung
---

Der Seitentitel ist bereits eine `h1`, deshalb beginnt der Text sinnvollerweise bei `##`. Diese
Seite geht trotzdem bis zur sechsten Ebene, damit das Inhaltsverzeichnis rechts jede Stufe zeigt.

```md
# Ebene 1 — der Seitentitel
## Ebene 2
### Ebene 3
#### Ebene 4
##### Ebene 5
###### Ebene 6
```

## Ebene 2

Ab hier gliedert sich die Seite. Die Vorlage gibt jeder Ebene bis vier eine eigene Größe; Ebene 5
und 6 wechseln stattdessen zu Versalien, weil ein Größenunterschied von einem Pixel keine
Information ist, die jemand lesen kann.

### Ebene 3

Der Abstand einer Überschrift liegt über ihr, nicht darunter: die Lücke sagt, was zur Überschrift
gehört.

#### Ebene 4

Im Inhaltsverzeichnis rechts rückt jede Ebene um dasselbe Maß ein wie im Explorer links.

##### Ebene 5

Ab hier wird nicht weiter eingerückt — fünf Einrückungen lassen in einer 260 Pixel breiten Spalte
kein Wort mehr übrig. Stattdessen bekommt der Eintrag einen Punkt als Marke.

###### Ebene 6

Die tiefste Ebene, mit zwei Punkten markiert.

## Trennlinien

```md
---
```

---

## Absätze

```md
Ein Absatz.

Ein zweiter Absatz, durch eine Leerzeile getrennt.
```

Ein Absatz.

Ein zweiter Absatz, durch eine Leerzeile getrennt.
