---
type: Component
title: mj-hero
description: A hero banner with a background image, behaving like a section with a single column.
resource: https://documentation.mjml.io/#mj-hero
tags: [mjml, content, hero, background-image]
timestamp: 2026-06-18T00:00:00Z
---

# mj-hero

Displays a hero image with overlaid content. It behaves like an [mj-section](/components/mj-section.md) containing a single [mj-column](/components/mj-column.md), and is the recommended way to put text over a full background image (more reliable than a section `background-url`).

## Key attributes

- `mode` — `fluid-height` (default) or `fixed-height`.
- `background-width` and `background-height` — **mandatory**. Use a `background-width` equal to the body width (600px) and a `background-height` ≥ the hero `height`.
- `height` — required only for `mode="fixed-height"`.
- `background-url`, `background-position` (`center center`), `background-color` — provide the color as a fallback for clients that drop the image.
- `padding`, `inner-padding`, `vertical-align`.

```xml
<mj-hero mode="fixed-height" height="469px"
         background-width="600px" background-height="469px"
         background-url="https://example.com/hero.jpg" background-color="#2a3448">
  <mj-text color="#ffffff" align="center" font-size="45px">GO TO SPACE</mj-text>
  <mj-button href="https://example.com/">Order now</mj-button>
</mj-hero>
```
