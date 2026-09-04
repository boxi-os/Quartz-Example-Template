---
title: Explorer
description: Der Ordnerbaum links — bis zur vierten Ebene gestaltet.
section: Gestaltung
tags:
  - gestaltung
  - navigation
---

Links im Fenster steht der Baum über alle Notizen. Er ist die Komponente mit dem größten
Gestaltungsaufwand in dieser Vorlage, weil die Tiefe das eigentliche Problem ist.

## Von Haus aus

Quartz rückt jede Ebene ein und färbt den aktiven Eintrag. Auf Ebene drei oder vier lässt sich
nicht mehr erkennen, zu welchem Elternordner eine Datei gehört — der Einzug allein trägt die
Struktur nicht.

## In dieser Vorlage

- **Führungslinie je Ebene.** Jede verschachtelte Liste bekommt eine Haarlinie zum Elternordner.
  Bei vier Ebenen sind das vier Linien, an denen das Auge zurückfindet.
- **Gewicht sinkt mit der Tiefe.** Ebene 1 ist fett, Ebene 2 halbfett, ab Ebene 3 normal und
  kleiner. Der Kopf einer Verzweigung ist damit auffindbar.
- **Ab Ebene fünf wird nicht weiter eingerückt**, nur noch die Linie geführt — fünf Einzüge lassen
  in einer 240 px breiten Spalte kein Wort mehr übrig.
- **Der aktive Eintrag** bekommt Farbe, Halbfett *und* einen Balken links.
- **Lange Namen** werden abgeschnitten statt umgebrochen; drei Zeilen für einen Dateinamen zerreißen
  den Baum.
- **Ein langer Baum scrollt in sich selbst** (60 % der Fensterhöhe) statt die Fußzeile
  wegzuschieben.

Zu sehen ist das am besten unter [[handbuch/grundlagen/begriffe/abkuerzungen/liste|Liste]] — vier
Ordner tief.

## Zwei Funde beim Bauen

Die Klassennamen führen in die Irre. **Nur die Wurzelliste heißt `explorer-ul`**; jede verschachtelte
heißt `ul.tree-item-children`. Und **`.nav-file-title` ist der Link selbst**, nicht sein Elternteil.
Die erste Fassung dieser Datei stylte deshalb ins Leere — sichtbar war das nicht, weil Quartz'
eigene Einrückung ähnlich genug aussah.

Zugeklappt kappt Quartz die ganze Komponente bei `1.2em`. Wer seiner Überschrift eine Zielgröße von
44 px gibt, verliert sie damit vollständig. Diese Vorlage verlegt das Einklappen deshalb auf den
Inhalt und lässt den Kopf stehen.

> [!note] Er startet zugeklappt
> Das ist Quartz' Verhalten, und die Plugin-Optionen kennen dafür keinen Schalter. Ein Klick auf
> die Überschrift öffnet ihn; der Zustand wird gemerkt.
