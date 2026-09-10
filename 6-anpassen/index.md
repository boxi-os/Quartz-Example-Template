---
title: 6 – Anpassen
description: Wo eine Farbe, eine Schrift, ein Abstand, das Seitenraster oder die Sprachen herkommen — und wie man sie ändert, meist ohne Code.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/index
---

Diese Vorlage ist zum Ändern gebaut. Fast alles, was man ändern will, ist eine **Variable**: ein
benannter Wert wie `--tpl-space-md: 1rem`, den QuartzControl unter *Stile → Variablen* anzeigt und
den man dort überschreibt, getrennt für hell und dunkel. Kein Code, keine Datei. Erst wenn nicht
der *Wert*, sondern die *Form* anders werden soll, braucht es ein [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]] — und auch dafür gibt
es einen Weg, der die Vorlage selbst nicht anfasst.

## Was will ich ändern?

| Ich will … | Dann |
| --- | --- |
| … eine Farbe ändern — den Akzent, den Grund, die [[7-nachschlagen/01-glossar#Callout\|Callouts]] | [[6-anpassen/02-farben-und-kontrast\|6.2 – Farben und Kontrast]] |
| … eine andere Schrift | [[6-anpassen/03-schriften\|6.3 – Schriften]] |
| … mehr oder weniger Abstand, größere Ecken, andere Textgrößen | [[6-anpassen/04-variablen\|6.4 – Variablen]] |
| … den Text breiter, die Seitenleisten schmaler, andere Umbruchbreiten | [[6-anpassen/05-seitenraster\|6.5 – Seitenraster]] |
| … wissen, was die Vorlage für Tastatur, Screenreader und Druck tut | [[6-anpassen/06-barrierefreiheit\|6.6 – Barrierefreiheit]] |
| … eine zweite Sprache, oder nur eine | [[6-anpassen/07-zwei-sprachen/index\|6.7 – Zwei Sprachen]] |
| … die Vorlage in ein anderes Projekt bringen oder weitergeben | [[6-anpassen/08-das-vorlagenpaket\|6.8 – Das Vorlagenpaket]] |
| … eine Komponente anders *geformt*, nicht nur anders gefärbt | [[6-anpassen/01-etwas-aendern\|6.1 – Etwas ändern]], Weg 2 und 3 |

## Die Seiten

1. [[6-anpassen/01-etwas-aendern|6.1 – Etwas ändern]] — die drei Ebenen, von der billigsten zur
   teuersten, und wo eine eigene Regel hingehört, damit sie gewinnt.
2. [[6-anpassen/02-farben-und-kontrast|6.2 – Farben und Kontrast]] — die neun Farbrollen, zwei davon
   verkehrt herum benannt, und die 93 gemessenen Paare.
3. [[6-anpassen/03-schriften|6.3 – Schriften]] — drei Familien, selbst gehostet, und warum ihre
   `@font-face`-Regeln ersetzt werden.
4. [[6-anpassen/04-variablen|6.4 – Variablen]] — die 50 Werte, aus denen die Gestaltung besteht, und
   was doch als Zahl in einer Datei steht.
5. [[6-anpassen/05-seitenraster|6.5 – Seitenraster]] — vier [[7-nachschlagen/01-glossar#Frame|Frames]], zwölf Spalten, drei Breiten.
6. [[6-anpassen/06-barrierefreiheit|6.6 – Barrierefreiheit]] — [[7-nachschlagen/01-glossar#Kontrast|Kontrast]], Tastatur, Zielgrößen,
   Systemeinstellungen, Druck.
7. [[6-anpassen/07-zwei-sprachen/index|6.7 – Zwei Sprachen]] — wie dieselbe Website in zwei Sprachen
   entsteht und wo das aufhört.
8. [[6-anpassen/08-das-vorlagenpaket|6.8 – Das Vorlagenpaket]] — die [[7-nachschlagen/01-glossar#Baustein|Bausteine]], was mitreist und was
   nicht.

> [!warning] Zwei Dinge vorher
> Änderungen an der Vorlage selbst — Weg 2 in 6.1 — kann der nächste Import eines Vorlagenpakets
> überschreiben. Und in `custom.scss` schreibt die App drei Blöcke bei jedem Speichern neu; was man
> dort von Hand einträgt, ist beim nächsten Klick weg. Beides steht ausführlich in 6.1.
