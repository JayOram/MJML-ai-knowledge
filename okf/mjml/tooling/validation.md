---
type: Reference
title: MJML Validation
description: The validator catches misplaced tags and unknown attributes; three levels trade safety for speed.
resource: https://documentation.mjml.io/#validating-mjml
tags: [mjml, tooling, validation, ci]
timestamp: 2026-06-18T00:00:00Z
---

# MJML Validation

The validator catches structural mistakes — a tag in the wrong context (see the [layout model](/concepts/layout-model.md)), unknown attributes, broken nesting — before they become silently wrong HTML.

## Levels

- `strict` — abort on any validation error. Best for CI and for machine-generated templates you won't eyeball.
- `soft` (default) — collect errors but still produce output.
- `skip` — no validation; fastest, for trusted input only.

Set the level via the [CLI](/tooling/cli.md) (`--config.validationLevel`) or the [Node API](/tooling/node-api.md) (`validationLevel`, or read the returned `errors`). When generating or transforming MJML on someone's behalf, prefer `strict` so structural errors surface immediately rather than rendering as a collapsed or duplicated layout.
