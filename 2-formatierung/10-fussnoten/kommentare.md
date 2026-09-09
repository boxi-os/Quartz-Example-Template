---
title: Kommentare
description: Text, der nur im Quelltext steht.
section: 2 – Formatierung
tags:
  - formatierung
  - fussnoten
translationKey: formatierung/fussnoten/kommentare
cover: "[[assets/covers/cover-fussnoten.svg]]"
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

Gemessen an der gebauten Seite: **beide Formen sind weg.** Ein HTML-Kommentar bleibt in vielen
Markdown-Werkzeugen im ausgelieferten [[7-nachschlagen/01-glossar#HTML|HTML]] stehen und ist dort im Quelltext lesbar — hier nicht,
Quartz entfernt ihn wie den `%%`-Kommentar. Verlassen sollte man sich auf keines von beidem: Was
nicht in der Ausgabe stehen darf, gehört nicht in die Datei.

> [!warning] Ein Kommentar ist keine Geheimhaltung
> Beide Formen stehen weiterhin in der Markdown-Datei. Wer das [[7-nachschlagen/01-glossar#Repository|Repository]] lesen kann, liest sie.
> Für wirklich Vertrauliches gibt es `ignorePatterns` oder das [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Encrypted pages*.
