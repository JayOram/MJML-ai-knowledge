---
okf_version: 0.1
type: Knowledge Bundle
title: MJML — The Responsive Email Framework
description: A portable knowledge bundle covering the MJML 5 markup language — its layout model, components, tooling, and rendering gotchas — for AI agents and humans building responsive HTML email.
resource: https://documentation.mjml.io/
tags: [mjml, email, html-email, responsive, frontend]
timestamp: 2026-06-18T00:00:00Z
---

# MJML Knowledge Bundle

MJML (Mailjet Markup Language) is a markup language that compiles a small set of semantic tags into responsive, client-compatible HTML email. Authors work at the layout level (`mj-section`, `mj-column`) and the engine emits the table-based, client-hardened HTML underneath.

This bundle targets **MJML 5**, the current major version. Behaviour that changed from v4 is flagged in the relevant concepts, since those changes are the most common cause of regressions.

## How to navigate this bundle

Start with the mental model, then drill into components or tooling as needed. Concepts cross-link, so an agent can follow `mj-group` → "columns must use % width" → the layout model without re-reading everything.

## Map

- **Concepts** — the mental model you must hold to use MJML correctly.
  - [Layout model](/concepts/layout-model.md) — the strict hierarchy and its five rules.
  - [Ending tags](/concepts/ending-tags.md) — which components can't contain other MJML.
  - [MJML 5 changes](/concepts/mjml-5-changes.md) — what moved between v4 and v5.
- **Components** — one concept per tag. See [the component index](/components/index.md).
- **Tooling** — compiling and validating. See [the tooling index](/tooling/index.md).

## Conformance

This bundle conforms to Open Knowledge Format v0.1: every non-reserved Markdown file carries YAML frontmatter with a non-empty `type` field, and the reserved files (`index.md`, `log.md`) follow their conventional structure. Cross-links are ordinary Markdown links using bundle-root-relative paths.
