---
title: 1.3 From note to website
description: The way a change travels — write, look, build, publish — and what happens where.
section: 1 Getting started
tags:
  - getting-started
translationKey: einstieg/von-der-notiz-zur-website
---

A change to this site begins in Obsidian and ends on a web space. In between lie four steps, and
each has a place.

## 1 · Writing — in Obsidian

You open the [[en/7-reference/01-glossary#Vault|vault]] in Obsidian and write. A new file is a new page; a folder a branch in the
[[en/7-reference/01-glossary#Explorer|explorer]]; a `[[wikilink]]` a reference that the [[en/7-reference/01-glossary#Graph|graph]] and the [[en/7-reference/01-glossary#Backlinks|backlinks]] see. Header lines between
two `---` at the very top of the file — the **frontmatter** — give the page its title,
description, date and tags; everything you can control with it stands in
[[en/4-controlling-a-page/index|4 Controlling a page]].

None of this needs the website yet. You can write for days without building.

## 2 · Looking — the preview in QuartzControl

Under *Preview & Build* the app starts a **dev server**: Quartz builds the site once and then again
after every saved change, and a browser window shows it at an address like `localhost:8080`. That
is your own machine; nobody else sees this page. Whoever saves in Obsidian sees the page in the
browser seconds later.

## 3 · Building — the build

The same area can also **build** the site without showing it: Quartz reads all notes, applies the
[[en/7-reference/01-glossary#Plugin|plugins]] — resolving links, generating the table of contents, indexing the search, creating pages
for folders and tags — and writes finished [[en/7-reference/01-glossary#HTML|HTML]] files into the output folder `public/`. A draft
(`draft: true` in the [[en/7-reference/01-glossary#Frontmatter|frontmatter]]) is left out; see
[[en/4-controlling-a-page/02-draft-and-unlisted|4.2 Draft and unlisted]].

## 4 · Publishing

Under *Publish* the app sends the output folder to a target: a folder, a server via rsync, a [[en/7-reference/01-glossary#git|git]]
[[en/7-reference/01-glossary#Repository|repository]] for GitHub Pages for instance, or it triggers a webhook. The credentials for that the
app keeps encrypted. From that moment on the page is public.

## Where the content lives — and why as a symlink

A Quartz project expects its notes in the folder `content/`. Here this folder is not a folder but a
**symlink**: a link that points to the Obsidian vault. Quartz sees the vault through the link as if
it lay in the project. The advantage: there is only one copy of the notes. You write in Obsidian,
and the project has it at once.

QuartzControl creates this link — under *Configuration → Content folder*, when you *link* the
content to an existing folder instead of *copying* it. Both can be changed later.

> [!warning] What a symlink costs
> Two things do not follow the link. **Snapshots** — the backups QuartzControl takes before every
> larger intervention — leave the content out as soon as `content/` is a link; the vault has to be
> backed up itself, here through its own git. And the plugin that reads a page's date from git
> miscalculates at the link and falls back to the file system — see
> [[en/4-controlling-a-page/01-title-description-date|4.1 Title, description, date]].

## Getting the template into a project of your own

Whoever wants not this site but one of their own with this design goes the other way round:
create a new project in QuartzControl, link your own vault, then import the template under
*Templates*. The app shows beforehand which parts the package contains and what in the project is
replaced by them, and takes a snapshot. What comes along and what does not:
[[en/6-adapting/08-the-template-package|6.8 The template package]].
