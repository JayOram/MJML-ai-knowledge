---
type: Component
title: mj-section
description: A row in the email layout; contains columns and carries backgrounds, borders, and padding.
resource: https://documentation.mjml.io/#mj-section
tags: [mjml, structural, layout, outlook]
timestamp: 2026-06-18T00:00:00Z
---

# mj-section

Sections are the rows that structure the layout. They contain [mj-column](/components/mj-column.md) (or [mj-group](/components/mj-group.md)) and **cannot be nested** in other sections — use [mj-wrapper](/components/mj-wrapper.md) to group sections.

## Key attributes

- `full-width="full-width"` — the background spans the viewport edge-to-edge while content stays at body width.
- `background-color`, `background-url`, `background-size`, `background-position`, `background-repeat`.
- `border` / `border-radius`, `padding` (default `20px 0`), `text-align` (default `center`).
- `direction="rtl"` — reverses the desktop display order of columns (author them in mobile order first).

## Outlook background caveat

In Outlook desktop, if `background-size` is omitted, `no-repeat` is ignored; a single percentage `background-size` makes the image shrink to fit rather than crop. **Always set `background-size`, `background-position`, and `background-repeat` explicitly** when a section has a background image. For full background banners with overlaid text, prefer [mj-hero](/components/mj-hero.md).

```xml
<mj-section background-color="#ffffff" padding="24px">
  <mj-column><!-- content --></mj-column>
</mj-section>
```
