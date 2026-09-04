---
title: Bilder je Farbschema
description: Zwei Bilder, von denen immer nur eines sichtbar ist.
section: Formatierung
tags:
  - formatierung
  - medien
translationKey: formatierung/medien/einbettungen
---

Das Plugin *Layout Box* dieser Vorlage schaltet Bilder nach Farbschema um: Ein Element mit der
Klasse `img-light` erscheint im hellen Modus, `img-dark` im dunklen.

```html
<img class="img-light" src="{{root}}/static/logo-hell.png" alt="" />
<img class="img-dark" src="{{root}}/static/logo-dunkel.png" alt="" />
```

Die Wortmarke oben links auf dieser Website funktioniert so — allerdings mit zwei Inline-SVGs statt
zwei Dateien, weil ein Vorlagenpaket keine Bilddateien transportiert.

## Warum das nicht mit CSS allein geht

Ein einzelnes Bild ließe sich per `filter: invert()` umfärben, aber das trifft alle Farben
gleichermaßen und macht aus einem grünen Logo ein magentafarbenes. Zwei Fassungen sind die
ehrlichere Lösung.

## Alternative: currentColor

Ein Inline-SVG, dessen Flächen `fill="currentColor"` tragen, folgt automatisch der Textfarbe und
braucht keine zweite Fassung. Das ist der einfachere Weg, sobald das Bild einfarbig ist.

Mehr zu den Instanzen: [[gestaltung/layout-box/die-fuenf-instanzen|Die fünf Instanzen]].
