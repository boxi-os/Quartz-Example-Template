---
title: 7.3 Patterns
description: The decisions that run through every component — said once, instead of repeated on thirty pages.
section: 7 Reference
tags:
  - reference
  - terms
translationKey: nachschlagen/muster
---

Three decisions carry the whole template; they stand in
[[en/1-getting-started/01-what-this-template-is|1.1 What this template is]]. Below them, smaller
patterns repeat in every component. Whoever changes a component or designs a new one keeps to
these, so that it fits the rest.

## What is the same everywhere

1. **Sidebar headings** are small, capitalised and muted — they are labelling, not content. The
   same form stands in nine [[en/7-reference/01-glossary#Stylesheet|stylesheets]], and that is intended: every page in chapter 5 is to show
   its own table of variables in full.
2. **A state is never shown by colour alone.** The active entry in the [[en/7-reference/01-glossary#Explorer|explorer]] has colour, weight
   *and* a bar; a completed task item is muted *and* struck through; an external link is coloured
   differently *and* carries an arrow.
3. **Borders of controls** draw their colour from `--tpl-rule-control`, not from `--lightgray`.
   The faint tone is enough for a divider, but not for the border of something you operate — [[en/7-reference/01-glossary#WCAG|WCAG]]
   demands 3:1 there.
4. **Everything you tap is at least 44 px** (`--tpl-target`). WCAG demands 24; 44 is the size at
   which nobody has to aim.
5. **Two line heights, not one.** 1.65 for body text, 1.45 for everything in small type — the
   sidebars and the footer. The same spacing at a smaller size tears a paragraph into single lines.
6. **A hovered link** turns accent-coloured and underlined, with the underline set lower. The same
   gesture in seven stylesheets, the same value from one variable.
7. **All fold-out chevrons are the same chevron** from the Lucide set — in the explorer, in the
   table of contents, in the collapsible [[en/7-reference/01-glossary#Layout box|layout box]].
8. **What overflows scrolls within itself** and fades out softly at the edge instead of making the
   page longer: the explorer, the table of contents, a wide table, a code block.
9. **An area that really has no business at a given width is hidden; a column that merely happens
   to be empty stays**, so that the text column does not move.
10. **Nothing moves when the system does not want it to.** `prefers-reduced-motion` sets a single
    variable to zero, and every transition of the template follows it.

## What deliberately is not unified

The nine panel headings and the seven [[en/7-reference/01-glossary#Hover|hover]] rules could be pulled into one shared file. That would
be wrong here: the stylesheets are cut by component, and the documentation hangs on that — every
page in chapter 5 shows the variables *its* component reads. What is shared are the **values**, and
they are: `--tpl-tracking-label` and `--tpl-underline-offset` stand once each. In full in
[[en/6-adapting/04-variables|6.4 Variables]].
