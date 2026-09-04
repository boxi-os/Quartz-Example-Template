---
title: Tokens
description: 49 Variablen, aus denen die ganze Gestaltung besteht.
section: Gestaltung
tags:
  - gestaltung
  - grundlagen
translationKey: gestaltung/grundlagen/tokens
---

**Kein Stylesheet dieser Vorlage enthält eine Farbe oder eine Länge als Zahl.** Alles liest
Variablen. Das ist keine Kosmetik: Nach dem Import bleiben sie in der App unter *Stile → Variablen*
bearbeitbar, ein Wert in SCSS nicht.

## Die sechs mit der größten Reichweite

| Token | Wert | Was sich ändert |
| --- | --- | --- |
| `--tpl-space-md` | 1rem | Grundabstand; die ganze Skala hängt daran |
| `--tpl-target` | 44px | Mindestgröße **aller** Bedienelemente |
| `--tpl-indent` | 0.85rem | Eine Ebene in Explorer *und* Inhaltsverzeichnis |
| `--tpl-radius-md` | 8px | Ecken von Karten, Codeblöcken, Callouts |
| `--tpl-accent-bar` | 3px | Jeder Akzentbalken |
| `--tpl-motion` | 150ms | Jede Übergangsdauer |

## Zwei Zeilenabstände, nicht einer

`--tpl-leading-normal` steht auf 1,65 und gilt für den Fließtext. Für alles, was in
`--tpl-text-sm` oder kleiner gesetzt ist, gibt es `--tpl-leading-snug` mit 1,45.

Das ist keine Feinheit. 1,65 ist ein Verhältnis, das für 1 rem über sechs Rasterspalten gemessen
wurde. Dieselbe Zahl bei 0,875 rem in einer drei Spalten schmalen Leiste legt fast 21 px zwischen
zwei Zeilen von 14 px Höhe — ein dreizeiliger Absatz liest sich dann wie drei einzelne. Genau so sah
die Notiz-Box in der Seitenleiste aus. Die drei Bereiche, die aus Kleinschrift bestehen — linke
Leiste, rechte Leiste, Fußzeile — sagen das einmal, statt dass jede Komponente darin es wiederholt.

## Drei Arten von Variablen

1. **Schriftstapel** — die Familie plus einen echten Fallback.
2. **Quartz-Variablen, wo die Vorlage widerspricht** — etwa der Rand von Bedienelementen. Diese
   liest *Quartz*, nicht unsere Stylesheets; sie sehen ungenutzt aus und sind es nicht.
3. **Eigene `--tpl-*`-Tokens** — das eigentliche System.

## Was Quartz stattdessen tut

**Von Haus aus** gibt es die neun Farbvariablen und die Schriftrollen, aber keine Skala für
Abstände, Radien, Zielgrößen oder Bewegung. Werte stehen dort direkt in den Regeln. Wer den
Grundabstand ändern will, sucht ihn an vielen Stellen.
