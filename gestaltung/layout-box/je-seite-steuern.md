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

## Warum jede Instanz einen eigenen Schlüssel hat

Ohne `frontmatterKey` würde ein `layoutBox: false` **alle fünf** Boxen gleichzeitig ausschalten. Die
Vorlage vergibt deshalb je Instanz einen eigenen Namen — das ist auch die im Plugin dokumentierte
Vorgehensweise für Mehrfachverwendung.
