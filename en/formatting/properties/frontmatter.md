---
title: Frontmatter
description: The fields at the very top of the file and what Quartz does with them.
section: Formatting
tags:
  - formatting
  - frontmatter
translationKey: formatierung/eigenschaften/frontmatter
cover: "[[assets/covers/cover-eigenschaften.svg]]"
---

Between two lines of three hyphens, at the very start of the file:

````md
---
title: Frontmatter
description: A short description for the preview and the search result.
tags:
  - formatting
  - frontmatter
date: 2026-09-01
lastmod: 2026-09-04
aliases:
  - Properties
draft: false
---
````

## What Quartz evaluates

| Field | Effect |
| ---- | ------- |
| `title` | page title, browser title, label in listings and search |
| `description` | preview text in search, listings and when sharing |
| `tags` | tag list under the title, tag pages, links |
| `date` / `lastmod` | date under the title, ordering in "Recently changed" |
| `aliases` | redirects from other paths — see [[en/formatting/links/aliases\|Aliases]] |
| `draft: true` | the page is not built at all |
| `unlisted: true` | the page is built but appears in no listing |
| `translationKey` | ties this page to its translation — see [[en/design/multilingual/linking\|How the two languages find each other]] |

## Where the date comes from

Without a `date` in the frontmatter Quartz takes the date from git — and without git from the file
system. The order is set on the *Created modified date* plugin; this template uses
`frontmatter → filesystem`, leaving git out because it cannot answer here — why, is under
[[en/design/above-the-content/title-and-date|Title and date]].

> [!tip] Fields of your own are allowed
> A field Quartz does not know does no harm. This template uses `section`, for instance — for the
> display in the properties and for a placeholder in the layout box.
