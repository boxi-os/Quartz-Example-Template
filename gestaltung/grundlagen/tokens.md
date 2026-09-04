---
title: Tokens
description: 46 Variablen, aus denen die ganze Gestaltung besteht.
section: Gestaltung
tags:
  - gestaltung
  - grundlagen
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

## Drei Arten von Variablen

1. **Schriftstapel** — die Familie plus einen echten Fallback.
2. **Quartz-Variablen, wo die Vorlage widerspricht** — etwa der Rand von Bedienelementen. Diese
   liest *Quartz*, nicht unsere Stylesheets; sie sehen ungenutzt aus und sind es nicht.
3. **Eigene `--tpl-*`-Tokens** — das eigentliche System.

## Was Quartz stattdessen tut

**Von Haus aus** gibt es die neun Farbvariablen und die Schriftrollen, aber keine Skala für
Abstände, Radien, Zielgrößen oder Bewegung. Werte stehen dort direkt in den Regeln. Wer den
Grundabstand ändern will, sucht ihn an vielen Stellen.
