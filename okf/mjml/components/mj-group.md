---
type: Component
title: mj-group
description: Keeps adjacent columns side-by-side on mobile instead of stacking.
resource: https://documentation.mjml.io/#mj-group
tags: [mjml, structural, responsive, mobile]
timestamp: 2026-06-18T00:00:00Z
---

# mj-group

By default, [columns](/components/mj-column.md) stack vertically on mobile. Wrapping them in `mj-group` keeps them horizontal on mobile too — useful for small side-by-side items like an icon row.

**Columns inside a group must use percentage widths, not pixels** (see the [layout model](/concepts/layout-model.md)). Both [mj-column](/components/mj-column.md) and `mj-group` can sit inside an [mj-section](/components/mj-section.md).

```xml
<mj-section>
  <mj-group>
    <mj-column width="50%"><!-- stays left on mobile --></mj-column>
    <mj-column width="50%"><!-- stays right on mobile --></mj-column>
  </mj-group>
</mj-section>
```
