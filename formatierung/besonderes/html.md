---
title: HTML im Markdown
description: Was durchgelassen wird und wo die Grenze liegt.
section: Formatierung
tags:
  - formatierung
  - besonderes
---

```md
<div style="text-align: center">Ein zentrierter Absatz.</div>
```

<div style="text-align: center">Ein zentrierter Absatz.</div>

## Aufklappbare Abschnitte

```md
<details>
<summary>Ein aufklappbarer Abschnitt</summary>

Der Inhalt erscheint beim Aufklappen. Zwischen `<summary>` und dem Text muss eine Leerzeile stehen,
sonst wird das Markdown darin nicht verarbeitet.

</details>
```

<details>
<summary>Ein aufklappbarer Abschnitt</summary>

Der Inhalt erscheint beim Aufklappen. Zwischen `<summary>` und dem Text muss eine Leerzeile stehen,
sonst wird das Markdown darin nicht verarbeitet.

</details>

## Wann HTML, wann Callout

Für Aufklappbares ist der [[formatierung/callouts/faltbar|faltbare Callout]] die bessere Wahl: Er
ist gestaltet, hat einen Fokusring und funktioniert in Obsidian genauso. HTML lohnt sich für
Dinge, die Markdown gar nicht kennt — etwa eine Tabelle mit verbundenen Zellen.

> [!warning] HTML wird nicht bereinigt
> Was hier steht, landet unverändert auf der Seite. Bei Inhalten aus fremder Quelle ist das ein
> Risiko.
