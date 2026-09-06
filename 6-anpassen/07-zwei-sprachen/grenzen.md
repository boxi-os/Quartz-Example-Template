---
title: Wo die zwei Sprachen aufhören
description: Was in einem Build einsprachig bleibt — gemessen, nicht vermutet.
section: Anpassen
tags:
  - anpassen
  - mehrsprachigkeit
translationKey: anpassen/zwei-sprachen/grenzen
---

Diese Website ist **ein** [[7-nachschlagen/01-glossar#Build|Build]] mit `locale: de-DE`. Der Inhalt ist zweisprachig, die Oberfläche
nicht. Was das konkret heißt:

## Die Oberfläche von Quartz bleibt deutsch

Jede sichtbare Beschriftung, die nicht aus einer Notiz kommt, holt ihre Sprache aus
`configuration.locale` — und zwar site-weit. Nachgesehen im gebauten Code der [[7-nachschlagen/01-glossar#Plugin|Plugins]]: Der [[7-nachschlagen/01-glossar#Explorer|Explorer]]
liest `cfg?.locale`, die [[7-nachschlagen/01-glossar#Rückverweise|Rückverweise]] `cfg.locale`; keine einzige Komponente sieht die Sprache der
Seite an, die sie gerade rendert.

Betroffen sind: „Explorer", „Backlinks", „[[7-nachschlagen/01-glossar#Graph|Graph]] View", „Table of Contents", „Recent Notes", der
Leerzustand der Rückverweise, die Beschriftungen der Suche.

**Ausnahme Daten.** `localizeDates: true` formatiert jedes `<time>`-Element im Browser nach der
Seitensprache. Das ist das Einzige, was das Plugin an dieser Grenze verschieben kann.

## Die Layout-Boxen sind die Ausnahme

Vier der fünf Boxen sprechen beide Sprachen — Inhalt und Überschrift. Sie sind damit das einzige
Bedienelement dieser Website, das die Sprache der *Seite* liest statt die der Website. Das kostet
vier Einträge `byLang` in der Konfiguration und keine Zeile in den Notizen; wie es aussieht, steht
in [[5-gestaltung/05-layout-boxen/die-fuenf-instanzen|Die fünf Instanzen]].

Es ist zugleich der Beleg dafür, woran die anderen scheitern: Das Plugin kann das nur, weil es
`fileData.frontmatter.lang` sieht. Quartz' eingebaute Komponenten bekommen an dieser Stelle
`cfg.locale` gereicht und hätten gar keine Möglichkeit, die Seitensprache zu erfahren.

## Eine Suche, ein Graph, eine Liste

Der Suchindex umfasst beide Sprachen — eine deutsche Seite kann in einem englischen Suchergebnis
auftauchen. Dasselbe gilt für „Zuletzt geändert" und für den globalen Graphen. Die Rückverweise
trennen sich von selbst, weil jede Seite nur innerhalb ihres eigenen Baums verlinkt.

## Die Fehlerseite hat keine Sprache

Quartz schreibt **eine** `404.html` für die ganze Website. Wer sich in einer englischen Adresse
vertippt, landet auf der deutschen Fehlerseite.

## Der Explorer musste von Hand getrennt werden

Das Plugin bringt einen Filter für den Explorer mit (`languageExplorerFilter`), aber der Explorer
nimmt Funktionen **nur aus `quartz.ts`** entgegen — [[7-nachschlagen/01-glossar#YAML|YAML]] kann keine Funktion transportieren. Dieses
Projekt baut sein Layout aus `quartz.config.yaml`, der Weg ist damit zu.

Gelöst ist es im [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]]. Der Explorer schreibt an jede Ordnerzeile ein `data-folderpath` mit dem
vollen Pfad und an jede Datei ein absolutes `href` — beides reicht, um den fremdsprachigen Ast
auszublenden:

```scss
html[lang^="de"] .explorer-ul > li:has(> [data-folderpath="en/index"]) { display: none; }
```

Auf einer englischen Seite wird umgekehrt alles außer diesem Ast ausgeblendet, und die Kopfzeile des
`en`-Ordners gleich mit — sonst stünde der ganze englische Baum eine Ebene eingerückt unter einem
Ordner namens „en".

## Seiten ohne Frontmatter lassen sich nicht verknüpfen

Eine `.base`- oder `.canvas`-Datei ist kein [[7-nachschlagen/01-glossar#Markdown|Markdown]] und hat keine Kopfzeilen. Sie kann deshalb
keinen `translationKey` tragen und keinen [[7-nachschlagen/01-glossar#Alias|Alias]]. Verknüpft würden zwei solche Seiten nur über den
Pfad — und der ist hier je Sprache verschieden. Der Umschalter bietet auf diesen Seiten deshalb die
Startseite der anderen Sprache an.

Aus demselben Grund tragen sie kein `lang` und gelten damit als deutsch — `<html lang="de">`, und
die [[7-nachschlagen/01-glossar#Layout-Box|Layout-Boxen]] zeigen ihre deutsche Grundeinstellung, obwohl die Seite unter `en/` liegt.
Gemessen an vier Seiten: drei [[7-nachschlagen/01-glossar#Base|Bases]] und einer [[7-nachschlagen/01-glossar#Canvas|Canvas]]. Wer das ändern will, muss es dort ändern, wo
die Sprache herkommt: `.base` und `.canvas` sind JSON und YAML, nicht Markdown, und haben keinen
Platz für ein Frontmatter-Feld.

## Was ein zweiter Build lösen würde

`publishLanguages: [de]` beziehungsweise `QUARTZ_LANGS=en` wirft vor dem Rendern alle anderen
Sprachen weg. Mit zwei Konfigurationen — jede mit eigenem `locale` und eigener `baseUrl` — entstehen
zwei vollständig lokalisierte Websites, samt Oberfläche, eigener Suche und eigener Fehlerseite.

Der Preis: zwei Adressen statt einer, zwei Builds, und ein Umschalter, der über die Domaingrenze
zeigt. Für diese Beispielwebsite ist der eine Build die bessere Wahl — sie soll zeigen, wie das
Plugin arbeitet, und dazu gehört auch, wo es aufhört.
