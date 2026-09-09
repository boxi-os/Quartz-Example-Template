---
title: Sprachen
description: Welche Hervorhebung wofür — mit Beispielen.
section: 2 – Formatierung
tags:
  - formatierung
  - code
translationKey: formatierung/code/sprachen
cover: "[[assets/covers/cover-code.svg]]"
---

Das Kürzel nach den drei Backticks bestimmt die Hervorhebung. Eine Auswahl:

```scss
.beispiel {
  color: var(--secondary);
  padding: var(--tpl-space-md);
}
```

```yaml
configuration:
  pageTitle: Example
  locale: de-DE
```

```bash
npx quartz build --serve
```

```python
def gruss(name: str) -> str:
    return f"Hallo, {name}"
```

```json
{ "name": "beispiel", "version": "1.0.0" }
```

```diff
- alte Zeile
+ neue Zeile
```

## Welches Thema

Diese Vorlage nutzt `github-light` und `github-dark` — zwei Themen, die zusammengehören und deren
Farben auf beiden Gründen lesbar bleiben. Eingestellt wird das beim [[7-nachschlagen/01-glossar#Plugin|Plugin]] *Syntax highlighting*.
