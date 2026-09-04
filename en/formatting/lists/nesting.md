---
title: Nesting and quotes
description: How deep you can go, and how quotes nest.
section: Formatting
tags:
  - formatting
  - lists
translationKey: formatierung/listen/verschachtelung
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Quote

```md
> A quote.
```

> A quote.

## Quote inside a quote

```md
> A quote.
>
> > And one inside it.
```

> A quote.
>
> > And one inside it.

## List inside a quote

```md
> A quote with a list:
>
> - first point
> - second point
```

> A quote with a list:
>
> - first point
> - second point

## In this template

**Out of the box** Quartz sets a quote with a grey bar on the left and italic text.

**In this template** the bar is in the accent colour, the text stays upright, and the block sits on
a slightly tinted surface with rounded corners on the right. Italics over several lines read worse,
and a quote is not a different tone of voice but a different voice.
