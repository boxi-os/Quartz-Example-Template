---
title: Sonstiges
description: HTML, Escapes, Emoji, Pfeile und die Kleinigkeiten dazwischen.
section: Formatierung
tags:
  - referenz
  - formatierung
---

## HTML

Quartz lässt HTML im Markdown durch.

```md
<div style="text-align: center">Ein zentrierter Absatz.</div>

<details>
<summary>Ein aufklappbarer Abschnitt</summary>

Der Inhalt erscheint beim Aufklappen.

</details>
```

<div style="text-align: center">Ein zentrierter Absatz.</div>

<details>
<summary>Ein aufklappbarer Abschnitt</summary>

Der Inhalt erscheint beim Aufklappen.

</details>

## Zeichen schützen

```md
\*keine Betonung\*, \[keine Klammer\], \# keine Überschrift
```

\*keine Betonung\*, \[keine Klammer\], \# keine Überschrift

## Pfeile

Das Obsidian-Plugin wandelt Pfeilfolgen um:

```md
--> und <-- und <--> und ==>
```

--> und <-- und <--> und ==>

## Emoji

```md
Direkt eingefügt: 📐 ✓ ⚠️
```

Direkt eingefügt: 📐 ✓ ⚠️

## Zeilenumbruch erzwingen

```md
Erste Zeile<br>Zweite Zeile
```

Erste Zeile<br>Zweite Zeile

## Was diese Vorlage nicht zeigt

Drei Dinge, die Quartz kann, deren Plugin hier aber ausgeschaltet ist — sie stehen als Hinweis da,
nicht als kaputtes Beispiel:

- **Literaturverweise** (`[@quelle]`) brauchen das Plugin *Citations* und eine `.bib`-Datei.
- **Verschlüsselte Seiten** brauchen *Encrypted pages* und ein Passwort im Frontmatter.
- **Excalidraw-Zeichnungen** brauchen das entsprechende Plugin und eine `.excalidraw.md`-Datei.

Alle drei lassen sich in der App unter *Plugins* einschalten; die Gestaltung dieser Vorlage steht
ihnen nicht im Weg.
