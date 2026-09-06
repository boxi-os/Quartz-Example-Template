---
title: Einbettungen
description: Eine andere Seite mitten in dieser anzeigen.
section: Formatierung
tags:
  - formatierung
  - links
translationKey: formatierung/links/einbettungen
cover: "[[assets/covers/cover-links.svg]]"
---

Ein Ausrufezeichen vor dem Wikilink bettet den Inhalt ein, statt darauf zu verweisen.

```md
![[2-formatierung/02-struktur/trennlinien]]
```

![[2-formatierung/02-struktur/trennlinien]]

## Nur einen Abschnitt

```md
![[2-formatierung/04-links/wikilinks#Kurzform]]
```

![[2-formatierung/04-links/wikilinks#Kurzform]]

## Nur einen Block

Mit der Blockkennung aus [[2-formatierung/04-links/ziele|Sprungziele]]:

```md
![[2-formatierung/04-links/ziele#^merksatz]]
```

![[2-formatierung/04-links/ziele#^merksatz]]

Das ist die feinste Stufe: ein einzelner Absatz statt einer ganzen Seite oder eines Abschnitts.

## Ein Bild von außerhalb

Auch eine URL lässt sich einbetten:

```md
![Beschreibung](https://example.com/bild.png)
```

Das lädt bei jedem Seitenaufruf von einem fremden Server. Für eine Website, die auch offline und in
zehn Jahren noch funktionieren soll, ist die Datei im Vault die bessere Wahl.

## In dieser Vorlage

Eine eingebettete Seite bekommt einen gestrichelten Balken links und eine getönte Fläche — man soll
sehen, wo fremder Inhalt anfängt und aufhört. **Von Haus aus** ist die Einbettung optisch nicht vom
umgebenden Text getrennt.

> [!warning] Vorsicht mit Ketten
> Bettet die eingebettete Seite ihrerseits etwas ein, wird die Seite schnell unübersichtlich — und
> ein Kreis (A bettet B ein, B bettet A ein) ist ein Fehler, den erst der Build zeigt.
