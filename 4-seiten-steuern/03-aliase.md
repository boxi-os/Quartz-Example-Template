---
title: 4.3 Aliase
description: Eine Seite unter mehreren Pfaden erreichbar machen — das Plugin Alias redirects legt Weiterleitungen an.
section: 4 Eine Seite steuern
tags:
  - seiten-steuern
aliases:
  - Zweitname
  - 4-seiten-steuern/anderer-pfad
translationKey: seiten-steuern/aliase
---

Ein **Alias** ist ein zweiter Name für eine Seite. In Obsidian findet die Schnellsuche eine Notiz
auch unter ihrem Alias, und ein `[[Alias]]` zeigt auf sie. Auf der Website baut das [[7-nachschlagen/01-glossar#Plugin|Plugin]]
*Alias redirects* für jeden Alias eine kleine Weiterleitungsseite: Wer die alte Adresse aufruft,
landet auf der neuen.

```yaml
---
aliases:
  - Zweitname
  - 4-seiten-steuern/anderer-pfad
---
```

Diese Seite ist damit unter drei Adressen erreichbar: unter ihrer eigenen, unter `/Zweitname` und
unter `/4-seiten-steuern/anderer-pfad`. Ein Alias darf ein Wort sein oder ein ganzer Pfad.

## Wofür

**Eine Seite wurde umbenannt oder verschoben.** Der alte Pfad als Alias hält alte Links am Leben —
Lesezeichen, Verweise von anderen Websites, Suchmaschinen-Treffer.

**Ein Begriff hat zwei Namen.** „Backlinks“ und „[[7-nachschlagen/01-glossar#Rückverweise|Rückverweise]]“ meinen dasselbe; ein Alias lässt
beide finden.

**Eine Übersetzung verbinden.** Ein Alias, der dem Titel der Seite in der anderen Sprache
entspricht, verbindet die beiden für den Sprachumschalter — siehe
[[4-seiten-steuern/07-uebersetzung|4.7 Übersetzung]].

> [!warning] Jeder Alias ist eine Seite
> Das Plugin baut für jeden Alias eine eigene Weiterleitungsdatei. Hundert Aliase sind hundert
> Dateien mehr in der Ausgabe. Das ist kein Fehler, aber ein Grund, Aliase dort zu setzen, wo sie
> etwas tun.

Wie man Aliase *schreibt* und wie ein Link darauf aussieht:
[[2-formatierung/04-links/aliase|Aliase]] in Kapitel 2.
