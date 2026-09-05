---
title: How a base is built
description: Filters, formulas and views — the YAML format explained.
section: Obsidian formats
tags:
  - obsidian-formats
  - bases
---

A `.base` file has up to three sections:

```yaml
filters:
  and:
    - file.hasTag("formatting")
    - file.ext == "md"

formulas:
  Area: file.folder

views:
  - type: table
    name: All formatting pages
    order:
      - file.name
      - description
      - formula.Area
    sort:
      - property: file.name
        direction: ASC
```

## filters

Which notes are taken in. Joined with `and`, `or` and `not`. Common expressions:

| Expression | Meaning |
| --- | --- |
| `file.hasTag("x")` | carries this tag |
| `file.inFolder("x")` | sits in this folder |
| `file.ext == "md"` | is a Markdown file |
| `property != null` | field is set |

## formulas

Calculated columns. They are available afterwards as `formula.Name` — handy for pulling two fields
together or shortening a path.

## views

A base can have several views of the same data. The Quartz plugin knows `table`, `list`, `cards`,
`board` and `gallery`; the default is `table`.

| Key | Effect |
| --- | --- |
| `type` | kind of view |
| `name` | label of the view |
| `order` | which columns, in which order |
| `sort` | ordering, with `property` and `direction` |
| `groupBy` | grouping by a field |
| `limit` | maximum number of entries |

## Where this is edited

Obsidian has an interface for it — the YAML file is only the store. Anyone writing it by hand
should open it in Obsidian afterwards and check it.

## Linking to one

A wikilink to such a file needs the **extension**:

```md
[[en/obsidian-formats/bases/Formatting-Pages.base|Formatting pages]]
[[en/obsidian-formats/canvas/Structure of the template.canvas|Structure of the template]]
```

Quartz keeps the extension in the address of the page (`…/formatting-pages.base`), unlike with
Markdown files. Without it the link leads nowhere — and that does not stand out, because an
unresolved wikilink gets no special marking here.
