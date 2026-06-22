# MJML for AI Tooling

Two complementary, ready-to-use resources for building responsive email with [MJML](https://mjml.io) when an LLM or agent is in the loop:

- a **Claude skill** that teaches Claude to author, compile, and debug MJML correctly, and
- an **Open Knowledge Format (OKF) bundle** — a portable, vendor-neutral wiki an agent or pipeline can read and extend.

Same MJML knowledge, two formats. Pick whichever fits your tool — or use both.

> Built and verified against **MJML 5**. This is an independent, community resource and is not affiliated with or endorsed by MJML or Mailjet.

## Which one do I want?

| If you're…                                                      | Use                              | Where                       |
| --------------------------------------------------------------- | -------------------------------- | --------------------------- |
| Working in Claude (Claude Code, the Claude apps, claude.ai)     | the **skill**                    | [`skill/mjml/`](skill/mjml) |
| Pointing an agent, RAG pipeline, or knowledge catalog at a wiki | the **OKF bundle**               | [`okf/mjml/`](okf/mjml)     |
| Just after a clean MJML reference                               | either — both are plain Markdown | —                           |

The skill is the _instructional_ layer: how to behave when writing MJML. The bundle is the _knowledge_ layer: a navigable graph of MJML concepts. They cover the same ground from two angles, so reaching for both is reasonable.

---

## The Claude skill

[`skill/mjml/`](skill/mjml) is a standard Claude skill — a `SKILL.md` plus a `references/` folder. Its description is written to trigger whenever you work with MJML, even if you only say "responsive email" or "newsletter HTML" without naming the framework.

**What it covers:** the strict `mjml → head/body → section → column → content` layout model and the five rules that catch most bugs; ending tags; the `mj-attributes` cascade; `mj-include` (disabled by default in v5); compiling via the CLI and the `mjml2html` Node API; validation levels; and the high-value rendering gotchas (Outlook backgrounds, `mj-button` clickability, `mj-hero` mandatory dimensions, templating-plus-minify). Exhaustive per-component attribute tables live in [`skill/mjml/references/components.md`](skill/mjml/references/components.md), kept out of the main file so it stays within the progressive-disclosure budget.

**Install:** the skill is just the folder that contains `SKILL.md`. Add it to Claude the way your surface accepts skills (the Skills section in settings, or your Claude Code skills directory) — see the [Skills documentation](https://docs.claude.com) for the current procedure. To work from a local clone:

```bash
git clone https://github.com/JayOram/mjml-ai-knowledge.git
# point Claude at:  mjml-ai-knowledge/skill/mjml
```

Once available, Claude consults it automatically when you write `.mjml`, use `mj-*` tags, compile MJML, or debug client rendering.

---

## The OKF bundle

[`okf/mjml/`](okf/mjml) is a conformant [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) **v0.1** bundle: a directory of cross-linked Markdown concept files, one concept per file, each carrying YAML frontmatter (`type`, `title`, `description`, `resource`, `tags`, `timestamp`). The file path is the concept's identity, and concepts link to each other with Markdown links, so the directory reads as a graph rather than a flat doc set.

**Use it:** point any OKF consumer or agent at the bundle root, `okf/mjml/`.

```bash
git clone https://github.com/JayOram/mjml-ai-knowledge.git
# mount / point your agent or consumer at:  mjml-ai-knowledge/okf/mjml
```

Validate it against the spec with a community OKF CLI, or with the included script ([Contributing](#contributing)):

```bash
okf validate ./okf/mjml          # e.g. the third-party W4G1/okf or WitsCode validators
```

You can also drop it into Google's reference static-HTML visualizer to browse it as an interactive graph — no backend required. The full v0.1 spec and reference tools live in the [knowledge-catalog repo](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf).

**Structure:**

```
okf/mjml/
├── index.md            # bundle root — declares okf_version: 0.1
├── log.md              # change history
├── concepts/           # the mental model
│   ├── layout-model.md
│   ├── ending-tags.md
│   └── mjml-5-changes.md
├── components/         # one file per mj-* tag (structural, content, head)
└── tooling/            # cli.md, node-api.md, validation.md
```

> **Note on links:** cross-links inside the bundle are _bundle-root-relative_ (e.g. `/components/mj-section.md`), the form OKF consumers resolve when the bundle root is mounted. They are deliberately not GitHub web links, so don't expect them to navigate from GitHub's file viewer.

---

## Repository layout

```
mjml-ai-knowledge/
├── README.md
├── LICENSE
├── scripts/
│   └── check-okf.py    # lightweight OKF v0.1 conformance + link check
├── skill/
│   └── mjml/           # the Claude skill (install this folder)
│       ├── SKILL.md
│       └── references/components.md
└── okf/
    └── mjml/           # the OKF bundle (point your agent here)
        ├── index.md
        └── ...
```

The repo is organized **format-first** (`skill/`, `okf/`) with the subject one level down. That keeps each format able to grow into a collection — adding a new topic is just `skill/<topic>/` or `okf/<topic>/` — while the MJML skill and MJML bundle still sit together in a single clone.

---

## Versioning & notes

- **Targets MJML 5**, the current major. Behaviour that changed from v4 (includes off by default, the `minifyCss` key rename) is flagged in the relevant concepts.
- `mjml2html` is shown as async (`await … → { html, errors }`) per the current docs. On the MJML 4.x line it is synchronous — drop the `await` if you're pinned there.
- The bundle's `log.md` tracks changes; bump it when you edit concepts, and update the `timestamp` frontmatter on touched files.

---

## Contributing

Issues and PRs welcome — corrections, new components, or new topic folders.

For the OKF bundle, please keep it **conformant**: every non-reserved `.md` file needs YAML frontmatter with a non-empty `type`, and cross-links should resolve. Check before opening a PR:

```bash
python3 scripts/check-okf.py okf/mjml
```

---

## License

Released under the [MIT License](LICENSE) so anyone can use, adapt, and redistribute it.

---

## Credits & sources

MJML is created by [Mailjet](https://mjml.io); the component behaviour here is synthesized from the [official MJML documentation](https://documentation.mjml.io/). The Open Knowledge Format is published by [Google Cloud](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing). This repository is an independent synthesis of public documentation; all facts describe the respective tools as faithfully as possible, but it carries no official endorsement.
