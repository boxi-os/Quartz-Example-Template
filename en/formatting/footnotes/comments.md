---
title: Comments
description: Text that only exists in the source.
section: Formatting
tags:
  - formatting
  - footnotes
translationKey: formatierung/fussnoten/kommentare
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## Obsidian comment

```md
%% This text only exists in the source and does not appear on the site. %%
```

%% This text only exists in the source and does not appear on the site. %%

Between this paragraph and the one before it there is a comment. On the site nothing of it is
visible — in Obsidian it is, where it appears in grey.

## Over several lines

```md
%%
Over several
lines too.
%%
```

## HTML comment

```md
<!-- This does not appear in the output either. -->
```

<!-- This does not appear in the output either. -->

The difference: an HTML comment stays in the delivered HTML (invisible, but readable in the page
source). A `%%` comment is removed at build time.

> [!warning] A comment is not secrecy
> Both forms remain in the Markdown file. Anyone who can read the repository reads them. For
> anything genuinely confidential there is `ignorePatterns` or the *Encrypted pages* plugin.
