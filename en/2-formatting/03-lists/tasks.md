---
title: Task lists
description: Boxes to tick — and why what is done is marked twice here.
section: Formatting
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
one.

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

> [!warning] On the site only open and done survive
> Measured: of all the characters, Quartz recognises only `[ ]` and `[x]` as a state — the rest
> become an empty box and the character is lost. Anyone who needs the intermediate states on the
> site as well writes them into the text rather than into the brackets.

> [!note] They are not clickable
> On a built site the box is a display, not a control. Ticking happens in Obsidian.
