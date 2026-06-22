---
type: Component
title: mj-column
description: A responsive cell inside a section; the unit of responsiveness that stacks on mobile.
resource: https://documentation.mjml.io/#mj-column
tags: [mjml, structural, layout, responsive]
timestamp: 2026-06-18T00:00:00Z
---

# mj-column

Columns organise a [section](/components/mj-section.md)'s content and **stack vertically on mobile**. They must live inside a section, must contain something, and **cannot contain other columns or sections**.

## Sizing

With no `width`, a section divides evenly across its columns (2 → 50% each, 3 → 33%, 4 → 25%). Set `width` in px or % to size manually; the sum across a section must be ≤ 100%. Every component inside a column fills 100% of the column — columns are containers, not offset tools. Inside an [mj-group](/components/mj-group.md), widths must be percentages.

## Key attributes

- `width`, `vertical-align` (`top`/`middle`/`bottom`; `middle` only applies when all columns use it).
- `background-color`, `border` / `border-radius`.
- `inner-background-color`, `inner-border*` — require a `padding` to take effect.
- `padding`, `css-class`.

```xml
<mj-section>
  <mj-column width="200px"><!-- fixed --></mj-column>
  <mj-column width="400px"><!-- fixed --></mj-column>
</mj-section>
```
