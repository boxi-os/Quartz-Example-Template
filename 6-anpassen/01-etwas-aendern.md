---
title: 6.1 – Etwas ändern
description: Drei Ebenen, von der billigsten zur teuersten — und wo die eigene Regel hingehört, damit sie gewinnt.
section: 6 – Anpassen
tags:
  - anpassen
translationKey: anpassen/etwas-aendern
---

Diese Vorlage ist zum Ändern gebaut. Es gibt drei Ebenen dafür, und die erste reicht öfter, als man
denkt.

## 1 · Eine Variable

**Der Normalfall.** 53 Variablen tragen jede Farbe und jedes Maß dieser Vorlage; keine Zeile CSS ist
dafür nötig. In der App unter *Stile → Variablen*, getrennt nach hell und dunkel.

Welche Variable wo greift, steht auf jeder Seite in [[5-gestaltung/index|Kapitel 5]] ganz unten — samt der Spalte, die
sagt, was sich noch mit ändert. `--tpl-space-md` anzufassen bewegt die ganze Website; `--tpl-fade`
bewegt zwei weiche Kanten.

## 2 · Eine Regel im vorhandenen Stylesheet

Wenn eine Variable nicht reicht, weil es nicht der Wert ist, sondern die Form: die 30 Stylesheets
liegen unter *Stile → Eigenes CSS*, **eins je Komponente**. Welches zu einer Komponente gehört,
steht in derselben Tabelle unten auf ihrer Seite.

Das ändert die Vorlage selbst. Beim nächsten Import eines Vorlagenpakets kann das überschrieben
werden — für eine dauerhafte Änderung ist der dritte Weg der sicherere.

## 3 · Ein eigenes Stylesheet

*Stile → Eigenes CSS → Neue Datei.* Eine neu angelegte Datei wird **ans Ende der Ladereihenfolge**
gehängt, und das ist der Punkt: Bei gleicher Spezifität gewinnt die zuletzt geladene Regel. Was hier
steht, schlägt die ganze Vorlage, ohne dass man ihr etwas wegnehmen muss.

> [!warning] Auch `a11y.scss` steht dann nicht mehr am Ende
> Diese eine Datei liegt mit Absicht zuletzt: Ihre Regeln müssen Entscheidungen weiter oben
> gewinnen — eine Bedienhilfe, die nur bei [[7-nachschlagen/01-glossar#Hover|Hover]] erschiene, ein Zustand, der nur an einer Farbe
> hinge. Eine eigene Datei landet dahinter. Wenn nach einer Änderung etwas verschwindet, das mit
> Tastatur, [[7-nachschlagen/01-glossar#Kontrast|Kontrast]] oder Druck zu tun hat, ist das die erste Stelle zum Nachsehen.

## Die Ausnahme: Diagramme

Bei [[7-nachschlagen/01-glossar#Mermaid|Mermaid]] reicht keiner der drei Wege ohne `!important`. Quartz übergibt dem Diagramm-Renderer
**neun** seiner rund hundert Theme-Variablen (`primaryColor`, `lineColor`, `secondaryColor` und
sechs weitere, fest im Quartz-Skript verdrahtet). Alles andere färbt Mermaid selbst — und schreibt
es als `<style>` mit der Kennung des jeweiligen SVG in die Grafik, also mit einem ID-Selektor, den
keine Klassenregel schlägt.

Deshalb stehen in `body-mermaid.scss` 122 `!important` — und deshalb braucht auch deine eigene Regel
eins. Zum Vergleich: In den 29 anderen Stylesheets zusammen sind es zwanzig, jedes mit einer
Begründung daneben.

## Was du nicht anfassen solltest

In `custom.scss` stehen drei Blöcke zwischen Markierungen (`imports`, `fonts`, `css-vars`). Die
schreibt die App bei jedem Speichern neu — was du dort von Hand einträgst, ist beim nächsten Klick
weg. Der Text außerhalb der Markierungen bleibt.
