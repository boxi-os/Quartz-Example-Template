---
title: Eigenschaften
description: Die Frontmatter-Tabelle unter dem Titel.
section: Gestaltung
tags:
  - gestaltung
  - ueber-dem-inhalt
translationKey: gestaltung/ueber-dem-inhalt/eigenschaften
---

## Von Haus aus

Eine schlichte Tabelle in Textfarbe, klappbar.

## In dieser Vorlage

- auf einer **getönten Fläche** mit Rahmen und runden Ecken
- die **Kopfzeile** versal, klein und gedämpft — sie ist Beschriftung, nicht Inhalt
- der **Schlüssel** gedämpft und so breit wie sein Text, der **Wert** nimmt den Rest
- **Werttypen** werden unterschieden: eine Zahl in Ziffernbreite, ein Wahrheitswert als
  eingefärbtes Wort, eine Liste als Reihe von Marken, ein leeres Feld kursiv

Zu sehen unter [[formatierung/eigenschaften/datentypen|Datentypen]], wo eine Seite alle vier Typen
mitbringt.

## Der Fund mit der Zellenbreite

Die naheliegende Lösung für „der Schlüssel ist so breit wie sein Inhalt" ist `width: 1%` auf der
Schlüsselzelle. Gemessen: Die Zelle wurde 7,94 px breit — exakt 1 % der Tabelle — und der Schlüssel
lag über dem Wert.

Der Weg, der funktioniert, ist der umgekehrte: **`width: 100%` auf die Wertzelle.** Sie beansprucht
alles, was übrig ist, und lässt dem Schlüssel seine Inhaltsbreite.
