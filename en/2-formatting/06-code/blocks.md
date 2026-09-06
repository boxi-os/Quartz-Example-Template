---
title: Code blocks
description: Code over several lines, with a language and a copy button.
section: 2 Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/bloecke
cover: "[[assets/covers/cover-code.svg]]"
---

````md
```ts
export function greet(name: string): string {
  return `Hello, ${name}`
}
```
````

```ts
export function greet(name: string): string {
  return `Hello, ${name}`
}
```

## Without a language

````md
```
Plain text without highlighting.
```
````

```
Plain text without highlighting.
```

## With a title

A `title=` after the language puts a label above the block — handy for naming the file the excerpt
belongs to.

````md
```yaml title="quartz.config.yaml"
configuration:
  pageTitle: Example
```
````

```yaml title="quartz.config.yaml"
configuration:
  pageTitle: Example
```

## Long lines

A code block does not wrap long lines, it scrolls: breaking a shell command costs more than
scrolling it.

```bash
npx quartz build --serve --port 8080 --wsPort 3001 --bundleInfo --verbose --directory content
```

## In this template

Three differences from the default:

- The **language** sits at the top left of the block, as an `::after` in the [[en/7-reference/01-glossary#Stylesheet|stylesheet]] — so it
  does not end up in a copy.
- The **copy button** is 44 px across and appears on [[en/7-reference/01-glossary#Hover|hover]], on focus *and* permanently on devices
  without a pointer. **Out of the box** it is only visible on hover and therefore unreachable on a
  phone.
- The **background** comes from the template, not from the syntax theme: `keepBackground: false`
  makes shiki set only the colours of the characters. That way the block fits in both colour
  schemes.
