---
title: Minimal & lesbar
description: Die Beispielvorlage für QuartzControl — alle zehn Bausteine, jede Komponente gestaltet, jeder Kontrast gemessen.
section: Start
tags:
  - vorlage
  - start
---

Diese Website ist der Beispielinhalt zur Vorlage **Minimal & lesbar**. Sie existiert, damit man die
Gestaltung sehen kann: Ein Explorer braucht Ordner, ein Inhaltsverzeichnis braucht Überschriften,
ein Graph braucht Verweise.

> [!tip] Vier Wege hinein
> Jeder Bereich zeigt etwas anderes an derselben Gestaltung.

| Bereich | Was darin steht |
| --- | --- |
| [[formatierung/index\|Formatierung]] | Jedes Obsidian-Element als Quelltext und gerendertes Ergebnis — 45 kurze Seiten |
| [[obsidian-formate/index\|Obsidian-Formate]] | Bases, Canvas und Excalidraw: drei Dateitypen, die keine Notizen sind |
| [[gestaltung/index\|Gestaltung]] | Je Komponente: was Quartz von Haus aus tut, und was diese Vorlage ändert |
| [[handbuch/index\|Handbuch]] | Vier Ordnerebenen tief — damit Explorer und Brotkrumen etwas zu zeigen haben |

## Die drei Entscheidungen, die alles tragen

1. **Die Breite entscheidet das Raster.** Der Frame gibt dem Text seine Spalte; es gibt keine
   zweite Begrenzung am einzelnen Absatz, die damit in Streit geraten könnte.
2. **Farben sind gemessen.** 78 Paare erfüllen WCAG AA in hell und dunkel, die zwölf Callout-Typen
   eingeschlossen. Quartz' eigene Callout-Farben tun das nicht — elf von zwölf scheitern.
3. **Kein Stylesheet enthält eine Zahl.** Alles liest Variablen, die nach dem Import in der App
   bearbeitbar bleiben.

## Wo der Inhalt gepflegt wird

In einem eigenen **Obsidian-Vault**. Das Projekt zeigt mit einem Symlink darauf, statt eine Kopie
zu halten. Wer hier etwas ändert, ändert es an der Quelle.

Ein Blick auf eine lange Seite lohnt sich: [[beispiele/langer-artikel|Ein langer Artikel]] —
Überschriften bis zur sechsten Ebene, damit das Inhaltsverzeichnis vollständig ist.
