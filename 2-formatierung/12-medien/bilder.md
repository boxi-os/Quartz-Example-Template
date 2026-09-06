---
title: Bilder
description: Fünf Formate, zwei Schreibweisen, Größenangaben — und wofür welches Format taugt.
section: Formatierung
tags:
  - formatierung
  - medien
translationKey: formatierung/medien/bilder
cover: "[[assets/covers/cover-medien.svg]]"
---

## Zwei Schreibweisen

```md
![Beschreibung](assets/beispiel-breit.png)
![[beispiel-breit.png]]
```

Die erste ist Standard-Markdown, die zweite Obsidians Wikilink-Form. Beide funktionieren; nur die
erste kennt einen Alternativtext.

![Eine Karte mit dem Wort PNG und der Angabe 960 mal 540 Pixel](assets/beispiel-breit.png)

## Der Alternativtext ist nicht optional

Was in den eckigen Klammern steht, wird vorgelesen, wenn das Bild nicht ankommt oder nicht gesehen
wird. „Bild" oder „Screenshot" steht dort besser nicht — beschreibe, was zu sehen ist. Ein rein
schmückendes Bild bekommt `![]()` mit leerer Klammer; dann wird es übersprungen statt mit dem
Dateinamen vorgelesen.

## Die Formate

| Format | Wofür | Beispiel |
| --- | --- | --- |
| **PNG** | Flächen, Text, scharfe Kanten, Transparenz | 14 KB für 960 × 540 |
| **JPEG** | Fotos und Verläufe | 40 KB für 1200 × 800 |
| **WebP** | dasselbe wie JPEG, kleiner | 9 KB für 800 × 800 |
| **GIF** | kurze Bewegtbilder ohne Ton | 14 KB, 12 Bilder |
| **SVG** | Diagramme, Logos, alles Gezeichnete | 3 KB, beliebig skalierbar |

### JPEG — für Fotos

![Ein Verlauf von Dunkelgrün nach Weiß mit drei konzentrischen Kreisen](assets/beispiel-foto.jpg)

### WebP — dasselbe kleiner

![Derselbe Verlauf im Quadrat](assets/beispiel-quadrat.webp)

### GIF — Bewegung ohne Videodatei

![Ein Punkt wandert von links nach rechts](assets/beispiel-animation.gif)

Ein GIF spielt automatisch und endlos. Für alles über ein paar Sekunden ist ein Video besser: Ein
GIF kennt keine Kompression über die Zeit und wird schnell größer als ein MP4 desselben Inhalts.

> [!warning] Automatische Bewegung ist eine Zugänglichkeitsfrage
> Ein endlos laufendes GIF lässt sich nicht anhalten. Bei Inhalten, die länger als fünf Sekunden
> laufen, verlangt [[7-nachschlagen/01-glossar#WCAG|WCAG]] eine Möglichkeit zum Stoppen — dafür ist ein Video mit Bedienelementen die
> richtige Wahl.

### SVG — gezeichnet statt fotografiert

![Der Aufbau des editorial-Frames: Kopfbereich, Navigation, Inhalt, Apparat](assets/frame-aufbau.svg)

Ein SVG ist Text. Es bleibt bei jeder Größe scharf, lässt sich versionieren und kann seine Farben
aus [[7-nachschlagen/01-glossar#CSS und SCSS|CSS]] beziehen.

## Größe steuern — nur mit der Wikilink-Form

```md
![[beispiel-breit.png|300]]
```

![[beispiel-breit.png|300]]

Auch Breite × Höhe ist möglich, verzerrt aber, wenn das Verhältnis nicht stimmt:

```md
![[beispiel-klein.png|200x120]]
```

![[beispiel-klein.png|200x120]]

> [!warning] Größe oder Alternativtext — beides geht nicht
> Gemessen an dieser Seite:
>
> | Schreibweise | Ergebnis |
> | --- | --- |
> | `![[bild.png\|300]]` | `<img width="300" height="auto" alt>` — Größe, **kein** Alternativtext |
> | `![Text\|300](bild.png)` | `alt="Text\|300"` — Alternativtext, **keine** Größe |
>
> Die Markdown-Form kennt die Größenangabe nicht: Der ganze String hinter dem Ausrufezeichen wird
> zum Alternativtext, `|300` eingeschlossen. Die Wikilink-Form setzt die Größe, lässt `alt` aber
> leer.
>
> Wer beides braucht, schreibt [[7-nachschlagen/01-glossar#HTML|HTML]]:
> `<img src="assets/bild.png" alt="Beschreibung" width="300">`

Und genau so, mit beidem:

<img src="assets/beispiel-klein.png" alt="Eine kleine Karte in 240 Pixeln Breite, mit Alternativtext" width="240">

## In dieser Vorlage

Jedes Bild bekommt einen zarten Rahmen und runde Ecken. Ohne den Rahmen sieht ein Bild mit weißem
Hintergrund auf dem warmen Grund dieser Seite wie ein Loch aus — **von Haus aus** steht es
rahmenlos.

Eine ausdrücklich gesetzte Breite bleibt erhalten; die Vorlage begrenzt nur nach oben auf die
Spaltenbreite.
