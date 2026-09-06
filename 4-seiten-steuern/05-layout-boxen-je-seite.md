---
title: 4.5 Layout-Boxen je Seite
description: Eine Layout-Box auf einer einzelnen Seite ausblenden, umbenennen oder anders füllen — im Frontmatter, nicht in der Konfiguration.
section: Seiten steuern
tags:
  - seiten-steuern
  - layout-box
layoutBoxNote: false
layoutBoxCta:
  html: "<p>Diese Box zeigt auf dieser einen Seite einen anderen Text — gesetzt im Frontmatter, nicht in der Konfiguration.</p>"
translationKey: seiten-steuern/layout-boxen-je-seite
---

Eine **Layout-Box** ist ein Kasten mit eigenem Inhalt, den das [[7-nachschlagen/01-glossar#Plugin|Plugin]] *quartz-layout-box* an eine
Stelle des Seitenlayouts setzt — die Wortmarke oben, die Box „Über dieses Handbuch“ links, der
Kasten „Weiterlesen“ unter dem Text. Diese Vorlage hat fünf davon; was jede tut, steht in
[[5-gestaltung/05-layout-boxen/index|5.5 Layout-Boxen]]. Hier geht es darum, wie eine einzelne
Seite eine davon anders haben kann.

Diese Seite steuert zwei der fünf Instanzen über ihr eigenes [[7-nachschlagen/01-glossar#Frontmatter|Frontmatter]]:

```yaml
---
layoutBoxNote: false
layoutBoxCta:
  html: "<p>Ein anderer Text, nur auf dieser Seite.</p>"
---
```

**Was man sehen sollte:** Die Box „Über dieses Handbuch“ in der linken Spalte fehlt hier — auf
allen anderen Seiten ist sie da. Und der Kasten unter diesem Text zeigt einen anderen Inhalt als
sonst.

## Die drei Formen

| Im Frontmatter | Wirkung |
| --- | --- |
| `layoutBoxNote: false` | Box auf dieser Seite ausblenden |
| `layoutBoxNote: andere.md` | anderen Schnipsel aus demselben Ordner laden |
| `layoutBoxNote: {html: "…"}` | eigenen Inhalt setzen; auch `{file: "…"}` und `{hidden: true}` |

In der ausführlichen Form nimmt der Schlüssel sechs Felder: `hidden`, `file`, `html`, `title`,
`collapsible` und `collapsed`. Eine Seite darf ihre Box also auch umbenennen oder zuklappen, nicht
nur umfüllen.

## Die fünf Schlüssel dieser Vorlage

| Schlüssel | Ort | Was die Box ist |
| --- | --- | --- |
| `layoutBoxMark` | Kopfbereich | die Wortmarke, ein Bild je [[7-nachschlagen/01-glossar#Farbschema\|Farbschema]] |
| `layoutBoxNote` | linke Spalte | „Über dieses Handbuch“, aus einer Markdown-Datei, aufklappbar |
| `layoutBoxHint` | linke Spalte | ein Hinweis, nur auf schmalen Bildschirmen |
| `layoutBoxCta` | nach dem Inhalt | „Weiterlesen“, mit Platzhaltern |
| `layoutBoxColophon` | Fußzeile | die Impressumszeile |

## Warum jede Instanz einen eigenen Schlüssel hat

Ohne `frontmatterKey` in der Konfiguration würde ein `layoutBox: false` **alle fünf** Boxen
gleichzeitig ausschalten. Die Vorlage vergibt deshalb je Instanz einen eigenen Namen — das ist auch
die im Plugin dokumentierte Vorgehensweise für Mehrfachverwendung.

## Wann das Frontmatter der richtige Ort ist — und wann nicht

Was für **diese eine Seite** gilt, gehört hierher. Was für **alle Seiten einer Sprache** gilt,
gehört in die Konfiguration unter `byLang` — sonst steht dieselbe Ausnahme in hundert Dateien.
Genau das war hier einmal der Fall: Die englischen Seiten trugen ihre vier Boxen selbst, bis das
Plugin `byLang` bekam. Siehe [[5-gestaltung/05-layout-boxen/die-fuenf-instanzen|Die fünf
Instanzen]].

Wenn beides zutrifft, gewinnt das Frontmatter. Die Rangfolge ist:

1. das Frontmatter dieser Seite
2. `byLang` für die Sprache dieser Seite
3. die Grundeinstellung des Eintrags

Diese Seite ist die Probe darauf: Ihr Kasten unter dem Text zeigt in beiden Sprachen den eigenen
Text aus dem Frontmatter, trägt aber die Überschrift, die `byLang` für die jeweilige Sprache setzt.
