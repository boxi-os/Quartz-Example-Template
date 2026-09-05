---
title: Fußzeile
description: Was unter jeder Seite steht — und aus welchen zwei Bausteinen es besteht.
section: Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/fusszeile
---

Ganz unten auf jeder Seite stehen zwei Dinge, die aus zwei verschiedenen Plugins kommen und wie
eines aussehen sollen.

## Von Haus aus

Das Plugin *Footer* schreibt eine Zeile „Erstellt mit Quartz" samt Jahreszahl und darunter die
Links, die in seinen Optionen stehen — hier zwei: Quartz selbst und das
[[gestaltung/layout-box/index|Layout-Box-Plugin]]. Gestaltet ist daran nichts; die Links erben, was
der Fließtext ihnen vorgibt.

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
Footer-Plugin, sondern ist eine der fünf Instanzen des Layout-Box-Plugins, gesetzt auf
`position: footer`. Sie steht dort als Beispiel für die drei Platzhalter `{{siteTitle}}`,
`{{locale}}` und `{{slug}}`; siehe [[gestaltung/layout-box/die-fuenf-instanzen|Die fünf Instanzen]].

Dass beide zusammen wie ein Block wirken, ist der Grund für die getrennte Behandlung: Das
Footer-Plugin bringt seinen eigenen Abstand mit, die Layout-Box ihren — und ohne Zutun stünden
zwischen den zwei Zeilen zwei verschiedene Lücken.

> [!note] Kommentare wären der dritte Teil
> Das Plugin *Comments* (giscus) ist in dieser Vorlage ausgeschaltet — es braucht ein
> GitHub-Repository, das eine importierende Website nicht hat. Die Gestaltung dafür reist trotzdem
> mit (`site-comments.scss`), damit ein Einschalten in der App nicht einen ungestalteten Rahmen
> unter jede Seite setzt.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 10 Variablen liest `site-footer.scss` und `site-comments.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--gray` | `#5F5D57` · dunkel `#A1A3A8` | 21 weitere Komponenten |
| `--secondary` | `#2A4E6C` · dunkel `#8CB8DA` | 21 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DEDCD5` | 16 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 14 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-xl` | `2.5rem` | 4 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 21 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
