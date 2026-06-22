---
type: Component
title: mj-attributes
description: Sets default attributes for components and defines reusable attribute classes; the mechanism for DRY templates.
resource: https://documentation.mjml.io/#mj-attributes
tags: [mjml, head, styling, defaults]
timestamp: 2026-06-18T00:00:00Z
---

# mj-attributes

Lives in [mj-head](/components/mj-head.md) and removes repetition. Three kinds of children:

- A component tag, e.g. `<mj-text padding="0" />`, overrides the default for **every** instance of that component.
- `<mj-all font-family="…" />` sets a default for **all** components.
- `<mj-class name="x" … />` defines a reusable attribute group, applied with `mj-class="x"` on a component. Combine groups by space-separating: `mj-class="big brand"`.

## The cascade

Highest priority first: **inline attribute on the tag → matching component tag in `mj-attributes` → `mj-all` → MJML built-in default.**

```xml
<mj-head>
  <mj-attributes>
    <mj-all font-family="Helvetica, Arial, sans-serif" />
    <mj-text font-size="16px" color="#222222" />
    <mj-class name="brand" color="#1a73e8" />
  </mj-attributes>
</mj-head>
```

For real CSS rules (as opposed to MJML attributes), use [mj-style](/components/mj-style.md).
