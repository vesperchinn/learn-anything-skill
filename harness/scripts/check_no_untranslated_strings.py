#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, ascii_ratio, has_cjk, ok, read_text, rel, run_check, warn


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for base in ["core/prompts", "prompts", "templates", "references", "evals"]:
        en_dir = root / base / "en-US"
        zh_dir = root / base / "zh-CN"
        if en_dir.exists():
            for path in en_dir.rglob("*"):
                if path.is_file() and path.suffix in {".md", ".yaml", ".template"} and has_cjk(read_text(path)):
                    issues.append(warn("UNTRANSLATED_CJK_IN_EN", rel(root, path), "Possible Chinese text in English locale file", "Review for untranslated text"))
        if zh_dir.exists():
            for path in zh_dir.rglob("*"):
                if path.is_file() and path.suffix in {".md", ".yaml", ".template"}:
                    text = read_text(path)
                    if len(text) > 400 and ascii_ratio(text) > 0.82:
                        issues.append(warn("UNTRANSLATED_EN_IN_ZH", rel(root, path), "Possible untranslated English-heavy Chinese locale file", "Review for untranslated text"))
    if not issues:
        issues.append(ok("NO_UNTRANSLATED_STRINGS_OK", "", "No obvious untranslated strings found"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check obvious untranslated strings.", check))

