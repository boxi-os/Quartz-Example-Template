---
title: Einbettungen
description: Eine andere Seite mitten in dieser anzeigen.
section: 2 – Formatierung
tags:
  - formatierung
  - links
translationKey: formatierung/links/einbettungen
cover: "[[assets/covers/cover-links.svg]]"
---

Ein Ausrufezeichen vor dem [[7-nachschlagen/01-glossar#Wikilink|Wikilink]] bettet den Inhalt ein, statt darauf zu verweisen.

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
zehn Jahren noch funktionieren soll, ist die Datei im [[7-nachschlagen/01-glossar#Vault|Vault]] die bessere Wahl.

## Was diese Vorlage anders macht

Eine eingebettete Seite bekommt einen gestrichelten Balken links und eine getönte Fläche — man soll
sehen, wo fremder Inhalt anfängt und aufhört. **Von Haus aus** ist die Einbettung optisch nicht vom
umgebenden Text getrennt.

> [!warning] Vorsicht mit Ketten
> Bettet die eingebettete Seite ihrerseits etwas ein, wird die Seite schnell unübersichtlich — und
> ein Kreis (A bettet B ein, B bettet A ein) ist ein Fehler, den erst der [[7-nachschlagen/01-glossar#Build|Build]] zeigt.

> [!bug] Eine Einbettung bringt ihre Überschriften-Kennungen mit
> Und zwar unverändert. Quartz bildet die Kennung einer Überschrift aus ihrem Text — aus „In dieser
> Vorlage“ wird `in-dieser-vorlage` — und rechnet beim Einbetten nicht nach, ob es die auf der
> Zielseite schon gibt. Heißt eine Überschrift der eingebetteten Seite so wie eine der einbettenden,
> tragen **zwei** Elemente dieselbe Kennung.
>
> Genau das stand bis zum 10.09.2026 auf dieser Seite: Der eingebettete Anfang trägt „In dieser
> Vorlage“, und so hieß auch der letzte Abschnitt hier. Gemessen an der gebauten Seite hatte das
> drei Folgen:
>
> - Der Verweis im [[5-gestaltung/04-neben-dem-inhalt/inhaltsverzeichnis|Inhaltsverzeichnis]] sprang auf die **erste** der beiden — auf Pixel 1005 statt
>   auf 2681. Ein Browser nimmt bei einer doppelten Kennung immer die erste.
> - Der letzte Eintrag der Gliederung war schon **ganz oben** markiert. Das Skript des Plugins
>   ordnet einer Überschrift ihren Eintrag über die Kennung zu; beide Überschriften zeigten damit
>   auf denselben Eintrag, und der weiter oben stehenden gehorchte er zuerst.
> - Die Fortschrittslinie hatte deshalb ein **Loch**: Auf halber Höhe waren der erste, der zweite
>   und der vierte Eintrag markiert, der dritte nicht.
>
> Zu beheben ist das nur dort, wo die Kennungen entstehen. Was hier hilft, ist die Überschrift
> umzubenennen — deshalb heißt der Abschnitt oben „Was diese Vorlage anders macht“ und nicht wie
> sonst in diesem Kapitel. Wer eine ganze Seite einbettet, sieht am besten einmal nach, ob sich
> zwei Überschriften ins Gehege kommen.
