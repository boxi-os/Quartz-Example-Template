---
title: Titel und Datum
description: Die Überschrift der Seite und die Zeile darunter.
section: Gestaltung
tags:
  - gestaltung
  - ueber-dem-inhalt
---

## Der Titel

**Von Haus aus** setzt Quartz die Seitenüberschrift in derselben Größe wie eine `h1` im Text.

**In dieser Vorlage** ist sie größer, enger gesperrt (`letter-spacing: -0.02em`) und **vom Lesemaß
ausgenommen**: Ein Titel wird überflogen, nicht Zeile für Zeile gelesen, und ein Titel, der nach
vier Wörtern umbricht, sieht aus wie ein Versehen. `text-wrap: balance` verteilt die Zeilen
gleichmäßig, wenn er doch umbricht.

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
