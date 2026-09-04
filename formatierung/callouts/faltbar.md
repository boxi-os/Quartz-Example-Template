---
title: Faltbare Callouts
description: Ein Callout, das sich zuklappen lässt.
section: Formatierung
tags:
  - formatierung
  - callouts
---

Ein `-` oder `+` hinter dem Typ macht den Callout faltbar.

````md
> [!question]- Zugeklappt (Minus)
> Erscheint erst beim Aufklappen.

> [!question]+ Aufgeklappt (Plus)
> Beginnt offen, lässt sich zuklappen.
````

> [!question]- Zugeklappt (Minus)
> Erscheint erst beim Aufklappen.

> [!question]+ Aufgeklappt (Plus)
> Beginnt offen, lässt sich zuklappen.

## In dieser Vorlage

Der Titel ist das Bedienelement. Er bekommt deshalb einen eigenen Fokusring in der Typfarbe —
**von Haus aus** ist er anklickbar, aber mit der Tastatur nicht als Steuerelement erkennbar.

Der Pfeil dreht sich beim Aufklappen; bei eingeschaltetem `prefers-reduced-motion` springt er
stattdessen.

> [!warning] Zugeklappter Inhalt ist trotzdem im Dokument
> Wer die Seite durchsucht oder ausdruckt, bekommt auch den zugeklappten Text. Faltbar heißt
> „ordentlich", nicht „versteckt".
