---
title: Dokumente
description: PDFs einbinden, verlinken und auf eine bestimmte Seite springen.
section: Formatierung
tags:
  - formatierung
  - medien
translationKey: formatierung/medien/dokumente
cover: "[[assets/covers/cover-medien.svg]]"
---

## Als Link

```md
[Das Beispieldokument](assets/beispiel-dokument.pdf)
```

[Das Beispieldokument](assets/beispiel-dokument.pdf)

Der Browser entscheidet, ob er das PDF anzeigt oder herunterlädt. Das ist der unaufwendigste Weg
und der einzige, der auf jedem Gerät gleich funktioniert.

## Als Einbettung

```md
![[beispiel-dokument.pdf]]
```

![[beispiel-dokument.pdf]]

## Auf eine bestimmte Seite

Obsidian kennt einen Seitenanker:

```md
![[beispiel-dokument.pdf#page=2]]
[Zur zweiten Seite](assets/beispiel-dokument.pdf#page=2)
```

[Zur zweiten Seite](assets/beispiel-dokument.pdf#page=2)

Der Anker ist eine Konvention der PDF-Betrachter, kein Teil des PDF-Formats.

> [!warning] Beim eingebetteten PDF geht der Anker verloren
> Gemessen: `![[beispiel-dokument.pdf#page=2]]` erzeugt `<iframe src="…/beispiel-dokument.pdf">` —
> **ohne** den Anker. Die Einbettung beginnt immer auf Seite 1. Nur der gewöhnliche Link behält
> ihn, und der oben funktioniert.

## Als eigenes Fenster

```md
<iframe src="assets/beispiel-dokument.pdf" width="100%" height="500"></iframe>
```

<iframe src="assets/beispiel-dokument.pdf" width="100%" height="500" title="Beispieldokument, drei Seiten"></iframe>

Der Weg über `<iframe>` ist der einzige, der die Größe wirklich bestimmt. Er braucht ein `title`,
sonst hat der Rahmen für einen Screenreader keinen Namen.

> [!warning] Ein eingebettetes PDF ist keine barrierefreie Seite
> Der Betrachter im Browser ist eine eigene Anwendung mit eigener Bedienung. Wer den Inhalt
> zugänglich machen will, stellt ihn zusätzlich als Text bereit — und verlinkt das PDF als
> Beigabe, nicht als einzige Quelle.

## In dieser Vorlage

Ein Link auf eine Datei sieht aus wie ein externer Link, mit Pfeil. Ein eingebettetes PDF bekommt
denselben Rahmen und dieselben Ecken wie ein Bild, damit es nicht als Fremdkörper in der Seite
sitzt.

**Von Haus aus** bindet Quartz PDFs nicht besonders ein — ein [[7-nachschlagen/01-glossar#Wikilink|Wikilink]] darauf wird zu einem
gewöhnlichen Link.
