---
title: 6.3 Schriften
description: Drei Familien, selbst gehostet — und warum die @font-face-Regeln von Hand korrigiert sind.
section: 6 Anpassen
tags:
  - anpassen
translationKey: anpassen/schriften
---

| Rolle | Schrift | Wofür |
| --- | --- | --- |
| header | **Instrument Sans** | Überschriften, Beschriftungen, Bedienelemente |
| body | **Inter** | Fließtext, aufrecht und kursiv |
| code | **JetBrains Mono** | Code, Zahlen in Tabellen, Pfade |

Alle drei stehen unter der SIL Open Font License und werden **selbst gehostet** — vier Dateien,
Latin-Ausschnitt, zusammen 157 KB. Es geht keine Anfrage an Google.

## Warum selbst hosten

**Von Haus aus** lädt Quartz Schriften von Google Fonts — bequem, aber jede Seitenanfrage geht
dabei an einen Dritten. Diese Vorlage stellt `fontOrigin: 'local'` und schaltet das
Schriften-Plugin ab; damit läuft keiner der beiden Google-Wege.

## Der Fund dahinter

Die App legt beim Import einer Schriftdatei eine `@font-face`-Regel an — **ohne `font-weight` und
ohne `font-style`**. Bei einer Variable Font heißt das: Der Browser behandelt sie als Gewicht 400
und verzerrt jeden fetten Schnitt selbst, statt die mitgelieferte Achse zu nutzen. Bei zwei
Schnitten derselben Familie verdrängt der zweite den ersten.

Diese Vorlage korrigiert den erzeugten Block deshalb: mit `font-weight: 400 700`, `font-style` und
`unicode-range`. Auf der Seite sieht man den Unterschied an jedem fetten Wort.

## Fallback

Jede Rolle hat einen echten Stapel dahinter (`ui-sans-serif, system-ui, …`). Wenn eine woff2 nicht
lädt, fällt die Seite auf etwas Gewähltes zurück, nicht auf die Voreinstellung des Browsers.
