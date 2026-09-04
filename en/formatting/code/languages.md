---
title: Languages
description: Which highlighting for what — with examples.
section: Formatting
tags:
  - formatting
  - code
translationKey: formatierung/code/sprachen
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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
  pageTitle: Minimal & lesbar
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
colours stay legible on both grounds. It is set on the *Syntax highlighting* plugin.
