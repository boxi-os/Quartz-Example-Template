---
title: Task lists
description: Boxes to tick — and why what is done is marked twice here.
section: 2 Formatting
tags:
  - formatting
  - lists
translationKey: formatierung/listen/aufgaben
cover: "[[assets/covers/cover-listen.svg]]"
---

```md
- [ ] Open
- [x] Done
- [ ] With sub-points
  - [x] Part one
  - [ ] Part two
```

- [ ] Open
- [x] Done
- [ ] With sub-points
  - [x] Part one
  - [ ] Part two

## What this template does differently

**Out of the box** Quartz shows a ticked box and leaves the text unchanged.

**In this template** a completed point also gets a muted colour *and* a strikethrough. A state that
hangs on a small tick alone is no state at all for some readers — hence three signals instead of
one. And the template draws **all six states** Obsidian knows, not just two — see below.

The list also loses its bullets as soon as it contains boxes: bullet and box next to each other are
one marker too many.

## Other characters in the box

Obsidian allows any character between the brackets and shows its own symbols for them:

```md
- [/] half done
- [-] dropped
- [>] deferred
- [?] questionable
```

- [/] half done
- [-] dropped
- [>] deferred
- [?] questionable

All four arrive on the site, and this template draws them — every character gets its own mark in
the box:

| Character | Mark | Colour | Text |
| --- | --- | --- | --- |
| `[ ]` | empty box | muted | plain |
| `[x]` | tick | accent | struck through |
| `[/]` | slash | accent | plain |
| `[-]` | minus | muted | struck through |
| `[>]` | arrow to the right | muted | plain |
| `[?]` | question mark | muted | plain |

The colour separates two groups: accent for what is still going somewhere, muted for what is being
left behind. A reader who does not know the characters at least sees those two groups.

> [!note] It was not always like this
> Until recently Quartz kept only `[ ]` and `[x]`; everything else became an empty box and the
> character was gone. Since the Obsidian plugin writes it onto the line as `data-task` it is there
> — and since then a template can do something with it.

> [!note] Clicking works, but it stays in this browser
> On the built site an open box can be ticked. Measured: Quartz remembers it in this browser's
> `localStorage` and restores it on your next visit — your note still says what it said, and
> another browser sees the list as written. Ticking things off still happens in Obsidian; the tick
> on the site is a note to yourself.
