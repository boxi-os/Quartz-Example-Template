---
title: Example
description: Das Handbuch der Vorlage Example für QuartzControl — zum Lesen, zum Nachschlagen und zum Vergleichen mit der eigenen Website.
section: Start
tags:
  - start
---

Diese Website ist das Handbuch der Vorlage **Example** für QuartzControl. Sie erklärt, was die
Vorlage tut und wie man sie anpasst — und sie ist zugleich der Beleg: Jede Seite hier ist mit genau
dieser Vorlage gebaut. Wer an seiner eigenen Website etwas ändert, kann es hier mit dem Original
vergleichen.

> [!tip] Drei Türen
> **Neu hier?** Kapitel [[1-einstieg/index|1 Einstieg]] erklärt auf vier kurzen Seiten, was
> Obsidian, Quartz und QuartzControl miteinander zu tun haben und wie aus einer Notiz eine Website
> wird.
>
> **Schreiben?** Kapitel [[2-formatierung/index|2 Formatierung]] zeigt jedes Element, das man in
> Obsidian schreiben kann — als Quelltext und als Ergebnis.
>
> **Etwas ändern?** Kapitel [[6-anpassen/index|6 Anpassen]] sagt, wo eine Farbe, eine Schrift oder
> ein Abstand herkommt und wie man ihn ändert, meist ohne eine Zeile Code.

## Die sieben Kapitel

| Kapitel | Die Frage, die es beantwortet |
| --- | --- |
| [[1-einstieg/index\|1 Einstieg]] | Was ist das hier, und wie hängt es zusammen? |
| [[2-formatierung/index\|2 Formatierung]] | Wie schreibe ich fett, eine Tabelle, ein Diagramm — und wie sieht es dann aus? |
| [[3-obsidian-formate/index\|3 Obsidian-Formate]] | Was wird aus einer Base, einem Canvas, einer Zeichnung? |
| [[4-seiten-steuern/index\|4 Eine Seite steuern]] | Wie verstecke ich eine Seite, gebe ihr ein Datum, einen zweiten Namen, ein Titelbild? |
| [[5-gestaltung/index\|5 Die Gestaltung]] | Was macht die Vorlage an jedem Teil der Seite anders als Quartz — und warum? |
| [[6-anpassen/index\|6 Anpassen]] | Wie ändere ich Farben, Schriften, Abstände, das Seitenraster, die Sprachen? |
| [[7-nachschlagen/index\|7 Nachschlagen]] | Was heißt dieses Wort? Was geht nicht, und warum? |

## Was die Vorlage ausmacht

Drei Entscheidungen tragen alles andere; ausführlich stehen sie unter
[[1-einstieg/01-was-diese-vorlage-ist|1.1 Was diese Vorlage ist]].

1. **Die Breite entscheidet das Raster.** Das Seitenraster gibt dem Text seine Spalte; es gibt
   keine zweite Begrenzung am einzelnen Absatz, die damit in Streit geraten könnte.
2. **Farben sind gemessen.** 89 Farbpaare erfüllen die Kontrastschwelle der Richtlinie WCAG in hell
   und dunkel, die dreizehn neu gesetzten Callout-Farben eingeschlossen. Quartz' eigene tun das
   nicht — elf von zwölf scheitern.
3. **Kein Stylesheet setzt eine Farbe oder ein Maß selbst.** Beides kommt aus Variablen, die nach
   dem Import in der App bearbeitbar bleiben.

## Zwei Sprachen, ein Vault

Dieselben Seiten gibt es auf Englisch; umgeschaltet wird oben rechts. Der Inhalt liegt in einem
eigenen Obsidian-Vault, auf den das Projekt per Symlink zeigt — wer hier etwas ändert, ändert es an
der Quelle. Wie beides gebaut ist: [[6-anpassen/07-zwei-sprachen/index|6.7 Zwei Sprachen]] und
[[1-einstieg/03-von-der-notiz-zur-website|1.3 Von der Notiz zur Website]].
