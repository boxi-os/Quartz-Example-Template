---
title: Video and audio
description: Embedding sound and moving images — with what Quartz makes of them on its own.
section: 2 – Formatting
tags:
  - formatting
  - media
translationKey: formatierung/medien/video-audio
cover: "[[assets/covers/cover-medien.svg]]"
---

## Audio

```md
![[beispiel-ton.wav]]
```

![[beispiel-ton.wav]]

The [[en/7-reference/01-glossary#Wikilink|wikilink]] becomes an `<audio controls>` — with a play button, progress and volume, without
anyone doing anything for it. The formats supported are the ones the browser knows: **WAV**,
**MP3**, **OGG**, **M4A**, **FLAC**, **WebM**.

As [[en/7-reference/01-glossary#HTML|HTML]] too, when attributes are needed:

```md
<audio src="assets/beispiel-ton.wav" controls preload="none"></audio>
```

<audio src="assets/beispiel-ton.wav" controls preload="none"></audio>

`preload="none"` loads the file only when it is played — with several recordings on one page that
is the difference between a fast and a slow page.

## Video

```md
![[film.mp4]]
<video src="assets/film.mp4" controls poster="assets/beispiel-breit.png"></video>
```

The same mechanism: the wikilink becomes a `<video controls>`. The formats are **MP4**, **WebM**
and **OGV**.

> [!info] There is no video file here
> This template deliberately brings none: even a few seconds of video weigh more than all the rest
> of the example content, and a template package carries no media files anyway. The design for
> `<video>` is there all the same and takes effect as soon as a file lies beside it.
>
> For short movement without sound a [[en/2-formatting/12-media/images|GIF]] is the simpler choice —
> there is one on the images page.

### The poster frame

`poster` decides what can be seen before playing. Without it the browser shows the first [[en/7-reference/01-glossary#Frame|frame]] —
and with a fade-in that is black.

### YouTube and other services

```md
![](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
```

The *Obsidian flavored [[en/7-reference/01-glossary#Markdown|markdown]]* [[en/7-reference/01-glossary#Plugin|plugin]] turns the bare URL into an embed when `enableYouTubeEmbed`
is active — in this template it is.

## In this template

- An **audio player** takes the full column width and gets space above and below. The control
  itself belongs to the browser; the template does not touch it, because a rebuilt player loses its
  keyboard operation.
- A **video** gets a border and corners like an image and keeps its aspect ratio.
- An **embed** (`iframe`) gets `aspect-ratio: 16/9`. Without that rule it collapses to zero height
  in a grid cell — which happens exactly when the page uses a grid of its own, that is, everywhere
  in this template.

> [!tip] Captions belong with it
> `<video>` takes `<track kind="captions" src="…vtt" srclang="en" default>`. Without captions a
> video is not accessible to some readers — and useless to everyone watching it without sound.
