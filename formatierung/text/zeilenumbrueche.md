---
title: Zeilenumbrüche
description: Warum ein einfacher Umbruch hier wirkt — und in Standard-Markdown nicht.
section: Formatierung
tags:
  - formatierung
  - text
---

## Ein Umbruch im Quelltext ist ein Umbruch auf der Seite

```md
Erste Zeile
Zweite Zeile
```

Erste Zeile
Zweite Zeile

Das ist **nicht** selbstverständlich. In Standard-Markdown werden diese beiden Zeilen zu einem
Absatz zusammengezogen; man bräuchte zwei Leerzeichen am Zeilenende oder ein `<br>`.

Hier wirkt der Umbruch, weil das Plugin *Hard line breaks* aktiv ist. Für Notizen, die in Obsidian
geschrieben werden, ist das die erwartete Schreibweise.

## Absatz statt Umbruch

```md
Ein Absatz.

Ein zweiter Absatz, durch eine Leerzeile getrennt.
```

Ein Absatz.

Ein zweiter Absatz, durch eine Leerzeile getrennt.

Der Unterschied ist sichtbar: Zwischen Absätzen liegt Abstand, zwischen umgebrochenen Zeilen nicht.

## Umbruch erzwingen

```md
Erste Zeile<br>Zweite Zeile
```

Erste Zeile<br>Zweite Zeile
