---
title: Je Seite steuern
description: Eine Box auf einer einzelnen Seite ausblenden oder anders füllen.
section: Gestaltung
tags:
  - gestaltung
  - layout-box
layoutBoxNote: false
layoutBoxCta:
  html: "<p>Diese Box zeigt auf dieser einen Seite einen anderen Text — gesetzt im Frontmatter, nicht in der Konfiguration.</p>"
translationKey: gestaltung/layout-box/je-seite-steuern
---

Diese Seite steuert zwei der fünf Instanzen über ihr eigenes Frontmatter:

```yaml
---
layoutBoxNote: false
layoutBoxCta:
  html: "<p>Ein anderer Text, nur auf dieser Seite.</p>"
---
```

**Was man sehen sollte:** Die Box „Über dieses Handbuch" in der linken Spalte fehlt hier — auf allen
anderen Seiten ist sie da. Und der Kasten unter diesem Text zeigt einen anderen Inhalt als sonst.

## Die drei Formen

| Im Frontmatter | Wirkung |
| --- | --- |
| `layoutBoxNote: false` | Box auf dieser Seite ausblenden |
| `layoutBoxNote: andere.md` | anderen Schnipsel aus demselben Ordner laden |
| `layoutBoxNote: {html: "…"}` | eigenen Inhalt setzen; auch `{file: "…"}` und `{hidden: true}` |

In der ausführlichen Form nimmt der Schlüssel sechs Felder: `hidden`, `file`, `html`, `title`,
`collapsible` und `collapsed`. Eine Seite darf ihre Box also auch umbenennen oder zuklappen,
nicht nur umfüllen.

## Warum jede Instanz einen eigenen Schlüssel hat

Ohne `frontmatterKey` würde ein `layoutBox: false` **alle fünf** Boxen gleichzeitig ausschalten. Die
Vorlage vergibt deshalb je Instanz einen eigenen Namen — das ist auch die im Plugin dokumentierte
Vorgehensweise für Mehrfachverwendung.

## Wann das Frontmatter der richtige Ort ist — und wann nicht

Was für **diese eine Seite** gilt, gehört hierher. Was für **alle Seiten einer Sprache** gilt,
gehört in die Konfiguration unter `byLang` — sonst steht dieselbe Ausnahme in hundert Dateien.
Genau das war hier einmal der Fall: Die englischen Seiten trugen ihre vier Boxen selbst, bis das
Plugin `byLang` bekam. Siehe
[[gestaltung/layout-box/die-fuenf-instanzen|Die fünf Instanzen]].

Wenn beides zutrifft, gewinnt das Frontmatter. Die Rangfolge ist:

1. das Frontmatter dieser Seite
2. `byLang` für die Sprache dieser Seite
3. die Grundeinstellung des Eintrags

Diese Seite ist die Probe darauf: Ihr Aufruf-Kasten zeigt in beiden Sprachen den eigenen Text aus
dem Frontmatter, trägt aber die Überschrift, die `byLang` für die jeweilige Sprache setzt.
