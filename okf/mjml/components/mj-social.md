---
type: Component
title: mj-social
description: A row of social-network share buttons composed of mj-social-element children.
resource: https://documentation.mjml.io/#mj-social
tags: [mjml, content, social]
timestamp: 2026-06-18T00:00:00Z
---

# mj-social

Renders calls-to-action for social networks. Add one `mj-social-element` per network. `mj-social-element` is an [ending tag](/concepts/ending-tags.md).

## Key attributes

On `mj-social`: `mode` (`horizontal`/`vertical`, default `horizontal`), `icon-size` (`20px`), `border-radius` (`3px`), `align` (`center`), `font-*`, `padding` (`10px 25px`). On `mj-social-element`: `name`, `href`, `src`, `background-color` (per-network default), `icon-size`, `alt`, `target`.

## Networks

With a share URL: `facebook`, `twitter`, `x`, `google`, `pinterest`, `linkedin`, `tumblr`, `xing`. Without: `github`, `instagram`, `web`, `snapchat`, `youtube`, `vimeo`, `medium`, `soundcloud`, `dribbble`. Append `-noshare` (e.g. `twitter-noshare`) to keep `href` unchanged.

```xml
<mj-social mode="horizontal" icon-size="30px">
  <mj-social-element name="facebook" href="https://example.com/">Facebook</mj-social-element>
  <mj-social-element name="x" href="https://example.com/">X</mj-social-element>
</mj-social>
```

**Caution:** the `name` shortcut pulls Mailjet-hosted icons. For production, supply your own `src` rather than depending on those assets.
