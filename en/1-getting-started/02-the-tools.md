---
title: 1.2 The tools
description: Obsidian, Quartz, QuartzControl and git — four programs, each with one job, and how they fit together.
section: Getting started
tags:
  - getting-started
translationKey: einstieg/die-werkzeuge
---

Whoever uses this template deals with four programs. You do not have to be able to operate all
four — QuartzControl takes two of them off your hands — but you should know what each one does.

## Obsidian — where the writing happens

Obsidian is a program for notes. It stores every note as an ordinary text file with the extension
`.md`, written in **Markdown**: a simple notation in which `**bold**` becomes bold and `# Heading`
a heading. A folder full of such files is called a **vault** in Obsidian. All the notes of this
site live in one vault; chapter 2 shows what you can write in it.

## Quartz — what turns it into a website

Quartz is a **static site generator**: a program that turns a folder full of Markdown files into a
folder full of [[en/7-reference/01-glossary#HTML|HTML]] pages — HTML being the language a browser understands. This process is called
a **[[en/7-reference/01-glossary#Build|build]]**. The result is a finished website without a database and without a program behind it,
which can be put on any web space. Quartz knows Obsidian's notation: [[en/7-reference/01-glossary#Wikilink|wikilinks]], [[en/7-reference/01-glossary#Callout|callouts]] and
embedded images are translated correctly.

Quartz consists of **plugins** — building blocks with one job each: one builds the [[en/7-reference/01-glossary#Explorer|explorer]] on the
left, one the table of contents on the right, one the search, one reads a file's date. Which
plugins there are and how they are set stands in a configuration file called
`quartz.config.yaml` in the project.

## QuartzControl — where the operating happens

QuartzControl is the interface for Quartz. Without it you operate Quartz from the command line and
edit the configuration in a text editor; with it you click. The app creates projects, links the
content to a vault, installs plugins, changes colours and typefaces, builds page grids in an
editor, starts the preview, builds the site and publishes it. A **project** is a folder with a
Quartz installation; QuartzControl can manage several of them.

This template is built with QuartzControl and made for QuartzControl: everything it sets is
visible and changeable in the app.

## git — where the history is kept

git is a program that records the history of files. Every saved state is called a **commit** and
carries a date, an author and a description; you can restore any earlier state and compare two
states. Such a comparison is called a **diff** and shows line by line what changed. A folder whose
history git keeps is called a **repository**.

You do not have to be able to operate git to use this template. It still appears in three places:
QuartzControl needs it for new projects, for plugins from a git source and for its [[en/7-reference/01-glossary#Snapshot|snapshots]] — and
takes the machine's git or brings one of its own. The date of a page can be read from git by Quartz
(not here; why, stands under
[[en/4-controlling-a-page/01-title-description-date|4.1 Title, description, date]]). And whoever
publishes their site through a git repository, on GitHub Pages for instance, sends it there with
git.

## How they fit together

```
Obsidian ─writes─▶ Vault ◀─symlink─ Project ─Quartz builds─▶ Website ─▶ Web space
                                       ▲                         ▲
                                       └────── QuartzControl ────┘
```

The vault is the source. The project points to it with a **symlink** — a link in the file system
that makes a folder appear in a second place without copying it. Quartz reads the content through
this link, builds the site from it, and QuartzControl controls both. How that goes in detail:
[[en/1-getting-started/03-from-note-to-website|1.3 From note to website]].
