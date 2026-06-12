#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from checklib import Issue, fail, find_path_mentions, ok, read_text, rel, run_check, warn


def mention_exists(root: Path, mention: str) -> bool:
    candidates = [mention]
    if "{locale}" in mention:
        candidates = [mention.replace("{locale}", "en-US"), mention.replace("{locale}", "zh-CN")]
    for candidate in candidates:
        path = root / candidate
        if path.exists():
            return True
    return False


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    prompt_files = list((root / "core/prompts").rglob("*.md")) + list((root / "prompts").rglob("*.md"))
    for path in prompt_files:
        text = read_text(path)
        for mention in find_path_mentions(text):
            if mention.startswith(("templates/", "references/")) and not mention_exists(root, mention):
                issues.append(fail("PROMPT_LINK_MISSING", rel(root, path), f"Referenced path does not exist: {mention}", "Fix the path or add the referenced file"))

    material_prompts = [p for p in (root / "prompts").rglob("material-*.md")]
    required_material_terms = ["material_manifest", "material_index", "material_coverage_map", "extraction_issues"]
    corpus = "\n".join(read_text(path) for path in material_prompts)
    for term in required_material_terms:
        if term not in corpus:
            issues.append(fail("PROMPT_MATERIAL_TEMPLATE_UNLINKED", "prompts/", f"Material prompt corpus does not mention {term}", "Reference the required material template or state file"))

    reliability_terms = ["source_notes", "claims_to_verify", "freshness_log"]
    prompt_corpus = "\n".join(read_text(path) for path in prompt_files)
    for term in reliability_terms:
        if term not in prompt_corpus:
            issues.append(warn("PROMPT_RELIABILITY_TEMPLATE_WEAK", "prompts/", f"Prompt corpus does not mention {term}", "Reference reliability templates where generated modules need them"))

    variable_pattern = re.compile(r"\{\{?([A-Za-z0-9_-]+)\}?\}")
    template_vars: set[str] = set()
    for path in (root / "templates").rglob("*"):
        if path.is_file():
            template_vars.update(variable_pattern.findall(read_text(path)))
    docs_corpus = "\n".join(read_text(path) for path in [root / "SKILL.md", root / "README.md", root / "README.zh-CN.md"] if path.exists())
    for var in sorted(template_vars):
        if var in {"domain", "domain-slug", "locale", "locations", "material_id", "material_ids", "page_or_slide_or_section"} or var.isupper() or any(ch.isdigit() for ch in var):
            continue
        if var not in docs_corpus and var.replace("-", "_") not in docs_corpus:
            issues.append(warn("TEMPLATE_VAR_UNEXPLAINED", "templates/", f"Template variable may be undocumented: {var}", "Explain the variable in SKILL.md or relevant prompt docs"))

    if not issues:
        issues.append(ok("PROMPT_TEMPLATE_LINKAGE_OK", "", "Prompt/template linkage checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check prompt/template linkage.", check))
