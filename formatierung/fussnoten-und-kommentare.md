---
title: Fußnoten und Kommentare
description: Fußnoten, Inline-Fußnoten und was Obsidian-Kommentare in Quartz tun.
section: Formatierung
tags:
  - referenz
  - formatierung
---

## Fußnote

```md
Ein Satz mit einer Fußnote.[^1]

[^1]: Der Text der Fußnote, ganz unten auf der Seite.
```

Ein Satz mit einer Fußnote.[^1]

[^1]: Der Text der Fußnote, ganz unten auf der Seite.

## Mehrere Fußnoten

```md
Erster Verweis[^zwei] und zweiter Verweis[^drei].

[^zwei]: Fußnoten dürfen benannt sein statt nummeriert.
[^drei]: Die Nummerierung in der Ausgabe entsteht aus der Reihenfolge im Text.
```

Erster Verweis[^zwei] und zweiter Verweis[^drei].

[^zwei]: Fußnoten dürfen benannt sein statt nummeriert.
[^drei]: Die Nummerierung in der Ausgabe entsteht aus der Reihenfolge im Text.

## Kommentare

```md
%% Dieser Text steht nur im Quelltext und erscheint nicht auf der Website. %%
```

%% Dieser Text steht nur im Quelltext und erscheint nicht auf der Website. %%

Zwischen diesem Absatz und dem vorigen steht ein Kommentar. Auf der Website ist davon nichts zu
sehen — das ist der Zweck.

> [!warning] Ein Kommentar ist keine Geheimhaltung
> Der Text wird beim Bauen entfernt, steht aber weiterhin in der Markdown-Datei. Wer das Repository
> lesen kann, liest ihn.

Ein HTML-Kommentar wirkt genauso:

```md
<!-- Auch das erscheint nicht in der Ausgabe. -->
```

<!-- Auch das erscheint nicht in der Ausgabe. -->
