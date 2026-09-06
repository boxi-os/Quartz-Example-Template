---
title: 7.4 Known limits
description: What does not work, why not, and what the template does instead — collected from all chapters, each with a link to the page that goes into it.
section: 7 Reference
tags:
  - reference
  - terms
translationKey: nachschlagen/bekannte-grenzen
---

Everything here was measured on the built site, not assumed. Most points are limits of Quartz or
of a [[en/7-reference/01-glossary#Plugin|plugin]] that a template cannot fix, only work around; a few are limits of QuartzControl, and
those are reported. The linked page has the details in each case.

## When writing

| Limit | Instead | Where |
| --- | --- | --- |
| Tasks on the site know only open and done; `[/]`, `[-]`, `[?]` become empty boxes | write the state into the text | [[en/2-formatting/03-lists/tasks\|Task lists]] |
| Inline footnotes `^[…]` stay raw text | write the footnote with `[^1]` | [[en/2-formatting/10-footnotes/variants\|Named and repeated footnotes]] |
| Arrows like `-->` do not become → | write the character → directly | [[en/2-formatting/13-special/arrows-and-emoji\|Arrows, tags and emoji]] |
| A tag in running text has a broken link — a bug in Quartz | tags in the [[en/7-reference/01-glossary#Frontmatter\|frontmatter]] | [[en/2-formatting/13-special/arrows-and-emoji\|Arrows, tags and emoji]] |
| An image has either a size or an alt text, not both | set the size via [[en/7-reference/01-glossary#HTML\|HTML]] when both are needed | [[en/2-formatting/12-media/images\|Images]] |
| An embedded PDF always starts on page 1 | use the page anchor in a link only | [[en/2-formatting/12-media/documents\|Documents]] |
| Definition lists do not exist | an HTML list `<dl>` | [[en/2-formatting/13-special/html\|HTML in Markdown]] |
| [[en/7-reference/01-glossary#Mermaid\|Mermaid]] ignores almost all of the template's colours; every rule of your own needs `!important` | the bundled [[en/7-reference/01-glossary#Stylesheet\|stylesheet]], which does exactly that | [[en/6-adapting/01-changing-something\|6.1 Changing something]] |

## Bases, canvas, drawings

| Limit | Instead | Where |
| --- | --- | --- |
| [[en/7-reference/01-glossary#Base\|Bases]] speak English: “Showing 45 of 45 entries” and the column headings come from the plugin and cannot be translated | the line is set quietly instead of removed | [[en/3-obsidian-formats/01-bases/index\|3.1 Bases]] |
| A base cannot group by a formula | group by a frontmatter field | [[en/3-obsidian-formats/01-bases/how-it-works\|How a base is built]] |
| Links in a [[en/7-reference/01-glossary#Canvas\|canvas]] file node get the folder prepended once more and, depending on the note's depth, lead nowhere — a bug in the plugin | choose nodes from the second or third level; otherwise click the node's title | [[en/3-obsidian-formats/02-canvas/index\|3.2 Canvas]] |
| A `.base` or `.canvas` file has no frontmatter and cannot link a translation | the switcher offers the other language's home page | [[en/6-adapting/07-two-languages/limits\|Where the two languages stop]] |
| An [[en/7-reference/01-glossary#Excalidraw\|Excalidraw]] page has neither sidebars nor a language switcher | — | [[en/3-obsidian-formats/03-excalidraw/index\|3.3 Excalidraw]] |

## Navigation and pages

| Limit | Instead | Where |
| --- | --- | --- |
| The [[en/7-reference/01-glossary#Explorer\|explorer]] starts folded; the option `folderDefaultState: open` is not read by the plugin | the folders on the way to the current page are open | [[en/5-design/01-navigation/explorer\|The explorer]] |
| The explorer sorts by title, not by file name, and the sort cannot be changed from the configuration | numbers in the title | [[en/5-design/01-navigation/explorer\|The explorer]] |
| The explorer cannot be filtered by language from the configuration | a stylesheet hides the other language's branch | [[en/6-adapting/07-two-languages/limits\|Where the two languages stop]] |
| The interface — explorer, search, [[en/7-reference/01-glossary#Backlinks\|backlinks]], [[en/7-reference/01-glossary#Graph\|graph]] — speaks one language site-wide; search, graph and “Recently changed” mix both languages; there is one error page for both | the [[en/7-reference/01-glossary#Layout box\|layout boxes]] speak both languages; one [[en/7-reference/01-glossary#Build\|build]] per language would solve the rest | [[en/6-adapting/07-two-languages/limits\|Where the two languages stop]] |
| Quartz renders no skip link; by keyboard the way to the text costs one tab stop per tree row | the styling for it lies ready | [[en/6-adapting/06-accessibility\|6.6 Accessibility]] |
| A page's date does not come from [[en/7-reference/01-glossary#git\|git]] because `content/` is a [[en/7-reference/01-glossary#Symlink\|symlink]] — a bug in the plugin | date in the frontmatter | [[en/4-controlling-a-page/01-title-description-date\|4.1 Title, description, date]] |

## In QuartzControl

| Limit | Instead | Where |
| --- | --- | --- |
| Only one of the five layout boxes survives the import of a template | create the other four anew | [[en/6-adapting/08-the-template-package\|6.8 The template package]] |
| A template package carries no images and no snippet files | inline HTML and inline SVG; copy one file by hand | [[en/6-adapting/08-the-template-package\|6.8 The template package]] |
| The part Translations does not reach the components' headings | — | [[en/6-adapting/08-the-template-package\|6.8 The template package]] |
| [[en/7-reference/01-glossary#Snapshot\|Snapshots]] do not contain the content when `content/` is a symlink | the [[en/7-reference/01-glossary#Vault\|vault]] backs itself up through its own git | [[en/1-getting-started/03-from-note-to-website\|1.3 From note to website]] |
| The app writes `@font-face` rules without weight and style | the rules are corrected by hand | [[en/6-adapting/03-typefaces\|6.3 Typefaces]] |
| In the [[en/7-reference/01-glossary#Frame\|frame]] editor a value may not contain a comma, and lengths stand as numbers, not as variables | `calc()` without a comma; numbers | [[en/6-adapting/05-page-grids\|6.5 Page grids]] |
| Three blocks in `custom.scss` are rewritten by the app on every save | your own rules outside the markers or in a file of your own | [[en/6-adapting/01-changing-something\|6.1 Changing something]] |
