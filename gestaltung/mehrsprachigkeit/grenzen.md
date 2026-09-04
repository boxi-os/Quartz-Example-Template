---
title: Wo die zwei Sprachen aufhören
description: Was in einem Build einsprachig bleibt — gemessen, nicht vermutet.
section: Gestaltung
tags:
  - gestaltung
  - mehrsprachigkeit
translationKey: gestaltung/mehrsprachigkeit/grenzen
---

Diese Website ist **ein** Build mit `locale: de-DE`. Der Inhalt ist zweisprachig, die Oberfläche
nicht. Was das konkret heißt:

## Die Oberfläche von Quartz bleibt deutsch

Jede sichtbare Beschriftung, die nicht aus einer Notiz kommt, holt ihre Sprache aus
`configuration.locale` — und zwar site-weit. Nachgesehen im gebauten Code der Plugins: Der Explorer
liest `cfg?.locale`, die Rückverweise `cfg.locale`; keine einzige Komponente sieht die Sprache der
Seite an, die sie gerade rendert.

Betroffen sind: „Explorer", „Backlinks", „Graph View", „Table of Contents", „Recent Notes", der
Leerzustand der Rückverweise, die Beschriftungen der Suche.

**Ausnahme Daten.** `localizeDates: true` formatiert jedes `<time>`-Element im Browser nach der
Seitensprache. Das ist das Einzige, was das Plugin an dieser Grenze verschieben kann.

## Die Layout-Boxen: Inhalt ja, Titel nein

Jede englische Seite setzt in ihrem Frontmatter vier der fünf Boxen auf englischen Inhalt: Die
Notiz-Box zeigt auf ein englisches Schnipsel; Hinweis, Aufruf und Impressumszeile stehen als
englisches HTML dort. Die fünfte ist die Wortmarke und trägt den Namen der Website, der nicht
übersetzt wird.

Was **nicht** geht, ist der Titel: Die Frontmatter-Steuerung des Plugins kennt `hidden`, `file` und
`html`, aber kein `title`. Die beiden betitelten Boxen — „Über dieses Handbuch" in der linken
Spalte und „Weiterlesen" unter dem Text — tragen deshalb auch auf englischen Seiten eine deutsche
Überschrift über englischem Inhalt. Der saubere Weg dafür wäre eine Option `title` in der
Frontmatter-Steuerung von `quartz-layout-box`; als Befund ist das festgehalten.

## Eine Suche, ein Graph, eine Liste

Der Suchindex umfasst beide Sprachen — eine deutsche Seite kann in einem englischen Suchergebnis
auftauchen. Dasselbe gilt für „Zuletzt geändert" und für den globalen Graphen. Die Rückverweise
trennen sich von selbst, weil jede Seite nur innerhalb ihres eigenen Baums verlinkt.

## Die Fehlerseite hat keine Sprache

Quartz schreibt **eine** `404.html` für die ganze Website. Wer sich in einer englischen Adresse
vertippt, landet auf der deutschen Fehlerseite.

## Der Explorer musste von Hand getrennt werden

Das Plugin bringt einen Filter für den Explorer mit (`languageExplorerFilter`), aber der Explorer
nimmt Funktionen **nur aus `quartz.ts`** entgegen — YAML kann keine Funktion transportieren. Dieses
Projekt baut sein Layout aus `quartz.config.yaml`, der Weg ist damit zu.

Gelöst ist es im Stylesheet. Der Explorer schreibt an jede Ordnerzeile ein `data-folderpath` mit dem
vollen Pfad und an jede Datei ein absolutes `href` — beides reicht, um den fremdsprachigen Ast
auszublenden:

```scss
html[lang^="de"] .explorer-ul > li:has(> [data-folderpath="en/index"]) { display: none; }
```

Auf einer englischen Seite wird umgekehrt alles außer diesem Ast ausgeblendet, und die Kopfzeile des
`en`-Ordners gleich mit — sonst stünde der ganze englische Baum eine Ebene eingerückt unter einem
Ordner namens „en".

## Seiten ohne Frontmatter lassen sich nicht verknüpfen

Eine `.base`- oder `.canvas`-Datei ist kein Markdown und hat keine Kopfzeilen. Sie kann deshalb
keinen `translationKey` tragen und keinen Alias. Verknüpft würden zwei solche Seiten nur über den
Pfad — und der ist hier je Sprache verschieden. Der Umschalter bietet auf diesen Seiten deshalb die
Startseite der anderen Sprache an.

## Was ein zweiter Build lösen würde

`publishLanguages: [de]` beziehungsweise `QUARTZ_LANGS=en` wirft vor dem Rendern alle anderen
Sprachen weg. Mit zwei Konfigurationen — jede mit eigenem `locale` und eigener `baseUrl` — entstehen
zwei vollständig lokalisierte Websites, samt Oberfläche, eigener Suche und eigener Fehlerseite.

Der Preis: zwei Adressen statt einer, zwei Builds, und ein Umschalter, der über die Domaingrenze
zeigt. Für diese Beispielwebsite ist der eine Build die bessere Wahl — sie soll zeigen, wie das
Plugin arbeitet, und dazu gehört auch, wo es aufhört.
