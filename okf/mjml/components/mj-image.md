---
type: Component
title: mj-image
description: A responsive image, analogous to the HTML img tag; fills the column width when no width is given.
resource: https://documentation.mjml.io/#mj-image
tags: [mjml, content, image, responsive]
timestamp: 2026-06-18T00:00:00Z
---

# mj-image

Displays a responsive image. With no `width`, it uses the parent [column](/components/mj-column.md) width.

## Key attributes

`src`, `alt`, `width`, `height`, `href` (+ `target`, default `_blank`), `align` (`center`), `border` / `border-radius`, `fluid-on-mobile` (full width on mobile if `true`), `max-height`, `sizes`, `srcset`, `container-background-color`, `padding` (`10px 25px`).

When a tag has no children, the XML self-closing form is valid: `<mj-image />`.

```xml
<mj-image width="300px" alt="Product" src="https://example.com/product.png" />
```

Because [mj-button](/components/mj-button.md) is only clickable on its inner area, a linked `mj-image` is the usual way to make a large clickable region.
