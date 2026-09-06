---
title: 6.1 Changing something
description: Three levels, cheapest first — and where your own rule belongs so that it wins.
section: Adapting
tags:
  - adapting
translationKey: anpassen/etwas-aendern
---

This template is built to be changed. There are three levels for it, and the first one is enough
more often than you would think.

## 1 · A variable

**The normal case.** 53 variables carry every colour and every measure of this template; not a line
of CSS is needed for them. In the app under *Styles → Variables*, separated into light and dark.

Which variable applies where stands at the bottom of every page in [[en/5-design/index|chapter 5]] — including the
column that says what else moves with it. Touching `--tpl-space-md` moves the whole site;
`--tpl-fade` moves two soft edges.

## 2 · A rule in an existing stylesheet

When a variable is not enough because it is not the value but the shape: the 30 stylesheets sit
under *Styles → Custom CSS*, **one per component**. Which one belongs to a component stands in the
same table at the bottom of its page.

That changes the template itself. Importing a template package again can overwrite it — for a
change meant to last, the third way is the safer one.

## 3 · A stylesheet of your own

*Styles → Custom CSS → New file.* A newly created file is appended to the **end of the load order**,
and that is the point: at equal specificity the rule loaded last wins. What stands here beats the
whole template without having to take anything away from it.

> [!warning] `a11y.scss` is then no longer last either
> That one file sits last on purpose: its rules have to win over decisions made further up — an
> affordance that would only appear on [[en/7-reference/01-glossary#Hover|hover]], a state that would hang on a colour alone. A file of
> your own lands behind it. If something to do with keyboard, [[en/7-reference/01-glossary#Contrast|contrast]] or print disappears after a
> change, that is the first place to look.

## The exception: diagrams

With [[en/7-reference/01-glossary#Mermaid|Mermaid]] none of the three ways works without `!important`. Quartz hands the diagram renderer
**nine** of its roughly hundred theme variables (`primaryColor`, `lineColor`, `secondaryColor` and
six more, hard-wired in Quartz's script). Everything else Mermaid colours itself — and writes as a
`<style>` carrying that SVG's own id into the graphic, an ID selector no class rule can beat.

That is why `body-mermaid.scss` holds 122 `!important` — and why your own rule needs one too. For
comparison: the other 29 stylesheets together hold twenty, each with its reason beside it.

## What not to touch

`custom.scss` holds three blocks between markers (`imports`, `fonts`, `css-vars`). The app rewrites
those on every save — whatever you enter there by hand is gone with the next click. The text outside
the markers stays.
