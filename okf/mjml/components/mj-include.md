---
type: Component
title: mj-include
description: Includes external .mjml, .css, or .html partials. Disabled by default in MJML 5.
resource: https://documentation.mjml.io/#mj-include
tags: [mjml, head, partials, includes, security]
timestamp: 2026-06-18T00:00:00Z
---

# mj-include

Pulls external files into a template to share headers, footers, and styles. **In MJML 5, includes are disabled by default and silently ignored** — see [MJML 5 changes](/concepts/mjml-5-changes.md). Enable with `ignoreIncludes: false` (Node) or `--config.allowIncludes true` (CLI).

## File types

- `.mjml` — default; inserted as MJML before rendering.
- `.css` — `type="css"`; behaves like [mj-style](/components/mj-style.md). Add `css-inline="inline"` to inline it.
- `.html` — `type="html"`; behaves like [mj-raw](/components/mj-raw.md).

## Security / sandboxing

Allowed folders are scoped via `includePath` (a string or array, resolved against `filePath`). Absolute paths, UNC paths, drive letters, null bytes, and `..` escapes outside the allowed roots are rejected; symlinks are followed and must resolve inside the roots. Best practice: set `filePath` to your templates root and use base-relative includes (`./_common/header.mjml`), or allowlist sibling folders via `includePath`.

```xml
<mj-body>
  <mj-include path="./_common/header.mjml" />
  <mj-include path="./styles.css" type="css" css-inline="inline" />
</mj-body>
```

See [the CLI](/tooling/cli.md) and [the Node API](/tooling/node-api.md) for enabling and scoping includes.
