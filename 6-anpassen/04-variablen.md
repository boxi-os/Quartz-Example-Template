---
title: 6.4 – Variablen
description: 66 Variablen, aus denen die ganze Gestaltung besteht.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/variablen
---

**Farbe und Maß dieser Vorlage stehen nicht in den [[7-nachschlagen/01-glossar#Stylesheet|Stylesheets]], sondern in 66 Variablen.** Das ist
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

## Woraus die 66 bestehen

Alle 66 sind eigene `--tpl-*`-Tokens — das eigentliche System. Schriften und die Farben der Palette
stehen nicht hier, sondern unter *Stile → Basis*; aus ihnen schreibt Quartz selbst `--bodyFont`,
`--secondary` und die übrigen. Bis zum 20.09.2026 standen hier auch Schriftstapel und Quartz-
Variablen, und die Schriftstapel verdeckten dabei Quartz' eigenen Rückfall
([[6-anpassen/03-schriften|6.3]]).

Drei Gruppen darunter sind jünger als der Rest und verdienen je einen Satz:

- **Dreizehn Callout-Farben** (`--tpl-callout-note` bis `--tpl-callout-quote`), je hell und dunkel.
  Sie bedeuten **Status**, nicht Palette: Ein `warning`, das der Akzentfarbe folgt, ist kein
  `warning` mehr. Und sie sind **gemessen, nicht gewählt** — elf von Quartz' zwölf Callout-Farben
  fallen auf hellem Grund durch AA. Jede Titelfarbe hält 4,5:1 auf dem Grund *und* auf der
  getönten Fläche ihres eigenen Kastens. Wer hier eine ändert, kann sie unter diese Schwelle
  setzen, und die App sagt nichts dazu.
- **Zwei für den Schleier** hinter jeder Schublade (`--tpl-backdrop`, `--tpl-backdrop-blur`):
  Abdunklung und Unschärfe, für die Navigation und den Explorer derselbe Wert.
- **Sechs Schalter für die Seitenspalten**, siehe den nächsten Abschnitt.

## Die Seitenspalten: stehen bleiben oder mitlaufen

Ob eine Seitenspalte beim Rollen stehen bleibt, entscheiden **drei Variablen je Spalte**, und sie
gehören zusammen: Eine Spalte, die stehen bleibt, braucht einen Höhendeckel (sonst ragt sie aus dem
Fenster und bleibt gar nicht stehen) und eine weiche Unterkante (sonst schneidet der Deckel eine
Zeile mitten durch). Wer umstellt, stellt alle drei um.

| Variable | stehen bleiben | mitlaufen |
| --- | --- | --- |
| `--tpl-col-…-position` | `sticky` | `static` |
| `--tpl-col-…-height` | `calc(100dvh - var(--tpl-header-h) - 2 * var(--tpl-space-lg))` | `none` |
| `--tpl-col-…-mask` | `var(--tpl-fade-mask-end)` | `none` |

Für `…` steht `left` oder `right`. **Die Vorgabe:** rechts bleibt stehen, links läuft mit. Ein
halber Zustand ist möglich und sieht aus wie ein Fehler — `static` mit Höhendeckel ist eine Spalte,
die mitten im Text aufhört und in sich selbst rollt.

Links umzustellen ist eine Entscheidung mit Folgen: Die Navigation dieses Handbuchs ist mit offenem
Kapitel rund 1640 px hoch, auf der Startseite rund 2560 px, bei 900 px Fensterhöhe. Stehen bleiben
heißt dort zwingend „rollt in sich selbst“. Das Basis-Template kommt auf rund 700 px und stünde
einfach still. Die zwei Spalten schalten an verschiedenen Breiten um: links ab 901 px, rechts ab
1201 px — darunter liegen sie unter dem Text, wo Stehenbleiben nichts bedeutet.

## Was doch literal dasteht

Gezählt am 21.09.2026 über die 31 Stylesheets, Kommentare und Variablendeklarationen abgezogen:
**16 Farbwerte** in drei Dateien. Alle haben denselben Grund — an dieser Stelle *kann* keine
Variable stehen.

| Wo | Was | Warum |
| --- | --- | --- |
| `body-code` | 10 Farben | Die fünf Syntax-Korrekturen — je der ersetzte und der ersetzende Wert. |
| `body-mermaid` | 4 Farben | Mermaids Fehlerzustand und seine zwei Fußnotenfarben, die es selbst einfärbt. |
| `a11y` | 2 Grautöne | In `@media print`. Auf Papier gilt weder die helle noch die dunkle Palette. |
| überall | 20× `1px`/`2px` | Haarlinien und Fokusringe. Eine Linie ist ein Pixel breit, nicht ein Rasterschritt. |
| überall | 56× `0.1em`, `1em` u. a. | Maße, die sich auf die Schriftgröße beziehen und nicht auf die Abstandsskala — der Innenabstand einer Code-Pille, die Größe eines Symbols in Zeilenhöhe. Die drei wiederkehrenden Laufweiten sind seit dem 05.09.2026 Tokens. |
| 28 Media-Queries | `480px`, `720px`, `900px`, `901px`, `1200px`, `1201px` | Eine Media-Query kann keine Variable lesen. |

## Was sich wiederholt, und warum es das darf

Zwei Formen stehen in mehreren Stylesheets fast wortgleich:

| Form | in wie vielen Dateien |
| --- | ---: |
| Die Panel-Überschrift — Überschriftenschrift, versal, halbfett, gedämpft, `--tpl-tracking-label` | 9 |
| Der überfahrene Link — Akzentfarbe, unterstrichen, `--tpl-underline-offset` | 8 |

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

Diese 48 Variablen liest `base.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--bodyFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 3 weitere Komponenten |
| `--col-ring-reach` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 22 weitere Komponenten |
| `--headerFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 15 weitere Komponenten |
| `--icon-chevron` | im Stylesheet gesetzt (`base.scss`) | Callouts |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 14 weitere Komponenten |
| `--tpl-col-left-height` | `none` | nur hier |
| `--tpl-col-left-mask` | `none` | nur hier |
| `--tpl-col-left-position` | `static` | nur hier |
| `--tpl-col-right-height` | `calc(100dvh - var(--tpl-header-h) - 2 * v…` | nur hier |
| `--tpl-col-right-mask` | `var(--tpl-fade-mask-end)` | nur hier |
| `--tpl-col-right-position` | `sticky` | nur hier |
| `--tpl-fade` | `14px` | nur hier |
| `--tpl-fade-mask` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--tpl-focus-color` | `var(--secondary)` = `#1463A3` | nur hier |
| `--tpl-focus-offset` | `2px` | Callouts |
| `--tpl-focus-width` | `2px` | Callouts |
| `--tpl-header-h` | im Stylesheet gesetzt (`base.scss`) | Explorer, Die Navigation |
| `--tpl-header-pad` | im Stylesheet gesetzt (`base.scss`) | Kopfbereich |
| `--tpl-icon-sm` | `0.95rem` | 3 weitere Komponenten |
| `--tpl-leading-normal` | `1.6` | Die Navigation |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-leading-tight` | `1.25` | nur hier |
| `--tpl-motion` | `150ms ease` | 13 weitere Komponenten |
| `--tpl-page-fade` | `24px` | Kopfbereich |
| `--tpl-radius-md` | `8px` | 17 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 10 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 19 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 12 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 5 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 20 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 weitere Komponenten |
| `--tpl-target` | `44px` | 12 weitere Komponenten |
| `--tpl-text-2xl` | `1.75rem` | Titel und Datum |
| `--tpl-text-3xl` | `2.25rem` | Titel und Datum, Fehlerseite |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |
| `--tpl-text-lg` | `1.15rem` | Suche, Link-Vorschau |
| `--tpl-text-sm` | `0.875rem` | 20 weitere Komponenten |
| `--tpl-text-xl` | `1.4rem` | Der Sprachumschalter |
| `--tpl-tracking-caps` | `0.06em` | Code, 3.1 – Bases |
| `--tpl-tracking-label` | `0.08em` | 9 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
