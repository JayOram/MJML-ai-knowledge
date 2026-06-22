---
type: Index
title: MJML Components
description: One concept per MJML component, grouped into structural, content, and head families. The file path is the concept identity.
timestamp: 2026-06-18T00:00:00Z
---

# Components

A component is an abstraction over a more complex responsive HTML layout, exposing attributes for styling. Hold the [layout model](/concepts/layout-model.md) and [ending tags](/concepts/ending-tags.md) concepts before composing these.

## Structural

- [mjml](/components/mjml.md) — document root.
- [mj-head](/components/mj-head.md) — head container.
- [mj-body](/components/mj-body.md) — email root.
- [mj-wrapper](/components/mj-wrapper.md) — group sections as a unit.
- [mj-section](/components/mj-section.md) — a row.
- [mj-group](/components/mj-group.md) — keep columns side-by-side on mobile.
- [mj-column](/components/mj-column.md) — a responsive cell.

## Content

- [mj-text](/components/mj-text.md) — styled text (ending tag).
- [mj-button](/components/mj-button.md) — bulletproof CTA (ending tag).
- [mj-image](/components/mj-image.md) — responsive image.
- [mj-divider](/components/mj-divider.md) — horizontal rule.
- [mj-spacer](/components/mj-spacer.md) — vertical gap.
- [mj-social](/components/mj-social.md) — social share row.
- [mj-hero](/components/mj-hero.md) — background-image banner.
- [mj-raw](/components/mj-raw.md) — arbitrary HTML escape hatch (ending tag).

## Head

- [mj-attributes](/components/mj-attributes.md) — default attributes and classes.
- [mj-style](/components/mj-style.md) — CSS for the head.
- [mj-font](/components/mj-font.md) — import hosted fonts.
- [mj-include](/components/mj-include.md) — partials and external files.

> The standard library also includes `mj-table`, `mj-accordion`, `mj-carousel`, `mj-navbar`, `mj-spacer`, `mj-breakpoint`, `mj-preview`, `mj-title`, and `mj-html-attributes`. They follow the same frontmatter + body pattern and can be added as new concept files.
