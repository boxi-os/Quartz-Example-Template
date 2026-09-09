---
title: 4.6 – Cover image
description: The field cover — one image per page for the gallery and the cards of a base.
section: 4 – Controlling a page
tags:
  - controlling-a-page
cover: "[[assets/covers/cover-index.svg]]"
translationKey: seiten-steuern/titelbild
---

A [[en/7-reference/01-glossary#Base|base]] — Obsidian's saved query over the [[en/7-reference/01-glossary#Vault|vault]], see
[[en/3-obsidian-formats/01-bases/index|3.1 – Bases]] — can show its entries as a gallery or as
cards. Both views take an option `image:` that names a **property**; its value may be a [[en/7-reference/01-glossary#Wikilink|wikilink]]
to an image, a path or a hex colour. Without it every tile shows the same hatched placeholder.

This site uses the field `cover` for it:

```yaml
---
cover: "[[assets/covers/cover-links.svg]]"
---
```

Every page from chapter 2 carries it — 63 pages per language, one image per section and one for
the chapter page, fourteen images in all. The bases *All views* and *Formatting pages* say with
`image: cover` that they read this field; the gallery under
[[en/3-obsidian-formats/01-bases/All-Views.base|All views]] shows the result.

## Where the images live

In the vault under `assets/covers/`, like all media of this site: there the vault's [[en/7-reference/01-glossary#git|git]] versions
them, and there Obsidian finds them while writing. The fourteen images are generated, not drawn —
a script in QuartzControl's [[en/7-reference/01-glossary#Repository|repository]] writes them.

The colours are deliberately close together: the same band of brightness, little saturation,
around the navy and the sienna of the palette. Fourteen full colours would be the loudest thing on
a site whose whole argument is restraint. A motif, no text: the title stands under the tile, and an
image that repeats it is an image wasted.

## For your own pages

The field may have any name; it only has to carry the same name under `image:` in the base. A
photo does the job as well as an SVG. A page without the field gets the placeholder in the gallery
— not an error, just an empty tile.
