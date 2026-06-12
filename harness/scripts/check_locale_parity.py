#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, WARN, ascii_ratio, fail, has_cjk, ok, read_text, rel, run_check, warn


PAIRED_DIRS = ["core/prompts", "prompts", "templates", "references", "evals"]
TERMS = ["interface_language", "learning_language", "locale"]
OPTIONAL_TERMS = ["material_language"]


def files_under(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {p.relative_to(path).as_posix() for p in path.rglob("*") if p.is_file()}


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for base in PAIRED_DIRS:
        en_dir = root / base / "en-US"
        zh_dir = root / base / "zh-CN"
        if not en_dir.is_dir():
            issues.append(fail("LOCALE_DIR_MISSING", rel(root, en_dir), "en-US directory missing", "Add en-US locale directory"))
            continue
        if not zh_dir.is_dir():
            issues.append(fail("LOCALE_DIR_MISSING", rel(root, zh_dir), "zh-CN directory missing", "Add zh-CN locale directory"))
            continue
        en_files = files_under(en_dir)
        zh_files = files_under(zh_dir)
        for item in sorted(en_files - zh_files):
            severity = WARN if base == "evals" else FAIL
            issues.append(Issue("LOCALE_PAIR_MISSING", severity, f"{base}/zh-CN/{item}", "Missing zh-CN counterpart", "Add matching zh-CN file or document why it is locale-specific"))
        for item in sorted(zh_files - en_files):
            if base == "evals" and item.startswith("platform_"):
                continue
            severity = WARN if base == "evals" else FAIL
            issues.append(Issue("LOCALE_PAIR_EXTRA", severity, f"{base}/zh-CN/{item}", "zh-CN file has no en-US counterpart", "Add matching en-US file or document why it is locale-specific"))

    for path in (root / "core").rglob("*.en-US.md"):
        if has_cjk(read_text(path)):
            issues.append(warn("LOCALE_CJK_IN_EN", rel(root, path), "English locale file contains CJK characters", "Review for untranslated Chinese text"))
    for directory in ["core/prompts/en-US", "prompts/en-US", "templates/en-US", "references/en-US", "evals/en-US"]:
        for path in (root / directory).rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yaml", ".template"} and has_cjk(read_text(path)):
                issues.append(warn("LOCALE_CJK_IN_EN", rel(root, path), "English locale file contains CJK characters", "Review for untranslated Chinese text"))

    for directory in ["core/prompts/zh-CN", "prompts/zh-CN", "templates/zh-CN", "references/zh-CN", "evals/zh-CN"]:
        for path in (root / directory).rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yaml", ".template"}:
                text = read_text(path)
                if len(text) > 400 and ascii_ratio(text) > 0.82:
                    issues.append(warn("LOCALE_HIGH_ASCII_IN_ZH", rel(root, path), "Chinese locale file appears mostly English", "Review for untranslated English text"))

    corpus = "\n".join(read_text(path) for path in [root / "SKILL.md", root / "README.md", root / "README.zh-CN.md"] if path.exists())
    for term in TERMS:
        if term not in corpus:
            issues.append(fail("LOCALE_TERM_MISSING", term, f"Required locale term not found: {term}", "Use the canonical locale variable name"))
    for term in OPTIONAL_TERMS:
        if term not in corpus and not any(term in read_text(p) for p in (root / "harness").rglob("*.yaml")):
            issues.append(warn("LOCALE_TERM_OPTIONAL_MISSING", term, f"Optional locale term not prominent: {term}", "Document if material language is intentionally folded into learning_language"))

    if not issues:
        issues.append(ok("LOCALE_PARITY_OK", "", "Locale parity checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check locale parity.", check))
