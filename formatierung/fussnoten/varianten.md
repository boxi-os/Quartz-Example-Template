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

> [!failure] Hier funktioniert sie nicht
> Die Zeile darüber ist der Beweis: Auf der gebauten Seite steht `^[Der Text steht direkt hier.]`
> als Rohtext, Klammern und Dach inbegriffen. Die Inline-Form ist eine Obsidian-Erweiterung, und
> keines der Markdown-Plugins dieser Vorlage kennt sie. In Obsidian sieht man eine ordentliche
> Fußnote, auf der Website nicht — der unangenehmste Fall, weil er beim Schreiben nicht auffällt.
>
> Die lange Form mit `[^name]` ist deshalb die einzige, die trägt.

## Dieselbe Fußnote zweimal

```md
Erster Verweis[^gleich] und später noch einer[^gleich].

[^gleich]: Beide Verweise zeigen auf diese eine Fußnote.
```

Erster Verweis[^gleich] und später noch einer[^gleich].

[^gleich]: Beide Verweise zeigen auf diese eine Fußnote.
