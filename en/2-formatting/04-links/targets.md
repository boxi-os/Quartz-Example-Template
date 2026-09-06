---
title: Jump targets
description: Linking to a heading or to a single block.
section: Formatting
tags:
  - formatting
  - links
translationKey: formatierung/links/ziele
cover: "[[assets/covers/cover-links.svg]]"
---

## To a heading

```md
[[en/2-formatting/02-structure/headings#Level 3|to the third level]]
```

[[en/2-formatting/02-structure/headings#Level 3|to the third level]]

## To a block

A block gets an identifier at the end of the line with `^`:

```md
This paragraph has an identifier. ^keypoint

[[en/2-formatting/04-links/targets#^keypoint|link to the paragraph]]
```

This paragraph has an identifier. ^keypoint

[[en/2-formatting/04-links/targets#^keypoint|link to the paragraph]]

## Within the same page

```md
[[#To a block|back up to the block]]
```

[[#To a block|back up to the block]]

> [!tip] Block identifiers are stable
> A heading changes when it is rephrased, a block identifier does not. For links that are meant to
> hold, `^identifier` is the more reliable choice.
