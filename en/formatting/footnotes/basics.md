---
title: Footnotes — the basic form
description: A marker in the text, the text at the foot of the page.
section: Formatting
tags:
  - formatting
  - footnotes
translationKey: formatierung/fussnoten/grundform
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
