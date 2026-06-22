---
type: Component
title: mj-style
description: Injects CSS into the document head, optionally inlining it.
resource: https://documentation.mjml.io/#mj-style
tags: [mjml, head, css, styling]
timestamp: 2026-06-18T00:00:00Z
---

# mj-style

Adds CSS that is applied to the rendered HTML. By default rules go into the `<head>`; `inline="inline"` inlines them (needed for properties many clients strip from `<head>`).

Because one MJML tag emits several HTML tags, a `css-class` lands on the **outermost** generated element. To target a child, inspect the compiled HTML to find the right selector. This differs from [mj-attributes](/components/mj-attributes.md), which sets MJML attributes rather than raw CSS.

```xml
<mj-head>
  <mj-style inline="inline">
    .brand-link a { color: #1a73e8 !important; }
  </mj-style>
</mj-head>
```
