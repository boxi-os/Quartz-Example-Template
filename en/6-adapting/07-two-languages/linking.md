---
title: How the two languages find each other
description: Three strategies, three proofs — and what the Obsidian plugin has to do with it.
section: 6 Adapting
tags:
  - adapting
  - multilingual
translationKey: anpassen/zwei-sprachen/verknuepfung
---

For the switcher to lead from a page to its translation, somebody has to say which two pages belong
together. The [[en/7-reference/01-glossary#Plugin|plugin]] knows three ways and tries them in this order.

## 1 · `translationKey` in the frontmatter

```yaml
---
title: Betonung
translationKey: formatierung/text/betonung
---
```

Two pages with the same key are translations of each other. **That is how 128 of this site's 133
pairs work** — everything that is an ordinary page. Four of them additionally carry [[en/7-reference/01-glossary#Alias|aliases]], so
that this route is visible on the site as well; they too are linked by the key. Of the remaining
five, three take the route below and one the route below that; the last, the two [[en/7-reference/01-glossary#Excalidraw|Excalidraw]]
drawings, is not linked at all — their page renders no switcher, because the plugin brings a [[en/7-reference/01-glossary#Frame|frame]]
of its own.

The reason is a measured one: several pages here carry the same title. "Grundform" exists three
times ([[en/7-reference/01-glossary#Callout|callouts]], tables, footnotes), "Code", "Eigenschaften" and "Callouts" twice each. Titles or
file names could not decide which English page is meant; the plugin recognises that and in such a
case prefers not to link at all, with a warning in the [[en/7-reference/01-glossary#Build|build]].

The key is the German path without its extension. It is unique, it rarely changes, and you can see
from the line what it points at.

## 2 · Aliases — the way through the Obsidian plugin

The Obsidian community plugin **Multilingual** translates the name of a note and writes it into the
`aliases`. That is exactly the field the Quartz plugin reads: an alias matching the title or the
file name of a page in another language links the two.

Three pages of this site hang on that **alone** and deliberately carry no `translationKey`:

| German page | Alias in it | English page |
| --- | --- | --- |
| [[3-obsidian-formate/01-bases/wie-es-funktioniert\|Wie eine Base aufgebaut ist]] | `How a base is built` | [[en/3-obsidian-formats/01-bases/how-it-works\|How a base is built]] |
| [[3-obsidian-formate/02-canvas/wie-es-funktioniert\|Wie ein Canvas aufgebaut ist]] | `How a canvas is built` | [[en/3-obsidian-formats/02-canvas/how-it-works\|How a canvas is built]] |
| [[3-obsidian-formate/03-excalidraw/wie-es-funktioniert\|Wie eine Excalidraw-Datei aufgebaut ist]] | `How an Excalidraw file is built` | [[en/3-obsidian-formats/03-excalidraw/how-it-works\|How an Excalidraw file is built]] |

All three have the same file name (`wie-es-funktioniert`) and sit in different folders — a good test
that the linking really goes through the title and not through the file name.

> [!warning] Why not aliases everywhere
> The *Alias redirects* plugin builds a forwarding page for **every** alias. If each of the 133
> German notes carried its English title as an alias, 133 extra pages would appear, leading from
> `/emphasis` to the *German* page. That is not a fault, but it would not have been a decision —
> hence the aliases only stand where they are meant to show something.

> [!note] The translation service did not run here
> The Obsidian plugin needs an API key for Google Translate or DeepL. It is installed in the [[en/7-reference/01-glossary#Vault|vault]]
> and set up for German → English, but the key is missing; the aliases above are entered in exactly
> the form the plugin would write. Anyone providing a key can have them generated from then on
> through the *Translate note name* command.

## 3 · The same path

Two pages whose path without the language part is identical belong together. On this site that
applies to **exactly one pair**, and to the most visible one at that: the home pages. `index.md`
falls into the default language, so its [[en/7-reference/01-glossary#Base|base]] path is `index`; `en/index.md` sits in the language
folder, so its base path is `index` too. The two are linked without a single field in the
[[en/7-reference/01-glossary#Frontmatter|frontmatter]].

For every other page the route does not apply, because the English paths are English —
`formatierung/text/betonung` becomes `formatting/text/emphasis`, not the same path in a different
folder. That is deliberate: an English address with German words in it would be half a translation.

## What comes out of it

After the build every page carries a `multilanguage` field with its language, its base path, the
strategy that detected it and the list of its translations. The switcher builds its entries from
that list, and the `hreflang` entries in the head of the page come from it too.
