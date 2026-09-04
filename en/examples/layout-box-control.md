---
title: Controlling the layout box per page
description: The same component, set up differently on this one page.
section: Examples
tags:
  - examples
  - layout-box
layoutBoxNote: false
layoutBoxCta:
  html: "<p>On this one page this box shows a different text — set in the frontmatter, not in the configuration.</p>"
translationKey: beispiele/layout-box-steuerung
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

This page controls two of the five layout box instances through its own frontmatter:

```yaml
---
layoutBoxNote: false
layoutBoxCta:
  html: "<p>A different text, on this page only.</p>"
---
```

**What you should see:** the box "Über dieses Handbuch" in the left column is missing here — on
every other page it is there. And the box below this text shows different content than usual.

That works because every instance has its own `frontmatterKey`. Without it, a single
`layoutBox: false` would switch off all five boxes at once.

## The three forms

| In the frontmatter | Effect |
| -------------- | ------- |
| `layoutBoxNote: false` | hide the box on this page |
| `layoutBoxNote: other.md` | load a different snippet from the same folder |
| `layoutBoxNote: {html: "…"}` | set your own content; `{file: "…"}` and `{hidden: true}` work too |

## The five instances of this template

| Key | Place | Form |
| --------- | --- | ---- |
| `layoutBoxMark` | header | word mark, one image per colour scheme |
| `layoutBoxNote` | left column | Markdown file, collapsible |
| `layoutBoxHint` | left column | narrow screens only |
| `layoutBoxCta` | after the content | call to action with placeholders |
| `layoutBoxColophon` | footer | colophon line |

Four of them take their content from the configuration (`html:`) and therefore travel with the
template package in full. The box in the left column loads from a file and shows the other way —
that file has to be copied along when the template is passed on.

> [!note] The title stays as configured
> The frontmatter can replace the content of a box, and can hide it, but not its title. That is why
> the two titled boxes still read German on the English pages of this site — see
> [[en/design/multilingual/limits|Where the two languages stop]].
