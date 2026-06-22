---
type: Component
title: mj-wrapper
description: Wraps multiple sections so they share a background, border, or padding and behave as a single block.
resource: https://documentation.mjml.io/#mj-wrapper
tags: [mjml, structural, layout]
timestamp: 2026-06-18T00:00:00Z
---

# mj-wrapper

Because [sections cannot nest](/concepts/layout-model.md), `mj-wrapper` is how you treat several [mj-section](/components/mj-section.md)s as one unit — for example a bordered "card" containing a header section, a body section, and a footer section.

It accepts the same background, border, padding, and `full-width` attributes as [mj-section](/components/mj-section.md).

```xml
<mj-wrapper background-color="#ffffff" border="1px solid #e0e0e0" padding="0">
  <mj-section><mj-column><!-- header --></mj-column></mj-section>
  <mj-section><mj-column><!-- body --></mj-column></mj-section>
</mj-wrapper>
```
