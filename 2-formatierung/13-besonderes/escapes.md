---
title: Zeichen schützen
description: Wenn Markdown etwas als Auszeichnung liest, das Text sein soll.
section: 2 Formatierung
tags:
  - formatierung
  - besonderes
translationKey: formatierung/besonderes/escapes
cover: "[[assets/covers/cover-besonderes.svg]]"
---

Ein Backslash davor nimmt dem Zeichen seine Bedeutung:

```md
\*keine Betonung\*, \[keine Klammer\], \# keine Überschrift, \| kein Spaltentrenner
```

\*keine Betonung\*, \[keine Klammer\], \# keine Überschrift, \| kein Spaltentrenner

## Was geschützt werden muss

| Zeichen | Sonst |
| --- | --- |
| `*` `_` | Betonung |
| `[` `]` | Link |
| `#` am Zeilenanfang | Überschrift |
| `-` `+` am Zeilenanfang | Listenpunkt |
| `` ` `` | Code |
| `\|` in Tabellen | Spaltentrenner |
| `$` | Formel |
| `%%` | Kommentar |

## Der andere Weg

Innerhalb von Inline-Code braucht nichts geschützt zu werden:

```md
`*hier gilt nichts davon*`
```

`*hier gilt nichts davon*`

Deshalb stehen auf diesen Seiten alle Beispiele in Codeblöcken — sonst würde jedes von ihnen sich
selbst rendern statt sich zu zeigen.
