---
title: Die fünf Instanzen
description: Dasselbe Plugin, fünfmal, für jeweils etwas anderes.
section: 5 Die Gestaltung
tags:
  - gestaltung
  - layout-box
translationKey: gestaltung/layout-boxen/die-fuenf-instanzen
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

Inline-HTML steckt dagegen im Konfigurationseintrag und reist mit dem [[7-nachschlagen/01-glossar#Baustein|Baustein]] *[[7-nachschlagen/01-glossar#Plugin|Plugins]]* mit. Auch
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

Das Plugin liest das Feld `lang` aus dem [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]] der Seite — dasselbe, aus dem Quartz das
`<html lang>` schreibt — und legt den passenden Eintrag über die Grundeinstellung. Es braucht dafür
keinen Partner: Ob `lang` vom Mehrsprachigkeits-Plugin kommt oder von Hand dasteht, ist ihm gleich.

Die fünfte ist die Wortmarke. Sie trägt den Namen der Website, der nicht übersetzt wird, und bleibt
deshalb ohne `byLang`.

> [!info] Vorher stand das in jeder Seite
> Bis zum 5. September 2026 gab es `byLang` nicht, und jede der 126 englischen Seiten trug vier
> Blöcke im eigenen Frontmatter — 876 Zeilen, die alle dasselbe sagten. Die Überschriften ließen
> sich so überhaupt nicht übersetzen, weil die Frontmatter-Steuerung damals kein `title` kannte.
> Beides hat das Plugin an diesem Tag nachgeholt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 27 Variablen liest `plugin-layout-box.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 weitere Komponenten |
| `--darkgray` | `#33322E` · dunkel `#D5D7DB` | 18 weitere Komponenten |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 20 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 13 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 20 weitere Komponenten |
| `--tertiary` | `#9C4221` · dunkel `#E8A56B` | Fließtext, 2.9 Diagramme |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 17 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5D57` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 6 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 4 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DEDCD5` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 13 weitere Komponenten |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 18 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
