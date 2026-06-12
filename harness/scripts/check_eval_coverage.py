#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, read_text, rel, run_check, warn


REQUIRED_FILES = [
    "evals/en-US/test_cases.yaml",
    "evals/zh-CN/test_cases.yaml",
    "evals/en-US/factuality_cases.yaml",
    "evals/zh-CN/factuality_cases.yaml",
    "evals/en-US/freshness_cases.yaml",
    "evals/zh-CN/freshness_cases.yaml",
    "evals/en-US/high_stakes_cases.yaml",
    "evals/zh-CN/high_stakes_cases.yaml",
    "evals/en-US/material_grounded_cases.yaml",
    "evals/zh-CN/material_grounded_cases.yaml",
    "evals/en-US/no_web_fallback_cases.yaml",
    "evals/zh-CN/no_web_fallback_cases.yaml",
    "evals/zh-CN/platform_coze_cases.yaml",
    "evals/zh-CN/platform_workbuddy_cases.yaml",
    "evals/zh-CN/platform_trae_cases.yaml",
    "evals/zh-CN/platform_codebuddy_cases.yaml",
    "evals/zh-CN/platform_generic_lowcode_cases.yaml",
]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "eval-contract.yaml")
    required_files = sorted(set(REQUIRED_FILES) | set(contract.get("required_files", [])))
    required_terms = contract.get("required_terms") or ["cases", "quality_checks", "fail_conditions"]
    for item in required_files:
        path = root / item
        if not path.exists():
            issues.append(fail("EVAL_FILE_MISSING", item, "Required eval file missing", "Add eval coverage for this behavior"))
            continue
        text = read_text(path)
        for term in required_terms:
            if term not in text and not (term == "quality_checks" and "expected" in text.lower()):
                issues.append(warn("EVAL_REQUIRED_TERM_MISSING", item, f"Eval file lacks required marker: {term}", "Add concrete behavior checks, expected behavior, or fail conditions"))
        if "input:" not in text:
            issues.append(warn("EVAL_INPUT_MISSING", item, "Eval file lacks explicit input markers", "Add realistic input prompts for cases"))

    for fixture in sorted((root / "harness/fixtures").rglob("*.md")):
        text = read_text(fixture).strip()
        if len(text) < 20:
            issues.append(fail("EVAL_FIXTURE_TOO_SMALL", rel(root, fixture), "Fixture is too small to exercise behavior", "Add a realistic fixture input"))

    fixture_terms = ["domain-learning-input", "material-learning-input", "no-web-input", "high-stakes-input", "platform-lowcode-input"]
    for locale in ("en-US", "zh-CN"):
        locale_files = {path.stem for path in (root / "harness/fixtures" / locale).glob("*.md")}
        for term in fixture_terms:
            if term not in locale_files:
                issues.append(fail("EVAL_FIXTURE_MISSING", f"harness/fixtures/{locale}/{term}.md", "Required fixture missing", "Add the fixture or update eval contract"))

    platform_files = list((root / "evals/zh-CN").glob("platform_*_cases.yaml"))
    if len(platform_files) < 5:
        issues.append(fail("EVAL_PLATFORM_COVERAGE_WEAK", "evals/zh-CN", "Platform eval coverage is incomplete", "Add platform eval files for all CN platform adapters"))
    if not any("hallucination" in read_text(path).lower() or "伪造" in read_text(path) for path in (root / "evals").rglob("*.yaml")):
        issues.append(warn("EVAL_HALLUCINATION_TRAP_WEAK", "evals/", "No explicit hallucination-trap marker found", "Add or label hallucination trap cases"))
    if not (root / "harness/architecture/release-gates.md").exists():
        issues.append(warn("EVAL_RELEASE_READINESS_UNLINKED", "harness/architecture/release-gates.md", "Release gates document missing", "Add release gates"))

    if not issues:
        issues.append(ok("EVAL_COVERAGE_OK", "", "Eval coverage checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check eval coverage.", check))
