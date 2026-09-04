---
title: Footnotes — the basic form
description: A marker in the text, the text at the foot of the page.
section: Formatting
tags:
  - formatting
  - footnotes
translationKey: formatierung/fussnoten/grundform
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

```md
A sentence with a footnote.[^1]

[^1]: The text of the footnote, right at the bottom of the page.
```

A sentence with a footnote.[^1]

[^1]: The text of the footnote, right at the bottom of the page.

## What happens there

The superscript number in the text is a jump link downwards. At the foot of the page stands the
text, and behind it an arrow leading back to the place in the text. Both directions are created
automatically.

The definition may stand anywhere in the file — usually directly below the paragraph or collected
at the end. The numbering in the output follows the order **in the text**, not that of the
definitions.

## In this template

The footnote area is set off by a line, set smaller and muted — it is apparatus, not text. A
footnote that has been jumped to is briefly highlighted, so that on landing you can see which one
was meant.

**Out of the box** the area is set at the same size as the body text and without a separation.
