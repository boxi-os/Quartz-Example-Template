---
title: Bases
description: Abfragen über den Vault, als Tabelle, Karten oder Liste.
section: Obsidian-Formate
tags:
  - obsidian-formate
  - bases
translationKey: obsidian-formate/bases/index
---

Eine Base ist eine gespeicherte Abfrage: Sie sammelt Notizen nach Kriterien und zeigt sie in einer
oder mehreren Ansichten. Die Datei ist YAML und endet auf `.base`.

Zwei Beispiele in diesem Vault, beide über die Notizen dieser Website selbst:

- [[obsidian-formate/bases/Alle-Ansichten.base|Alle Ansichten]] — **alle fünf Darstellungsformen**
  derselben Daten: Tabelle, Kacheln, Liste, Board und Galerie
- [[obsidian-formate/bases/Formatierungsseiten.base|Formatierungsseiten]] — Tabelle und Kacheln
- [[obsidian-formate/bases/Gestaltungsseiten.base|Gestaltungsseiten]] — Liste, nach Bereich gruppiert

Wie das Format aufgebaut ist: [[obsidian-formate/bases/wie-es-funktioniert|Wie es funktioniert]].

## Die fünf Darstellungsformen

Eine Base kann dieselben Daten auf fünf Arten zeigen; die Umschalter stehen oben auf der Seite.

| Ansicht | Wofür sie taugt |
| --- | --- |
| **Tabelle** | viele Spalten vergleichen, nach einer Spalte sortieren |
| **Kacheln** | wenige Angaben je Eintrag, nebeneinander überfliegen |
| **Liste** | kompakt untereinander, mit Gruppierung |
| **Board** | nach einem Feld in Spalten aufgeteilt, wie ein Kanban |
| **Galerie** | großflächig, für Einträge mit Bild |

Alle fünf sind in dieser Vorlage gestaltet — zu sehen unter
[[obsidian-formate/bases/Alle-Ansichten.base|Alle Ansichten]].

## In dieser Vorlage

Bases-Seiten nutzen den Frame **`index`** — zwei Spalten, keine rechte Leiste. Eine Tabelle braucht
kein Inhaltsverzeichnis.

> [!warning] Der Umschalter findet diese Seiten nicht
> Eine `.base`-Datei hat kein Frontmatter und kann deshalb keinen `translationKey` tragen. Der
> Sprachumschalter bietet auf so einer Seite die Startseite der anderen Sprache an statt der
> entsprechenden Base. Siehe [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].

> [!note] Bases sind neu
> Sie kamen mit Obsidian 1.9 als Kernfunktion dazu. Ältere Vaults haben sie nicht; im
> Beispiel-Vault ist die Funktion eingeschaltet.
