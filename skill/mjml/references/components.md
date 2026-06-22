# MJML Component Reference

Full attribute tables for MJML 5 standard components. Source of truth: https://documentation.mjml.io/. Attributes marked *(ending tag)* may contain raw HTML but not nested MJML components.

Common conventions: padding attributes accept up to 4 values (`top right bottom left`) and have per-side variants (`padding-top`, etc.); `css-class` is supported by every body component and lands on the outermost generated element; color attributes accept any CSS color format.

## Contents
- [Root & document](#root--document)
- [Head components](#head-components)
- [Layout components](#layout-components)
- [Content components](#content-components)
- [Interactive components](#interactive-components)

---

## Root & document

### mjml
Root element. Contains only `mj-head` and `mj-body`.

| attribute | accepts | default | notes |
|---|---|---|---|
| owa | string | none | `desktop` forces desktop layout for old self-hosted Outlook.com |
| lang | string | und | adds `lang` to `html` and body `div` |
| dir | string | auto | adds `dir` to `html` and body `div` |

### mj-body
Email root container. Auto-adds an accessible `div` (`role="article"`, `aria-roledescription="email"`, `aria-label` from `mj-title`).

| attribute | accepts | default |
|---|---|---|
| background-color | color | — |
| width | px | 600px |
| css-class | string | — |
| id | string | — |

### mj-head
Container for head components (no attributes of its own).

---

## Head components

### mj-attributes
Holds default-attribute overrides. Children: a component tag (e.g. `<mj-text padding="0" />`) sets that component's default; `<mj-all … />` sets defaults for everything; `<mj-class name="x" … />` defines a reusable attribute group applied via `mj-class="x"`. Cascade: inline > `mj-attributes` component tag > `mj-all` > built-in default.

### mj-breakpoint
`<mj-breakpoint width="480px" />` — sets the width at which the layout switches between mobile and desktop.

### mj-font
`<mj-font name="Raleway" href="https://fonts.googleapis.com/css?family=Raleway" />` — `href` points to a hosted CSS file with an `@font-face` declaration. Only injected into output if the font is actually used.

### mj-preview
`<mj-preview>Inbox preview text</mj-preview>` — no attributes. Sets the hidden preheader.

### mj-title
`<mj-title>Document title</mj-title>` — populates `<title>` and the body `div`'s `aria-label`.

### mj-style
CSS for the `<head>`. `inline="inline"` inlines the rules (use `!important` and target generated child selectors as needed).

| attribute | accepts | default |
|---|---|---|
| inline | string | — (`inline` to inline) |

### mj-html-attributes
Injects arbitrary attributes onto generated HTML via CSS selectors. Structure: `mj-html-attributes` > `mj-selector path="<css selector>"` > `mj-html-attribute name="<attr>"`value`</mj-html-attribute>`. Niche; mostly for editable templates. Inspect compiled HTML to find selectors.

### mj-include
Pulls in external files. **Disabled by default in v5** (`ignoreIncludes: false` / `--config.allowIncludes true` to enable).

| attribute | accepts | notes |
|---|---|---|
| path | string | file path, resolved against `filePath` / `includePath` |
| type | `css` `html` | omit for `.mjml`; `css` behaves like `mj-style`, `html` like `mj-raw` |
| css-inline | `inline` | with `type="css"`, inlines the CSS |

---

## Layout components

### mj-wrapper
Wraps multiple `mj-section`s so they share a background/border and behave as one block. Accepts the same background/border/padding attributes as `mj-section` plus `full-width`.

### mj-section
A row. Columns go inside.

| attribute | accepts | default |
|---|---|---|
| background-color | color | — |
| background-url | string | — |
| background-position | string (`left/center/right` + `top/center/bottom`) | top center |
| background-position-x / -y | string | — |
| background-repeat | `repeat` `no-repeat` | — |
| background-size | `auto` `cover` `contain` px/% | auto |
| border / border-{top,right,bottom,left} | CSS border | — |
| border-radius | string | — |
| direction | `ltr` `rtl` | ltr |
| full-width | `full-width` `false` | — |
| padding | px/% | 20px 0 |
| text-align | `left` `center` `right` | center |
| css-class | string | — |

Note: `full-width="full-width"` makes the *background* span the viewport while content stays at body width. Sections cannot nest. Outlook background caveats: always set `background-size` explicitly.

### mj-column
A responsive cell. Stacks vertically on mobile. Must contain content.

| attribute | accepts | default |
|---|---|---|
| width | px/% | (100 / non-raw children)% |
| background-color | color | — |
| border / border-{side} | CSS border | — |
| border-radius | string | — |
| inner-background-color | color | — (requires padding) |
| inner-border / inner-border-{side} / inner-border-radius | CSS border | — (requires padding) |
| direction | `ltr` `rtl` | ltr |
| vertical-align | `top` `middle` `bottom` | top |
| padding | px/% | — |
| css-class | string | — |

Cannot nest columns or sections inside a column. `vertical-align: middle` only applies when all columns in the section use it.

### mj-group
Keeps its columns side-by-side on mobile instead of stacking. **Columns inside must use % widths, not px.**

| attribute | accepts | default |
|---|---|---|
| background-color | color | — |
| direction | `ltr` `rtl` | ltr |
| vertical-align | `top` `middle` `bottom` | — |
| width | px/% | (100 / non-raw children)% |
| css-class | string | — |

---

## Content components

### mj-text *(ending tag)*
Styled text block; put HTML inside.

| attribute | accepts | default |
|---|---|---|
| align | `left` `right` `center` `justify` | left |
| color | color | #000000 |
| font-family | string | Ubuntu, Helvetica, Arial, sans-serif |
| font-size | px | 13px |
| font-style / font-weight | string | — |
| line-height | px/% | 1 |
| letter-spacing | px/em | — |
| height | px | — |
| text-decoration / text-transform | string | — |
| container-background-color | color | — |
| padding | px/% | 10px 25px |
| css-class | string | — |

### mj-button *(ending tag)*
Bulletproof CTA. Only the inner area is clickable.

| attribute | accepts | default |
|---|---|---|
| href | string | — |
| align | `left` `center` `right` | center |
| background-color | color | #414141 |
| color | color | #ffffff |
| border / border-{side} | CSS border | none |
| border-radius | string | 3px |
| font-family | string | Ubuntu, Helvetica, Arial, sans-serif |
| font-size | px | 13px |
| font-weight | string | normal |
| inner-padding | px/% | 10px 25px |
| line-height | px/% | 120% |
| padding | px/% | 10px 25px |
| width / height | px/% | — |
| target | string | _blank |
| rel / name / title | string | — |
| text-align / text-decoration / text-transform | string | — |
| vertical-align | `top` `bottom` `middle` | middle |
| container-background-color | color | — |
| css-class | string | — |

### mj-image
Responsive `<img>`. Omit `width` to fill the column.

| attribute | accepts | default |
|---|---|---|
| src | string | — |
| alt | string | '' |
| width / height | px | auto |
| href | string | — |
| target | string | _blank |
| align | `left` `center` `right` | center |
| border / border-{side} / border-radius | CSS border | 0 |
| fluid-on-mobile | boolean | — (full width on mobile if true) |
| max-height | px/% | — |
| sizes / srcset | string | — |
| usemap | string | — (limited support) |
| rel / name / title | string | — |
| container-background-color | color | — |
| padding | px/% | 10px 25px |
| css-class | string | — |

### mj-divider
Horizontal rule.

| attribute | accepts | default |
|---|---|---|
| border-color | color | #000000 |
| border-style | string (`solid` `dashed` `dotted`) | solid |
| border-width | px | 4px |
| width | px/% | 100% |
| align | `left` `center` `right` | center |
| container-background-color | color | — |
| padding | px/% | 10px 25px |
| css-class | string | — |

### mj-spacer
Vertical blank space.

| attribute | accepts | default |
|---|---|---|
| height | px/% | 0px |
| container-background-color | color | — |
| padding | px/% | — |
| css-class | string | — |

### mj-table *(ending tag)*
Raw HTML data table. Style `<tr>`/`<td>` inline.

| attribute | accepts | default |
|---|---|---|
| align | `left` `right` `center` | left |
| border | CSS border | none |
| cellpadding / cellspacing | integer | 0 |
| color | color | #000000 |
| font-family | string | Ubuntu, Helvetica, Arial, sans-serif |
| font-size | px | 13px |
| line-height | px/% | 22px |
| role | `none` `presentation` | — |
| table-layout | `auto` `fixed` `initial` `inherit` | auto |
| width | px/% `auto` | 100% |
| container-background-color | color | — |
| padding | px/% | 10px 25px |
| css-class | string | — |

### mj-social / mj-social-element *(element is ending tag)*
Row of social share buttons.

`mj-social` attributes: `mode` (`horizontal`/`vertical`, default horizontal), `icon-size` (20px), `icon-height`, `icon-padding`, `text-padding`, `inner-padding`, `border-radius` (3px), `align` (center), `color` (#333333), `font-*`, `line-height` (22px), `padding` (10px 25px), `container-background-color`, `css-class`.

`mj-social-element` attributes: `name`, `href`, `src`, `background-color` (per-network default), `icon-size`, `icon-height`, `icon-position` (`left`/`right`), `alt`, `title`, `target` (_blank), `rel`, `align`, `color` (#000), `border-radius` (3px), `font-*`, `line-height`, `padding` (4px), `text-padding` (4px 4px 4px 0), `text-decoration`, `vertical-align`, `sizes`, `srcset`.

Networks **with** share URL: `facebook`, `twitter`, `x`, `google`, `pinterest`, `linkedin`, `tumblr`, `xing`. **Without** share URL: `github`, `instagram`, `web`, `snapchat`, `youtube`, `vimeo`, `medium`, `soundcloud`, `dribbble`. Append `-noshare` (e.g. `twitter-noshare`) to keep `href` unchanged. Custom network: supply `src` + `background-color` and omit `name`.

### mj-hero
Background-image banner; behaves like a section with one column.

| attribute | accepts | default |
|---|---|---|
| mode | `fluid-height` `fixed-height` | fluid-height |
| background-url | string | null |
| background-width | px/% | parent width (**mandatory**) |
| background-height | px/% | — (**mandatory**) |
| background-color | color | #ffffff (fallback) |
| background-position | string | center center |
| height | px/% | 0px (required for fixed-height) |
| border-radius | string | — |
| inner-background-color | color | — |
| inner-padding | px/% | — |
| padding | px/% | 0px |
| vertical-align | `top` `middle` `bottom` | top |
| css-class | string | — |

### mj-raw *(ending tag)*
Arbitrary unparsed HTML. In `mj-head`, content is appended to `<head>`. `position="file-start"` injects before `<!doctype html>`. Wrap fragile/template content in `<!-- htmlmin:ignore -->` to survive minification.

---

## Interactive components

(Interactivity degrades gracefully; support is client-specific.)

### mj-accordion / mj-accordion-element / mj-accordion-title / mj-accordion-text
Collapsible stacked panels — good for long mobile content; expands by default where responsive styles are unsupported (most desktop clients). Titles/text are ending tags.

`mj-accordion` attributes: `border` (2px solid black), `font-family` (Ubuntu…), `icon-align` (middle), `icon-height`/`icon-width` (32px), `icon-position` (right), `icon-wrapped-url`/`icon-unwrapped-url`, `icon-wrapped-alt` (+) / `icon-unwrapped-alt` (-), `padding` (10px 25px), `container-background-color`, `css-class`. `mj-accordion-element` overrides per panel. `mj-accordion-title`/`-text` take `background-color`, `color`, `font-family`, `font-size` (13px), `font-weight`, `padding` (16px); text also `line-height` (1), `letter-spacing`.

### mj-carousel / mj-carousel-image *(image is ending tag)*
Hover/click image gallery; limited client support.

`mj-carousel` attributes: `align` (center), `border-radius` (6px), `icon-width` (44px), `left-icon`/`right-icon`, `tb-border` (2px solid transparent), `tb-border-radius` (6px), `tb-hover-border-color` (#fead0d), `tb-selected-border-color` (#ccc), `tb-width`, `thumbnails` (`visible`/`hidden`/`supported`, default hidden), `container-background-color`, `padding`, `css-class`. `mj-carousel-image`: `src`, `alt`, `href`, `target` (_blank), `rel`, `title`, `border-radius`, `tb-border`, `tb-border-radius`, `thumbnails-src`, `css-class`.

### mj-navbar / mj-navbar-link *(link is ending tag)*
Horizontal menu with optional hamburger (Apple Mail only; links render inline elsewhere).

`mj-navbar` attributes: `base-url` (prefixes child hrefs), `align` (center), `hamburger` (`hamburger` to enable), and `ico-*` (only with hamburger): `ico-color` (#000000), `ico-align` (center), `ico-open` (&#9776;), `ico-close` (&#8855;), `ico-font-family`/`-font-size` (30px)/`-line-height` (30px), `ico-padding` (10px), `ico-text-decoration` (none), `ico-text-transform` (uppercase), plus `padding`, `css-class`.

`mj-navbar-link` attributes: `href`, `base-url` inherited, `color` (#000000), `font-family` (Ubuntu…), `font-size` (13px), `font-style`, `font-weight`, `line-height` (22px), `letter-spacing`, `text-decoration` (none), `text-transform` (uppercase), `padding` (15px 10px), `target`, `rel`, `name`, `css-class`. Must be a direct child of `mj-navbar`.
