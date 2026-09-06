---
title: Aufgabenlisten
description: Kästchen zum Abhaken — und warum Erledigtes hier zweifach markiert ist.
section: 2 Formatierung
tags:
  - formatierung
  - listen
translationKey: formatierung/listen/aufgaben
cover: "[[assets/covers/cover-listen.svg]]"
---

```md
- [ ] Offen
- [x] Erledigt
- [ ] Mit Unterpunkten
  - [x] Teil eins
  - [ ] Teil zwei
```

- [ ] Offen
- [x] Erledigt
- [ ] Mit Unterpunkten
  - [x] Teil eins
  - [ ] Teil zwei

## Was diese Vorlage anders macht

**Von Haus aus** zeigt Quartz ein angehaktes Kästchen und lässt den Text unverändert.

**In dieser Vorlage** bekommt ein erledigter Punkt zusätzlich gedämpfte Farbe *und* eine
Durchstreichung. Ein Zustand, der nur an einem kleinen Häkchen hängt, ist für einen Teil der Leser
kein Zustand — deshalb drei Signale statt einem.

Außerdem verliert die Liste ihre Aufzählungspunkte, sobald sie Kästchen enthält: Punkt und Kästchen
nebeneinander sind eine Marke zu viel.

## Andere Zeichen im Kästchen

Obsidian erlaubt beliebige Zeichen zwischen den Klammern und zeigt dafür eigene Symbole:

```md
- [/] halb erledigt
- [-] verworfen
- [>] verschoben
- [?] fraglich
```

- [/] halb erledigt
- [-] verworfen
- [>] verschoben
- [?] fraglich

> [!warning] Auf der Website bleibt nur offen und erledigt
> Gemessen: Von allen Zeichen erkennt Quartz nur `[ ]` und `[x]` als Zustand — der Rest wird zu
> einem leeren Kästchen, das Zeichen geht verloren. Wer die Zwischenzustände auch auf der Website
> braucht, schreibt sie in den Text statt in die Klammer.

> [!note] Anklickbar sind sie nicht
> Auf einer gebauten Website ist das Kästchen eine Anzeige, kein Bedienelement. Abgehakt wird in
> Obsidian.
