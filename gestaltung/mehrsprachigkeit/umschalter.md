---
title: Der Sprachumschalter
description: Drei Bauformen, eine davon sichtbar — und wo sie steht.
section: Gestaltung
tags:
  - gestaltung
  - mehrsprachigkeit
translationKey: gestaltung/mehrsprachigkeit/umschalter
---

Der Umschalter steht in der **Werkzeugleiste im Kopfbereich**, rechts neben Suche,
Farbschema-Umschalter und Lesemodus. Er teilt deren Maße: 44 px hoch, gleicher Rahmen, gleiche
Ecken, gleiche Rückmeldung beim Überfahren. Vier Bedienelemente in einer Zeile, die sich in der Höhe
unterscheiden, lesen sich als Fehler.

## Drei Bauformen

Das Plugin kennt drei Darstellungen. **Alle drei sind in dieser Vorlage gestaltet**, sichtbar ist
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
