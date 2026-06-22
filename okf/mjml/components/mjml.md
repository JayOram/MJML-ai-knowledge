---
type: Component
title: mjml (root)
description: The root element of an MJML document; contains only mj-head and mj-body.
resource: https://documentation.mjml.io/#mjml
tags: [mjml, structural, root]
timestamp: 2026-06-18T00:00:00Z
---

# mjml

Every document begins with `<mjml>`. It may contain only [mj-head](/components/mj-head.md) and [mj-body](/components/mj-body.md), mirroring `<head>`/`<body>` in HTML.

```xml
<mjml>
  <mj-head><!-- … --></mj-head>
  <mj-body><!-- … --></mj-body>
</mjml>
```

## Key attributes

- `lang` — adds a `lang` attribute to the `html` and body `div` (default `und`).
- `dir` — adds a `dir` attribute (default `auto`).
- `owa` — set to `desktop` to force the desktop layout for older self-hosted Outlook.com that lacks media-query support.

An [mj-raw](/components/mj-raw.md) with `position="file-start"` may sit directly inside `mjml`, outside head and body, to inject content before `<!doctype html>`.
