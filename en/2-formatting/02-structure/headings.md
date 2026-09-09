---
title: Headings
description: Six levels — and why the last two stop shrinking here.
section: 2 – Formatting
tags:
  - formatting
  - structure
translationKey: formatierung/struktur/ueberschriften
cover: "[[assets/covers/cover-struktur.svg]]"
---

The page title is already an `h1`, so the text sensibly starts at `##`. This page nonetheless goes
down to the sixth level, so that the table of contents on the right shows every step.

```md
# Level 1 — the page title
## Level 2
### Level 3
#### Level 4
##### Level 5
###### Level 6
```

## Level 2

From here on the page divides itself.

### Level 3

The space of a heading sits above it, not below: the gap says what belongs to the heading.

#### Level 4

Up to here the levels differ in size.

##### Level 5

From here on they no longer do. Five and six switch to capitals and letter-spacing, because a
difference of one or two pixels is not information anyone recognises reliably.

###### Level 6

The deepest level, smaller and muted.

## What this template does differently

**Out of the box** Quartz sets all six levels in the same typeface with falling size, and the space
sits above and below.

**In this template** the space sits above only, the font size follows a named scale
(`--tpl-text-3xl` down to `--tpl-text-sm`), and the two deepest levels change the means rather than
the size. More on that: [[en/5-design/03-in-the-content/body-text|Body text]].
