---
title: 1.1 What this template is
description: A design for Quartz sites that you import into QuartzControl — and the three decisions it is made of.
section: Getting started
tags:
  - getting-started
translationKey: einstieg/was-diese-vorlage-ist
---

**Example** is a template for QuartzControl. A template here is a *design*: colours, typefaces,
spacing, the page grid, the arrangement of the components, the settings of the [[en/7-reference/01-glossary#Plugin|plugins]] —
everything that makes a website, except its content. It travels as one file with the extension
`.qtpl` and is imported into a project of your own in the app under *Templates*. After that your
own site looks like this one, with your own notes in it.

The template is meant to be used **and** to be rebuilt. Nothing about it is hidden: every colour
and every measure is a variable you can change in the app. Every [[en/7-reference/01-glossary#Stylesheet|stylesheet]] — the file in which the
look of a component is described — belongs to exactly one component and is named after it.

## Why this site exists

A design cannot be looked at in the abstract. An [[en/7-reference/01-glossary#Explorer|explorer]] needs folders, a table of contents needs
headings, a [[en/7-reference/01-glossary#Graph|graph]] needs links, a table needs rows. This site supplies all of it: it is the
template's handbook and its demonstration at the same time. Every element Obsidian can write
appears here at least once — and whoever wants to check an adaptation of their own finds here the
page on which the difference shows.

## The three decisions

Everything else follows from these three.

### 1. The width decides the grid

The page grid — called a *[[en/7-reference/01-glossary#Frame|frame]]* in Quartz — divides the page into twelve equally wide columns and
gives the text six of them. How wide a line of text gets is thereby decided, in exactly one place.
There is no second limit on the paragraph that could fall out with the first. What that means for
tablet and phone stands under [[en/6-adapting/05-page-grids|6.5 Page grids]].

### 2. Colours are measured

[[en/7-reference/01-glossary#Contrast|Contrast]] is the ratio of brightness between text and ground. The guideline for accessible
websites, [[en/7-reference/01-glossary#WCAG|WCAG]], demands at least 4.5:1 for normal text. This template measures 89 colour pairs in
light and dark on every run — every text-on-ground combination, the thirteen [[en/7-reference/01-glossary#Callout|callout]] colours, the
colours of the code syntax theme — and stops if one of them falls below. Quartz's own colours do
not pass this check: eleven of the twelve callout colours fail in light mode. That is why they are
restated here. More under [[en/6-adapting/02-colours-and-contrast|6.2 Colours and contrast]].

### 3. No stylesheet sets a colour or a measure itself

Colours and measures stand in 53 variables, not in the stylesheets. That is not cosmetics: after
the import, variables stay editable in the app under *Styles → Variables*; a value that stands in
a stylesheet file does not. What does stand as a number in a file is named and justified — the
callout and syntax colours, because they mean a status and are not a palette; the hairlines; and
the [[en/7-reference/01-glossary#Breakpoint|breakpoints]], because a [[en/7-reference/01-glossary#Media query|media query]] cannot read a variable. More under
[[en/6-adapting/04-variables|6.4 Variables]].

## What the template does not contain

**No content.** The notes of this site do not travel with the template; they live in an Obsidian
[[en/7-reference/01-glossary#Vault|vault]] of their own. Whoever imports the template gets the design and writes their own pages into
it.

**No images and no snippet files.** A template package carries stylesheets and font files, no
other files. What that means for the one [[en/7-reference/01-glossary#Layout box|layout box]] that reads from a file stands under
[[en/6-adapting/08-the-template-package|6.8 The template package]].
