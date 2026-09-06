---
title: 4 Controlling a page
description: What a page's frontmatter does — title, date, draft, alias, custom fields, layout boxes, cover image, translation.
section: Controlling a page
tags:
  - controlling-a-page
translationKey: seiten-steuern/index
---

At the very top of a note, between two lines of three hyphens, stand statements *about* the page:
its title, a description, tags, a date. This block is called the **frontmatter**; Obsidian shows it
as “Properties”. Quartz reads it and acts on it — and that is exactly what you control here: not
what something looks like, but what happens to the page.

```yaml
---
title: A page
description: One sentence for search, preview and lists.
tags:
  - example
date: 2026-09-01
draft: false
---
```

How to *write* frontmatter — the data types, the display — stands in
[[en/2-formatting/11-properties/index|2.11 Properties]]. Here stands what every field *does*.

## The fields at a glance

| Field | Effect | Page |
| --- | --- | --- |
| `title`, `description` | title and preview text of the page | [[en/4-controlling-a-page/01-title-description-date\|4.1]] |
| `date`, `lastmod` | date under the title, order in “Recently changed” | [[en/4-controlling-a-page/01-title-description-date\|4.1]] |
| `draft: true` | the page is not built | [[en/4-controlling-a-page/02-draft-and-unlisted\|4.2]] |
| `unlisted: true` | the page is built but appears in no list | [[en/4-controlling-a-page/02-draft-and-unlisted\|4.2]] |
| `aliases` | further paths under which the page can be reached | [[en/4-controlling-a-page/03-aliases\|4.3]] |
| `tags` | tag list under the title, tag pages, filter of a base | [[en/5-design/02-above-the-content/tags\|Tags]] |
| custom fields such as `section` | appear in the property table | [[en/4-controlling-a-page/04-custom-fields\|4.4]] |
| `layoutBoxNote`, `layoutBoxCta`, … | hide or refill a layout box on this page | [[en/4-controlling-a-page/05-layout-boxes-per-page\|4.5]] |
| `cover` | a cover image for gallery and cards | [[en/4-controlling-a-page/06-cover-image\|4.6]] |
| `translationKey`, `lang` | connect the page with its translation | [[en/4-controlling-a-page/07-translation\|4.7]] |

> [!tip] Custom fields are allowed
> A field Quartz does not know does no harm. This template uses `section`, for instance, for the
> display in the property table; and a layout box can insert any field as a placeholder
> `{{frontmatter.name}}`.
