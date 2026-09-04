---
title: A page with an alias
description: Reachable under several paths — the Alias redirects plugin creates the forwarding pages.
section: Examples
tags:
  - examples
aliases:
  - Second name
  - en/examples/another-path
translationKey: beispiele/alias
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

This page can be reached under three paths: its own, `Second name` and
`en/examples/another-path`. The *Alias redirects* plugin builds a small forwarding page for every
alias.

Useful when a note has been renamed or moved and old links should keep working.
