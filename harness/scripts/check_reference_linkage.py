#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from checklib import Issue, fail, find_path_mentions, markdown_files, ok, read_text, rel, run_check


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def mention_exists(root: Path, mention: str) -> bool:
    if "references/templates/prompts" in mention:
        return True
    candidates = [mention]
    if "{locale}" in mention:
        candidates = [mention.replace("{locale}", "en-US"), mention.replace("{locale}", "zh-CN")]
    return any((root / candidate).exists() for candidate in candidates)


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    files = markdown_files(root, ["SKILL.md", "core", "prompts", "references", "adapters", "platforms", "docs", "README.md", "README.zh-CN.md"])
    for path in files:
        text = read_text(path)
        for mention in find_path_mentions(text):
            if mention.startswith("references/") and not mention_exists(root, mention):
                issues.append(fail("REFERENCE_PATH_MISSING", rel(root, path), f"Reference path missing: {mention}", "Fix the reference path or add the referenced document"))
        for match in LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.endswith((".md", ".template", ".yaml", ".yml")):
                candidate = (path.parent / target).resolve()
                if not candidate.exists():
                    issues.append(fail("MARKDOWN_LINK_MISSING", rel(root, path), f"Markdown link target missing: {target}", "Fix or remove the broken link"))

    if not issues:
        issues.append(ok("REFERENCE_LINKAGE_OK", "", "Reference linkage checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check reference linkage.", check))
