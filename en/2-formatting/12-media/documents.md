---
title: Documents
description: Embedding PDFs, linking to them and jumping to a particular page.
section: Formatting
tags:
  - formatting
  - media
translationKey: formatierung/medien/dokumente
cover: "[[assets/covers/cover-medien.svg]]"
---

## As a link

```md
[The example document](assets/beispiel-dokument.pdf)
```

[The example document](assets/beispiel-dokument.pdf)

The browser decides whether it shows the PDF or downloads it. That is the least laborious way and
the only one that works the same on every device.

## As an embed

```md
![[beispiel-dokument.pdf]]
```

![[beispiel-dokument.pdf]]

## To a particular page

Obsidian knows a page anchor:

```md
![[beispiel-dokument.pdf#page=2]]
[To the second page](assets/beispiel-dokument.pdf#page=2)
```

[To the second page](assets/beispiel-dokument.pdf#page=2)

The anchor is a convention of the PDF viewers, not part of the PDF format.

> [!warning] The embedded PDF loses the anchor
> Measured: `![[beispiel-dokument.pdf#page=2]]` produces `<iframe src="…/beispiel-dokument.pdf">` —
> **without** the anchor. The embed always begins on page 1. Only the ordinary link keeps it, and
> the one above works.

## As a frame of its own

```md
<iframe src="assets/beispiel-dokument.pdf" width="100%" height="500"></iframe>
```

<iframe src="assets/beispiel-dokument.pdf" width="100%" height="500" title="Example document, three pages"></iframe>

The way through `<iframe>` is the only one that really decides the size. It needs a `title`,
otherwise the [[en/7-reference/01-glossary#Frame|frame]] has no name for a screen reader.

> [!warning] An embedded PDF is not an accessible page
> The viewer in the browser is an application of its own with controls of its own. Anyone wanting
> to make the content accessible provides it as text as well — and links the PDF as an addition,
> not as the only source.

## In this template

A link to a file looks like an external link, with an arrow. An embedded PDF gets the same border
and the same corners as an image, so that it does not sit in the page as a foreign body.

**Out of the box** Quartz does not embed PDFs in any special way — a [[en/7-reference/01-glossary#Wikilink|wikilink]] to one becomes an
ordinary link.
