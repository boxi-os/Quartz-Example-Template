---
title: 6.4 – Variablen
description: 53 Variablen, aus denen die ganze Gestaltung besteht.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/variablen
---

**Farbe und Maß dieser Vorlage stehen nicht in den [[7-nachschlagen/01-glossar#Stylesheet|Stylesheets]], sondern in 53 Variablen.** Das ist
keine Kosmetik: Nach dem Import bleiben sie in der App unter *Stile → Variablen* bearbeitbar, ein
Wert in [[7-nachschlagen/01-glossar#CSS und SCSS|SCSS]] nicht.

## Die sechs mit der größten Reichweite

| Token | Wert | Was sich ändert |
| --- | --- | --- |
| `--tpl-space-md` | 1rem | Grundabstand; die ganze Skala hängt daran |
| `--tpl-target` | 44px | Mindestgröße **aller** Bedienelemente |
| `--tpl-indent` | 0.85rem | Eine Ebene in [[7-nachschlagen/01-glossar#Explorer\|Explorer]] *und* Inhaltsverzeichnis |
| `--tpl-radius-md` | 8px | Ecken von Karten, Codeblöcken, [[7-nachschlagen/01-glossar#Callout\|Callouts]] |
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

## Was doch literal dasteht

Gemessen über die 30 Stylesheets, Kommentare abgezogen: **41 Farbwerte** und **91 Längen**. Alle
haben denselben Grund — an dieser Stelle *kann* keine Variable stehen.

| Wo | Was | Warum |
| --- | --- | --- |
| `body-callouts` | 24 Farben | Dreizehn Callout-Töne in zwei Modi, abzüglich des Zitat-Callouts, das die Akzentfarbe liest. Sie bedeuten **Status**, nicht Palette: Ein `warning`, das der Akzentfarbe folgt, ist kein `warning` mehr. |
| `body-code` | 10 Farben | Die fünf Syntax-Korrekturen — je der ersetzte und der ersetzende Wert. |
| `body-mermaid` | 2 Rottöne | Mermaids Fehlerzustand, den es selbst einfärbt. |
| `a11y` | 2 Grautöne | In `@media print`. Auf Papier gilt weder die helle noch die dunkle Palette. |
| `nav-explorer` | 1 Schwarz | Die Abdunklung hinter der Schublade auf dem Handy — kein Farbwert, ein Schleier. |
| überall | 20× `1px`/`2px` | Haarlinien und Fokusringe. Eine Linie ist ein Pixel breit, nicht ein Rasterschritt. |
| überall | 27× `0.1em`, `1em` u. a. | Maße, die sich auf die Schriftgröße beziehen und nicht auf die Abstandsskala — der Innenabstand einer Code-Pille, die Größe eines Symbols in Zeilenhöhe. Die drei wiederkehrenden Laufweiten sind seit dem 05.09.2026 Tokens. |
| 13 Regeln | `720px`, `800px`, `801px` | Eine Media-Query kann keine Variable lesen. |

## Was sich wiederholt, und warum es das darf

Zwei Formen stehen in mehreren Stylesheets fast wortgleich:

| Form | in wie vielen Dateien |
| --- | ---: |
| Die Panel-Überschrift — Überschriftenschrift, versal, halbfett, gedämpft, `--tpl-tracking-label` | 9 |
| Der überfahrene Link — Akzentfarbe, unterstrichen, `--tpl-underline-offset` | 7 |

Das ließe sich zu einer gemeinsamen Datei zusammenziehen, und genau das wäre hier falsch. Die
Stylesheets sind nach Komponenten geschnitten, und die Doku hängt daran: Auf jeder Seite dieses
Bereichs steht die Tabelle der Variablen, die *ihre* Komponente liest. Zöge man die Panel-Überschrift
nach `base.scss`, verschwände sie aus neun dieser Tabellen und tauchte in einer auf, die niemand
liest, während man die [[7-nachschlagen/01-glossar#Rückverweise|Rückverweise]] anpasst.

Was geteilt werden muss, sind die **Werte** — und die sind es: `--tpl-tracking-label` und
`--tpl-underline-offset` stehen je einmal und gelten überall. Die Form daneben ist sechs Zeilen, die
lesbar dort stehen, wo sie wirken.

> [!note] Eine gemeinsame Datei ginge hier ohnehin nicht ohne Weiteres
> Sass löst so etwas über Partials (`_shared.scss`). Die App lässt einen Dateinamen mit führendem
> Unterstrich nicht zu, und eine Datei ohne ihn stünde in der Liste unter *Stile → Eigenes [[7-nachschlagen/01-glossar#CSS und SCSS|CSS]]* als
> Stylesheet, das nichts ausgibt.

## Was Quartz stattdessen tut

**Von Haus aus** gibt es die neun Farbvariablen und die Schriftrollen, aber keine Skala für
Abstände, Radien, Zielgrößen oder Bewegung. Werte stehen dort direkt in den Regeln. Wer den
Grundabstand ändern will, sucht ihn an vielen Stellen.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 40 Variablen liest `base.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bodyFont` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 weitere Komponenten |
| `--icon-chevron` | im Stylesheet gesetzt (`base.scss`) | Callouts |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--tpl-fade` | `14px` | nur hier |
| `--tpl-fade-mask` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--tpl-fade-mask-end` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--tpl-focus-color` | `var(--secondary)` = `#2A4E6C` | nur hier |
| `--tpl-focus-offset` | `2px` | Callouts |
| `--tpl-focus-width` | `2px` | Callouts |
| `--tpl-header-h` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--tpl-header-pad` | im Stylesheet gesetzt (`base.scss`) | Kopfbereich |
| `--tpl-icon-sm` | `0.95rem` | Explorer, Der Sprachumschalter |
| `--tpl-leading-normal` | `1.6` | nur hier |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-leading-tight` | `1.25` | nur hier |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xl` | `4rem` | Fehlerseite |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 4 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-2xl` | `1.75rem` | Titel und Datum |
| `--tpl-text-3xl` | `2.25rem` | Titel und Datum, Fehlerseite |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |
| `--tpl-text-lg` | `1.15rem` | Suche, Link-Vorschau |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |
| `--tpl-text-xl` | `1.4rem` | Der Sprachumschalter |
| `--tpl-tracking-caps` | `0.06em` | Code, 3.1 Bases |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
