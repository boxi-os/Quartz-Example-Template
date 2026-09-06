---
title: 1.3 Von der Notiz zur Website
description: Der Weg einer Änderung — schreiben, ansehen, bauen, veröffentlichen — und was dabei wo passiert.
section: Einstieg
tags:
  - einstieg
translationKey: einstieg/von-der-notiz-zur-website
---

Eine Änderung an dieser Website beginnt in Obsidian und endet auf einem Webspace. Dazwischen
liegen vier Schritte, und jeder hat einen Ort.

## 1 · Schreiben — in Obsidian

Man öffnet den Vault in Obsidian und schreibt. Eine neue Datei ist eine neue Seite; ein Ordner ein
Ast im Explorer; ein `[[Wikilink]]` ein Verweis, den der Graph und die Rückverweise sehen.
Kopfzeilen zwischen zwei `---` ganz oben in der Datei — das **Frontmatter** — geben der Seite
Titel, Beschreibung, Datum und Tags; was man damit alles steuern kann, steht in
[[4-seiten-steuern/index|4 Eine Seite steuern]].

Nichts davon braucht die Website schon. Man kann tagelang schreiben, ohne zu bauen.

## 2 · Ansehen — die Vorschau in QuartzControl

Unter *Vorschau & Build* startet die App einen **Dev-Server**: Quartz baut die Website einmal und
danach bei jeder gespeicherten Änderung neu, und ein Browserfenster zeigt sie unter einer Adresse
wie `localhost:8080`. Das ist der eigene Rechner; niemand sonst sieht diese Seite. Wer in Obsidian
speichert, sieht die Seite Sekunden später im Browser.

## 3 · Bauen — der Build

Derselbe Bereich kann die Website auch **bauen**, ohne sie zu zeigen: Quartz liest alle Notizen,
wendet die Plugins an — Links auflösen, Inhaltsverzeichnis erzeugen, Suche indexieren, Seiten für
Ordner und Tags anlegen — und schreibt fertige HTML-Dateien in den Ausgabeordner `public/`. Ein
Entwurf (`draft: true` im Frontmatter) wird dabei ausgelassen; siehe
[[4-seiten-steuern/02-entwurf-und-ungelistet|4.2 Entwurf und ungelistet]].

## 4 · Veröffentlichen

Unter *Veröffentlichen* schickt die App den Ausgabeordner an ein Ziel: einen Ordner, einen Server
per rsync, ein git-Repository etwa für GitHub Pages, oder sie stößt einen Webhook an. Die
Zugangsdaten dafür verwahrt die App verschlüsselt. Von diesem Moment an ist die Seite öffentlich.

## Wo der Inhalt liegt — und warum als Symlink

Ein Quartz-Projekt erwartet seine Notizen im Ordner `content/`. Hier ist dieser Ordner kein
Ordner, sondern ein **Symlink**: eine Verknüpfung, die auf den Obsidian-Vault zeigt. Quartz sieht
durch den Link den Vault, als läge er im Projekt. Der Vorteil: Es gibt nur eine Kopie der Notizen.
Man schreibt in Obsidian, und das Projekt hat es sofort.

QuartzControl legt diesen Link an — unter *Konfiguration → Content-Ordner*, wenn man den Inhalt
mit einem bestehenden Ordner *verknüpft* statt ihn zu *kopieren*. Beides lässt sich später ändern.

> [!warning] Was ein Symlink kostet
> Zwei Dinge folgen dem Link nicht. **Snapshots** — die Sicherungen, die QuartzControl vor jedem
> größeren Eingriff anlegt — lassen den Inhalt aus, sobald `content/` ein Link ist; der Vault muss
> selbst gesichert sein, hier über sein eigenes git. Und das Plugin, das das Datum einer Seite aus
> git liest, verrechnet sich am Link und fällt auf das Dateisystem zurück — siehe
> [[4-seiten-steuern/01-titel-beschreibung-datum|4.1 Titel, Beschreibung, Datum]].

## Die Vorlage in ein eigenes Projekt holen

Wer nicht diese Website, sondern eine eigene mit dieser Gestaltung will, geht den Weg andersherum:
ein neues Projekt in QuartzControl anlegen, den eigenen Vault verknüpfen, dann unter *Vorlagen*
die Vorlage importieren. Die App zeigt vorher, welche Bausteine das Paket enthält und was im
Projekt dadurch ersetzt wird, und legt einen Snapshot an. Was mitkommt und was nicht:
[[6-anpassen/08-das-vorlagenpaket|6.8 Das Vorlagenpaket]].
