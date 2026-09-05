---
title: Comments
description: Text that only exists in the source.
section: Formatting
tags:
  - formatting
  - footnotes
translationKey: formatierung/fussnoten/kommentare
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

Measured on the built page: **both forms are gone.** In many Markdown tools an HTML comment
survives into the delivered HTML and is readable in the page source — not here; Quartz strips it
just like the `%%` comment. Rely on neither: what must not appear in the output does not belong in
the file.

> [!warning] A comment is not secrecy
> Both forms remain in the Markdown file. Anyone who can read the repository reads them. For
> anything genuinely confidential there is `ignorePatterns` or the *Encrypted pages* plugin.
