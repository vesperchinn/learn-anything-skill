#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, ok, read_text, run_check


REQUIRED = [
    "Source Notes",
    "Freshness Risk",
    "Claims to Verify",
    "Last Verified",
    "Recommended Review Interval",
]

ZH_REQUIRED = ["来源", "时效", "待验证"]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    targets = [
        root / "templates/en-US/concept-template.md",
        root / "templates/zh-CN/concept-template.md",
        root / "templates/en-US/source_notes.md.template",
        root / "templates/zh-CN/source_notes.md.template",
    ]
    for path in targets:
        if not path.exists():
            issues.append(fail("SOURCE_NOTES_TEMPLATE_MISSING", path.name, "Source notes target missing", "Add source notes template"))
            continue
        text = read_text(path)
        terms = REQUIRED if "en-US" in path.as_posix() else ZH_REQUIRED
        for term in terms:
            if term not in text:
                issues.append(fail("SOURCE_NOTES_FIELD_MISSING", path.as_posix(), f"Missing source notes field: {term}", "Add required source notes field"))
    if not issues:
        issues.append(ok("SOURCE_NOTES_OK", "", "Source notes templates contain required fields"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check source notes fields.", check))
