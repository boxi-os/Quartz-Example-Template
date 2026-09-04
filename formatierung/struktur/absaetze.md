---
title: Absätze
description: Wie ein Absatz entsteht und wie breit er wird.
section: Formatierung
tags:
  - formatierung
  - struktur
---

## Ein Absatz

```md
Ein Absatz entsteht durch eine Leerzeile davor und danach.

Dieser hier ist der zweite.
```

Ein Absatz entsteht durch eine Leerzeile davor und danach.

Dieser hier ist der zweite.

## Das Lesemaß

Fließtext ist in dieser Vorlage auf **68 Zeichen** begrenzt — unabhängig davon, wie breit das
Fenster ist. Dieser Absatz zeigt es: Er bricht um, obwohl rechts noch Platz wäre. Eine Zeile mit
140 Zeichen zwingt das Auge, den Zeilenanfang zu suchen.

Was **nicht** als Fließtext gilt und die volle Spalte nehmen darf: Tabellen, Codeblöcke, Diagramme,
Bilder und Formeln.

> [!info] Von Haus aus
> Quartz begrenzt den Text nicht auf eine Zeichenzahl, sondern die ganze Seite auf eine Pixelbreite
> (`.page { max-width: … }`). Bei einem breiten Fenster wird die Zeile dadurch länger, nicht die
> Spalte daneben. Der Unterschied steht unter [[gestaltung/grundlagen/tokens|Tokens]].
