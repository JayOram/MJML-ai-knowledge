---
type: Concept
title: The MJML Layout Model
description: MJML's strict shallow hierarchy (mjml → head/body → section → column → content) and the five rules that prevent most rendering bugs.
resource: https://documentation.mjml.io/#getting-started
tags: [mjml, layout, structure, responsive]
timestamp: 2026-06-18T00:00:00Z
---

# The Layout Model

An MJML document is a strict, shallow tree. Each tag has exactly one valid parent context, and the large majority of rendering bugs are a tag placed in the wrong context.

```
mjml
├── mj-head      (optional metadata, fonts, styles, defaults)
└── mj-body      (width = 600px by default)
    └── mj-wrapper        (optional — groups sections as one unit)
        └── mj-section    (a row)
            ├── mj-column (a responsive cell; stacks on mobile)
            │   └── content (mj-text, mj-image, mj-button, …)
            └── mj-group  (keeps columns side-by-side on mobile)
                └── mj-column
```

## The five rules

1. **Content lives in columns, never directly in a section.** Even a single-column row needs its [mj-column](/components/mj-column.md).
2. **Columns live in sections.** An [mj-column](/components/mj-column.md) outside an [mj-section](/components/mj-section.md) is ignored.
3. **Sections don't nest and columns don't nest.** Use [mj-wrapper](/components/mj-wrapper.md) to stack sections as a block, and [mj-group](/components/mj-group.md) to keep columns together. This is the most common structural mistake.
4. **Column widths in a section sum to ≤ 100% (or the section width).** With no `width`, the section divides evenly across columns. Any component inside a column fills 100% of that column — columns are containers, not spacers.
5. **Columns inside an [mj-group](/components/mj-group.md) must use percentage widths, not pixels.**

## Responsiveness

Columns are the unit of responsiveness: on mobile they stack vertically by default. Override the desktop↔mobile switch width with [mj-breakpoint](/components/mj-include.md). To stop columns stacking, wrap them in [mj-group](/components/mj-group.md). To reverse desktop column order without disturbing the stacked mobile order, author columns in mobile order and add `direction="rtl"` to the [mj-section](/components/mj-section.md).

## Related

- [Ending tags](/concepts/ending-tags.md) — why content components can't hold nested MJML.
- [mj-section](/components/mj-section.md), [mj-column](/components/mj-column.md), [mj-wrapper](/components/mj-wrapper.md), [mj-group](/components/mj-group.md).
