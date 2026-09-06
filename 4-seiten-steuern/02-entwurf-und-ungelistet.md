---
title: 4.2 Entwurf und ungelistet
description: Zwei Wege, eine Seite zurückzuhalten — einer baut sie gar nicht, der andere versteckt sie nur.
section: 4 Eine Seite steuern
tags:
  - seiten-steuern
translationKey: seiten-steuern/entwurf-und-ungelistet
---

## `draft: true` — die Seite wird nicht gebaut

Ein Entwurf bleibt im [[7-nachschlagen/01-glossar#Vault|Vault]] und in Obsidian, aber Quartz überspringt ihn beim Bauen. Es gibt keine
Datei dafür in der Ausgabe, keinen Eintrag im [[7-nachschlagen/01-glossar#Explorer|Explorer]], kein Suchergebnis; ein Link darauf führt
ins Leere. Das ist der Weg für alles, was noch nicht fertig ist.

Dafür sorgt das [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Remove draft*. Ist es abgeschaltet, werden Entwürfe wie alle anderen Seiten
gebaut.

## `unlisted: true` — gebaut, aber unsichtbar

Eine ungelistete Seite existiert auf der Website und ist über ihre Adresse erreichbar, taucht aber
in keiner Ordnerübersicht, keiner Tag-Seite und keinem Suchergebnis auf. Wer die Adresse kennt,
kann sie lesen; wer sie nicht kennt, findet sie nicht. Das ist der Weg für eine Seite, die man nur
per Link weitergibt.

## Die zwei Testseiten

In diesem Kapitel liegen zwei Seiten, die genau das vorführen:

- [[4-seiten-steuern/entwurf|Ein Entwurf]] — dieser Link führt ins Leere, weil die Seite nicht
  gebaut wird. Erscheint sie doch, ist das Plugin aus oder das Feld falsch geschrieben.
- [[4-seiten-steuern/unlisted|Eine ungelistete Seite]] — dieser Link funktioniert, aber in keiner
  Liste dieser Website ist die Seite zu finden.

> [!note] Ungelistet heißt nicht geheim
> Die Seite liegt auf dem Webspace wie jede andere. Eine Suchmaschine kann sie finden, sobald
> irgendwo ein Link darauf steht. Was wirklich nicht öffentlich sein soll, bleibt ein Entwurf.
