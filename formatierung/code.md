---
title: Code
description: Inline, Blöcke, Sprachen und Hervorhebung einzelner Zeilen.
section: Formatierung
tags:
  - referenz
  - formatierung
  - code
---

## Inline

```md
Ein Befehl wie `npm run build` mitten im Satz.
```

Ein Befehl wie `npm run build` mitten im Satz.

Inline-Code ist eine Tönung, kein Kasten — genug, um ihn vom Fließtext zu trennen, zu wenig, um
den Satz zu unterbrechen.

## Block mit Sprache

````md
```ts
export function greet(name: string): string {
  return `Hallo, ${name}`
}
```
````

```ts
export function greet(name: string): string {
  return `Hallo, ${name}`
}
```

Die Sprache steht oben links am Block. Rechts erscheint beim Überfahren eine Schaltfläche zum
Kopieren — auf Geräten ohne Zeiger ist sie dauerhaft sichtbar, und mit der Tastatur erreichbar.

## Ohne Sprache

````md
```
Reiner Text ohne Hervorhebung.
```
````

```
Reiner Text ohne Hervorhebung.
```

## Weitere Sprachen

```scss
.beispiel {
  color: var(--secondary);
  padding: var(--tpl-space-md);
}
```

```yaml
configuration:
  pageTitle: Minimal & lesbar
  locale: de-DE
```

```bash
npx quartz build --serve
```

```python
def gruss(name: str) -> str:
    return f"Hallo, {name}"
```

## Einzelne Zeilen hervorheben

````md
```js {2}
const a = 1
const b = 2   // diese Zeile ist hervorgehoben
const c = 3
```
````

```js {2}
const a = 1
const b = 2
const c = 3
```

## Lange Zeilen

Ein Codeblock ist die eine Stelle, an der das Lesemaß nicht gilt: einen Shell-Befehl umzubrechen
kostet mehr, als ihn zu scrollen.

```bash
npx quartz build --serve --port 8080 --wsPort 3001 --bundleInfo --verbose --directory content
```
