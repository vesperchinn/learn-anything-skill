#!/usr/bin/env python3
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from checklib import Issue, ok, read_text, rel, run_check, warn


DATE_RE = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b")


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    targets = list(root.rglob("freshness_log.md")) + list(root.rglob("freshness_log.md.template"))
    today = date.today()
    for path in targets:
        text = read_text(path)
        for year, month, day in DATE_RE.findall(text):
            try:
                found = date(int(year), int(month), int(day))
            except ValueError:
                continue
            if found < today and "template" not in path.name:
                issues.append(warn("STALE_DATE_FOUND", rel(root, path), f"Past review date found: {found.isoformat()}", "Review whether the module needs freshness updates"))
    if not targets:
        issues.append(warn("STALE_NO_FRESHNESS_LOGS", "freshness_log.md", "No freshness logs found", "Confirm freshness tracking templates/examples exist"))
    if not issues:
        issues.append(ok("STALE_MODULES_OK", "", "No stale module dates found by static scan"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check stale module dates.", check))

