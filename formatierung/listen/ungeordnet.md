---
title: Ungeordnete Listen
description: Aufzählungen und ihre Verschachtelung.
section: Formatierung
tags:
  - formatierung
  - listen
---

```md
- Erster Punkt
- Zweiter Punkt
- Dritter Punkt
```

- Erster Punkt
- Zweiter Punkt
- Dritter Punkt

## Verschachtelt

Jede Ebene rückt um zwei Leerzeichen ein.

```md
- Erste Ebene
  - Zweite Ebene
    - Dritte Ebene
      - Vierte Ebene
```

- Erste Ebene
  - Zweite Ebene
    - Dritte Ebene
      - Vierte Ebene

## Mehrzeilige Punkte

```md
- Ein Punkt, dessen Text so lang ist, dass er umbricht,
  und dessen zweite Zeile bündig unter der ersten steht.

- Ein Punkt mit einem eigenen Absatz.

  Der zweite Absatz gehört noch zum selben Punkt.
```

- Ein Punkt, dessen Text so lang ist, dass er umbricht,
  und dessen zweite Zeile bündig unter der ersten steht.

- Ein Punkt mit einem eigenen Absatz.

  Der zweite Absatz gehört noch zum selben Punkt.

## In dieser Vorlage

Der Aufzählungspunkt nimmt `--gray` statt der Textfarbe: Er ist Struktur, nicht Inhalt.
