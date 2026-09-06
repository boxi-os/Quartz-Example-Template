---
title: Überschriften
description: Sechs Ebenen — und warum die letzten beiden hier nicht weiter schrumpfen.
section: Formatierung
tags:
  - formatierung
  - struktur
translationKey: formatierung/struktur/ueberschriften
cover: "[[assets/covers/cover-struktur.svg]]"
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

Ab hier gliedert sich die Seite.

### Ebene 3

Der Abstand einer Überschrift liegt über ihr, nicht darunter: Die Lücke sagt, was zur Überschrift
gehört.

#### Ebene 4

Bis hierher unterscheiden sich die Ebenen in der Größe.

##### Ebene 5

Ab hier nicht mehr. Fünf und sechs wechseln zu Versalien und Sperrung, weil ein Unterschied von
einem oder zwei Pixeln keine Information ist, die jemand zuverlässig erkennt.

###### Ebene 6

Die tiefste Ebene, kleiner und gedämpft.

## Was diese Vorlage anders macht

**Von Haus aus** setzt Quartz alle sechs Ebenen in derselben Schrift mit fallender Größe, die
Abstände liegen ober- und unterhalb.

**In dieser Vorlage** liegt der Abstand nur oben, die Schriftgröße folgt einer benannten Skala
(`--tpl-text-3xl` bis `--tpl-text-sm`), und die beiden tiefsten Ebenen wechseln das Mittel statt
die Größe. Mehr dazu: [[gestaltung/im-inhalt/fliesstext|Fließtext]].
