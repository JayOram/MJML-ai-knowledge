---
type: Component
title: mj-text
description: A styled text block that holds raw HTML; an ending tag.
resource: https://documentation.mjml.io/#mj-text
tags: [mjml, content, text, ending-tag]
timestamp: 2026-06-18T00:00:00Z
---

# mj-text

Displays styled text. It is an [ending tag](/concepts/ending-tags.md): put ordinary HTML (`<h1>`, `<p>`, `<a>`, `<strong>`, inline `style`) inside it, but never nested MJML components.

## Key attributes

`align` (default `left`), `color` (`#000000`), `font-family`, `font-size` (`13px`), `font-style`, `font-weight`, `line-height`, `letter-spacing`, `text-decoration`, `text-transform`, `container-background-color`, `padding` (`10px 25px`).

```xml
<mj-text font-size="16px" color="#222222">
  <h1>Title</h1>
  <p>Body copy with a <a href="#">link</a>.</p>
</mj-text>
```

Set shared text defaults once via [mj-attributes](/components/mj-attributes.md) rather than repeating them.
