---
title: Named and repeated footnotes
description: Names instead of numbers, several references, footnotes inline.
section: 2 Formatting
tags:
  - formatting
  - footnotes
translationKey: formatierung/fussnoten/varianten
cover: "[[assets/covers/cover-fussnoten.svg]]"
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

> [!failure] It does not work here
> The line above is the proof: on the built page `^[The text stands right here.]` shows as raw
> text, caret and brackets included. The inline form is an Obsidian extension, and none of this
> template's [[en/7-reference/01-glossary#Markdown|Markdown]] [[en/7-reference/01-glossary#Plugin|plugins]] knows it. In Obsidian you see a proper footnote, on the site you do
> not — the nastiest case, because nothing about it shows while writing.
>
> The long form with `[^name]` is therefore the only one that holds.

## The same footnote twice

```md
First reference[^same] and later another one[^same].

[^same]: Both references point to this one footnote.
```

First reference[^same] and later another one[^same].

[^same]: Both references point to this one footnote.
