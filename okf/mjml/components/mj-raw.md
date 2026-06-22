---
type: Component
title: mj-raw
description: An escape hatch for arbitrary HTML that the MJML engine does not parse; an ending tag.
resource: https://documentation.mjml.io/#mj-raw
tags: [mjml, content, raw-html, templating, ending-tag]
timestamp: 2026-06-18T00:00:00Z
---

# mj-raw

Outputs raw, unparsed HTML — your responsibility to keep it responsive. It is an [ending tag](/concepts/ending-tags.md). Inside [mj-head](/components/mj-head.md), its content is appended to the HTML `<head>`. Inside [mjml](/components/mjml.md) (outside head and body) with `position="file-start"`, it is injected before `<!doctype html>`.

## Templating languages

`mj-raw` is the usual home for Handlebars/Liquid/AMPscript blocks. When using the `minify` option, a `<` in a template expression can cause a parsing error — wrap fragile fragments in `<!-- htmlmin:ignore --> … <!-- htmlmin:ignore -->` so the minifier leaves them alone. See [validation](/tooling/validation.md) and [the CLI](/tooling/cli.md).

```xml
<mj-raw>
  <!-- htmlmin:ignore --> {% if total < 5 %} <!-- htmlmin:ignore -->
</mj-raw>
```
