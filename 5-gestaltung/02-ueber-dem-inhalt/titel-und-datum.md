---
title: Titel und Datum
description: Die Überschrift der Seite und die Zeile darunter.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - ueber-dem-inhalt
translationKey: gestaltung/ueber-dem-inhalt/titel-und-datum
---

## Der Titel

**Von Haus aus** setzt Quartz die Seitenüberschrift in derselben Größe wie eine `h1` im Text.

**In dieser Vorlage** ist sie größer und enger gesperrt (`letter-spacing: -0.02em`), und ihre
Zeilen werden ausgeglichen statt gefüllt (`text-wrap: balance`): Ein Titel wird überflogen, nicht
Zeile für Zeile gelesen, und einer, der nach vier Wörtern umbricht, sieht aus wie ein Versehen.

Auf schmalen Bildschirmen sinkt er eine Stufe — bei 390 px wäre die volle Größe der halbe
Bildschirm.

## Datum und Lesezeit

**Von Haus aus** eine Zeile in Textfarbe.

**In dieser Vorlage** gedämpft, kleiner, und die Teile sind durch einen Mittelpunkt getrennt, der
noch blasser ist als der Text. Die Werte sind der Inhalt, die Zeichensetzung tritt zurück.

## Woher das Datum kommt

Aus dem [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]], sonst aus dem Dateisystem — in dieser Reihenfolge, eingestellt beim [[7-nachschlagen/01-glossar#Plugin|Plugin]]
*Created modified date*.

> [!warning] Ein Symlink nimmt Quartz die git-Daten
> Von Haus aus steht dort `frontmatter → git → filesystem`, und [[7-nachschlagen/01-glossar#git|git]] wäre die bessere Quelle: Ein
> Commit-Datum überlebt ein Kopieren, ein Wiederherstellen und ein frisches Auschecken, die
> Änderungszeit einer Datei nicht. Hier fehlt es trotzdem. Der Inhalt dieser Website liegt in einem
> Obsidian-Vault, auf den `content/` per [[7-nachschlagen/01-glossar#Symlink|Symlink]] zeigt; das Plugin folgt dem Symlink und findet auch
> das git des [[7-nachschlagen/01-glossar#Vault|Vaults]], rechnet den Dateipfad danach aber weiter gegen das Projektverzeichnis — und
> fragt so nach einem Pfad, der aus dem Vault wieder herausführt. Jede Abfrage scheitert. Für **250
> der 254 Seiten** stand deshalb *„isn't yet tracked by git, dates will be inaccurate"* im
> Bauprotokoll; stumm blieben nur die vier Seiten, die ein `lastmod` im Frontmatter tragen und git
> daher gar nicht erst fragen. Das Datum kam die ganze Zeit aus dem Dateisystem, `git` in der Liste
> war nur Lärm. Der Fehler ist gemeldet; sobald er behoben ist, gehört `git` wieder davor.

> [!note] Das Format folgt der Seite, nicht der Website
> Quartz formatiert Daten site-weit nach `configuration.locale`, hier also deutsch. Das
> `localizeDates` des Mehrsprachigkeits-Plugins formatiert jedes `<time>`-Element im Browser in der
> Sprache der Seite nach — eine englische Seite zeigt damit ein englisches Datum.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 7 Variablen liest `meta-title-and-date.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 8 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-2xl` | `1.75rem` | 6.4 Variablen |
| `--tpl-text-3xl` | `2.25rem` | 6.4 Variablen, Fehlerseite |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
