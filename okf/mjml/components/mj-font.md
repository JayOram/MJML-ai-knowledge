---
type: Component
title: mj-font
description: Imports an external web font from a hosted CSS file, injected only if the font is used.
resource: https://documentation.mjml.io/#mj-font
tags: [mjml, head, fonts, typography]
timestamp: 2026-06-18T00:00:00Z
---

# mj-font

Imports an external font. `href` must point to a hosted CSS file containing an `@font-face` declaration (e.g. a Google Fonts URL). The import is only added to the output **if the template actually uses the font**.

## Attributes

- `name` — the font-family name to reference elsewhere.
- `href` — URL of the hosted CSS file.

```xml
<mj-head>
  <mj-font name="Raleway" href="https://fonts.googleapis.com/css?family=Raleway" />
</mj-head>
<!-- then: <mj-text font-family="Raleway, Arial">…</mj-text> -->
```

Always provide a web-safe fallback in `font-family` for clients that block remote fonts. Set it globally via [mj-attributes](/components/mj-attributes.md).
