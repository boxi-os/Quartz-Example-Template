---
title: Alignment
description: Colons in the separator row control the column alignment.
section: 2 Formatting
tags:
  - formatting
  - tables
translationKey: formatierung/tabellen/ausrichtung
cover: "[[assets/covers/cover-tabellen.svg]]"
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
