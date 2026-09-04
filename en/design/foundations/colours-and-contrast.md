---
title: Colours and contrast
description: Nine roles, two of them named the wrong way round — and 78 measured pairs.
section: Design
tags:
  - design
  - basics
translationKey: gestaltung/grundlagen/farben-und-kontrast
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

## The nine roles

Quartz names its palette by role. **Two of them read backwards:** `light` is the *background*,
`dark` the *text* — in dark mode too, where `light` is nearly black. Anyone who misses that builds
their first dark colour scheme inside out.

| Role | What for | light | dark |
| --- | --- | --- | --- |
| `light` | page ground | `#FCFCFA` | `#16171A` |
| `lightgray` | lines, cards, code blocks | `#DEDCD5` | `#2E3036` |
| `gray` | secondary text **and every border of a control** | `#5F5D57` | `#A1A3A8` |
| `darkgray` | body text | `#33322E` | `#D5D7DB` |
| `dark` | headings | `#17171A` | `#F3F4F6` |
| `secondary` | links, the one accent | `#2A4E6C` | `#8CB8DA` |
| `tertiary` | link hover, active navigation | `#9C4221` | `#E8A56B` |
| `highlight` | tinted surface | 10 % accent | 12 % accent |
| `textHighlight` | `==highlight==` | warm yellow | accent, 30 % |

The two accents are deliberately **two different colours** and not two brightnesses of the same
one. `tertiary` marks what is being touched or is currently active; if it were only a darker
variant of `secondary`, you would not be able to tell from the result which of the two roles is
taking effect. A deep navy and a warm sienna answer that question at a glance — and both measure
themselves against every ground they occur on (6.36:1 for sienna on the page ground, 4.76:1 on a
card).

## What is measured

**83 pairs**, on every run: every text-on-ground combination in both modes, the alpha colours
computed over the ground, all twelve callout colours against the ground *and* against their own
tinted surface, and since 2026-09-05 the five corrected colours of the syntax theme against the code
block's surface. The tightest value is 4.68:1 against a threshold of 4.5.

The three checks read their values from different files but on the same principle: from
`palette.mjs`, from `body-callouts.scss` and from `body-code.scss` — always from what ships, never
from a second list that can be forgotten.

## The one exception, and where it leads

`lightgray` reaches only 1.34:1 against the ground. That is deliberate: it is a separating line
*and* a surface at once, and WCAG 1.4.11 asks 3:1 of *controls*, not of a decorative line. Raising
it to 3:1 would turn every code block mid-grey.

The obligation does not disappear, it moves: **everything you operate takes its border from
`gray`.** That is done through three variables that were pulled from `lightgray` over to `gray` —
`--background-modifier-border` and its like.

**Out of the box** Quartz checks none of this; the palette it ships fails in several places, most
clearly with the callout colours.
