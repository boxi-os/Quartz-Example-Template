---
title: 4.5 Layout-Boxen je Seite
description: Dieselbe Komponente, auf dieser Seite anders eingestellt.
section: Seiten steuern
tags:
  - seiten-steuern
  - layout-box
layoutBoxNote: false
layoutBoxCta:
  html: "<p>Diese Box zeigt auf dieser einen Seite einen anderen Text — gesetzt im Frontmatter, nicht in der Konfiguration.</p>"
translationKey: seiten-steuern/layout-boxen-je-seite
---

Diese Seite steuert zwei der fünf Layout-Box-Instanzen über ihr eigenes Frontmatter:

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

Möglich ist das, weil jede Instanz einen eigenen `frontmatterKey` hat. Ohne das würde ein
`layoutBox: false` alle fünf Boxen gleichzeitig ausschalten.

## Die drei Formen

| Im Frontmatter | Wirkung |
| -------------- | ------- |
| `layoutBoxNote: false` | Box auf dieser Seite ausblenden |
| `layoutBoxNote: andere.md` | anderes Snippet aus demselben Ordner laden |
| `layoutBoxNote: {html: "…"}` | eigenen Inhalt setzen; auch `{file: "…"}` und `{hidden: true}` |

Die ausführliche Form nimmt sechs Felder: `hidden`, `file`, `html`, `title`, `collapsible` und
`collapsed`.

## Die fünf Instanzen dieser Vorlage

| Schlüssel | Ort | Form |
| --------- | --- | ---- |
| `layoutBoxMark` | Kopfbereich | Wortmarke, Bild je Farbschema |
| `layoutBoxNote` | linke Spalte | Markdown-Datei, aufklappbar |
| `layoutBoxHint` | linke Spalte | nur auf schmalen Bildschirmen |
| `layoutBoxCta` | nach dem Inhalt | Aufruf mit Platzhaltern |
| `layoutBoxColophon` | Fußzeile | Impressumszeile |

Vier davon holen ihren Inhalt aus der Konfiguration (`html:`) und reisen deshalb vollständig mit
dem Vorlagen-Paket. Die Box in der linken Spalte lädt aus einer Datei und zeigt damit den anderen
Weg — die Datei muss beim Weitergeben mitkopiert werden.

> [!note] Für eine ganze Sprache gibt es einen besseren Ort
> Das Frontmatter gilt für **eine** Seite. Was für alle Seiten einer Sprache gelten soll, steht in
> der Konfiguration unter `byLang` und braucht keine Zeile in den Notizen — siehe
> [[5-gestaltung/05-layout-boxen/die-fuenf-instanzen|Die fünf Instanzen]]. Treffen beide zu, gewinnt das
> Frontmatter: Der Kasten unter diesem Text zeigt seinen eigenen Inhalt, trägt aber die
> Überschrift der Seitensprache.
