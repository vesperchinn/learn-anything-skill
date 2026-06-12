#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, all_text_files, fail, ok, read_text, rel, run_check, warn


PLACEHOLDERS = ["lorem ipsum", "TODO:", "TBD", "FIXME", "待补充", "占位符"]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in all_text_files(root):
        r = rel(root, path)
        if r.startswith("harness/reports/") or r.startswith("harness/scripts/check_"):
            continue
        if path.stat().st_size == 0 and path.name != ".gitkeep":
            issues.append(fail("PLACEHOLDER_EMPTY_FILE", r, "Empty file found", "Add content or remove the file"))
            continue
        text = read_text(path)
        for marker in PLACEHOLDERS:
            if marker in text:
                issues.append(warn("PLACEHOLDER_TEXT", r, f"Placeholder text found: {marker}", "Replace placeholder text or document why it is intentional"))
    if not issues:
        issues.append(ok("NO_PLACEHOLDERS_OK", "", "No placeholder files found"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check placeholder files.", check))
