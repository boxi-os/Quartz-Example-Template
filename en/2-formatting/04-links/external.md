---
title: External links
description: Links to the outside — and how you recognise them.
section: 2 Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/extern
cover: "[[assets/covers/cover-links.svg]]"
---

```md
[Quartz](https://quartz.jzhao.xyz/)
<https://quartz.jzhao.xyz/>
```

[Quartz](https://quartz.jzhao.xyz/)
<https://quartz.jzhao.xyz/>

## In this template

**Out of the box** external links look like internal ones.

**In this template** they get a small arrow after the text: ↗. That is not decoration. Anyone
reading the page should know beforehand that a click leaves it — and the colour alone does not say
so.

The arrow sits in the [[en/7-reference/01-glossary#Stylesheet|stylesheet]] as an `::after`, not in the text. So it does not end up in a copy,
nor in the reading order of a screen reader.

## Title

```md
[Quartz](https://quartz.jzhao.xyz/ "The documentation")
```

[Quartz](https://quartz.jzhao.xyz/ "The documentation")

The text in quotation marks appears as a tooltip on [[en/7-reference/01-glossary#Hover|hover]]. Do not rely on it: on a phone there is
none.
