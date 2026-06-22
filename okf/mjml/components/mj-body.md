---
type: Component
title: mj-body
description: The root container for email content; sets overall width and injects accessibility wrappers.
resource: https://documentation.mjml.io/#mj-body
tags: [mjml, structural, accessibility]
timestamp: 2026-06-18T00:00:00Z
---

# mj-body

The starting point of the email. It automatically adds a child `div` with `role="article"`, `aria-roledescription="email"`, and `aria-label` taken from `mj-title`, plus the `lang`/`dir` from [mjml](/components/mjml.md). Contains [mj-section](/components/mj-section.md) (optionally wrapped in [mj-wrapper](/components/mj-wrapper.md)).

## Key attributes

- `width` — email width (default `600px`). This value seeds default column sizing.
- `background-color` — page background behind the sections.
- `css-class`, `id` — applied to the generated `body` tag.

```xml
<mj-body background-color="#f4f4f4" width="600px">
  <!-- sections -->
</mj-body>
```
