---
title: 6.3 – Schriften
description: Zwei Familien, selbst gehostet — und warum die @font-face-Regeln ersetzt werden.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/schriften
---

| Rolle | Schrift | Wofür |
| --- | --- | --- |
| header | **Noto Sans** | Überschriften, Beschriftungen, Bedienelemente |
| body | **Noto Sans** | Fließtext, aufrecht und kursiv |
| code | **Noto Sans Mono** | Code, Zahlen in Tabellen, Pfade |

Beide stehen unter der SIL Open Font License und werden **selbst gehostet** — drei Dateien,
Latin-Ausschnitt, zusammen 105 KB. Es geht keine Anfrage an Google.

Überschrift und Fließtext teilen sich eine Familie. Der Unterschied zwischen beiden entsteht über
Größe und Gewicht — Überschriften stehen auf 600 —, nicht über einen Wechsel der Schrift. Bis zum
20.09.2026 waren es drei Familien (Instrument Sans, Inter, JetBrains Mono) in vier Dateien; die
eine Familie weniger spart der Website eine Datei und nimmt ihr nichts, was ein Leser benennen
könnte.

## Warum selbst hosten

**Von Haus aus** lädt Quartz Schriften von Google Fonts — bequem, aber jede Seitenanfrage geht
dabei an einen Dritten. Diese Vorlage stellt `fontOrigin: 'local'` und schaltet das
Schriften-Plugin ab; damit läuft keiner der beiden Google-Wege.

## Der Fund dahinter

Bis zum 06.09.2026 legte die App beim Import einer Schriftdatei eine `@font-face`-Regel **ohne
`font-weight` und ohne `font-style`** an. Bei einer Variable Font hieß das: Der Browser behandelt
sie als Gewicht 400 und verzerrt jeden fetten Schnitt selbst, statt die mitgelieferte Achse zu
nutzen. Bei zwei Schnitten derselben Familie verdrängte der zweite den ersten — genau der Fall des
aufrechten und des kursiven Schnitts, die diese Vorlage von ihrer Textschrift mitbringt.

**Das ist behoben.** Die App liest jetzt die Gewichtsachse und das Kursiv-Bit aus der Datei selbst
und schreibt beides. Ein Wert fehlt weiterhin: die `unicode-range`. Ohne sie lädt der Browser die
Datei auch für Zeichen, die im Latin-Ausschnitt gar nicht enthalten sind, und setzt sie dann aus
einer Schrift, die keine Glyphe dafür hat, statt auf den Stapel zurückzufallen.

Diese Vorlage ersetzt den erzeugten Block deshalb weiterhin — mit denselben Gewichten und Stilen,
die die App heute selbst schreiben würde, plus dem Bereich.

## Fallback

Hinter jede Rolle setzt Quartz selbst einen Stapel — `system-ui, "Segoe UI", Roboto, …` für Text,
`ui-monospace, SFMono-Regular, …` für Code. Wenn eine woff2 nicht lädt, fällt die Seite auf etwas
Gewähltes zurück, nicht auf die Voreinstellung des Browsers.
