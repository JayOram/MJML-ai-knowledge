---
type: Component
title: mj-button
description: A bulletproof call-to-action button; an ending tag whose inner area is the clickable link.
resource: https://documentation.mjml.io/#mj-button
tags: [mjml, content, cta, button, ending-tag]
timestamp: 2026-06-18T00:00:00Z
---

# mj-button

A customisable CTA that compiles to a client-hardened table+anchor structure. It is an [ending tag](/concepts/ending-tags.md).

**Only the inner text area is clickable**, due to email client support — do not rely on an edge-to-edge tap target. For a truly full-bleed clickable block, give an [mj-image](/components/mj-image.md) (or wrap the column content) an `href` instead.

## Key attributes

`href`, `align` (`center`), `background-color` (`#414141`), `color` (`#ffffff`), `border` / `border-radius` (`3px`), `font-family`, `font-size` (`13px`), `inner-padding` (`10px 25px`), `padding` (`10px 25px`), `width`, `height`, `target` (`_blank`), `text-transform`, `container-background-color`.

```xml
<mj-button href="https://example.com" background-color="#1a73e8">
  Read more
</mj-button>
```
