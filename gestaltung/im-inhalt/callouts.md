---
title: Callouts
description: Zwölf Farben, alle neu gesetzt und gemessen.
section: Gestaltung
tags:
  - gestaltung
  - im-inhalt
  - callouts
translationKey: gestaltung/im-inhalt/callouts
---

## Von Haus aus

Quartz liefert zwölf Typfarben mit, jeweils dieselbe in beiden Farbschemata, dazu einen Rahmen und
eine sehr blasse Fläche.

Gemessen gegen den hellen Grund dieser Vorlage scheitern **elf von zwölf** an der WCAG-Schwelle:

| Typ | Standardfarbe | gegen hellen Grund |
| --- | --- | --- |
| `note` | `#448aff` | 3,23 : 1 |
| `question` | `#dba642` | 2,14 : 1 |
| `tip` | `#00bfa5` | 2,27 : 1 |
| `danger` / `failure` / `bug` | `#db4242` | 4,20 : 1 — und 4,16 : 1 im dunklen Modus |

## In dieser Vorlage

Alle dreizehn sind neu gesetzt, **je Modus einmal**, und werden bei jedem Lauf zweifach gemessen:
gegen den Seitengrund und gegen die eigene getönte Fläche. Der Farbton bleibt erhalten — Blau bleibt
Blau —, damit der Typ weiterhin an der Farbe erkennbar ist.

Dazu drei Struktur-Entscheidungen:

- **Balken statt Vollrahmen.** Ein Callout soll auffallen, ohne die Spalte zu zerschneiden.
- **Der Titel ist das Bedienelement**, wenn der Callout faltbar ist — mit eigenem Fokusring in der
  Typfarbe.
- **Verschachtelte Callouts** geben ihren Rahmen auf und behalten nur den Balken.

Die Prüfung liest die Farben **aus dem Stylesheet**, nicht aus einer Kopie in der Konfiguration.
Ein Wert, der hier geändert wird, wird auch hier gemessen.
