---
title: 4.7 Translation
description: The fields that connect a page with its translation — translationKey, aliases, lang — and when you need them.
section: Controlling a page
tags:
  - controlling-a-page
  - multilingual
translationKey: seiten-steuern/uebersetzung
---

This site exists in German and English. For the switcher at the top right to find its way from a
page to its translation, both have to say that they belong together. That happens in the
frontmatter — in three ways, of which you usually need only the first.

## `translationKey` — the normal case

```yaml
---
title: Emphasis
translationKey: formatierung/text/betonung
---
```

Two pages with the same key are translations of each other. The key can be chosen freely; this
handbook takes the German path without the chapter numbers, because it is unique and the line
shows what it points to. This is how all regular pages here are connected.

## `aliases` — the way via the title

An alias that matches the title or file name of the page in the other language connects the two
as well. The Obsidian plugin *Multilingual* writes such aliases automatically. Three pages of this
site deliberately hang on that alone, to demonstrate the way.

## Same path

Two pages whose path is the same without the language folder belong together. Here that applies
only to the two home pages: `index.md` and `en/index.md`.

## `lang` — the language of a page

The plugin recognises the language by the folder: what lies under `en/` is English; everything
else falls into the default language, German. A field `lang` is only needed when a page lies
somewhere other than where it speaks.

How all of this works in detail, with the measured numbers and the limits:
[[en/6-adapting/07-two-languages/index|6.7 Two languages]].
