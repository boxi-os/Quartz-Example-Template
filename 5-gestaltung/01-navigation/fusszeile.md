---
title: Fußzeile
description: Was unter jeder Seite steht — und aus welchen zwei Bausteinen es besteht.
section: 5 – Die Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/fusszeile
---

Ganz unten auf jeder Seite stehen zwei Dinge, die aus zwei verschiedenen [[7-nachschlagen/01-glossar#Plugin|Plugins]] kommen und wie
eines aussehen sollen.

## Von Haus aus

Das Plugin *Footer* schreibt eine Zeile „Erstellt mit Quartz" samt Jahreszahl und darunter die
Links, die in seinen Optionen stehen — hier vier: Quartz selbst, QuartzControl und die zwei Plugins,
die diese Vorlage benutzt ([[5-gestaltung/05-layout-boxen/index|Layout-Box]] und Mehrsprachigkeit).
Gestaltet ist daran nichts; die Links erben, was der Fließtext ihnen vorgibt.

## In dieser Vorlage

- Eine **Haarlinie** trennt die Fußzeile vom Text, mit derselben Farbe und derselben Breite wie
  jede andere Trennlinie der Seite.
- Alles steht **gedämpft und kleiner**: Die Fußzeile ist Apparat, nicht Inhalt.
- Die Links sind **nicht unterstrichen**, solange man sie nicht überfährt — anders als im
  Fließtext, wo die Unterstreichung Pflicht ist. Hier stehen sie in einer Reihe für sich; dass es
  Links sind, sagt die Reihe.
- Jeder Link hat **Innenabstand nach oben und unten**. Sie sind klein und oft das Letzte, was
  jemand auf einem Telefon zu treffen versucht.
- Die Linkreihe **bricht um** statt überzulaufen.

## Die zweite Hälfte ist eine Layout-Box

Die Zeile darunter — Websitename, Sprache und der Pfad der aktuellen Seite — kommt nicht vom
Footer-Plugin, sondern ist eine der sieben Instanzen des Layout-Box-Plugins, gesetzt auf
`position: footer`. Sie steht dort als Beispiel für die drei Platzhalter `{{siteTitle}}`,
`{{locale}}` und `{{slug}}`; siehe [[5-gestaltung/05-layout-boxen/die-instanzen|Die Instanzen]].

Dass beide zusammen wie ein Block wirken, ist der Grund für die getrennte Behandlung: Das
Footer-Plugin bringt seinen eigenen Abstand mit, die [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]] ihren — und ohne Zutun stünden
zwischen den zwei Zeilen zwei verschiedene Lücken.

> [!note] Die Fußzeile liegt über der rechten Spalte
> Ein `position: sticky`-Rasterelement bleibt in Chromium **nicht** in seinem Bereich: Die rechte
> Spalte lief auf langen Seiten in die Fußzeile hinein. Nachgewiesen, dass das Raster daran nichts
> ändert — ein ausdrückliches `grid-row` verschob die Überlappung um einen Pixel. Gelöst ist es
> über die Reihenfolge beim Zeichnen: Die Fußzeile bekommt eine eigene Ebene und ihren eigenen
> Grund und deckt damit ab, was von oben hereinragt.

> [!note] Kommentare wären der dritte Teil
> Das Plugin *Comments* (giscus) ist in dieser Vorlage ausgeschaltet — es braucht ein
> GitHub-Repository, das eine importierende Website nicht hat. Die Gestaltung dafür reist trotzdem
> mit — im unteren Teil von `site-footer.scss` —, damit ein Einschalten in der App nicht einen
> ungestalteten Rahmen
> unter jede Seite setzt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 11 Variablen liest `site-footer.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 15 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 5 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-underline-offset` | `0.18em` | 6 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
