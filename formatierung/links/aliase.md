---
title: Aliase
description: Eine Seite unter mehreren Namen erreichbar machen.
section: Formatierung
tags:
  - formatierung
  - links
aliases:
  - Zweitname für Aliase
---

Im Frontmatter:

```md
---
aliases:
  - Zweitname
  - alter/pfad
---
```

Diese Seite selbst hat einen Alias — sie ist auch unter *Zweitname für Aliase* erreichbar.

## Was das bewirkt

In **Obsidian**: Der Alias taucht in der Schnellsuche auf, und `[[Zweitname]]` findet die Seite.

Auf der **gebauten Website**: Das Plugin *Alias redirects* legt für jeden Alias eine kleine
Weiterleitungsseite an. Alte Links funktionieren also weiter, wenn eine Notiz umbenannt oder
verschoben wurde.

## Wann sich das lohnt

- Eine Notiz wird umbenannt, aber es gibt schon Links darauf — der alte Pfad wird zum Alias.
- Ein Begriff hat mehrere gebräuchliche Namen.
- Eine Abkürzung soll dieselbe Seite finden wie das ausgeschriebene Wort.

Ein Beispiel mit mehreren Aliassen: [[beispiele/alias|Eine Seite mit Alias]].
