---
title: Line breaks
description: Why a break in the source is not one on the page here — and how to force one.
section: Formatting
tags:
  - formatting
  - text
translationKey: formatierung/text/zeilenumbrueche
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## A break in the source is not one on the page

```md
First line
Second line
```

First line
Second line

Both lines form **one paragraph**. That is the behaviour of standard Markdown: a single break in
the source counts as a space, and the text flows.

That matters for notes that are written wrapped in the editor — like every page of this site. They
are wrapped at column 100 so that they can be read and compared; none of that is visible on the
page.

## Paragraph

```md
A paragraph.

A second paragraph, separated by a blank line.
```

A paragraph.

A second paragraph, separated by a blank line.

**That is the usual way.** Where a break is needed semantically, a paragraph is usually what is
meant.

## Forcing a break

For the cases where a break really does belong inside a paragraph — an address, a verse, a line in
a form:

```md
First line<br>Second line
```

First line<br>Second line

Or with two spaces at the end of the line, which is invisible in the source and therefore easily
lost.

## The switch behind it

The *Hard line breaks* plugin reverses this rule: with it, **every** break in the source becomes a
break on the page. Obsidian itself behaves that way, which makes the switch tempting.

> [!warning] This template leaves it off
> Measured before it was switched off: nine forced breaks on a single page, every one of them in
> the middle of a sentence. Anyone who wraps their notes in the editor — and almost everyone
> writing long texts does — gets chopped-up body text with the plugin.
>
> Anyone writing line by line (lists, verse, short lines) who really means the break switches it
> back on in the app under *Plugins*.
