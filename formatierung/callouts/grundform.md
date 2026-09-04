---
title: Callouts — Grundform
description: Der Aufbau eines Callouts, mit und ohne eigenen Titel.
section: Formatierung
tags:
  - formatierung
  - callouts
translationKey: formatierung/callouts/grundform
---

## Mit eigenem Titel

````md
> [!note] Ein eigener Titel
> Der Inhalt des Callouts.
````

> [!note] Ein eigener Titel
> Der Inhalt des Callouts.

## Ohne Titel

Dann steht der Typ als Titel:

````md
> [!warning]
> Ohne eigenen Titel.
````

> [!warning]
> Ohne eigenen Titel.

## Mit beliebigem Inhalt

Ein Callout kann alles enthalten, was sonst auch geht:

````md
> [!example] Mit allem drin
>
> 1. Eine Liste
> 2. Mit zwei Punkten
>
> | Und | eine Tabelle |
> | --- | ------------ |
> | a   | b            |
>
> ```js
> const auch = "Code"
> ```
````

> [!example] Mit allem drin
>
> 1. Eine Liste
> 2. Mit zwei Punkten
>
> | Und | eine Tabelle |
> | --- | ------------ |
> | a   | b            |
>
> ```js
> const auch = "Code"
> ```

Weiter: [[formatierung/callouts/alle-typen|alle dreizehn Typen]],
[[formatierung/callouts/faltbar|faltbar]], [[formatierung/callouts/verschachtelt|verschachtelt]].
