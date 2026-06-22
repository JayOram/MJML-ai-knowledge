---
type: Reference
title: MJML Node API
description: Programmatic compilation via mjml2html(input, options), returning html and errors.
resource: https://documentation.mjml.io/#inside-node-js
tags: [mjml, tooling, nodejs, api]
timestamp: 2026-06-18T00:00:00Z
---

# MJML Node API

`mjml2html(input, options)` compiles an MJML string and returns `{ html, errors }`.

```js
import mjml2html from 'mjml'

const { html, errors } = await mjml2html(mjmlSource, {
  validationLevel: 'soft',   // 'strict' throws on invalid markup
  minify: false,
  beautify: false,
  ignoreIncludes: false,     // enable mj-include (off by default in v5)
  filePath: '/project/templates/email.mjml',
  includePath: ['/project/templates/_common'],
})
```

## Key options

- `validationLevel` — `strict` | `soft` | `skip`. See [validation](/tooling/validation.md).
- `ignoreIncludes` — `false` to process [mj-include](/components/mj-include.md); scope with `filePath` + `includePath`.
- `minify` / `minifyOptions` — `minifyOptions.minifyCss` can be `false`, `"lite"`, `"default"`, or a cssnano preset (`minifyCss` replaced `minifyCSS` in v5).
- `keepComments`, `preprocessors` (array of `(xml) => xml`), `fonts`.

Always surface the `errors` array to the user — each entry pinpoints the offending tag and line.
