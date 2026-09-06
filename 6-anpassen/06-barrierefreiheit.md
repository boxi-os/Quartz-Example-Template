---
title: 6.6 Barrierefreiheit
description: Was diese Vorlage dafür tut — und warum es meist nur eine Zeile mehr ist.
section: Anpassen
tags:
  - anpassen
  - barrierefreiheit
translationKey: anpassen/barrierefreiheit
---

## Kein Zustand hängt allein an der Farbe

Der aktive Eintrag im Explorer hat Farbe, Schriftschnitt **und** einen Balken. Ein erledigter
Aufgabenpunkt ist gedämpft **und** durchgestrichen. Ein externer Link ist andersfarbig **und**
trägt einen Pfeil. Wer Farben nicht unterscheiden kann, verliert dadurch keine Information.

## Bedienbar mit der Tastatur

Jedes Bedienelement hat einen sichtbaren Fokusring — eine einzige Regel über `:focus-visible`, mit
eigener Farbe auf getönten Flächen, damit der Ring nicht auf der eigenen Farbe liegt. `outline:
none` kommt in dieser Vorlage nirgends vor.

Der Kopierknopf am Codeblock erscheint bei Hover, bei Fokus *und* dauerhaft auf Geräten ohne
Zeiger. **Von Haus aus** ist er nur bei Hover sichtbar — und damit auf einem Telefon unerreichbar.

## Zielgrößen

Alles, was man antippt, ist mindestens 44 px groß (`--tpl-target`). WCAG 2.2 verlangt 24; 44 ist
die Größe, bei der niemand zielen muss.

## Systemeinstellungen werden beachtet

| Einstellung | Wirkung |
| --- | --- |
| `prefers-reduced-motion` | setzt `--tpl-motion` auf 0 — eine Stelle für alle Übergänge |
| `prefers-reduced-transparency` | ersetzt die durchscheinenden Flächen von Suche und Graph |
| `forced-colors` | zeichnet Ränder, wo die Vorlage sonst mit Flächen arbeitet |
| Druck | entfernt alle Leisten, schreibt Link-Ziele aus, verhindert Umbrüche in Blöcken |

## Was fehlt

Quartz rendert **keinen Skip-Link**, und ein Stylesheet kann keinen hinzufügen — das Element muss
im Markup stehen, um fokussierbar zu sein. Auf einer Seite mit Explorer kostet der Weg zum Artikel
per Tastatur deshalb einen Tabstopp pro Baumzeile. Die Gestaltung dafür liegt bereit; sie greift,
sobald ein solcher Link existiert.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese Variable liest `a11y.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
