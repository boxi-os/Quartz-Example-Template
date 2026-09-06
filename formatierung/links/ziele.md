---
title: Sprungziele
description: Auf eine Überschrift oder einen einzelnen Block verweisen.
section: Formatierung
tags:
  - formatierung
  - links
translationKey: formatierung/links/ziele
cover: "[[assets/covers/cover-links.svg]]"
---

## Auf eine Überschrift

```md
[[formatierung/struktur/ueberschriften#Ebene 3|zur dritten Ebene]]
```

[[formatierung/struktur/ueberschriften#Ebene 3|zur dritten Ebene]]

## Auf einen Block

Ein Block bekommt am Zeilenende eine Kennung mit `^`:

```md
Dieser Absatz hat eine Kennung. ^merksatz

[[formatierung/links/ziele#^merksatz|Verweis auf den Absatz]]
```

Dieser Absatz hat eine Kennung. ^merksatz

[[formatierung/links/ziele#^merksatz|Verweis auf den Absatz]]

## Innerhalb derselben Seite

```md
[[#Auf einen Block|nach oben zum Block]]
```

[[#Auf einen Block|nach oben zum Block]]

> [!tip] Blockkennungen sind stabil
> Eine Überschrift ändert sich beim Umformulieren, eine Blockkennung nicht. Für Verweise, die
> halten sollen, ist `^kennung` die verlässlichere Wahl.
