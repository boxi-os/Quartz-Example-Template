---
title: Kommentare
description: Text, der nur im Quelltext steht.
section: Formatierung
tags:
  - formatierung
  - fussnoten
---

## Obsidian-Kommentar

```md
%% Dieser Text steht nur im Quelltext und erscheint nicht auf der Website. %%
```

%% Dieser Text steht nur im Quelltext und erscheint nicht auf der Website. %%

Zwischen diesem Absatz und dem vorigen steht ein Kommentar. Auf der Website ist davon nichts zu
sehen — in Obsidian schon, dort erscheint er grau.

## Mehrzeilig

```md
%%
Auch über
mehrere Zeilen.
%%
```

## HTML-Kommentar

```md
<!-- Auch das erscheint nicht in der Ausgabe. -->
```

<!-- Auch das erscheint nicht in der Ausgabe. -->

Der Unterschied: Ein HTML-Kommentar bleibt im ausgelieferten HTML stehen (unsichtbar, aber im
Quelltext der Seite lesbar). Ein `%%`-Kommentar wird schon beim Bauen entfernt.

> [!warning] Ein Kommentar ist keine Geheimhaltung
> Beide Formen stehen weiterhin in der Markdown-Datei. Wer das Repository lesen kann, liest sie.
> Für wirklich Vertrauliches gibt es `ignorePatterns` oder das Plugin *Encrypted pages*.
