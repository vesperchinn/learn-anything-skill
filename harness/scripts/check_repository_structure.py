#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, all_text_files, fail, ok, read_text, rel, run_check, warn


REQUIRED_DIRS = [
    "core",
    "core/prompts/en-US",
    "core/prompts/zh-CN",
    "prompts/en-US",
    "prompts/zh-CN",
    "templates/en-US",
    "templates/zh-CN",
    "references/en-US",
    "references/zh-CN",
    "adapters",
    "platforms",
    "examples",
    "evals",
    "scripts",
    "harness",
]

CACHE_NAMES = {".DS_Store", "Thumbs.db"}
CACHE_PARTS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
PLACEHOLDERS = ["lorem ipsum", "TBD", "TODO:", "待补充", "占位"]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for item in REQUIRED_DIRS:
        if not (root / item).is_dir():
            issues.append(fail("STRUCTURE_DIR_MISSING", item, "Required directory is missing", f"Create `{item}` or update the contract"))

    for path in root.rglob("*"):
        r = rel(root, path)
        if any(part in CACHE_PARTS for part in path.parts) or path.name in CACHE_NAMES:
            issues.append(warn("STRUCTURE_CACHE_FILE", r, "Cache or temporary file found", "Remove generated cache files from the repository"))
        if path.is_file() and path.stat().st_size == 0 and path.name != ".gitkeep":
            issues.append(fail("STRUCTURE_EMPTY_FILE", r, "Empty file found", "Add real content or remove the file"))

    for path in all_text_files(root):
        r = rel(root, path)
        if r.startswith("harness/reports/") or r.startswith("harness/scripts/check_"):
            continue
        text = read_text(path)
        for marker in PLACEHOLDERS:
            if marker in text:
                issues.append(warn("STRUCTURE_PLACEHOLDER", r, f"Placeholder marker found: {marker}", "Replace placeholder text with final content or remove it"))

    if not issues:
        issues.append(ok("STRUCTURE_OK", "", "Repository structure looks valid"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check repository structure.", check))
