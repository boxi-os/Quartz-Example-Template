---
title: 2 Formatierung
description: Jedes Element, das Obsidian schreibt und Quartz rendert — Quelltext und Ergebnis nebeneinander, 62 kurze Seiten in dreizehn Abschnitten.
section: Formatierung
tags:
  - formatierung
translationKey: formatierung/index
cover: "[[assets/covers/cover-index.svg]]"
---

Notizen in Obsidian sind **Markdown**: Text mit ein paar Zeichen darin, die Bedeutung tragen — zwei
Sternchen für fett, eine Raute für eine Überschrift, eckige Klammern für einen Link. Quartz liest
diese Zeichen und macht daraus die Seite. Dieses Kapitel zeigt jedes Element, das man so schreiben
kann, auf einer eigenen kurzen Seite: zuerst der Quelltext in einem Codeblock, direkt darunter, was
die Website daraus macht.

> [!tip] Zum Abschreiben
> Der Kasten oben auf jeder Seite ist genau das, was man in Obsidian tippt. Wer ein Element
> nachbauen will, kopiert ihn — und vergleicht sein Ergebnis mit dem darunter.

## Die dreizehn Abschnitte

| Abschnitt | Was darin steht |
| --- | --- |
| [[2-formatierung/01-text/index\|2.1 Text]] | fett, kursiv, durchgestrichen, hervorgehoben, Sonderzeichen, Zeilenumbrüche |
| [[2-formatierung/02-struktur/index\|2.2 Struktur]] | Überschriften, Absätze, Trennlinien |
| [[2-formatierung/03-listen/index\|2.3 Listen]] | ungeordnet, geordnet, Aufgaben, Verschachtelung |
| [[2-formatierung/04-links/index\|2.4 Links]] | [[7-nachschlagen/01-glossar#Wikilink\|Wikilinks]], Sprungziele, externe Links, [[7-nachschlagen/01-glossar#Alias\|Aliase]], Einbettungen |
| [[2-formatierung/05-callouts/index\|2.5 Callouts]] | alle dreizehn Typen, faltbar, verschachtelt |
| [[2-formatierung/06-code/index\|2.6 Code]] | inline, Blöcke, Sprachen, Zeilenhervorhebung |
| [[2-formatierung/07-tabellen/index\|2.7 Tabellen]] | Grundform, Ausrichtung, Inhalte, breite Tabellen |
| [[2-formatierung/08-mathematik/index\|2.8 Mathematik]] | Formeln inline und als Block |
| [[2-formatierung/09-diagramme/index\|2.9 Diagramme]] | [[7-nachschlagen/01-glossar#Mermaid\|Mermaid]]: vierzehn Diagrammarten auf sechs Seiten |
| [[2-formatierung/10-fussnoten/index\|2.10 Fußnoten]] | Fußnoten, Varianten, Kommentare |
| [[2-formatierung/11-eigenschaften/index\|2.11 Eigenschaften]] | [[7-nachschlagen/01-glossar#Frontmatter\|Frontmatter]], Datentypen, Anzeige |
| [[2-formatierung/12-medien/index\|2.12 Medien]] | Bilder, Größen, Video, Audio, Dokumente, Einbettungen |
| [[2-formatierung/13-besonderes/index\|2.13 Besonderes]] | [[7-nachschlagen/01-glossar#HTML\|HTML]], Escapes, Pfeile, Emoji |

Was **keine** Markdown-Seite ist — [[7-nachschlagen/01-glossar#Base|Bases]], [[7-nachschlagen/01-glossar#Canvas|Canvas]] und [[7-nachschlagen/01-glossar#Excalidraw|Excalidraw]] — steht in
[[3-obsidian-formate/index|3 Obsidian-Formate]]. Was das Frontmatter einer Seite *bewirkt* —
Entwurf, Datum, Alias, Titelbild —, steht in [[4-seiten-steuern/index|4 Eine Seite steuern]].

## Was Obsidian kann und Quartz nicht

Obsidian und Quartz sprechen fast dieselbe Sprache, aber nicht ganz. Diese Abweichungen sind an der
gebauten Website gemessen; die verlinkte Seite zeigt jeweils, was stattdessen geht.

| In Obsidian | Auf der Website | Wo es steht |
| --- | --- | --- |
| Aufgaben mit Zwischenzuständen (`[/]`, `[-]`, `[?]`) | nur offen und erledigt; jedes andere Zeichen wird ein leeres Kästchen | [[2-formatierung/03-listen/aufgaben\|Aufgaben]] |
| Inline-Fußnote `^[Text]` | bleibt als Rohtext stehen | [[2-formatierung/10-fussnoten/varianten\|Varianten]] |
| Pfeile wie `-->` werden zu → | bleiben Rohtext; mit *GitHub flavored markdown* wird `—>` daraus | [[2-formatierung/13-besonderes/pfeile-und-emoji\|Pfeile und Emoji]] |
| Ein Tag im Fließtext | der Link daran führt aus der Website heraus — ein Fehler in Quartz | [[2-formatierung/13-besonderes/pfeile-und-emoji\|Pfeile und Emoji]] |
| Bild mit Größe *und* Alternativtext | nur eines von beiden | [[2-formatierung/12-medien/bilder\|Bilder]] |
| Eingebettetes PDF ab Seite 2 | beginnt immer auf Seite 1 | [[2-formatierung/12-medien/dokumente\|Dokumente]] |
| Definitionslisten | gibt es in beiden nicht, HTML hilft aus | [[2-formatierung/13-besonderes/html\|HTML]] |

Dazu kommt, was auf dieser Website absichtlich anders aussieht als in Quartz von Haus aus — die
Callout-Farben etwa. Das steht nicht hier, sondern in [[5-gestaltung/index|5 Die Gestaltung]] bei
der jeweiligen Komponente.
