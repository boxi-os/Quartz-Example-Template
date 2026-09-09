---
title: HTML in Markdown
description: What is let through and where the limit is.
section: 2 – Formatting
tags:
  - formatting
  - special
translationKey: formatierung/besonderes/html
cover: "[[assets/covers/cover-besonderes.svg]]"
---

```md
<div style="text-align: center">A centred paragraph.</div>
```

<div style="text-align: center">A centred paragraph.</div>

## Collapsible sections

```md
<details>
<summary>A collapsible section</summary>

The content appears when unfolded. There has to be a blank line between `<summary>` and the text,
otherwise the Markdown inside it is not processed.

</details>
```

<details>
<summary>A collapsible section</summary>

The content appears when unfolded. There has to be a blank line between `<summary>` and the text,
otherwise the [[en/7-reference/01-glossary#Markdown|Markdown]] inside it is not processed.

</details>

## When HTML, when a callout

For anything collapsible the [[en/2-formatting/05-callouts/foldable|foldable callout]] is the better
choice: it is designed, it has a focus ring and it works the same way in Obsidian. HTML pays off
for things Markdown does not know at all — a table with merged cells, for instance.

## What Markdown cannot do here

**Definition lists** (`term` / `: explanation`) are known to neither Obsidian nor Quartz —
measured: the colon line stays there as text. Anyone needing them writes HTML:

```md
<dl>
  <dt>Term</dt>
  <dd>The explanation for it</dd>
</dl>
```

<dl>
  <dt>Term</dt>
  <dd>The explanation for it</dd>
</dl>

For most cases a two-column table does the job — and it reads better on a phone.

> [!warning] HTML is not sanitised
> What stands here lands on the page unchanged. With content from a foreign source that is a risk.
