---
title: Verschachtelte Callouts
description: Ein Callout im Callout — und wo die Grenze liegt.
section: Formatierung
tags:
  - formatierung
  - callouts
translationKey: formatierung/callouts/verschachtelt
---

````md
> [!info] Außen
> Text im äußeren Callout.
>
> > [!tip] Innen
> > Der innere verliert seinen Rahmen, behält aber den Farbbalken.
````

> [!info] Außen
> Text im äußeren Callout.
>
> > [!tip] Innen
> > Der innere verliert seinen Rahmen, behält aber den Farbbalken.

## Zwei Ebenen tief

````md
> [!example] Erste Ebene
> > [!note] Zweite Ebene
> > > [!tip] Dritte Ebene
> > > Geht, ist aber selten eine gute Idee.
````

> [!example] Erste Ebene
> > [!note] Zweite Ebene
> > > [!tip] Dritte Ebene
> > > Geht, ist aber selten eine gute Idee.

## In dieser Vorlage

Ein verschachtelter Callout gibt seinen eigenen Rahmen auf und behält nur den Farbbalken links.
Zwei vollständige Kästen ineinander lesen sich als Fehler, nicht als Struktur.

**Von Haus aus** behält der innere Callout seinen kompletten Rahmen samt Ecken.
