---
title: Die Instanzen
description: Dasselbe Plugin, siebenmal, für jeweils etwas anderes.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - layout-box
aliases:
  - 5-gestaltung/05-layout-boxen/die-fuenf-instanzen
translationKey: gestaltung/layout-boxen/die-instanzen
---

| Schlüssel | Ort | Form | Was daran zu sehen ist |
| --- | --- | --- | --- |
| `layoutBoxMark` | Kopfbereich | inline, SVG hell/dunkel | Bildumschaltung, `{{root}}`, `{{siteTitle}}` |
| `layoutBoxPageName` | Kopfbereich | inline, leeres `span` | `{{frontmatter.section}}` in einem Attribut |
| `layoutBoxNote` | linke Spalte | `file:` mit `.md`, eingeklappt | Markdown-Schnipsel, `<details>` |
| `layoutBoxCta` | nach dem Inhalt | inline, eigene Klasse | `{{root}}`, `{{siteTitle}}`, `title:` |
| `layoutBoxHint` | nach dem Inhalt | inline, nur mobil | `display: mobile-only` an einer Instanz |
| `layoutBoxColophon` | Fußzeile | inline | `{{locale}}`, `{{slug}}` |
| — | Fußzeile | inline, nur ein `<style>` | `{{slug}}` als Teil eines Selektors |

Die letzte hat keinen Schlüssel im [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]] und ist auch sonst keine Box im üblichen Sinn:
Sie gibt nichts aus als ein `<style>` und ist selbst ausgeblendet. Warum es sie trotzdem gibt, steht
weiter unten.

## Sechs von sieben nutzen `html:`, eine `file:`

Das war bis zum 6. September 2026 eine Notwendigkeit: Schnipsel-Dateien liegen unter
`quartz/static/snippets/`, und kein [[7-nachschlagen/01-glossar#Baustein|Baustein]] eines Vorlagenpakets sammelte diesen Ordner ein. Eine
Instanz mit `file:` kam im Zielprojekt mit einem Verweis ins Leere an.

Seitdem trägt der Baustein *Statische Dateien* alles unter `quartz/static/`, und beide Wege
funktionieren. Die Aufteilung ist damit eine Vorführung geworden: Die eine `file:`-Instanz zeigt den
Weg über eine Datei, die sechs anderen zeigen, dass Markup im Konfigurationseintrag ohne diesen
Eintrag gar nicht erst ankommen kann. Auch die Wortmarke bleibt deshalb ein Inline-SVG.

## Die Gestaltung je Ort

Die Stelle im Layout entscheidet über die Form: Eine Box im Kopfbereich ist eine Wortmarke, dieselbe
Komponente nach dem Inhalt ist ein Aufruf mit Fläche und Balken, in der Fußzeile eine zentrierte,
kleine Zeile.

## Vier davon sprechen zwei Sprachen

Vier der sieben tragen Text und stehen deshalb in der Konfiguration zweimal: einmal deutsch als
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

Die drei anderen tragen keinen Fließtext: Die Wortmarke trägt den Namen der Website, der nicht
übersetzt wird; der Kapitelname in der Leiste kommt aus dem Frontmatter der Seite selbst und ist
damit schon in ihrer Sprache; und die letzte gibt überhaupt keinen Text aus.

> [!info] Vorher stand das in jeder Seite
> Bis zum 5. September 2026 gab es `byLang` nicht, und jede der 126 englischen Seiten trug vier
> Blöcke im eigenen Frontmatter — 876 Zeilen, die alle dasselbe sagten. Die Überschriften ließen
> sich so überhaupt nicht übersetzen, weil die Frontmatter-Steuerung damals kein `title` kannte.
> Beides hat das Plugin an diesem Tag nachgeholt.

## Zwei Instanzen, die nichts anzeigen

Die zwei jüngsten Boxen sind keine Kästen. Sie nutzen das Plugin als das, was es im Kern ist: ein
Weg, Markup an eine bestimmte Stelle der Seite zu bekommen — mit Platzhaltern, die beim Rendern
dieser einen Seite aufgelöst werden.

**Der Kapitelname in der Leiste** ist ein leeres `span`, das seinen Text über `content: attr()` aus
einem Attribut zieht. Das klingt umständlich und ist der einzige Weg, der eine Seite ohne
Frontmatter überlebt: Einen Platzhalter, den es nicht auflösen kann, lässt das Plugin als Text
stehen — mit dem Wert im Text hätten 72 der 345 gebauten Seiten `{{frontmatter.section}}` in der
Leiste gezeigt. Im Attribut lässt sich genau das abfragen (`[data-section^="{{"]`) und der Kasten
ausblenden.

**Der Ordnerseiten-Marker** rendert ein `<style>`, das nur die aktuelle Seite kennt. Er ist die
einzige Möglichkeit, im [[7-nachschlagen/01-glossar#Explorer|Explorer]] die *Ordnerseite* zu markieren, auf der man gerade steht: Das
Explorer-Plugin setzt seine `.active`-Klasse ausschließlich auf Datei-Zeilen, eine Ordnerzeile trägt
nur ein `data-folderpath`, und die aktuelle Seite steht in `<body data-slug>`. Zwei Attribute
miteinander zu vergleichen kann kein Selektor. Also wird die Regel gebaut statt gesucht — `{{slug}}`
steht beim Rendern zur Verfügung und füllt genau den einen Wert, den der Selektor braucht.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 27 Variablen liest `plugin-layout-box.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--codeFont` | `"JetBrains Mono", ui-monospace, SFMono-Re…` | 4 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tertiary` | `#196B6B` · dunkel `#2CAFAD` | Fließtext, 2.9 – Diagramme |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-leading-snug` | `1.4rem` | 4 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-strong` | `var(--gray)` = `#5F5F5F` | 8 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 15 weitere Komponenten |
| `--tpl-space-3xs` | `0.125rem` | 6 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-sm` | `0.75rem` | 10 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 5 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DDDDDD` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 weitere Komponenten |
| `--tpl-text-base` | `1rem` | 4 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
