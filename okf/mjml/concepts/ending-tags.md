---
type: Concept
title: Ending Tags
description: The MJML components that may contain raw HTML but not other MJML components, and the practical consequences for authoring.
resource: https://documentation.mjml.io/#ending-tags
tags: [mjml, components, html]
timestamp: 2026-06-18T00:00:00Z
---

# Ending Tags

An **ending tag** is a component that may contain raw HTML but **not** other MJML components. The set is:

- [mj-text](/components/mj-text.md)
- [mj-button](/components/mj-button.md)
- [mj-raw](/components/mj-raw.md)
- `mj-table`
- `mj-social-element` (inside [mj-social](/components/mj-social.md))
- `mj-navbar-link`
- `mj-accordion-title`, `mj-accordion-text`
- `mj-carousel-image`

## Practical consequence

Rich formatting goes *inside* an ending tag as ordinary HTML, not as more `mj-*` tags. A button cannot be nested inside text — close the text and add a sibling button in the same [mj-column](/components/mj-column.md):

```xml
<mj-text>
  <h1>Title</h1>
  <p>Paragraph with a <a href="#">link</a> and <strong>bold</strong>.</p>
</mj-text>
<mj-button href="#">Sibling button, not nested</mj-button>
```

Trying to place an MJML component inside an ending tag is a frequent structural error; see the [layout model](/concepts/layout-model.md).
