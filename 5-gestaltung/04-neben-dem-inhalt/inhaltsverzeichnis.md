---
title: Inhaltsverzeichnis
description: Die Gliederung rechts — alle Ebenen, nicht nur drei.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - seitenapparat
translationKey: gestaltung/neben-dem-inhalt/inhaltsverzeichnis
---

## Von Haus aus

Quartz zeigt die Überschriften einer Seite als flache Liste mit Einzug. **Die Voreinstellung ist
`maxDepth: 3`** — alles ab der vierten Überschriftenebene fehlt, und im Markup tauchen nur die
Tiefen 0 und 1 auf.

## In dieser Vorlage

`maxDepth` steht auf **6**. Damit erscheint jede Ebene bis `h6`; auf einer normalen Seite sind das
die Tiefen 0 bis 4. Zu sehen ist das unter
[[1-einstieg/04-so-ist-eine-seite-aufgebaut|Ein langer Artikel]].

Gestaltet ist jede Stufe einzeln:

- **Einzug** steigt bis Tiefe 4 um je ein `--tpl-indent` — dasselbe Maß wie im [[7-nachschlagen/01-glossar#Explorer|Explorer]], damit die
  beiden Leisten miteinander fluchten.
- **Größe und Gewicht** sinken mit der Tiefe; ab Tiefe 3 wird kleiner gesetzt.
- **Ab Tiefe 5** wird nicht weiter eingerückt, sondern mit einem Punkt markiert. Fünf Einzüge in
  einer drei Spalten breiten Leiste lassen kein Wort mehr übrig.
- **Wie weit man ist**, sagt die Führungslinie: Sie steht im Akzent bis zu der Überschrift, die
  eben vorbeigezogen ist, und bleibt darunter grau. Eine Fortschrittsleiste, gebaut aus den
  Einträgen selbst — sie stapeln sich lückenlos, ihre 2-px-Ränder ergeben eine Linie.
- **Wo man ist**, sagt ein Wort: der letzte markierte Eintrag steht im Akzent. Das Gewicht bleibt
  aus dem Spiel — die Einträge sind 13 px, und ein Sprung auf 600 setzt bei jedem Scrollen die
  ganze Spalte neu.
- **Es zeigt sich ganz.** Quartz deckelt diese Komponente gleich dreifach — `flex: 0 0.5 auto` mit
  `overflow-y: hidden`, dazu `max-height: calc(100% - 2rem)` auf der Liste und noch eine Regel in
  seinem Basis-Stylesheet. Zusammen machen die drei aus einer langen Gliederung einen kurzen Stummel
  mit eigener Rollleiste, mitten in einer Spalte, die selbst schon rollte. Alle drei sind hier
  aufgehoben.
- **Gerollt wird eine Ebene höher**, in der rechten Spalte als Ganzem — mit derselben weichen Kante
  wie im Explorer und mit nur einer Rollleiste statt zweier ineinander. Der Innenabstand der Spalte
  ist so tief wie die Kante, damit der erste und der letzte Eintrag nicht darunter liegen.
- **Kein Ausblenden per Deckkraft.** Quartz dimmt einen Eintrag, der noch nicht gelesen ist, auf
  `opacity: 0.35`; das misst sich auf diesem Grund unter 3:1. Der Zustand bleibt, gesagt wird er in
  zwei Stufen der Palette — `--gray` und `--darkgray`, beide gemessen — statt in Deckkraft.

## Die rechte Spalte steht

Ein Inhaltsverzeichnis, das mit dem Text nach oben wegrollt, ist eine Liste von Stellen, zu denen
man nicht mehr springen kann. Solange es eine rechte Spalte gibt — also ab 1201 px — bleibt sie
deshalb stehen (`position: sticky`) und rollt nur in sich selbst, wenn ihr Inhalt höher wird als das
Fenster. Am Tablet gibt es keine Spalte mehr, in der etwas kleben könnte: Inhaltsverzeichnis und
Graph stehen dort als zwei Kästen nebeneinander unter dem Text.

Drei Dinge gehören dafür zusammen, und ohne eines davon passiert gar nichts: `align-self: start` —
ein Raster-Element füllt sonst seine Zeile, und was schon ganz oben *und* ganz unten ist, kann
nirgends kleben —, ein `top`, und eine Maximalhöhe.

Das `top` ist seit dem 05.09.2026 keine feste Zahl mehr, sondern `--tpl-header-h` plus einen
Abstand: Der Kopfbereich klebt selbst, und die Spalte liest seine Höhe aus derselben Rechnung,
statt eine zweite Kopie davon zu führen.

> [!note] Die Tiefenzahlen sind relativ
> `depth-0` ist nicht `h1`, sondern die flachste Überschrift der Seite. Auf einer normalen Seite ist
> das `h2`, also landet `h6` auf `depth-4`.

> [!note] Quartz markiert nicht, wo man ist, sondern wie weit man kam
> Der Beobachter des Plugins setzt `.in-view` auf **jeden** Eintrag, dessen Überschrift über dem
> unteren Fensterrand liegt, und nimmt es vom Rest wieder weg — eine Marke „bis hierher gelesen“,
> keine Marke „hier stehst du“. Wer das für Letzteres hält, färbt auf einer langen Seite die halbe
> Gliederung ein, und eine halb hervorgehobene Gliederung hebt nichts hervor.
>
> Die Linie ist der richtige Gebrauch dafür: Eine Skala darf halb voll sein. Wo sie endet, ist die
> aktuelle Stelle — und das ist genau der letzte markierte Eintrag, also der markierte, auf den kein
> markierter mehr folgt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 17 Variablen liest `aside-toc.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tpl-indent` | `0.85rem` | Explorer |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 6 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
