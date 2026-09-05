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

## Vier davon sprechen zwei Sprachen

Vier der fünf tragen Text und stehen deshalb in der Konfiguration zweimal: einmal deutsch als
Grundeinstellung, einmal englisch unter `byLang`.

```yaml
options:
  file: sidebar-note.md
  title: Über dieses Handbuch
  byLang:
    en:
      file: sidebar-note.en.md
      title: About this handbook
```

Das Plugin liest das Feld `lang` aus dem Frontmatter der Seite — dasselbe, aus dem Quartz das
`<html lang>` schreibt — und legt den passenden Eintrag über die Grundeinstellung. Es braucht dafür
keinen Partner: Ob `lang` vom Mehrsprachigkeits-Plugin kommt oder von Hand dasteht, ist ihm gleich.

Die fünfte ist die Wortmarke. Sie trägt den Namen der Website, der nicht übersetzt wird, und bleibt
deshalb ohne `byLang`.

> [!info] Vorher stand das in jeder Seite
> Bis zum 5. September 2026 gab es `byLang` nicht, und jede der 126 englischen Seiten trug vier
> Blöcke im eigenen Frontmatter — 876 Zeilen, die alle dasselbe sagten. Die Überschriften ließen
> sich so überhaupt nicht übersetzen, weil die Frontmatter-Steuerung damals kein `title` kannte.
> Beides hat das Plugin an diesem Tag nachgeholt.
