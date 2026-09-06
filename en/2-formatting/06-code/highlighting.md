---
title: Highlighting lines
description: Emphasising single lines in a block.
section: 2 Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/hervorhebung
cover: "[[assets/covers/cover-code.svg]]"
---

Curly braces after the language mark lines:

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

## Several lines and ranges

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

## In this template

The highlighted line gets a tinted surface **and** a bar on the left edge. A tint alone is too weak
on a code block that is tinted anyway.
