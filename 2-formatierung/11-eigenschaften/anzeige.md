---
title: Anzeige der Eigenschaften
description: Wo die Tabelle steht, was sie zeigt und wie man das ändert.
section: 2 – Formatierung
tags:
  - formatierung
  - frontmatter
translationKey: formatierung/eigenschaften/anzeige
cover: "[[assets/covers/cover-eigenschaften.svg]]"
---

Die Eigenschaften stehen als klappbare Tabelle unter dem Artikel.

## Die Stellschrauben

| Option | Wirkung |
| --- | --- |
| `includeAll: true` | zeigt **jedes** Frontmatter-Feld |
| `includedProperties` | zeigt nur diese, in dieser Reihenfolge |
| `excludedProperties` | blendet einzelne aus |
| `hidePropertiesView: true` | schaltet die Tabelle ganz ab |

In dieser Vorlage steht `includeAll` auf `false` — sonst stünde auf jeder Seite dieselbe
Wiederholung dessen, was ohnehin darüber steht.

## In dieser Vorlage

**Von Haus aus** rendert das [[7-nachschlagen/01-glossar#Plugin|Plugin]] eine schlichte Tabelle in Textfarbe.

**In dieser Vorlage** liegt sie auf einer getönten Fläche mit Rahmen, der Schlüssel steht gedämpft
und schmal, der Wert nimmt den Rest. Die Kopfzeile ist versal und klein — sie ist Beschriftung,
nicht Inhalt.

Eine Feinheit mit Messung dahinter: Die Schlüsselspalte bekommt **keine** Breite zugewiesen,
sondern die Wertspalte `width: 100%`. Beides heißt „der Schlüssel ist so breit wie sein Inhalt" —
aber nur der zweite Weg funktioniert. Mit `width: 1%` auf dem Schlüssel maß die Zelle 7,94 px, und
der Text lag über dem Wert.
