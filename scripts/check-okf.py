#!/usr/bin/env python3
"""Lightweight OKF v0.1 conformance + cross-link checker.

Usage:  python3 scripts/check-okf.py <bundle-dir>   (default: okf/mjml)

Conformance (OKF v0.1): every non-reserved .md file has a parseable YAML
frontmatter block with a non-empty `type` field; reserved files (index.md,
log.md) are allowed their own structure. This script also reports broken
bundle-root-relative cross-links as a courtesy (the spec tolerates them).

Exits non-zero if any hard conformance error is found, so it drops into CI.
"""
import os, re, sys

try:
    import yaml  # optional; falls back to a regex check for `type:`
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"\]\((/[^)\s#]+\.md)")


def main(root: str) -> int:
    if not os.path.isdir(root):
        print(f"error: {root} is not a directory")
        return 2

    md = []
    for dp, _, files in os.walk(root):
        md += [os.path.join(dp, f) for f in files if f.endswith(".md")]
    known = {os.path.relpath(p, root).replace(os.sep, "/") for p in md}

    errors, warnings = [], []
    for path in sorted(md):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        text = open(path, encoding="utf-8").read()
        m = FM.match(text)
        if not m:
            errors.append(f"{rel}: no parseable YAML frontmatter")
            continue
        block = m.group(1)
        if HAVE_YAML:
            data = yaml.safe_load(block) or {}
            t = data.get("type") if isinstance(data, dict) else None
            if not t or not str(t).strip():
                errors.append(f"{rel}: missing/empty required `type` field")
        elif not re.search(r"^type:\s*\S", block, re.MULTILINE):
            errors.append(f"{rel}: missing `type` field")
        for link in LINK.findall(text):
            if link.lstrip("/") not in known:
                warnings.append(f"{rel}: broken cross-link -> {link}")

    print(f"scanned {len(md)} markdown files in {root}")
    for w in warnings:
        print("  ! ", w)
    if errors:
        print(f"\nFAIL — {len(errors)} conformance error(s):")
        for e in errors:
            print("  x ", e)
        return 1
    print("\nPASS — conformant with OKF v0.1" +
          ("" if HAVE_YAML else "  (install PyYAML for a stricter check)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "okf/mjml"))
