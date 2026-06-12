#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, ok, read_text, run_check, warn


REQUIRED = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CHANGELOG.md",
    "ROADMAP.md",
    "SKILL.md",
    "harness/architecture/release-gates.md",
    "harness/checklists/release-checklist.md",
    "platforms/capability-matrix.md",
    "dist/package-manifest.md",
]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for item in REQUIRED:
        if not (root / item).exists():
            issues.append(fail("RELEASE_REQUIRED_FILE_MISSING", item, "Release-required file missing", "Add the required file before release"))

    readme = read_text(root / "README.md") if (root / "README.md").exists() else ""
    readme_zh = read_text(root / "README.zh-CN.md") if (root / "README.zh-CN.md").exists() else ""
    for term in ["Maintenance Harness", "Multi-Platform Support"]:
        if term not in readme:
            issues.append(warn("RELEASE_README_SECTION_WEAK", "README.md", f"README may not mention {term}", "Add concise release-facing section"))
    for term in ["Maintenance Harness", "中国大陆平台适配"]:
        if term not in readme_zh:
            issues.append(warn("RELEASE_README_ZH_SECTION_WEAK", "README.zh-CN.md", f"README.zh-CN may not mention {term}", "Add concise release-facing section"))

    if any(issue.severity == "FAIL" for issue in issues):
        issues.append(fail("RELEASE_METADATA_STATUS", "", "RELEASE_METADATA_NOT_READY", "Resolve release metadata FAIL items before release"))
    elif any(issue.severity == "WARN" for issue in issues):
        issues.append(warn("RELEASE_METADATA_STATUS", "", "RELEASE_METADATA_READY_WITH_WARNINGS", "Review release metadata WARN items before release"))
    else:
        issues.append(ok("RELEASE_METADATA_STATUS", "", "Release metadata files are present. Overall release status is reported by run_all_checks.py as HARNESS_STATUS"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check release readiness.", check))
