---
title: Video und Audio
description: Ton und Bewegtbild einbinden — mit dem, was Quartz von selbst daraus macht.
section: Formatierung
tags:
  - formatierung
  - medien
translationKey: formatierung/medien/video-audio
cover: "[[assets/covers/cover-medien.svg]]"
---

## Audio

```md
![[beispiel-ton.wav]]
```

![[beispiel-ton.wav]]

Aus dem [[7-nachschlagen/01-glossar#Wikilink|Wikilink]] wird ein `<audio controls>` — mit Abspielknopf, Fortschritt und Lautstärke, ohne
dass man etwas dafür tut. Unterstützt werden die Formate, die der Browser kennt: **WAV**, **MP3**,
**OGG**, **M4A**, **FLAC**, **WebM**.

Auch als [[7-nachschlagen/01-glossar#HTML|HTML]], wenn man Attribute braucht:

```md
<audio src="assets/beispiel-ton.wav" controls preload="none"></audio>
```

<audio src="assets/beispiel-ton.wav" controls preload="none"></audio>

`preload="none"` lädt die Datei erst beim Abspielen — bei mehreren Aufnahmen auf einer Seite ist
das der Unterschied zwischen einer schnellen und einer langsamen Seite.

## Video

```md
![[film.mp4]]
<video src="assets/film.mp4" controls poster="assets/beispiel-breit.png"></video>
```

Dieselbe Mechanik: Der Wikilink wird zu einem `<video controls>`. Formate sind **MP4**, **WebM**
und **OGV**.

> [!info] Hier liegt keine Videodatei
> Diese Vorlage bringt bewusst keine mit: Schon ein paar Sekunden Video wiegen mehr als der ganze
> übrige Beispielinhalt, und ein Vorlagenpaket transportiert ohnehin keine Mediendateien. Die
> Gestaltung für `<video>` ist trotzdem da und greift, sobald eine Datei danebenliegt.
>
> Für kurze Bewegung ohne Ton ist ein [[2-formatierung/12-medien/bilder|GIF]] die einfachere Wahl —
> eines liegt auf der Bilderseite.

### Das Vorschaubild

`poster` bestimmt, was vor dem Abspielen zu sehen ist. Ohne Angabe zeigt der Browser das erste
Bild — und das ist bei einer Aufblende schwarz.

### YouTube und andere Dienste

```md
![](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
```

Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Obsidian flavored markdown* wandelt die nackte URL in eine Einbettung, wenn
`enableYouTubeEmbed` aktiv ist — in dieser Vorlage ist es das.

## In dieser Vorlage

- Ein **Audiospieler** nimmt die volle Spaltenbreite und bekommt Abstand nach oben und unten. Das
  Bedienelement selbst gehört dem Browser; die Vorlage rührt es nicht an, weil ein nachgebauter
  Spieler seine Tastaturbedienung verliert.
- Ein **Video** bekommt Rahmen und Ecken wie ein Bild und behält sein Seitenverhältnis.
- Eine **Einbettung** (`iframe`) bekommt `aspect-ratio: 16/9`. Ohne diese Regel fällt sie in einer
  Grid-Zelle auf null Höhe zusammen — was genau dann passiert, wenn die Seite ein eigenes Raster
  verwendet, also in dieser Vorlage überall.

> [!tip] Untertitel gehören dazu
> `<video>` nimmt `<track kind="captions" src="…vtt" srclang="de" default>`. Ohne Untertitel ist
> ein Video für einen Teil der Leser nicht zugänglich — und für alle unbrauchbar, die es ohne Ton
> ansehen.
