---
title: 6.2 – Colours and contrast
description: Nine roles, two of them named the wrong way round — and 93 measured pairs.
section: 6 – Adapting
tags:
  - adapting
translationKey: anpassen/farben-und-kontrast
---

## The nine roles

Quartz names its palette by role. **Two of them read backwards:** `light` is the *background*,
`dark` the *text* — in dark mode too, where `light` is nearly black. Anyone who misses that [[en/7-reference/01-glossary#Build|builds]]
their first dark [[en/7-reference/01-glossary#Colour scheme|colour scheme]] inside out.

| Role | What for | light | dark |
| --- | --- | --- | --- |
| `light` | page ground | `#FCFCFA` | `#16171A` |
| `lightgray` | lines, cards, code blocks | `#DDDDDD` | `#2E2E2E` |
| `gray` | secondary text **and every border of a control** | `#5F5F5F` | `#A1A1A1` |
| `darkgray` | body text | `#333333` | `#DDDDDD` |
| `dark` | headings | `#17171A` | `#FCFCFA` |
| `secondary` | links, the one accent | `#1463A3` | `#699DC3` |
| `tertiary` | link [[en/7-reference/01-glossary#Hover\|hover]], active navigation | `#196B6B` | `#2CAFAD` |
| `highlight` | tinted surface | 10 % accent | 12 % accent |
| `textHighlight` | `==highlight==` | warm yellow, 55 % | accent, 30 % |

The two accents are deliberately **two different colours** and not two brightnesses of the same
one. `tertiary` marks what is being touched or is currently active; if it were only a darker
variant of `secondary`, you would not be able to tell from the result which of the two roles is
taking effect. A clear mid blue and a dark teal answer that question at a glance — close enough
that the site has one colour family, far enough apart that the change is visible.

Both measure themselves against **every** ground they occur on, not only against the page ground:
6.11:1 and 6.09:1 on the page, 4.62:1 and 4.61:1 on a card. The second value is the one that gets
missed — a link inside a [[en/7-reference/01-glossary#Callout|callout]] or a code caption sits on exactly that surface.

## What is measured

**93 pairs**, on every run: every text-on-ground combination in both modes, the alpha colours
computed over the ground, all thirteen [[en/7-reference/01-glossary#Callout|callout]] colours against the ground *and* against their own
tinted surface, and since 2026-09-05 the five corrected colours of the syntax theme against the code
block's surface. The tightest value is 4.61:1 against a threshold of 4.5 — the hovered link on a
card, and that is exactly what `tertiary` was darkened once more for on 2026-09-09.

The three checks read their values from different files but on the same principle: from
`palette.mjs`, from `body-callouts.scss` and from `body-code.scss` — always from what ships, never
from a second list that can be forgotten.

## The one exception, and where it leads

`lightgray` reaches only 1.32:1 against the ground. That is deliberate: it is a separating line
*and* a surface at once, and WCAG 1.4.11 asks 3:1 of *controls*, not of a decorative line. Raising
it to 3:1 would turn every code block mid-grey.

The obligation does not disappear, it moves: **everything you operate takes its border from
`gray`.** That is done through three variables that were pulled from `lightgray` over to `gray` —
`--background-modifier-border` and its like.

**Out of the box** Quartz checks none of this; the palette it ships fails in several places, most
clearly with the callout colours.
