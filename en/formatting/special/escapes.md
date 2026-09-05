---
title: Escaping characters
description: When Markdown reads something as markup that is meant to be text.
section: Formatting
tags:
  - formatting
  - special
translationKey: formatierung/besonderes/escapes
---

A backslash in front takes the meaning away from a character:

```md
\*no emphasis\*, \[no bracket\], \# no heading, \| no column separator
```

\*no emphasis\*, \[no bracket\], \# no heading, \| no column separator

## What has to be escaped

| Character | Otherwise |
| --- | --- |
| `*` `_` | emphasis |
| `[` `]` | link |
| `#` at the start of a line | heading |
| `-` `+` at the start of a line | list item |
| `` ` `` | code |
| `\|` in tables | column separator |
| `$` | formula |
| `%%` | comment |

## The other way

Inside inline code nothing needs escaping:

```md
`*none of this applies here*`
```

`*none of this applies here*`

That is why every example on these pages sits in a code block — otherwise each of them would render
itself instead of showing itself.
