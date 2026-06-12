#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, all_text_files, ok, read_text, rel, run_check, warn


MARKERS = ["[unverified]", "[未验证]", "Unverified Draft", "未验证草稿"]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    allowed_parts = {"templates", "prompts", "references", "evals", "harness", "core", "docs", "platforms", "scripts", "skills"}
    allowed_files = {"README.md", "README.zh-CN.md", "SKILL.md"}
    for path in all_text_files(root):
        r = rel(root, path)
        if r in allowed_files:
            continue
        text = read_text(path)
        if any(marker in text for marker in MARKERS):
            if allowed_parts.intersection(path.relative_to(root).parts):
                continue
            issues.append(warn("UNVERIFIED_MARKER_REVIEW", r, "Unverified marker found outside templates/prompts/references/evals/harness", "Confirm it is intentional or move the claim into claims_to_verify"))
    if not issues:
        issues.append(ok("UNVERIFIED_CLAIMS_OK", "", "No unexpected unverified claim markers found"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check unverified claim markers.", check))
