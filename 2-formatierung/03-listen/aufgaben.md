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
kein Zustand — deshalb drei Signale statt einem. Und die Vorlage zeichnet **alle sechs Zustände**,
die Obsidian kennt, nicht nur zwei — siehe unten.

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

Alle vier kommen auf der Website an, und diese Vorlage zeichnet sie — jedes Zeichen bekommt seine
eigene Marke im Kästchen:

| Zeichen | Marke | Farbe | Text |
| --- | --- | --- | --- |
| `[ ]` | leeres Kästchen | gedämpft | normal |
| `[x]` | Haken | Akzent | durchgestrichen |
| `[/]` | Schrägstrich | Akzent | normal |
| `[-]` | Minus | gedämpft | durchgestrichen |
| `[>]` | Pfeil nach rechts | gedämpft | normal |
| `[?]` | Fragezeichen | gedämpft | normal |

Die Farbe trennt zwei Gruppen: Akzent für das, was noch irgendwohin führt, gedämpft für das, was
liegen bleibt. Wer die Zeichen nicht kennt, sieht wenigstens diese zwei Gruppen.

> [!note] Das war nicht immer so
> Bis vor Kurzem behielt Quartz nur `[ ]` und `[x]`, alles andere wurde ein leeres Kästchen und das
> Zeichen war weg. Seit das Obsidian-Plugin es als `data-task` an die Zeile schreibt, ist es da —
> und seitdem kann eine Vorlage etwas damit anfangen.

> [!note] Anklicken geht, aber es bleibt in diesem Browser
> Auf der gebauten Website lässt sich ein offenes Kästchen anhaken. Gemessen: Quartz merkt sich das
> in `localStorage` dieses Browsers und stellt es beim nächsten Besuch wieder her — in deiner Notiz
> steht danach trotzdem nichts anderes, und ein anderer Browser sieht die Liste wieder wie
> geschrieben. Abgehakt wird also weiterhin in Obsidian; der Haken auf der Website ist eine Notiz an
> dich selbst.
