---
title: 7.1 Glossary
description: Every term of this handbook in two or three sentences — alphabetical, with a link to the page that goes into it.
section: Reference
tags:
  - reference
  - terms
translationKey: nachschlagen/glossar
---

Every entry is a heading and therefore linkable: `[[en/7-reference/01-glossary#Symlink]]` jumps
straight to the term.

### Accessibility

Building a site so that it stays usable without a mouse, without colour vision, with a screen
reader or with system settings such as “reduce motion”. The rules for it are called WCAG. →
[[en/6-adapting/06-accessibility|6.6 Accessibility]]

### Alias

A second name for a page, entered in the frontmatter under `aliases`. Obsidian finds the note
under it too; on the site a plugin builds a redirect for every alias. →
[[en/4-controlling-a-page/03-aliases|4.3 Aliases]]

### Backlinks

The list of pages that link to the current page, in the right column. →
[[en/5-design/04-beside-the-content/backlinks|Backlinks]]

### Base

A saved query over the vault in Obsidian: it collects notes by criteria and shows them as a
table, list, cards, board or gallery. The file ends in `.base`. →
[[en/3-obsidian-formats/01-bases/index|3.1 Bases]]

### Breadcrumbs

The line above the title that shows the way from the home page to the current one: “2 Formatting
› 2.5 Callouts › Callouts — the basic form”. →
[[en/5-design/02-above-the-content/breadcrumbs|Breadcrumbs]]

### Breakpoint

The window width at which a page breaks differently. This template has two: 1100 px (desktop to
tablet) and 800 px (tablet to phone). → [[en/6-adapting/05-page-grids|6.5 Page grids]]

### Build

The process in which Quartz produces the finished site from the notes: read Markdown, apply
plugins, write HTML files into the output folder `public/`. In QuartzControl under
*Preview & Build*. → [[en/1-getting-started/03-from-note-to-website|1.3 From note to website]]

### Callout

A highlighted box in the text, written in Obsidian as `> [!note]`. There are thirteen types with a
colour and a symbol each; this template restates all the colours. →
[[en/2-formatting/05-callouts/index|2.5 Callouts]]

### Canvas

A free surface in Obsidian on which you arrange cards and connect them with arrows. The file
ends in `.canvas`; Quartz makes a zoomable page from it. →
[[en/3-obsidian-formats/02-canvas/index|3.2 Canvas]]

### Commit

A saved state in git, with date, author and description. You can return to any commit. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Colour scheme

Light or dark. The site follows the system setting and has a switch in the header; every colour
of the template is set and measured for both schemes. →
[[en/5-design/01-navigation/colour-scheme|Colour scheme switch]]

### Component

A part of the page with a job of its own — the explorer, the search, the table of contents —,
each built by a plugin. QuartzControl's layout editor calls them building blocks. →
[[en/5-design/index|5 The design]]

### CSS and SCSS

CSS is the language in which the look of a website is described — colours, spacing, typefaces,
arrangement. SCSS is an extension of it with variables and nesting, translated to CSS at build
time. Quartz and this template write SCSS. →
[[en/6-adapting/01-changing-something|6.1 Changing something]]

### Dev server

A small web server on your own machine that QuartzControl starts under *Preview & Build*. It
rebuilds the site on every change and shows it at `localhost:8080` — visible only to you. →
[[en/1-getting-started/03-from-note-to-website|1.3 From note to website]]

### Diff

The comparison of two states of a file, line by line: what was added, what was dropped. git shows
this way what a commit changed. → [[en/1-getting-started/02-the-tools|1.2 The tools]]

### Draft

A page with `draft: true` in the frontmatter. It stays in the vault but is not built. →
[[en/4-controlling-a-page/02-draft-and-unlisted|4.2 Draft and unlisted]]

### Excalidraw

A drawing tool for sketches and diagrams, as a plugin in Obsidian. The drawing lives in an
`.excalidraw.md` file; on the site it stays zoomable. →
[[en/3-obsidian-formats/03-excalidraw/index|3.3 Excalidraw]]

### Explorer

The folder tree of all pages in the left column. It sorts by the pages' titles, not by file name.
→ [[en/5-design/01-navigation/explorer|The explorer]]

### Frame

The page grid: which areas a page has, where they lie, how wide they are — per screen width.
Quartz brings three fixed ones; this template builds three of its own (`editorial`, `index`,
`drawing`) in QuartzControl's frame editor. → [[en/6-adapting/05-page-grids|6.5 Page grids]]

### Frame box

Width, alignment and padding of a frame, set per breakpoint. It decides how wide the text gets. →
[[en/6-adapting/05-page-grids|6.5 Page grids]]

### Frontmatter

The block at the very top of a note between two lines of `---`, in which statements about the
page stand: title, description, tags, date. Obsidian calls it “Properties”. →
[[en/4-controlling-a-page/index|4 Controlling a page]]

### git

A program that records the history of files: every saved state, with date and description. You do
not have to operate it for this template; QuartzControl brings it along. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Graph

The pages drawn as dots and their links as lines, in the right column. →
[[en/5-design/04-beside-the-content/graph|The graph]]

### Hover

The state of an element while the mouse pointer rests on it. A link changes colour then; on a
touch screen this state does not exist, which is why nothing may be visible *only* on hover. →
[[en/6-adapting/06-accessibility|6.6 Accessibility]]

### HTML

The language web pages are written in and a browser reads. Quartz translates Markdown into HTML.
You can also write HTML directly into a note. →
[[en/2-formatting/13-special/html|HTML in Markdown]]

### Contrast

The ratio of brightness between text and ground, written as 4.5:1. WCAG demands at least 4.5:1
for normal text, 3:1 for large type. This template measures 89 pairs on every run. →
[[en/6-adapting/02-colours-and-contrast|6.2 Colours and contrast]]

### Layout

Which component appears at which place of the page — header, left and right column, before and
after the content, footer —, per page type. In QuartzControl under *Layout*. →
[[en/1-getting-started/04-how-a-page-is-built|1.4 How a page is built]]

### Layout box

A plugin that places a box of your own with HTML or Markdown at a spot of the layout. This
template uses it five times: word mark, sidebar box, mobile hint, “Read on”, colophon. →
[[en/5-design/05-layout-boxes/index|5.5 Layout boxes]]

### Markdown

The notation of the notes: text with few characters that carry meaning — `**bold**`, `# Heading`,
`[[link]]`. Obsidian writes it, Quartz reads it. → [[en/2-formatting/index|2 Formatting]]

### Media query

A condition in CSS that applies rules only at a certain window width — this is how breakpoints
come about. A media query cannot read a variable; that is why the breakpoints stand as numbers in
the stylesheets. → [[en/6-adapting/04-variables|6.4 Variables]]

### Mermaid

A text notation for diagrams — flowcharts, sequences, timelines — that Quartz translates into a
graphic. → [[en/2-formatting/09-diagrams/index|2.9 Diagrams]]

### Obsidian

The program in which the notes are written. It stores Markdown files in a vault. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Part

A delimited piece of a template package — colours, stylesheets, plugins — that you can take over
individually on import. → [[en/6-adapting/08-the-template-package|6.8 The template package]]

### Plugin

A building block of Quartz with one job: one builds the explorer, one the search, one reads the
date. Quartz brings many along; more come from the marketplace in QuartzControl. Obsidian has
plugins of its own that have nothing to do with Quartz's. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Project

A folder with a Quartz installation, its configuration and the content. QuartzControl manages
several of them. → [[en/1-getting-started/02-the-tools|1.2 The tools]]

### Publishing

Bringing the built site to its destination: a folder, a server, a git repository. In
QuartzControl under *Publish*. →
[[en/1-getting-started/03-from-note-to-website|1.3 From note to website]]

### Quartz

The static site generator that builds a website from Markdown notes and understands Obsidian's
notation. → [[en/1-getting-started/02-the-tools|1.2 The tools]]

### QuartzControl

The app with which you operate Quartz: projects, plugins, colours, typefaces, layout, preview,
build, publishing. This template is made for it. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Repository

A folder whose history git keeps. The vault of this site is one; the Quartz project is a second. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Slug

The part of the address that names a page: `en/2-formatting/05-callouts/basics.md` becomes
`/en/2-formatting/05-callouts/basics`. Quartz derives it from the file path; spaces become
hyphens. → [[en/2-formatting/04-links/wikilinks|Wikilinks]]

### Snapshot

A backup of the project that QuartzControl takes before larger interventions — before an import,
an update, a plugin change — and that you can return to. The content is not included when
`content/` is a symlink. →
[[en/1-getting-started/03-from-note-to-website|1.3 From note to website]]

### Static site generator

A program that produces finished HTML pages from text files, pages that can lie on any web space
without a database and without a running program. Quartz is one. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Stylesheet

A file with CSS or SCSS that describes the look. This template has 30, one per component, under
*Styles → Custom CSS*. → [[en/5-design/index|5 The design]]

### Symlink

A link in the file system that makes a folder appear in a second place without copying it. The
folder `content/` of this project is a symlink to the vault. →
[[en/1-getting-started/03-from-note-to-website|1.3 From note to website]]

### Tag

A keyword, in the frontmatter under `tags` or in the text as `#word`. Quartz builds a page for
every tag with all the notes that carry it. → [[en/5-design/02-above-the-content/tags|Tags]]

### Template

A design for QuartzControl, packed into a `.qtpl` file that you import into a project. This site
is the handbook of the template *Example*. →
[[en/1-getting-started/01-what-this-template-is|1.1 What this template is]]

### Token

A named variable the design is made of — `--tpl-space-md` for the base spacing, `--tpl-radius-md`
for the corners. Change the token and every place that reads it changes. In QuartzControl they are
simply called *variables*. → [[en/6-adapting/04-variables|6.4 Variables]]

### Unlisted

A page with `unlisted: true`: built and reachable through its address, but in no list. →
[[en/4-controlling-a-page/02-draft-and-unlisted|4.2 Draft and unlisted]]

### Vault

Obsidian's word for the folder in which the notes live. This site has one of its own. →
[[en/1-getting-started/02-the-tools|1.2 The tools]]

### Wikilink

A reference to another note in double square brackets: `[[Page]]` or `[[Page|displayed text]]`.
The notation comes from Obsidian; Quartz resolves it at build time. →
[[en/2-formatting/04-links/wikilinks|Wikilinks]]

### YAML

The notation of the frontmatter and of the Quartz configuration: `key: value`, lists with one
hyphen per line, indentation with spaces. →
[[en/2-formatting/11-properties/frontmatter|Frontmatter]]
