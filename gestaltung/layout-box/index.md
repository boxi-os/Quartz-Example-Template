---
title: Layout-Box
description: Ein Plugin, das beliebiges Markup an jede Stelle des Layouts setzt.
section: Gestaltung
tags:
  - gestaltung
  - layout-box
---

`quartz-layout-box` rendert einen HTML- oder Markdown-Schnipsel an jeder Stelle des Seitenlayouts:
Kopfbereich, Seitenleisten, vor oder nach dem Inhalt, Fußzeile. Diese Vorlage nutzt es **fünfmal**,
jedes Mal für etwas anderes.

## Was das Plugin kann

| Möglichkeit | Option |
| --- | --- |
| Inhalt aus einer Datei | `file:` |
| Inhalt aus der Konfiguration | `html:` |
| Markdown statt HTML | Datei auf `.md` enden lassen |
| Überschrift darüber | `title:` |
| Aufklappbar | `collapsible:` und `collapsed:` |
| Eigene CSS-Klasse | `className:` |
| Platzhalter ersetzen | `placeholders:` |
| Je Seite steuerbar | `frontmatterKey:` |
| Bild je Farbschema | Klassen `img-light` / `img-dark` |

## Platzhalter

`{{title}}`, `{{slug}}`, `{{root}}`, `{{siteTitle}}`, `{{baseUrl}}`, `{{locale}}` und jedes
Frontmatter-Feld über `{{frontmatter.name}}`. `{{root}}` ist der relative Weg zur Startseite — damit
funktioniert ein Link auch, wenn die Seite in einem Unterpfad liegt.

## Die Gestaltung

Das Plugin liefert bewusst **farblose** Stile mit: Breite, Bildumschaltung, ein gestrichelter
Platzhalter für fehlende Dateien. Das ist die richtige Entscheidung für ein Komponenten-Plugin — es
überlässt das Aussehen der Website.

Diese Vorlage gestaltet jede Klasse: `.layout-box`, `.layout-box-title`, `.layout-box-content`,
`.layout-box-missing`, dazu fünf eigene Varianten.

Weiter: [[gestaltung/layout-box/die-fuenf-instanzen|Die fünf Instanzen]] ·
[[gestaltung/layout-box/je-seite-steuern|Je Seite steuern]]
