---
name: mjml
description: Author, compile, debug, and refactor MJML (Mailjet Markup Language) responsive email templates. Use this skill whenever the user is working with MJML — writing or editing .mjml files, building or fixing a responsive HTML email, using mj-* tags (mj-section, mj-column, mj-button, mj-hero, etc.), compiling MJML to HTML via the CLI or the mjml2html Node API, setting up shared partials with mj-include, or asking why an email renders wrong in Outlook/Gmail. Trigger it even when the user says "email template," "newsletter HTML," or "responsive email" without naming MJML explicitly, since MJML is usually the right tool and its layout rules are easy to get subtly wrong.
---

# MJML

MJML compiles a small set of semantic tags into responsive, client-compatible HTML email. You write `<mj-section>`/`<mj-column>` instead of nested tables and bulletproof-button hacks; the engine emits the ugly, well-tested HTML. The whole value proposition is that you stay at the layout level and never hand-write the table soup.

This skill assumes MJML 5 (the current major). Where v5 changed behavior from v4, it is called out — those changes are the most common source of "it worked before and now it doesn't."

## The mental model (internalize this first)

An MJML document is a strict, shallow hierarchy. Every tag has exactly one valid parent context, and most rendering bugs are a tag in the wrong slot.

```
mjml
├── mj-head        (optional: metadata, fonts, styles, default attributes)
└── mj-body        (width=600px by default)
    └── mj-wrapper (optional: groups multiple sections, e.g. a bordered card)
        └── mj-section          (a row)
            ├── mj-column        (a responsive cell — stacks on mobile)
            │   └── content      (mj-text, mj-image, mj-button, mj-divider, …)
            └── mj-group         (keeps columns side-by-side on mobile)
                └── mj-column
```

Five rules cover almost everything:

1. **Content lives in columns, never directly in a section.** `mj-text`, `mj-image`, `mj-button` etc. must sit inside an `mj-column`. A single-column row still needs the column.
2. **Columns live in sections.** `mj-column` outside an `mj-section` is ignored.
3. **Sections don't nest, and columns don't nest.** You cannot put an `mj-section` inside an `mj-column`, or an `mj-column` inside an `mj-column`. To get nested-looking layouts, use `mj-wrapper` (to stack sections) or `mj-group` (to keep columns together). This is the single most common structural mistake.
4. **Column widths in a section must sum to ≤ the section width (≤100%).** With no explicit `width`, the section splits evenly across its columns (2 columns → 50% each, 3 → 33%, 4 → 25%). Any component inside a column is 100% of that column's width — columns are containers, not offset/spacer tools.
5. **Columns inside an `mj-group` must use percentage widths, not pixels.** Pixel widths break grouping.

## Canonical starter template

When the user wants a fresh template, start from this and build outward. It is valid, accessible, and exercises the head/body split.

```xml
<mjml>
  <mj-head>
    <mj-title>Newsletter</mj-title>
    <mj-preview>One-line inbox preview text</mj-preview>
    <mj-attributes>
      <mj-all font-family="Helvetica, Arial, sans-serif" />
      <mj-text font-size="16px" line-height="24px" color="#222222" />
      <mj-class name="brand" color="#1a73e8" />
    </mj-attributes>
    <mj-style>
      .link-light a { color: #1a73e8 !important; }
    </mj-style>
  </mj-head>
  <mj-body background-color="#f4f4f4" width="600px">
    <mj-section background-color="#ffffff" padding="24px">
      <mj-column>
        <mj-image width="120px" src="https://example.com/logo.png" alt="Logo" />
        <mj-divider border-color="#e0e0e0" />
        <mj-text mj-class="brand" font-size="22px">Hello World</mj-text>
        <mj-text>Body copy goes here.</mj-text>
        <mj-button href="https://example.com" background-color="#1a73e8">Read more</mj-button>
      </mj-column>
    </mj-section>
  </mj-body>
</mjml>
```

## Ending tags (why you can't nest MJML in some places)

Some components are **ending tags**: they may contain raw HTML but **not** other MJML components. The set is `mj-text`, `mj-button`, `mj-table`, `mj-raw`, `mj-social-element`, `mj-navbar-link`, `mj-accordion-title`, `mj-accordion-text`, and `mj-carousel-image`.

Practical consequence: rich text formatting goes *inside* `mj-text` as ordinary HTML (`<h1>`, `<p>`, `<a>`, `<strong>`, inline `style`), not as more `mj-*` tags. Putting an `mj-button` inside an `mj-text` will not work — close the text and add a sibling `mj-button` in the same column.

```xml
<mj-text>
  <h1>Title</h1>
  <p>A paragraph with a <a href="#">link</a>.</p>
</mj-text>
<mj-button href="#">Sibling button, not nested</mj-button>
```

## Styling and default attributes (DRY templates)

Set defaults once in `mj-head` rather than repeating attributes on every tag. The cascade, highest priority first: **inline attribute on the tag → matching component tag inside `mj-attributes` → `mj-all` → MJML built-in default.**

- `mj-attributes` > `<mj-text padding="0" />` overrides the default for *every* `mj-text`.
- `mj-attributes` > `<mj-all font-family="…" />` sets a default for *all* components.
- `mj-attributes` > `<mj-class name="big" font-size="20px" />` defines a reusable group applied with `mj-class="big"` (space-separate to combine: `mj-class="big brand"`).
- `mj-style` holds real CSS for the `<head>`; add `inline="inline"` to inline it (needed for properties many clients strip from `<head>`). Because one MJML tag emits several HTML tags, `css-class` lands on the outermost element — inspect the compiled HTML to find the right child selector.

## Components at a glance

Reach for `references/components.md` for the full attribute tables. Quick index of what each tag is for:

**Layout:** `mj-wrapper` (stack sections as a unit), `mj-section` (row; `full-width="full-width"` makes the background span edge-to-edge while content stays 600px), `mj-column` (responsive cell), `mj-group` (lock columns side-by-side on mobile).

**Content:** `mj-text`, `mj-image` (responsive `<img>`; omit `width` to fill the column), `mj-button` (bulletproof CTA), `mj-divider`, `mj-spacer` (vertical gap), `mj-table` (raw HTML table for data), `mj-social` + `mj-social-element` (share rows), `mj-hero` (background-image banner; `background-width`/`background-height` are mandatory), `mj-accordion` (collapsible, Apple-Mail-only interactivity), `mj-carousel` (image gallery, limited client support), `mj-navbar` + `mj-navbar-link` (menu, optional hamburger on Apple Mail), `mj-raw` (escape hatch for arbitrary HTML).

**Head:** `mj-title`, `mj-preview`, `mj-attributes`, `mj-style`, `mj-font` (import a hosted `@font-face` CSS, only injected if used), `mj-breakpoint` (set the desktop↔mobile switch width), `mj-html-attributes` (inject attributes onto generated HTML via CSS selectors), `mj-include` (partials — see below).

## Shared partials with mj-include (changed in v5)

`mj-include` pulls in external `.mjml`, `.css` (`type="css"`, optionally `css-inline="inline"`), or `.html` (`type="html"`) files. **In MJML 5, includes are disabled by default and silently ignored.** If included content is missing from the output, the includes are off, not broken.

- CLI: add `--config.allowIncludes true`.
- Node: pass `ignoreIncludes: false`.
- Scope which folders are allowed with `includePath` (string or array), resolved against `filePath`. Absolute paths and `..` escapes outside the allowed roots are rejected. Set `filePath` to your templates root and write base-relative includes (`./_common/header.mjml`), or keep template-relative paths and allowlist sibling folders.

```xml
<mjml>
  <mj-body>
    <mj-include path="./_common/header.mjml" />
    <!-- sections -->
    <mj-include path="./_common/footer.mjml" />
  </mj-body>
</mjml>
```

## Compiling MJML → HTML

**CLI** (from `npm install mjml`):

```bash
mjml input.mjml -o output.html          # write to file
mjml input.mjml -s                       # write to stdout
mjml -w input.mjml                        # watch a file or folder
mjml input.mjml -o out.html --config.validationLevel strict --config.minify true
```

Useful `--config.*` flags: `allowIncludes`, `beautify` (default true in CLI), `minify` (default false), `minifyOptions` (`{"minifyCss": false | "lite" | "default" | <cssnano preset>}` — **`minifyCss` replaced the old `minifyCSS` key in v5**, though the old key still maps through), `validationLevel` (`strict` | `soft` | `skip`), `includePath`, `filePath`.

**Node API** — `mjml2html(input, options)` returns `{ html, errors }`:

```js
import mjml2html from 'mjml'

const { html, errors } = await mjml2html(mjmlSource, {
  validationLevel: 'soft',     // 'strict' throws on invalid markup
  minify: false,
  ignoreIncludes: false,       // enable mj-include
  filePath: '/project/templates/email.mjml',
  includePath: ['/project/templates/_common'],
})
```

Always surface `errors` to the user when compiling programmatically — they pinpoint the offending tag and line. There is also a hosted MJML API (mjml.io/api) for environments that can't run Node.

## Validation levels

The validator catches misplaced tags, unknown attributes, and broken structure before they become silently wrong HTML.

- `strict` — abort on any validation error. Best for CI and when generating templates you can't eyeball.
- `soft` (default) — collect errors but still produce output.
- `skip` — no validation (fastest; use only when you trust the input).

When writing or transforming MJML for someone, prefer compiling with `strict` (or at least reading the `errors` array) so structural mistakes surface immediately rather than rendering as a collapsed or duplicated layout.

## High-value gotchas

These are the things that waste the most time, drawn from real client-rendering behavior:

- **Outlook backgrounds.** On `mj-section`/`mj-hero`, if `background-size` is omitted, `no-repeat` is ignored in Outlook; a single percentage `background-size` makes the image shrink-to-fit rather than crop. Always set `background-size`, `background-position`, and `background-repeat` explicitly when a section has a background image.
- **`mj-button` is not fully clickable.** Only the text/inner area is the link, due to client support — don't promise an edge-to-edge tap target. For a true full-bleed clickable block, wrap an `mj-image` (or the whole column content) in an `href` instead.
- **`mj-hero` requires `background-width` and `background-height`**, and `height` is required only in `mode="fixed-height"`. Provide a `background-color` fallback for clients that drop the image.
- **Templating languages (Handlebars/Liquid/AMPscript) + `minify`.** A `<` in a template expression can trigger a parsing error during minification. Wrap fragile blocks in `<!-- htmlmin:ignore --> … <!-- htmlmin:ignore -->`, or keep them inside `mj-raw`. Use `mj-raw position="file-start"` to inject content before `<!doctype html>`.
- **Reverse column order without breaking mobile stacking.** Author columns in mobile (stacked) order, then add `direction="rtl"` to the `mj-section` to flip the desktop order.
- **Self-hosted Outlook.com / media-query-less clients.** `owa="desktop"` on the `mjml` tag forces the desktop layout for those clients.
- **Social icons.** `mj-social-element name="facebook"` is a convenience that pulls Mailjet-hosted icons; for production, supply your own `src` rather than depending on those assets. Append `-noshare` to a network name to stop MJML rewriting your `href` into a share URL.

## Working approach

When the user hands you MJML to fix, first locate the structural error against the five rules and the ending-tag list before touching styling — a "broken" email is far more often a column in the wrong place than a bad attribute. When building from scratch, sketch the section/column skeleton first, get it compiling clean under `strict`, then layer in content and head-level defaults. When the deliverable is the email itself, compile it and report the `errors` array rather than assuming the source is correct.

For exhaustive per-component attributes, defaults, and supported social networks, read `references/components.md`.
