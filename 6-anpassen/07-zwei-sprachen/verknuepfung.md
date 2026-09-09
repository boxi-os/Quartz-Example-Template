---
title: Wie die Sprachen sich finden
description: Drei Strategien, drei Belege — und was das Obsidian-Plugin damit zu tun hat.
section: 6 – Anpassen
tags:
  - anpassen
  - mehrsprachigkeit
translationKey: anpassen/zwei-sprachen/verknuepfung
---

Damit der Umschalter von einer Seite zu ihrer Übersetzung führen kann, muss jemand sagen, welche
zwei Seiten zusammengehören. Das [[7-nachschlagen/01-glossar#Plugin|Plugin]] kennt dafür drei Wege und probiert sie in dieser
Reihenfolge.

## 1 · `translationKey` im Frontmatter

```yaml
---
title: Betonung
translationKey: formatierung/text/betonung
---
```

Zwei Seiten mit demselben Schlüssel sind Übersetzungen voneinander. **So arbeiten 128 der 133
Paare dieser Website** — alles, was eine gewöhnliche Seite ist. Vier davon tragen zusätzlich
[[7-nachschlagen/01-glossar#Alias|Aliase]], damit auch dieser Weg auf der Website zu sehen ist; verknüpft sind auch sie über den
Schlüssel. Von den übrigen fünf gehen drei den Weg darunter und eines den darunter; das letzte,
die beiden Excalidraw-Zeichnungen, ist gar nicht verknüpft — ihre Seite rendert den Umschalter
nicht, weil das Plugin ein eigenes [[7-nachschlagen/01-glossar#Frame|Frame]] mitbringt.

Der Grund ist ein gemessener: Mehrere Seiten hier tragen denselben Titel. „Grundform" gibt es
dreimal ([[7-nachschlagen/01-glossar#Callout|Callouts]], Tabellen, Fußnoten), „Code", „Eigenschaften" und „Callouts" je zweimal. Über
Titel oder Dateinamen wäre nicht entscheidbar, welche englische Seite gemeint ist; das Plugin
erkennt das und verknüpft in so einem Fall lieber gar nicht, mit einer Warnung im [[7-nachschlagen/01-glossar#Build|Build]].

Als Schlüssel dient der deutsche Pfad ohne Endung. Er ist eindeutig, ändert sich selten, und man
sieht der Zeile an, worauf sie zeigt.

## 2 · Aliase — der Weg über das Obsidian-Plugin

Das Obsidian-Community-Plugin **Multilingual** übersetzt den Namen einer Notiz und schreibt ihn in
die `aliases`. Genau dieses Feld liest das Quartz-Plugin: Ein Alias, der dem Titel oder dem
Dateinamen einer Seite in einer anderen Sprache entspricht, verknüpft die beiden.

Drei Seiten dieser Website hängen **allein** daran und tragen absichtlich keinen `translationKey`:

| Deutsche Seite | Alias darin | Englische Seite |
| --- | --- | --- |
| [[3-obsidian-formate/01-bases/wie-es-funktioniert\|Wie eine Base aufgebaut ist]] | `How a base is built` | `en/obsidian-formats/bases/how-it-works` |
| [[3-obsidian-formate/02-canvas/wie-es-funktioniert\|Wie ein Canvas aufgebaut ist]] | `How a canvas is built` | `en/obsidian-formats/canvas/how-it-works` |
| [[3-obsidian-formate/03-excalidraw/wie-es-funktioniert\|Wie eine Excalidraw-Datei aufgebaut ist]] | `How an Excalidraw file is built` | `en/obsidian-formats/excalidraw/how-it-works` |

Alle drei heißen im Dateinamen gleich (`wie-es-funktioniert`) und liegen in verschiedenen Ordnern —
ein guter Prüfstein dafür, dass wirklich über den Titel und nicht über den Dateinamen verknüpft
wird.

> [!warning] Warum nicht überall Aliase
> Das Plugin *Alias redirects* baut für **jeden** Alias eine Weiterleitungsseite. Hätte jede der 133
> deutschen Notizen ihren englischen Titel als Alias, entstünden 133 zusätzliche Seiten, die von
> `/emphasis` auf die *deutsche* Seite führen. Das ist kein Fehler, aber es war keine Entscheidung —
> deshalb stehen die Aliase nur dort, wo sie etwas zeigen sollen.

> [!note] Der Übersetzungsdienst ist hier nicht gelaufen
> Das Obsidian-Plugin braucht einen API-Schlüssel für Google Translate oder DeepL. Es ist im [[7-nachschlagen/01-glossar#Vault|Vault]]
> installiert und für Deutsch → Englisch eingerichtet, der Schlüssel fehlt aber; die Aliase oben sind
> in genau der Form eingetragen, die das Plugin schreiben würde. Wer einen Schlüssel hinterlegt,
> kann sie ab dann über den Befehl *Translate note name* erzeugen lassen.

## 3 · Gleicher Pfad

Zwei Seiten, deren Pfad ohne Sprachanteil gleich ist, gehören zusammen. Auf dieser Website trifft
das auf **genau ein Paar** zu, und zwar auf das sichtbarste: die Startseiten.
`index.md` fällt in die Standardsprache, ihr Basispfad ist damit `index`; `en/index.md` liegt im
Sprachordner, ihr Basispfad ist ebenfalls `index`. Beide sind ohne ein einziges Feld im [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]]
verknüpft.

Für alle anderen Seiten greift der Weg nicht, weil die englischen Pfade englisch sind — aus
`formatierung/text/betonung` wird `formatting/text/emphasis`, nicht derselbe Pfad in einem anderen
Ordner. Das ist Absicht: Eine englische Adresse mit deutschen Wörtern darin wäre eine halbe
Übersetzung.

## Was dabei herauskommt

Jede Seite trägt nach dem Bauen ein Feld `multilanguage` mit ihrer Sprache, ihrem Basispfad, der
Strategie, über die das erkannt wurde, und der Liste ihrer Übersetzungen. Aus dieser Liste baut der
Umschalter seine Einträge, und aus ihr kommen die `hreflang`-Angaben im Kopf der Seite.
