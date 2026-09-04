---
title: Jump targets
description: Linking to a heading or to a single block.
section: Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/ziele
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## To a heading

```md
[[en/formatting/structure/headings#Level 3|to the third level]]
```

[[en/formatting/structure/headings#Level 3|to the third level]]

## To a block

A block gets an identifier at the end of the line with `^`:

```md
This paragraph has an identifier. ^keypoint

[[en/formatting/links/targets#^keypoint|link to the paragraph]]
```

This paragraph has an identifier. ^keypoint

[[en/formatting/links/targets#^keypoint|link to the paragraph]]

## Within the same page

```md
[[#To a block|back up to the block]]
```

[[#To a block|back up to the block]]

> [!tip] Block identifiers are stable
> A heading changes when it is rephrased, a block identifier does not. For links that are meant to
> hold, `^identifier` is the more reliable choice.
