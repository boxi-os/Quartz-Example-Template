---
title: Externe Links
description: Verweise nach draußen — und woran man sie erkennt.
section: Formatierung
tags:
  - formatierung
  - links
translationKey: formatierung/links/extern
cover: "[[assets/covers/cover-links.svg]]"
---

```md
[Quartz](https://quartz.jzhao.xyz/)
<https://quartz.jzhao.xyz/>
```

[Quartz](https://quartz.jzhao.xyz/)
<https://quartz.jzhao.xyz/>

## In dieser Vorlage

**Von Haus aus** sehen externe Links aus wie interne.

**In dieser Vorlage** bekommen sie einen kleinen Pfeil hinter dem Text: ↗. Das ist kein Schmuck.
Wer die Seite liest, soll vorher wissen, dass ein Klick sie verlässt — und die Farbe allein sagt
das nicht.

Der Pfeil steht als `::after` im [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]], nicht im Text. Er landet damit nicht in einer Kopie
und nicht in der Vorlesereihenfolge.

## Titel

```md
[Quartz](https://quartz.jzhao.xyz/ "Die Dokumentation")
```

[Quartz](https://quartz.jzhao.xyz/ "Die Dokumentation")

Der Text in Anführungszeichen erscheint beim Überfahren als Tooltip. Verlass dich nicht darauf:
Auf einem Telefon gibt es ihn nicht.
