---
title: Named and repeated footnotes
description: Names instead of numbers, several references, footnotes inline.
section: Formatting
tags:
  - formatting
  - footnotes
translationKey: formatierung/fussnoten/varianten
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Named instead of numbered

```md
First reference[^measurement] and second reference[^source].

[^measurement]: Names are easier to read in the source than numbers.
[^source]: And they do not slip when a footnote is inserted in between.
```

First reference[^measurement] and second reference[^source].

[^measurement]: Names are easier to read in the source than numbers.
[^source]: And they do not slip when a footnote is inserted in between.

On the site numbers still appear — the name only exists in the source.

## Footnotes over several lines

Continuation lines are indented:

```md
[^long]: The first line.

    A second paragraph, indented by four spaces.
```

## Inline footnotes

Obsidian knows a short form without a separate definition:

```md
A sentence with an inline footnote.^[The text stands right here.]
```

A sentence with an inline footnote.^[The text stands right here.]

> [!warning] Not supported everywhere
> The inline form is an Obsidian extension. If it appears on the built page as raw text instead of
> a footnote, support is missing — then the long form with `[^name]` is the safe choice.

## The same footnote twice

```md
First reference[^same] and later another one[^same].

[^same]: Both references point to this one footnote.
```

First reference[^same] and later another one[^same].

[^same]: Both references point to this one footnote.
