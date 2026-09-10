---
title: 6.3 – Schriften
description: Drei Familien, selbst gehostet — und warum die @font-face-Regeln ersetzt werden.
section: 6 – Anpassen
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

Bis zum 06.09.2026 legte die App beim Import einer Schriftdatei eine `@font-face`-Regel **ohne
`font-weight` und ohne `font-style`** an. Bei einer Variable Font hieß das: Der Browser behandelt
sie als Gewicht 400 und verzerrt jeden fetten Schnitt selbst, statt die mitgelieferte Achse zu
nutzen. Bei zwei Schnitten derselben Familie verdrängte der zweite den ersten — genau der Fall des
aufrechten und des kursiven Inter dieser Vorlage.

**Das ist behoben.** Die App liest jetzt die Gewichtsachse und das Kursiv-Bit aus der Datei selbst
und schreibt beides. Ein Wert fehlt weiterhin: die `unicode-range`. Ohne sie lädt der Browser die
Datei auch für Zeichen, die im Latin-Ausschnitt gar nicht enthalten sind, und setzt sie dann aus
einer Schrift, die keine Glyphe dafür hat, statt auf den Stapel zurückzufallen.

Diese Vorlage ersetzt den erzeugten Block deshalb weiterhin — mit denselben Gewichten und Stilen,
die die App heute selbst schreiben würde, plus dem Bereich.

## Fallback

Jede Rolle hat einen echten Stapel dahinter (`ui-sans-serif, system-ui, …`). Wenn eine woff2 nicht
lädt, fällt die Seite auf etwas Gewähltes zurück, nicht auf die Voreinstellung des Browsers.
