---
title: Der Sprachumschalter
description: Drei Bauformen, eine davon sichtbar — und wo sie steht.
section: Gestaltung
tags:
  - gestaltung
  - mehrsprachigkeit
translationKey: gestaltung/navigation/sprachumschalter
---

Der Umschalter steht in der **Werkzeugleiste im Kopfbereich**, rechts neben Suche,
Farbschema-Umschalter und Lesemodus. Er teilt deren Maße: 44 px hoch, gleicher Rahmen, gleiche
Ecken, gleiche Rückmeldung beim Überfahren. Vier Bedienelemente in einer Zeile, die sich in der Höhe
unterscheiden, lesen sich als Fehler.

## Drei Bauformen

Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] kennt drei Darstellungen. **Alle drei sind in dieser Vorlage gestaltet**, sichtbar ist
eine — welche, entscheidet `switcher.style` in der Konfiguration.

| Form | Was sie ist | Wofür sie taugt |
| --- | --- | --- |
| `dropdown` | ein `<details>`-Element mit Liste darunter | **hier in Gebrauch** — ein Bedienelement, egal wie viele Sprachen |
| `links` | die Sprachen nebeneinander, durch `\|` getrennt | zwei Sprachen, viel Platz |
| `flags` | Flaggen-Emoji statt Namen | sehr eng, wenn die Sprachen bekannt sind |

Gewählt ist `dropdown`, weil er als **ein** Kasten neben dem Suchfeld steht und nicht breiter wird,
wenn eine dritte Sprache dazukommt. Die Liste öffnet sich nach unten, rechtsbündig unter dem Knopf,
mit demselben Schatten wie Suche und Vorschau — den einzigen beiden anderen Stellen dieser Vorlage,
die wirklich über der Seite schweben.

Die beiden anderen Formen sind trotzdem vollständig gestaltet: Wer in der App auf `links` oder
`flags` umstellt, bekommt keine ungestaltete Komponente, sondern eine, die in dieselbe Leiste passt.
Bei `flags` wächst das Emoji auf Lesegröße und der Knopf bleibt quadratisch.

## Was der Umschalter zeigt

- Die **aktuelle Sprache** steht als Knopfbeschriftung und in der Liste als hervorgehobener,
  nicht anklickbarer Eintrag mit `aria-current`.
- Die Beschriftung ist der **Name in der jeweiligen Sprache** (`switcher.label: native`) — „Deutsch"
  und „English", nicht „German". Ein Sprachname, den man nicht liest, weil man die Sprache nicht
  kann, ist keine Hilfe.
- Gibt es **keine Übersetzung** dieser Seite, führt der Eintrag auf die Startseite der anderen
  Sprache (`switcher.missing: home`) und sagt das im `title`. Die Alternativen wären, den Eintrag
  auszublenden — dann verschwindet der Ausweg — oder ihn auszugrauen, was eine Sackgasse zeigt,
  statt einen Weg anzubieten.
- Jeder Eintrag trägt `lang` und `hreflang`. Ein Screenreader spricht „English" damit englisch aus,
  auch mitten in einer deutschen Seite.

## Am Telefon

Die Werkzeugleiste ist eine Flex-Zeile mit `wrap`. Auf 390 px teilen sich Schubladen-Knopf,
Seitenname und vier Bedienelemente den Platz; die Suche gibt ihr Wort auf und wird ein Quadrat, der
Umschalter behält seinen Namen, weil zwei Buchstaben („DE") weniger sagen als „Deutsch" und der
Platz dafür reicht.

## Die Merkung

`rememberChoice: true` legt die gewählte Sprache im `localStorage` ab. Genutzt wird das von der
Wurzel-Weiche — die diese Website nicht hat, weil ihre Wurzel die deutsche Startseite ist — und von
den Hinweisen über der Seite: Wer einmal auf Englisch umgeschaltet hat, bekommt den Hinweis danach
auf Englisch, unabhängig von der Browsersprache.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 23 Variablen liest `nav-language-switcher.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#F3F4F6` | 13 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--font-interface` | `"Inter", ui-sans-serif, system-ui, -apple…` | 3 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tpl-icon-sm` | `0.95rem` | 6.4 Variablen, Explorer |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule-control` | `color-mix(in srgb, var(--gray) 70%, var(-…` | 11 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 6 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |
| `--tpl-text-xl` | `1.4rem` | 6.4 Variablen |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
