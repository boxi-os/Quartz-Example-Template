---
title: HTML im Markdown
description: Was durchgelassen wird und wo die Grenze liegt.
section: Formatierung
tags:
  - formatierung
  - besonderes
translationKey: formatierung/besonderes/html
cover: "[[assets/covers/cover-besonderes.svg]]"
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

Für Aufklappbares ist der [[2-formatierung/05-callouts/faltbar|faltbare Callout]] die bessere Wahl: Er
ist gestaltet, hat einen Fokusring und funktioniert in Obsidian genauso. HTML lohnt sich für
Dinge, die Markdown gar nicht kennt — etwa eine Tabelle mit verbundenen Zellen.

## Was Markdown hier nicht kann

**Definitionslisten** (`Begriff` / `: Erklärung`) kennt weder Obsidian noch Quartz — gemessen: Die
Doppelpunktzeile bleibt als Text stehen. Wer sie braucht, schreibt HTML:

```md
<dl>
  <dt>Begriff</dt>
  <dd>Die Erklärung dazu</dd>
</dl>
```

<dl>
  <dt>Begriff</dt>
  <dd>Die Erklärung dazu</dd>
</dl>

Für die meisten Fälle tut es eine Tabelle mit zwei Spalten — und die ist auf einem Telefon besser
zu lesen.

> [!warning] HTML wird nicht bereinigt
> Was hier steht, landet unverändert auf der Seite. Bei Inhalten aus fremder Quelle ist das ein
> Risiko.
