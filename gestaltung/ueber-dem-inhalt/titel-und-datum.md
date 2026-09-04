---
title: Titel und Datum
description: Die Überschrift der Seite und die Zeile darunter.
section: Gestaltung
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

Aus dem Frontmatter, sonst aus git, sonst aus dem Dateisystem — in dieser Reihenfolge, eingestellt
beim Plugin *Created modified date*. Bei einer Notiz, die noch nie committet wurde, warnt der Build:
*„isn't yet tracked by git, dates will be inaccurate"*.

> [!note] Das Format folgt der Seite, nicht der Website
> Quartz formatiert Daten site-weit nach `configuration.locale`, hier also deutsch. Das
> `localizeDates` des Mehrsprachigkeits-Plugins formatiert jedes `<time>`-Element im Browser in der
> Sprache der Seite nach — eine englische Seite zeigt damit ein englisches Datum.
