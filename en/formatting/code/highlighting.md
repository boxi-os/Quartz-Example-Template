---
title: Highlighting lines
description: Emphasising single lines in a block.
section: Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/hervorhebung
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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
