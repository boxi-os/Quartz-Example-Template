---
title: 4 Eine Seite steuern
description: Was das Frontmatter einer Seite bewirkt — Titel, Datum, Entwurf, Alias, eigene Felder, Layout-Boxen, Titelbild, Übersetzung.
section: Seiten steuern
tags:
  - seiten-steuern
translationKey: seiten-steuern/index
---

Ganz oben in einer Notiz, zwischen zwei Zeilen aus drei Bindestrichen, stehen Angaben *über* die
Seite: ihr Titel, eine Beschreibung, Tags, ein Datum. Diesen Block nennt man **Frontmatter**;
Obsidian zeigt ihn als „Eigenschaften“ an. Quartz liest ihn und richtet sich danach — und genau das
steuert man hier: nicht, wie etwas aussieht, sondern was mit der Seite geschieht.

```yaml
---
title: Eine Seite
description: Ein Satz für Suche, Vorschau und Listen.
tags:
  - beispiel
date: 2026-09-01
draft: false
---
```

Wie man Frontmatter *schreibt* — die Datentypen, die Anzeige — steht in
[[2-formatierung/11-eigenschaften/index|2.11 Eigenschaften]]. Hier steht, was jedes Feld *tut*.

## Die Felder im Überblick

| Feld | Wirkung | Seite |
| --- | --- | --- |
| `title`, `description` | Titel und Vorschautext der Seite | [[4-seiten-steuern/01-titel-beschreibung-datum\|4.1]] |
| `date`, `lastmod` | Datum unter dem Titel, Reihenfolge in „Zuletzt geändert“ | [[4-seiten-steuern/01-titel-beschreibung-datum\|4.1]] |
| `draft: true` | Die Seite wird nicht gebaut | [[4-seiten-steuern/02-entwurf-und-ungelistet\|4.2]] |
| `unlisted: true` | Die Seite wird gebaut, erscheint aber in keiner Liste | [[4-seiten-steuern/02-entwurf-und-ungelistet\|4.2]] |
| `aliases` | weitere Pfade, unter denen die Seite erreichbar ist | [[4-seiten-steuern/03-aliase\|4.3]] |
| `tags` | Tag-Liste unter dem Titel, Tag-Seiten, Filter einer [[7-nachschlagen/01-glossar#Base\|Base]] | [[5-gestaltung/02-ueber-dem-inhalt/tags\|Tags]] |
| eigene Felder wie `section` | erscheinen in der Eigenschaften-Tabelle | [[4-seiten-steuern/04-eigene-felder\|4.4]] |
| `layoutBoxNote`, `layoutBoxCta`, … | eine [[7-nachschlagen/01-glossar#Layout-Box\|Layout-Box]] auf dieser Seite ausblenden oder umfüllen | [[4-seiten-steuern/05-layout-boxen-je-seite\|4.5]] |
| `cover` | ein Titelbild für Galerie und Kacheln | [[4-seiten-steuern/06-titelbild\|4.6]] |
| `translationKey`, `lang` | die Seite mit ihrer Übersetzung verbinden | [[4-seiten-steuern/07-uebersetzung\|4.7]] |

> [!tip] Eigene Felder sind erlaubt
> Ein Feld, das Quartz nicht kennt, stört nicht. Diese Vorlage nutzt zum Beispiel `section` für
> die Anzeige in der Eigenschaften-Tabelle; und eine Layout-Box kann jedes Feld als Platzhalter
> `{{frontmatter.name}}` einsetzen.
