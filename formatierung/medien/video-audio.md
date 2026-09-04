---
title: Video und Audio
description: Bewegtbild und Ton einbinden.
section: Formatierung
tags:
  - formatierung
  - medien
---

## Aus dem Vault

```md
![[video.mp4]]
![[ton.mp3]]
```

Obsidian und Quartz erzeugen daraus `<video>` bzw. `<audio>` mit Bedienelementen.

## Als HTML

```md
<video src="assets/video.mp4" controls></video>
<audio src="assets/ton.mp3" controls></audio>
```

Der Weg über HTML erlaubt zusätzliche Attribute wie `poster`, `loop` oder `muted`.

## YouTube

```md
![](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
```

Das Plugin *Obsidian flavored markdown* wandelt die URL in eine Einbettung, wenn
`enableYouTubeEmbed` aktiv ist — in dieser Vorlage ist es das.

## In dieser Vorlage

Eine Einbettung behält das Seitenverhältnis 16:9. Ohne diese Regel fällt ein `iframe` in einer
Grid-Zelle auf null Höhe zusammen — das passiert genau dann, wenn die Seite ein eigenes
Seitenraster verwendet, also in dieser Vorlage überall.

> [!note] Kein Beispiel auf dieser Seite
> Video- und Audiodateien würden das Vorlagenpaket unnötig schwer machen. Die Regeln sind
> vorhanden, das Beispiel fehlt bewusst.
