---
title: 5 – Die Gestaltung
description: Was Quartz von Haus aus tut und was diese Vorlage daran ändert — Komponente für Komponente, mit der Tabelle der Variablen, die jede davon liest.
section: 5 – Die Gestaltung
tags:
  - gestaltung
translationKey: gestaltung/index
---

Eine Quartz-Website besteht aus **Komponenten**: dem [[7-nachschlagen/01-glossar#Explorer|Explorer]], der Suche, dem Inhaltsverzeichnis,
den [[7-nachschlagen/01-glossar#Brotkrumen|Brotkrumen]], der Fußzeile — jede von einem [[7-nachschlagen/01-glossar#Plugin|Plugin]] gebaut, jede mit einem eigenen Aussehen.
Dieses Kapitel geht sie der Reihe nach durch, sortiert nach ihrem Ort auf der Seite; die Orte sind
in [[1-einstieg/04-so-ist-eine-seite-aufgebaut|1.4 – So ist eine Seite aufgebaut]] benannt.

## Wie jede Seite aufgebaut ist

Jede Seite behandelt **eine** Komponente und hat zwei Absätze:

> **Von Haus aus** — was Quartz ohne Zutun macht.
> **In dieser Vorlage** — was hier anders ist, und warum.

Der Vergleich steht direkt bei dem Element, das man dabei ansieht. Wer seine eigene Website mit
dieser vergleicht, findet so den Unterschied benannt. Und wer ihn ändern will, findet unten auf
derselben Seite die Tabelle **„Welche Variablen hier greifen“**: die Variablen, die das
Stylesheet dieser Komponente liest, mit ihrem Wert und der Angabe, was sich sonst noch mit ändert.
Diese Tabellen sind erzeugt, nicht von Hand gepflegt; sie können den Stylesheets nicht
widersprechen.

Ein **Stylesheet** ist die Datei, in der das Aussehen beschrieben ist — in der Sprache [[7-nachschlagen/01-glossar#CSS und SCSS|CSS]], hier in
ihrer Erweiterung [[7-nachschlagen/01-glossar#CSS und SCSS|SCSS]]. Diese Vorlage hat 30 davon, eins je Komponente, und jede Seite hier nennt
das ihre. Ändern lassen sie sich in QuartzControl unter *Stile → Eigenes CSS*; wann das nötig ist
und wann eine Variable reicht, steht in [[6-anpassen/01-etwas-aendern|6.1 – Etwas ändern]].

## Die Abschnitte

| Abschnitt | Komponenten |
| --- | --- |
| [[5-gestaltung/01-navigation/index\|5.1 – Navigation]] | Explorer, Suche, [[7-nachschlagen/01-glossar#Farbschema\|Farbschema]], Lesemodus, Kopfbereich, Fußzeile, Sprachumschalter |
| [[5-gestaltung/02-ueber-dem-inhalt/index\|5.2 – Über dem Inhalt]] | Brotkrumen, Titel und Datum, Eigenschaften, Tags |
| [[5-gestaltung/03-im-inhalt/index\|5.3 – Im Inhalt]] | Fließtext, [[7-nachschlagen/01-glossar#Callout\|Callouts]], Code, Tabellen und Medien |
| [[5-gestaltung/04-neben-dem-inhalt/index\|5.4 – Neben dem Inhalt]] | Inhaltsverzeichnis, [[7-nachschlagen/01-glossar#Rückverweise\|Rückverweise]], [[7-nachschlagen/01-glossar#Graph\|Graph]], Zuletzt geändert |
| [[5-gestaltung/05-layout-boxen/index\|5.5 – Layout-Boxen]] | ein Plugin, fünfmal eingesetzt |
| [[5-gestaltung/06-erzeugte-seiten/index\|5.6 – Erzeugte Seiten]] | Ordner- und Tag-Seiten, Suchergebnisse, Link-Vorschau, Fehlerseite |

Zwei Komponenten stehen woanders, weil ihr Stylesheet zu einem Abschnitt in Kapitel 2 gehört: die
Diagramme unter [[2-formatierung/09-diagramme/index|2.9 – Diagramme]] und die Formeln unter
[[2-formatierung/08-mathematik/index|2.8 – Mathematik]]. Und was unter allem liegt — Farben,
Schriften, Variablen, Seitenraster, [[7-nachschlagen/01-glossar#Barrierefreiheit|Barrierefreiheit]] — ist Kapitel [[6-anpassen/index|6 – Anpassen]].

## Die drei Entscheidungen, die alles andere tragen

1. **Die Breite entscheidet das Raster** — der [[7-nachschlagen/01-glossar#Frame|Frame]], an einer Stelle, nicht zusätzlich der Absatz.
2. **Farben sind gemessen.** 89 Paare, alle über der WCAG-Schwelle, in beiden Modi.
3. **Farbe und Maß stehen nicht in den Stylesheets**, sondern in 53 Variablen, die in der App
   bearbeitbar bleiben. Was doch literal dasteht, ist benannt und begründet.
