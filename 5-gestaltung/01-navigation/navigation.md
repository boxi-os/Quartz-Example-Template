---
title: Die Navigation
description: Das Akkordeon links, die Schublade am Telefon, „Zurück“ und „Weiter“ unter dem Text.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/navigation
---

Durch dieses Handbuch führen zwei Navigationen: links ein Menü über alle Kapitel, unter jedem
Text „Zurück“ und „Weiter“. Beide kommen aus demselben [[7-nachschlagen/01-glossar#Plugin|Plugin]],
`quartz-navigations`, das eine Komponente mit zehn Darstellungen mitbringt; diese Website setzt
zwei davon ein.

## Von Haus aus

Quartz bringt für die Navigation den [[5-gestaltung/01-navigation/explorer|Explorer]] mit, einen
Ordnerbaum. Er stand bis zum 20.09.2026 auch hier. Ein Baum zeigt alles auf einmal, und bei sieben
Kapiteln mit zusammen über hundert Notizen sind das aufgeklappt mehr Zeilen, als die Spalte hoch
ist. Der Explorer ist seither abgeschaltet und bleibt trotzdem gestaltet — wer ihn einschaltet,
findet ihn fertig vor.

## Das Menü links

Die Darstellung heißt **Akkordeon**: Jedes Kapitel ist eine Zeile, die aufklappt.

- **Ein Kapitel ist offen, und zwar das, in dem man liest.** Öffnet man ein anderes, schließt sich
  das vorige. Welches offen steht, entscheidet die gelesene Seite — ein zweites Gedächtnis dafür im
  Browser gibt es bewusst nicht, es könnte ihr nur widersprechen.
- **Die ganze Zeile klappt auf.** Die Kapitelseite selbst steht als erster Eintrag *im*
  aufgeklappten Kapitel, unter der Überschrift „Übersicht“. Vorher war die Zeile ein Link und nur
  ein 24 px breiter Pfeil am Rand klappte auf.
- **„Start“ steht ganz oben** und führt zur Startseite.
- **Die Reihenfolge** kommt zuerst aus der Nummer vor dem Dateinamen, dann aus dem Titel. Die
  Nummern stehen trotzdem auch im Titel — dort liest sie der Leser. Abgeschnitten werden sie nicht:
  Die Option dafür schnitt sie auch aus „1 – Einstieg“, und im Menü stand dann „– Einstieg“.
- **Entwürfe und ungelistete Seiten** fehlen im Menü, wie überall sonst
  ([[4-seiten-steuern/02-entwurf-und-ungelistet|4.2]]).

## Am Telefon

Unter 900 px wird das Menü zur **Schublade**. Der Knopf dafür sitzt in der App-Leiste oben links,
die Schublade fährt über eine abgedunkelte und leicht unscharfe Seite, und ein eigener
Schließknopf steht in der Schublade selbst. Die Zeilen bekommen dort ihre Daumenhöhe von 44 px
zurück; in der Seitenleiste am Desktop sind 32 px richtig.

## Zurück und Weiter

Unter jedem Text stehen zwei Knöpfe zur vorigen und zur nächsten Seite. Die Reihenfolge läuft durch
die ganze Gliederung, über Kapitelgrenzen hinweg — ein Handbuch wird der Reihe nach gelesen, und am
Ende eines Kapitels geht es ins nächste statt in eine Sackgasse.

Sie stehen **ganz unten**: nach dem Text, den zwei Kästen, „Weiterlesen“ und den Eigenschaften.
Dort sucht man den Weg zur nächsten Seite. Am Telefon stehen die zwei Knöpfe untereinander, damit
ein langer Seitentitel nicht in einem halben Knopf umbrechen muss, und auf der Startseite, wo es
kein „Zurück“ gibt, steht kein leerer Kasten. Beides tut das Plugin seit Fassung 0.3.1 selbst.

„Zurück“ und „Weiter“ sind klein, versal und gesperrt gesetzt — dieselbe Beschriftung wie über den
Kästen daneben.

## Was die Vorlage dazutut

Fast nichts, und das ist Absicht. Das Plugin gestaltet Zeilen, Klappen, Pager und Schublade
selbst, über rund sechzig eigene Variablen. Die Vorlage verbindet diese Variablen mit ihren
eigenen — Farben, Abstände, Radien, Schatten —, und ergänzt, wofür es keine Variable gibt: die
Unschärfe hinter der Schublade, die Daumenhöhe am Telefon, die Beschriftung des Pagers.

Die Variablen des Plugins stehen deshalb **nicht** unter *Stile → Variablen*: Es deklariert sie auf
seinem eigenen Element, und ein Wert von außen käme dort nie an. Was sich ändern lässt, sind die
`--tpl-*`-Tokens, an denen sie hängen — die Tabelle unten.

## Die anderen acht

Gestaltet sind alle zehn Darstellungen, nicht nur die zwei, die hier zu sehen sind — wer eine
andere einschaltet, bekommt sie fertig. Eine davon, eine waagerechte Kapitelleiste im
Kopfbereich, stand einen Nachmittag lang hier und ist an einer Rechnung gescheitert: Die sieben
Kapitelnamen sind zusammen rund 880 px breit, und der Kopf hat neben Wortmarke und Bedienelementen
rund 680 px übrig.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 27 Variablen liest `nav-navigations.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 22 weitere Komponenten |
| `--headerFont` | `"Noto Sans", system-ui, "Segoe UI", Robot…` | 15 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 14 weitere Komponenten |
| `--tpl-accent-bar` | `3px` | 6 weitere Komponenten |
| `--tpl-backdrop` | `rgba(0, 0, 0, 0.3)` | Explorer |
| `--tpl-backdrop-blur` | `4px` | Explorer |
| `--tpl-drawer-width` | `min(86vw, 340px)` | Explorer |
| `--tpl-header-h` | im Stylesheet gesetzt (`base.scss`) | 6.4 – Variablen, Explorer |
| `--tpl-icon` | `1.1rem` | 3 weitere Komponenten |
| `--tpl-icon-sm` | `0.95rem` | 3 weitere Komponenten |
| `--tpl-indent` | `0.85rem` | Inhaltsverzeichnis, Explorer |
| `--tpl-leading-normal` | `1.6` | 6.4 – Variablen |
| `--tpl-motion` | `150ms ease` | 13 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 17 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 10 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 19 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 25 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 5 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 16 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 12 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 18 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 20 weitere Komponenten |
| `--tpl-target` | `44px` | 12 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 20 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 10 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 9 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
