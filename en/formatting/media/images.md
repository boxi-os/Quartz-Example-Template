---
title: Images
description: Five formats, two notations, sizes — and which format is good for what.
section: Formatting
tags:
  - formatting
  - media
translationKey: formatierung/medien/bilder
---

## Two notations

```md
![Description](assets/beispiel-breit.png)
![[beispiel-breit.png]]
```

The first is standard Markdown, the second Obsidian's wikilink form. Both work; only the first
knows an alternative text.

![A card with the word PNG and the note 960 by 540 pixels](assets/beispiel-breit.png)

## The alternative text is not optional

What stands in the square brackets is read out when the image does not arrive or is not seen.
"Image" or "screenshot" had better not stand there — describe what can be seen. A purely decorative
image gets `![]()` with an empty bracket; then it is skipped instead of being read out by its file
name.

## The formats

| Format | What for | Example |
| --- | --- | --- |
| **PNG** | flat areas, text, sharp edges, transparency | 14 KB for 960 × 540 |
| **JPEG** | photographs and gradients | 40 KB for 1200 × 800 |
| **WebP** | the same as JPEG, smaller | 9 KB for 800 × 800 |
| **GIF** | short moving images without sound | 14 KB, 12 frames |
| **SVG** | diagrams, logos, everything drawn | 3 KB, scalable at will |

### JPEG — for photographs

![A gradient from dark green to white with three concentric circles](assets/beispiel-foto.jpg)

### WebP — the same, smaller

![The same gradient, square](assets/beispiel-quadrat.webp)

### GIF — movement without a video file

![A dot travels from left to right](assets/beispiel-animation.gif)

A GIF plays automatically and endlessly. For anything over a few seconds a video is better: a GIF
knows no compression over time and quickly grows larger than an MP4 of the same content.

> [!warning] Automatic movement is an accessibility question
> An endlessly looping GIF cannot be stopped. For content running longer than five seconds, WCAG
> requires a way to stop it — a video with controls is the right choice for that.

### SVG — drawn rather than photographed

![The structure of the editorial frame: header, navigation, content, apparatus](assets/frame-aufbau-en.svg)

An SVG is text. It stays sharp at every size, can be versioned and can take its colours from CSS.

## Controlling the size — only with the wikilink form

```md
![[beispiel-breit.png|300]]
```

![[beispiel-breit.png|300]]

Width × height is possible too, but distorts when the ratio does not match:

```md
![[beispiel-klein.png|200x120]]
```

![[beispiel-klein.png|200x120]]

> [!warning] Size or alternative text — not both
> Measured on this page:
>
> | Notation | Result |
> | --- | --- |
> | `![[image.png\|300]]` | `<img width="300" height="auto" alt>` — size, **no** alternative text |
> | `![Text\|300](image.png)` | `alt="Text\|300"` — alternative text, **no** size |
>
> The Markdown form does not know the size notation: the whole string after the exclamation mark
> becomes the alternative text, `|300` included. The wikilink form sets the size but leaves `alt`
> empty.
>
> Anyone needing both writes HTML:
> `<img src="assets/image.png" alt="Description" width="300">`

And exactly that, with both:

<img src="assets/beispiel-klein.png" alt="A small card 240 pixels wide, with an alternative text" width="240">

## In this template

Every image gets a delicate border and rounded corners. Without the border an image with a white
background looks like a hole on the warm ground of this page — **out of the box** it stands
unframed.

An explicitly set width is kept; the template only caps it at the column width.
