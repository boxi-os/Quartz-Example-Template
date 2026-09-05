---
title: Callouts — the basic form
description: How a callout is built, with and without a title of its own.
section: Formatting
tags:
  - formatting
  - callouts
translationKey: formatierung/callouts/grundform
---

## With a title of your own

````md
> [!note] A title of your own
> The content of the callout.
````

> [!note] A title of your own
> The content of the callout.

## Without a title

Then the type stands as the title:

````md
> [!warning]
> Without a title of its own.
````

> [!warning]
> Without a title of its own.

## With any content

A callout can contain everything that works elsewhere:

````md
> [!example] With everything in it
>
> 1. A list
> 2. With two points
>
> | And | a table |
> | --- | ------- |
> | a   | b       |
>
> ```js
> const also = "code"
> ```
````

> [!example] With everything in it
>
> 1. A list
> 2. With two points
>
> | And | a table |
> | --- | ------- |
> | a   | b       |
>
> ```js
> const also = "code"
> ```

Further: [[en/formatting/callouts/all-types|all thirteen types]],
[[en/formatting/callouts/foldable|foldable]], [[en/formatting/callouts/nested|nested]].
