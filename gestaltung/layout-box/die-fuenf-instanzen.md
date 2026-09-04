---
title: Die fünf Instanzen
description: Dasselbe Plugin, fünfmal, für jeweils etwas anderes.
section: Gestaltung
tags:
  - gestaltung
  - layout-box
translationKey: gestaltung/layout-box/die-fuenf-instanzen
---

| Schlüssel | Ort | Form | Was daran zu sehen ist |
| --- | --- | --- | --- |
| `layoutBoxMark` | Kopfbereich | inline, SVG hell/dunkel | Bildumschaltung, `{{root}}`, `{{siteTitle}}` |
| `layoutBoxNote` | linke Spalte | `file:` mit `.md`, aufklappbar | Markdown-Schnipsel, `<details>` |
| `layoutBoxHint` | linke Spalte | inline, nur mobil | zwei Instanzen unabhängig steuerbar |
| `layoutBoxCta` | nach dem Inhalt | inline, eigene Klasse | `{{frontmatter.…}}` |
| `layoutBoxColophon` | Fußzeile | inline | `{{locale}}`, `{{slug}}` |

## Warum vier von fünf `html:` statt `file:` nutzen

**Ein Vorlagenpaket transportiert `quartz/styles/` und `quartz/static/fonts/` — sonst nichts.**
Snippet-Dateien und Bilder bleiben zurück. Eine Instanz mit `file:` käme im Zielprojekt mit einem
Verweis ins Leere an.

Inline-HTML steckt dagegen im Konfigurationseintrag und reist mit dem Baustein *Plugins* mit. Auch
die Wortmarke ist deshalb ein Inline-SVG und keine Bilddatei.

Die fünfte Instanz nutzt bewusst den Datei-Weg — sie zeigt beides: dass es geht, und dass die Datei
beim Weitergeben mitkopiert werden muss.

## Die Gestaltung je Ort

Die Stelle im Layout entscheidet über die Form: Eine Box im Kopfbereich ist eine Wortmarke, dieselbe
Komponente nach dem Inhalt ist ein Aufruf mit Fläche und Balken, in der Fußzeile eine zentrierte,
kleine Zeile.

## Eine offene Einschränkung

Beim Import einer Vorlage überlebt derzeit **nur eine** der fünf Instanzen. Alle tragen denselben
abgeleiteten Namen (`quartz-layout-box`), und der Import ordnet die Einträge nach Namen zu. Das ist
gemessen und als Befund festgehalten.

> [!note] Die englischen Seiten füllen vier davon selbst
> Inhalt lässt sich je Seite ersetzen, deshalb zeigt jede englische Seite mit `layoutBoxNote` auf
> ein englisches Schnipsel und setzt Hinweis, Aufruf und Impressumszeile auf englischen Text.
> Der *Titel* einer Box lässt sich so nicht ersetzen — siehe
> [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].
