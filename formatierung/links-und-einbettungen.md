---
title: Links und Einbettungen
description: Wikilinks, Aliasse, Sprungmarken, Blockreferenzen und Transklusion.
section: Formatierung
tags:
  - referenz
  - formatierung
  - links
---

## Interner Link (Wikilink)

```md
[[handbuch/index]]
[[handbuch/index|mit eigenem Text]]
```

[[handbuch/index]]
[[handbuch/index|mit eigenem Text]]

## Auf eine Überschrift

```md
[[formatierung/ueberschriften#Trennlinien|zu den Trennlinien]]
```

[[formatierung/ueberschriften#Trennlinien|zu den Trennlinien]]

## Externer Link

```md
[Quartz](https://quartz.jzhao.xyz/)
<https://quartz.jzhao.xyz/>
```

[Quartz](https://quartz.jzhao.xyz/)
<https://quartz.jzhao.xyz/>

> [!note] Externe Links sind markiert
> Ein Link nach außen bekommt einen Pfeil. Das ist kein Schmuck: die Farbe allein sagt nicht, dass
> man die Seite verlässt.

## Link auf eine Seite, die es nicht gibt

```md
[[gibt-es-nicht]]
```

[[gibt-es-nicht]]

Ein Wikilink ins Leere wird gepunktet unterstrichen — er sieht unfertig aus, nicht kaputt.

## Blockreferenz

Ein Block bekommt eine Kennung, auf die woanders verwiesen werden kann.

```md
Dieser Absatz hat eine Kennung. ^merksatz

[[formatierung/links-und-einbettungen#^merksatz|Verweis auf den Absatz]]
```

Dieser Absatz hat eine Kennung. ^merksatz

[[formatierung/links-und-einbettungen#^merksatz|Verweis auf den Absatz]]

## Transklusion

Der Inhalt einer anderen Seite wird hier eingesetzt.

```md
![[handbuch/vertiefung/muster]]
```

![[handbuch/vertiefung/muster]]

## Vorschau beim Überfahren

Interne Links zeigen beim Überfahren mit dem Zeiger eine Vorschau. Auf Geräten ohne Zeiger gibt es
sie nicht — deshalb steht nie eine Information ausschließlich in einer Vorschau.
