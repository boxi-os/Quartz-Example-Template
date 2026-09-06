---
title: Zeilen hervorheben
description: Einzelne Zeilen in einem Block betonen.
section: 2 Formatierung
tags:
  - formatierung
  - code
translationKey: formatierung/code/hervorhebung
cover: "[[assets/covers/cover-code.svg]]"
---

Geschweifte Klammern hinter der Sprache markieren Zeilen:

````md
```js {2}
const a = 1
const b = 2
const c = 3
```
````

```js {2}
const a = 1
const b = 2
const c = 3
```

## Mehrere Zeilen und Bereiche

````md
```js {1,3-4}
const a = 1
const b = 2
const c = 3
const d = 4
```
````

```js {1,3-4}
const a = 1
const b = 2
const c = 3
const d = 4
```

## In dieser Vorlage

Die hervorgehobene Zeile bekommt eine getönte Fläche **und** einen Balken am linken Rand. Eine
Tönung allein ist auf einem Codeblock, der ohnehin getönt ist, zu schwach.
