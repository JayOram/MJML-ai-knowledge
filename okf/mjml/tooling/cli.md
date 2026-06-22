---
type: Reference
title: MJML CLI
description: Command-line usage for compiling, watching, and configuring MJML output.
resource: https://documentation.mjml.io/#command-line-interface
tags: [mjml, tooling, cli, build]
timestamp: 2026-06-18T00:00:00Z
---

# MJML CLI

From `npm install mjml`:

```bash
mjml input.mjml -o output.html     # write to a file
mjml input.mjml -s                  # write to stdout
mjml -w input.mjml                   # watch a file or folder
```

## Useful --config flags

- `--config.allowIncludes true` — enable [mj-include](/components/mj-include.md) (off by default in v5).
- `--config.includePath` / `--config.filePath` — scope where includes may be read from.
- `--config.validationLevel` — `strict` | `soft` (default) | `skip`. See [validation](/tooling/validation.md).
- `--config.beautify` — pretty output (default `true` in CLI).
- `--config.minify` — minify (default `false`).
- `--config.minifyOptions` — e.g. `'{"minifyCss": false}'` or `"lite"` / `"default"` / a cssnano preset. **`minifyCss` replaced `minifyCSS` in v5** (legacy key still maps through).

```bash
mjml template.mjml -o out.html \
  --config.allowIncludes true \
  --config.includePath '["../_common","../vendor"]' \
  --config.validationLevel strict
```

See [MJML 5 changes](/concepts/mjml-5-changes.md) for the include and minify behaviour.
