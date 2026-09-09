---
title: Images per colour scheme
description: Two images, of which only ever one is visible.
section: 2 – Formatting
tags:
  - formatting
  - media
translationKey: formatierung/medien/einbettungen
cover: "[[assets/covers/cover-medien.svg]]"
---

The *[[en/7-reference/01-glossary#Layout box|Layout Box]]* [[en/7-reference/01-glossary#Plugin|plugin]] of this template switches images by [[en/7-reference/01-glossary#Colour scheme|colour scheme]]: an element with the
class `img-light` appears in light mode, `img-dark` in dark mode.

```html
<img class="img-light" src="{{root}}/static/logo-light.png" alt="" />
<img class="img-dark" src="{{root}}/static/logo-dark.png" alt="" />
```

The word mark at the top left of this site works that way — although with two inline SVGs instead
of two files, because a template package carries no image files.

## Why CSS alone will not do

A single image could be recoloured with `filter: invert()`, but that hits every colour equally and
turns a green logo magenta. Two versions are the more honest solution.

## Alternative: currentColor

An inline SVG whose areas carry `fill="currentColor"` follows the text colour automatically and
needs no second version. That is the simpler way as soon as the image is one colour.

More on the instances: [[en/5-design/05-layout-boxes/the-five-instances|The five instances]].
