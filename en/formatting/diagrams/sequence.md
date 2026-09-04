---
title: Sequence diagrams
description: Who says what to whom, and in which order.
section: Formatting
tags:
  - formatting
  - diagrams
translationKey: formatierung/diagramme/sequenz
layoutBoxNote: sidebar-note.en.md
layoutBoxHint:
  html: "<p>On a narrow screen the navigation is collapsed at the top.</p>"
layoutBoxCta:
  html: "<p>This page belongs to <a href=\"{{root}}/en/\">{{siteTitle}}</a> — the example template for QuartzControl. An overview of every area is on the <a href=\"{{root}}/en/\">English home page</a>.</p>"
layoutBoxColophon:
  html: "<p>{{siteTitle}} · Language: {{locale}} · This page: <code>{{slug}}</code></p>"
---

````md
```mermaid
sequenceDiagram
    User->>App: choose template
    App->>Package: preview (dry run)
    Package-->>App: ten parts
    App->>Project: create snapshot
    App->>Project: apply
    Project-->>User: done, no warnings
```
````

```mermaid
sequenceDiagram
    User->>App: choose template
    App->>Package: preview (dry run)
    Package-->>App: ten parts
    App->>Project: create snapshot
    App->>Project: apply
    Project-->>User: done, no warnings
```

The solid arrow `->>` is a call, the dashed `-->>` a reply.
