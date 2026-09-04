---
title: Benannte und mehrfache Fußnoten
description: Namen statt Zahlen, mehrere Verweise, Fußnoten im Fließtext.
section: Formatierung
tags:
  - formatierung
  - fussnoten
translationKey: formatierung/fussnoten/varianten
---

## Benannt statt nummeriert

```md
Erster Verweis[^messung] und zweiter Verweis[^quelle].

[^messung]: Namen sind im Quelltext lesbarer als Zahlen.
[^quelle]: Und sie verrutschen nicht, wenn eine Fußnote dazwischenkommt.
```

Erster Verweis[^messung] und zweiter Verweis[^quelle].

[^messung]: Namen sind im Quelltext lesbarer als Zahlen.
[^quelle]: Und sie verrutschen nicht, wenn eine Fußnote dazwischenkommt.

Auf der Website erscheinen trotzdem Zahlen — der Name existiert nur im Quelltext.

## Mehrzeilige Fußnoten

Folgezeilen werden eingerückt:

```md
[^lang]: Die erste Zeile.

    Ein zweiter Absatz, um vier Leerzeichen eingerückt.
```

## Inline-Fußnoten

Obsidian kennt eine Kurzform ohne separate Definition:

```md
Ein Satz mit einer Inline-Fußnote.^[Der Text steht direkt hier.]
```

Ein Satz mit einer Inline-Fußnote.^[Der Text steht direkt hier.]

> [!warning] Nicht überall unterstützt
> Die Inline-Form ist eine Obsidian-Erweiterung. Wenn sie auf der gebauten Seite als Rohtext
> erscheint statt als Fußnote, fehlt die Unterstützung — dann ist die lange Form mit `[^name]` die
> sichere Wahl.

## Dieselbe Fußnote zweimal

```md
Erster Verweis[^gleich] und später noch einer[^gleich].

[^gleich]: Beide Verweise zeigen auf diese eine Fußnote.
```

Erster Verweis[^gleich] und später noch einer[^gleich].

[^gleich]: Beide Verweise zeigen auf diese eine Fußnote.
