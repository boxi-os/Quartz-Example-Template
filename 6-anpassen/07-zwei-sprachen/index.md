---
title: 6.7 Zwei Sprachen
description: Wie dieselbe Website auf Deutsch und Englisch entsteht — aus einem Vault und einem Build.
section: Anpassen
tags:
  - anpassen
  - mehrsprachigkeit
translationKey: anpassen/zwei-sprachen/index
---

Quartz kennt **ein** `locale` je Website. Diese Vorlage veröffentlicht trotzdem zwei Sprachen aus
einem Vault, mit dem Plugin `quartz-multilanguage`.

## Der Aufbau

| | Deutsch | Englisch |
| --- | --- | --- |
| Wo die Dateien liegen | im Wurzelverzeichnis des Vaults | unter `en/` |
| Wie die Sprache erkannt wird | `defaultLanguage` — nichts passt, also deutsch | Ordner-Strategie: der erste Pfadteil ist `en` |
| Adressen | `/formatierung/text/betonung` | `/en/formatting/text/emphasis` |
| Dateinamen | deutsch | englisch |
| Tags | `formatierung`, `gestaltung`, … | `formatting`, `design`, … |

**Die deutschen Notizen mussten dafür nicht umziehen.** Das ist der Grund für diesen Zuschnitt: Die
Ordner-Strategie hätte auch `de/` verlangen können, aber dann hätte jede der 127 Notizen einen neuen
Pfad bekommen und jeder der 143 Wikilinks eine Korrektur. Eine Seite, auf die keine Strategie passt,
fällt in die Standardsprache — das genügt.

## Die Teile

| Teil | Wo |
| --- | --- |
| Spracherkennung und Verknüpfung | [[6-anpassen/07-zwei-sprachen/verknuepfung\|Wie die Sprachen sich finden]] |
| Der Umschalter im Kopfbereich | [[5-gestaltung/01-navigation/sprachumschalter\|Der Sprachumschalter]] |
| Was einsprachig bleibt | [[6-anpassen/07-zwei-sprachen/grenzen\|Wo die zwei Sprachen aufhören]] |

## Was das Plugin sonst noch tut

- **`<html lang>` je Seite.** Das Plugin trägt in jede Seite ohne eigenes `lang` das Locale ihrer
  Sprache ein. Ein Screenreader wechselt damit die Aussprache, und die Stylesheets dieser Vorlage
  hängen ihre Explorer-Regel daran.
- **`hreflang` und `og:locale`.** Jede Seite mit Übersetzung bekommt `<link rel="alternate">` auf
  ihre Geschwister und ein `x-default`. Dafür braucht die Konfiguration `baseUrl`.
- **Hinweise über der Seite.** Wer mit englischer Browsersprache auf einer deutschen Seite landet,
  bekommt oben einen Kasten: „Diese Seite gibt es auch auf Englisch." Der Text wird erst im Browser
  eingesetzt und steht deshalb weder im Suchindex noch in der Beschreibung.
- **Daten in der Seitensprache.** `localizeDates: true` formatiert jedes `<time>`-Element im
  Browser nach — das Einzige an der Quartz-Oberfläche, was ohne zweiten Build zweisprachig wird.

## Ein Build oder zwei

Diese Website ist **ein** Build. Das hält die Suche, den Graphen und die Adressen zusammen, kostet
aber die Oberfläche: Alles, was Quartz selbst beschriftet, folgt `configuration.locale` und bleibt
deutsch. Das Plugin kennt dafür `publishLanguages` — ein Build je Sprache, jeder mit eigenem
`locale` und eigener `baseUrl`. Was das jeweils bedeutet, steht unter
[[6-anpassen/07-zwei-sprachen/grenzen|Wo die zwei Sprachen aufhören]].
