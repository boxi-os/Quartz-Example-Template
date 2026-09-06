---
title: 4.6 Titelbild
description: Das Feld cover — ein Bild je Seite für die Galerie und die Kacheln einer Base.
section: Seiten steuern
tags:
  - seiten-steuern
cover: "[[assets/covers/cover-index.svg]]"
translationKey: seiten-steuern/titelbild
---

Eine Base — Obsidians gespeicherte Abfrage über den Vault, siehe
[[3-obsidian-formate/01-bases/index|3.1 Bases]] — kann ihre Einträge als Galerie oder als Kacheln
zeigen. Beide Ansichten nehmen eine Option `image:`, die den **Namen einer Eigenschaft** nennt;
deren Wert darf ein Wikilink auf ein Bild, ein Pfad oder eine Hex-Farbe sein. Ohne sie zeigt jede
Kachel denselben schraffierten Platzhalter.

Diese Website nutzt dafür das Feld `cover`:

```yaml
---
cover: "[[assets/covers/cover-links.svg]]"
---
```

Jede Seite aus Kapitel 2 trägt es — 63 Seiten je Sprache, ein Bild je Abschnitt und eines für die
Kapitelseite, vierzehn Bilder insgesamt. Die Bases *Alle Ansichten* und *Formatierungsseiten* sagen
mit `image: cover`, dass sie dieses Feld lesen; die Galerie unter
[[3-obsidian-formate/01-bases/Alle-Ansichten.base|Alle Ansichten]] zeigt das Ergebnis.

## Wo die Bilder liegen

Im Vault unter `assets/covers/`, wie alle Medien dieser Website: Dort versioniert sie das git des
Vaults, und dort findet Obsidian sie beim Schreiben. Die vierzehn Bilder sind erzeugt, nicht
gezeichnet — ein Skript im Repository von QuartzControl schreibt sie.

Die Farben sind absichtlich eng beieinander: gleiches Helligkeitsband, wenig Sättigung, um das Navy
und das Sienna der Palette herum. Vierzehn volle Farben wären das Lauteste auf einer Website, deren
ganzes Argument Zurückhaltung ist. Ein Motiv, kein Text: Der Titel steht unter der Kachel, und ein
Bild, das ihn wiederholt, ist ein verschenktes Bild.

## Für eigene Seiten

Das Feld darf beliebig heißen; es muss nur in der Base unter `image:` denselben Namen tragen. Ein
Foto tut es genauso wie ein SVG. Eine Seite ohne das Feld bekommt in der Galerie den Platzhalter —
kein Fehler, nur eine leere Kachel.
