---
title: 4.4 Custom fields
description: Frontmatter fields Quartz does not know — and how the property table shows them.
section: 4 Controlling a page
date: 2026-07-02
lastmod: 2026-09-01
tags:
  - controlling-a-page
  - frontmatter
aliases:
  - Frontmatter example
number: 42
truthy: true
falsy: false
list:
  - one
  - two
  - three
empty:
translationKey: seiten-steuern/eigene-felder
---

A [[en/7-reference/01-glossary#Frontmatter|frontmatter]] may contain fields Quartz does not know. They do no harm, and they are useful:
Obsidian can search and sort by them, a [[en/7-reference/01-glossary#Base|base]] can filter by them, and the [[en/7-reference/01-glossary#Plugin|plugin]] *Note properties*
shows them in a table under the title — as at the top of this page.

## What this page carries

It has more frontmatter than is displayed. The template lists thirteen fields on the plugin under
`includedProperties`: `description`, `tags` and `section`, which every page can have, plus the five
demo fields — `number`, `truthy`, `falsy`, `list`, `empty` — and the same five once more with
German names, because the German version of this page calls them so. A field a page does not have
gets no row; the table above therefore counts eight.

The five demo fields exist so that every kind of value appears once: a number, a yes, a no, a
list, an empty field. How the table shows each of them differently stands in
[[en/5-design/02-above-the-content/properties|The property table]].

`aliases` and `translationKey` are not displayed: both are machinery and would stand on almost
every page.

## `section` — this site's own field

Every page here carries `section` with the name of its chapter. Quartz does not know the field. It
appears in the property table, the base [[en/7-reference/All pages.base|All pages]] groups by it,
and a [[en/7-reference/01-glossary#Layout box|layout box]] could insert it as the placeholder `{{frontmatter.section}}`.

## Showing all fields

Whoever wants to see all fields sets the option `includeAll` to true in QuartzControl under
*Plugins → Note properties*. Then [[en/7-reference/01-glossary#Alias|aliases]] and translation keys appear as well.

How to *write* fields and which data types there are:
[[en/2-formatting/11-properties/index|2.11 Properties]].
