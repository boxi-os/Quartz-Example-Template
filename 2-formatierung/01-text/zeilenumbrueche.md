---
title: Zeilenumbrüche
description: Warum ein Umbruch im Quelltext hier keiner auf der Seite ist — und wie man einen erzwingt.
section: 2 – Formatierung
tags:
  - formatierung
  - text
translationKey: formatierung/text/zeilenumbrueche
cover: "[[assets/covers/cover-text.svg]]"
---

## Ein Umbruch im Quelltext ist keiner auf der Seite

```md
Erste Zeile
Zweite Zeile
```

Erste Zeile
Zweite Zeile

Beide Zeilen bilden **einen Absatz**. Das ist das Verhalten von Standard-Markdown: Ein einfacher
Umbruch im Quelltext gilt als Leerzeichen, und der Text fließt.

Das ist wichtig für Notizen, die im Editor umbrochen geschrieben werden — so wie alle Seiten dieser
Website. Sie sind bei Spalte 100 umgebrochen, damit sie sich lesen und vergleichen lassen; auf der
Seite ist davon nichts zu sehen.

## Absatz

```md
Ein Absatz.

Ein zweiter Absatz, durch eine Leerzeile getrennt.
```

Ein Absatz.

Ein zweiter Absatz, durch eine Leerzeile getrennt.

**Das ist der übliche Weg.** Wo ein Umbruch semantisch nötig ist, ist meist ein Absatz gemeint.

## Umbruch erzwingen

Für die Fälle, in denen wirklich ein Umbruch innerhalb eines Absatzes gehört — eine Anschrift, ein
Vers, eine Zeile in einem Formular:

```md
Erste Zeile<br>Zweite Zeile
```

Erste Zeile<br>Zweite Zeile

Oder mit zwei Leerzeichen am Zeilenende, was im Quelltext allerdings unsichtbar ist und deshalb
leicht verloren geht.

## Der Schalter dahinter

Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Hard line breaks* dreht diese Regel um: Mit ihm wird **jeder** Umbruch im Quelltext zu
einem Umbruch auf der Seite. Obsidian selbst verhält sich so, weshalb der Schalter naheliegt.

> [!warning] Diese Vorlage lässt ihn aus
> Gemessen, bevor er ausgeschaltet wurde: neun aufgezwungene Umbrüche auf einer einzigen Seite,
> jeder mitten im Satz. Wer seine Notizen im Editor umbricht — und das tut fast jeder, der lange
> Texte schreibt — bekommt mit dem Plugin einen zerhackten Fließtext.
>
> Wer zeilenweise schreibt (Listen, Verse, kurze Zeilen) und den Umbruch wirklich meint, schaltet
> es in der App unter *Plugins* wieder ein.
