---
type: Concept
title: What Changed in MJML 5
description: Behavioural differences between MJML 4 and MJML 5 that most often cause templates or build pipelines to break.
resource: https://documentation.mjml.io/#mj-include
tags: [mjml, versioning, migration, breaking-changes]
timestamp: 2026-06-18T00:00:00Z
---

# What Changed in MJML 5

These are the v4 → v5 changes that most often surprise people. When a template "worked before," check these first.

## Includes are disabled by default

[mj-include](/components/mj-include.md) tags are **silently ignored** unless explicitly enabled. If included content is missing from the output, includes are off, not broken.

- CLI: `--config.allowIncludes true`
- Node: `ignoreIncludes: false`

Includes are also sandboxed: allowed folders are scoped via `includePath` (resolved against `filePath`), and absolute paths or `..` escapes outside those roots are rejected. See [the Node API](/tooling/node-api.md) and [the CLI](/tooling/cli.md).

## CSS minification key renamed

The minify option `minifyCSS` became `minifyCss`. The legacy key still maps through for compatibility, but new code should use `minifyCss`, which accepts `false`, `"lite"`, `"default"`, or a cssnano preset object. See [the CLI](/tooling/cli.md).

## Related

- [Tooling index](/tooling/index.md)
- [Validation](/tooling/validation.md)
