---
title: Alignment
description: Colons in the separator row control the column alignment.
section: Formatting
tags:
  - formatting
  - tables
translationKey: formatierung/tabellen/ausrichtung
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
| Left  | Centre    |  Right |
| :---- | :-------: | -----: |
| a     |     b     |      c |
| aaaa  |    bbbb   |   cccc |
```

| Left  | Centre    |  Right |
| :---- | :-------: | -----: |
| a     |     b     |      c |
| aaaa  |    bbbb   |   cccc |

| Colon | Effect |
| --- | --- |
| `:---` | left-aligned (default) |
| `:---:` | centred |
| `---:` | right-aligned |

> [!tip] Numbers belong on the right
> Digits can only be compared when the units line up under one another. So `---:` for columns of
> numbers — and in this template lists additionally get `tabular-nums`, so that the digits are
> equally wide.
