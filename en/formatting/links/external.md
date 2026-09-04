---
title: External links
description: Links to the outside — and how you recognise them.
section: Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/extern
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
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

The arrow sits in the stylesheet as an `::after`, not in the text. So it does not end up in a copy,
nor in the reading order of a screen reader.

## Title

```md
[Quartz](https://quartz.jzhao.xyz/ "The documentation")
```

[Quartz](https://quartz.jzhao.xyz/ "The documentation")

The text in quotation marks appears as a tooltip on hover. Do not rely on it: on a phone there is
none.
