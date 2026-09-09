---
title: Kopfbereich
description: Wortmarke, Seitentitel und die vier Bedienelemente in einer Zeile.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/kopfbereich
---

Oben steht die Wortmarke, daneben der Seitentitel, am rechten Ende Suche, Farbschema-Umschalter,
Lesemodus und der Sprachumschalter. Darunter eine Trennlinie.

## Von Haus aus

Der Kopfbereich enthält nur den Seitentitel. Eine Marke gibt es nicht — dafür müsste man eine
eigene Komponente bauen. Suche und die beiden Umschalter sitzen in der linken Seitenleiste.

## In dieser Vorlage

Die Marke kommt aus einer **Layout-Box-Instanz** mit Inline-SVG, einmal hell und einmal dunkel. Sie
ist zugleich der Link zur Startseite.

Zwei Feinheiten:

- Der **Text der Marke ist visuell versteckt**, aber im Dokument vorhanden. Der Link enthält sonst
  nur ein SVG und hätte keinen zugänglichen Namen. `display: none` wäre hier falsch gewesen — genau
  dieser Fehler steckte in der ersten Fassung.
- Die vier Bedienelemente stehen **im Kopf, nicht in der Leiste**. Dort sucht man sie, und es ist
  der einzige Bereich, den jeder [[7-nachschlagen/01-glossar#Frame|Frame]] hat — auf der Fehlerseite gab es vorher weder Suche noch
  Farbschema-Umschalter, weil sie keine Seitenleisten hat.
- Sie bilden eine **Gruppe** (`toolbar`) mit `wrap`, damit vier Bedienelemente und der Seitenname
  auch auf einem 360 px breiten Telefon nebeneinander passen.
- Am Telefon wird der Kopf zur **App-Leiste**: Er bleibt beim Scrollen oben stehen, läuft über die
  volle Breite und nimmt den Schubladen-Knopf des [[7-nachschlagen/01-glossar#Explorer|Explorers]] mit auf. Die Suche gibt dort ihr Wort
  auf und wird ein Quadrat wie die beiden anderen; ihre 44 px behält sie.

## Er bleibt stehen, der Titel geht

Seit dem 05.09.2026 klebt der Kopf auf jeder Breite oben am Fenster, nicht mehr nur am Telefon: Die
vier Bedienelemente und der Weg zurück zur Startseite sind das, wonach man mitten in einem langen
Artikel greift, und mehrere Seiten hier sind drei Bildschirme hoch.

Seine Höhe ändert sich dabei nicht. Was sich ändert, ist die Seite darum: Der Kopf ist die eine von
**zwei Ebenen**, und die andere scrollt weg. Über dem Text steht der Bereich `beforeBody` mit
Brotkrumen, Tags, Überschrift und Datum — der Titelblock der Seite, und der geht mit dem Text. Die
Leiste bleibt. Genau das ist die Veränderung beim Scrollen, und sie braucht keinen Effekt: Sie
folgt daraus, wo die Dinge stehen.

Damit die Leiste in diesem Zustand noch etwas sagt, trägt sie **zwei Namen nebeneinander** — den
der Website und den des Kapitels (`{{frontmatter.section}}`, aus dem Frontmatter jeder Notiz). Das
Kapitel wiederholt die Überschrift nicht, also dürfen beide dauerhaft dastehen; wer über die
Überschrift hinausgescrollt ist, weiß weiter, wo er ist.

> [!note] Vorher stand hier ein Effekt, und er lief nur in zwei von drei Browsern
> Bis zum 09.09.2026 schrumpfte der Kopf beim Scrollen um 8 px, tauschte den Sitenamen gegen den
> Seitennamen und trug eine Fortschrittslinie. Alle drei hingen an `animation-timeline` —
> CSS, das an die Scrollposition gebunden ist statt an die Uhr. Chromium und WebKit können das,
> **Firefox nicht**: an der installierten Fassung 155.0.1 nachgemessen, alle fünf Abfragen negativ,
> und es ist seit Jahren nicht in Sicht. Die Effekte standen hinter `@supports` und passierten dort
> also einfach nicht — das sichtbarste Element der Website war in zwei Engines das eine und im
> dritten ein anderes.
>
> Die Fortschrittslinie fehlt seitdem ersatzlos, und das ist kein Verlust: Das
> [[5-gestaltung/04-neben-dem-inhalt/inhaltsverzeichnis|Inhaltsverzeichnis]] markiert längst, wie
> weit gelesen ist, und tut das mit einem Skript des Plugins — also in jedem Browser.

Zwei Dinge hängen an der Höhe des Kopfes und stehen deshalb in derselben Rechnung:

- Die **rechte Spalte** klebt unter dem Kopf, nicht darunter verborgen: Ihr `top` liest
  `--tpl-header-h`, dieselbe Rechnung, aus der der Kopf selbst seine Höhe bezieht.
- **Sprungziele** halten die Höhe der Leiste über sich frei, dazu die 24 px der Ausblendung darunter
  (`scroll-margin-block-start`) — sonst landet jede angesprungene Überschrift hinter dem Kopf oder
  im Verlauf, der ihn nach unten abschließt.

## Ein Fund beim Bauen

Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] setzt `width: 100%` auf jede [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]]. In einer Flex-Zeile machte das die Marke
1376 px breit und schob den Titel in die nächste Zeile. `flex` hebt eine gesetzte Breite nicht auf —
sie musste ausdrücklich zurückgenommen werden.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 15 Variablen liest `nav-header.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--titleFont` | `"Instrument Sans", ui-sans-serif, system-…` | nur hier |
| `--tpl-header-pad` | im Stylesheet gesetzt (`base.scss`) | 6.4 Variablen |
| `--tpl-header-title` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--tpl-page-fade` | `24px` | nur hier |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
