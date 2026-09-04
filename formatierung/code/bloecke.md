---
title: Codeblöcke
description: Mehrzeiliger Code, mit Sprache und Kopierknopf.
section: Formatierung
tags:
  - formatierung
  - code
---

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

## Ohne Sprache

````md
```
Reiner Text ohne Hervorhebung.
```
````

```
Reiner Text ohne Hervorhebung.
```

## Lange Zeilen

Ein Codeblock ist die eine Stelle, an der das Lesemaß nicht gilt: Einen Shell-Befehl umzubrechen
kostet mehr, als ihn zu scrollen.

```bash
npx quartz build --serve --port 8080 --wsPort 3001 --bundleInfo --verbose --directory content
```

## In dieser Vorlage

Drei Unterschiede zum Standard:

- Die **Sprache** steht oben links am Block, als `::after` im Stylesheet — sie landet damit nicht
  in einer Kopie.
- Der **Kopierknopf** ist 44 px groß und erscheint bei Hover, bei Fokus *und* dauerhaft auf
  Geräten ohne Zeiger. **Von Haus aus** ist er nur bei Hover sichtbar und damit auf einem Telefon
  unerreichbar.
- Der **Hintergrund** kommt von der Vorlage, nicht vom Syntax-Thema: `keepBackground: false` sorgt
  dafür, dass shiki nur die Farben der Zeichen setzt. So passt der Block in beiden Farbschemata.
