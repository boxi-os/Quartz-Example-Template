---
title: 7.3 – Muster
description: Die Entscheidungen, die sich durch jede Komponente ziehen — einmal gesagt, statt auf dreißig Seiten wiederholt.
section: 7 – Nachschlagen
tags:
  - nachschlagen
  - referenz
translationKey: nachschlagen/muster
---

Drei Entscheidungen tragen die ganze Vorlage; sie stehen in
[[1-einstieg/01-was-diese-vorlage-ist|1.1 – Was diese Vorlage ist]]. Darunter wiederholen sich
kleinere Muster in jeder Komponente. Wer eine Komponente ändert oder eine neue gestaltet, hält sich
an diese, damit sie zum Rest passt.

## Was überall gleich ist

1. **Überschriften der Seitenleisten** sind klein, versal und gedämpft — sie sind Beschriftung,
   nicht Inhalt. Dieselbe Form steht in neun [[7-nachschlagen/01-glossar#Stylesheet|Stylesheets]], und das ist Absicht: Jede Seite in
   Kapitel 5 soll ihre eigene Tabelle der Variablen vollständig zeigen.
2. **Ein Zustand wird nie nur durch Farbe gezeigt.** Der aktive Eintrag im [[7-nachschlagen/01-glossar#Explorer|Explorer]] hat Farbe,
   Schriftschnitt *und* einen Balken; ein erledigter Aufgabenpunkt ist gedämpft *und*
   durchgestrichen; ein externer Link ist andersfarbig *und* trägt einen Pfeil.
3. **Ränder von Bedienelementen** ziehen ihre Farbe aus `--tpl-rule-control`, nicht aus
   `--lightgray`. Der zarte Ton reicht für eine Trennlinie, aber nicht für den Rand von etwas, das
   man bedient — [[7-nachschlagen/01-glossar#WCAG|WCAG]] verlangt dort 3:1.
4. **Alles, was man antippt, ist mindestens 44 px groß** (`--tpl-target`). WCAG verlangt 24; 44
   ist die Größe, bei der niemand zielen muss.
5. **Zwei Zeilenabstände, nicht einer.** 1,65 für den Fließtext, 1,45 für alles in Kleinschrift —
   die Seitenleisten und die Fußzeile. Derselbe Abstand bei kleinerer Schrift zerreißt einen
   Absatz in Einzelzeilen.
6. **Ein überfahrener Link** wird akzentfarbig und unterstrichen, mit tiefer gesetzter
   Unterstreichung. Dieselbe Geste in sieben Stylesheets, derselbe Wert aus einer Variable.
7. **Alle Ausklapp-Pfeile sind dieselbe Chevron** aus dem Lucide-Satz — im Explorer, im
   Inhaltsverzeichnis, in der aufklappbaren [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]].
8. **Was über den Rand läuft, scrollt in sich selbst** und blendet dabei weich aus, statt die
   Seite länger zu machen: der Explorer, das Inhaltsverzeichnis, eine breite Tabelle, ein
   Codeblock.
9. **Ein Bereich, der auf einer Breite wirklich nichts zu suchen hat, wird ausgeblendet; eine
   Spalte, die nur gerade leer ist, bleibt stehen**, damit die Textspalte nicht wandert.
10. **Nichts bewegt sich, wenn das System es nicht will.** `prefers-reduced-motion` setzt eine
    einzige Variable auf null, und jeder Übergang der Vorlage folgt ihr.

## Was bewusst nicht vereinheitlicht ist

Die neun Panel-Überschriften und die sieben Hover-Regeln ließen sich in eine gemeinsame Datei
ziehen. Das wäre hier falsch: Die Stylesheets sind nach Komponenten geschnitten, und die
Dokumentation hängt daran — jede Seite in Kapitel 5 zeigt die Variablen, die *ihre* Komponente
liest. Geteilt werden die **Werte**, und die sind es: `--tpl-tracking-label` und
`--tpl-underline-offset` stehen je einmal. Ausführlich in [[6-anpassen/04-variablen|6.4 – Variablen]].
