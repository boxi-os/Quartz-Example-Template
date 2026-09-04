---
title: Bilder
description: Einbinden, benennen, in der Größe steuern.
section: Formatierung
tags:
  - formatierung
  - medien
---

## Zwei Schreibweisen

```md
![Beschreibung](assets/frame-aufbau.svg)
![[frame-aufbau.svg]]
```

Die erste ist Standard-Markdown, die zweite Obsidians Wikilink-Form. Beide funktionieren.

![Der Aufbau des editorial-Frames: Kopfbereich, Navigation, Inhalt, Apparat](assets/frame-aufbau.svg)

## Der Alternativtext ist nicht optional

Was in den eckigen Klammern steht, wird vorgelesen, wenn das Bild nicht ankommt oder nicht gesehen
wird. „Bild" oder „Screenshot" steht dort besser nicht — beschreibe, was zu sehen ist.

Bei der Wikilink-Form gibt es keinen Alternativtext. Für Bilder, die Information tragen, ist die
Markdown-Form deshalb die bessere Wahl.

## Größe

```md
![[frame-aufbau.svg|300]]
![Beschreibung|300](assets/frame-aufbau.svg)
```

![Der Aufbau des Frames, klein|300](assets/frame-aufbau.svg)

Die Zahl ist die Breite in Pixeln. Die Vorlage begrenzt nur nach oben auf die Spaltenbreite.

## In dieser Vorlage

Jedes Bild bekommt einen zarten Rahmen und runde Ecken. Ohne den Rahmen sieht ein Bild mit weißem
Hintergrund auf dem warmen Grund dieser Seite wie ein Loch aus — **von Haus aus** steht es
rahmenlos.
