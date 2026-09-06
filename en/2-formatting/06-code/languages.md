---
title: Languages
description: Which highlighting for what — with examples.
section: Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/sprachen
cover: "[[assets/covers/cover-code.svg]]"
---

The short name after the three backticks decides the highlighting. A selection:

```scss
.example {
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
def greet(name: str) -> str:
    return f"Hello, {name}"
```

```json
{ "name": "example", "version": "1.0.0" }
```

```diff
- old line
+ new line
```

## Which theme

This template uses `github-light` and `github-dark` — two themes that belong together and whose
colours stay legible on both grounds. It is set on the *Syntax highlighting* [[en/7-reference/01-glossary#Plugin|plugin]].
