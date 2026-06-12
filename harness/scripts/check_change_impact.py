#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from checklib import Issue, exit_code, make_parser, ok, print_issues, rel, warn, write_report


RULES = [
    ("SKILL.md", ["check_skill_manifest.py", "check_docs_consistency.py", "check_eval_coverage.py", "check_platform_adapters.py"]),
    ("core/", ["check_locale_parity.py", "check_prompt_template_linkage.py", "check_docs_consistency.py"]),
    ("prompts/en-US/", ["check_locale_parity.py", "check_prompt_template_linkage.py", "check_eval_coverage.py"]),
    ("prompts/zh-CN/", ["check_locale_parity.py", "check_prompt_template_linkage.py", "check_eval_coverage.py"]),
    ("templates/", ["check_prompt_template_linkage.py", "check_material_grounding.py", "check_reliability_layer.py", "check_source_notes.py"]),
    ("references/", ["check_reference_linkage.py", "check_reliability_layer.py", "check_material_grounding.py", "check_docs_consistency.py"]),
    ("platforms/", ["check_platform_adapters.py", "check_eval_coverage.py", "check_docs_consistency.py"]),
    ("adapters/", ["check_platform_adapters.py", "check_docs_consistency.py"]),
    ("scripts/", ["check_script_contract.py", "check_docs_consistency.py"]),
    ("docs/", ["check_docs_consistency.py", "check_locale_parity.py", "check_release_readiness.py"]),
    ("dist/", ["check_contracts.py", "check_release_readiness.py"]),
    ("harness/", ["check_contracts.py", "check_script_contract.py", "check_release_readiness.py"]),
    ("harness/scripts/", ["check_script_contract.py", "check_contracts.py"]),
    ("harness/contracts/", ["check_contracts.py"]),
    ("evals/", ["check_eval_coverage.py"]),
    ("README.md", ["check_docs_consistency.py", "check_locale_parity.py", "check_release_readiness.py"]),
    ("README.zh-CN.md", ["check_docs_consistency.py", "check_locale_parity.py", "check_release_readiness.py"]),
    ("CONTRIBUTING.md", ["check_docs_consistency.py", "check_locale_parity.py", "check_release_readiness.py"]),
    ("CONTRIBUTING.zh-CN.md", ["check_docs_consistency.py", "check_locale_parity.py", "check_release_readiness.py"]),
]


def git_changed_files(root: Path) -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=root, text=True, capture_output=True)
    if result.returncode != 0:
        return []
    files: list[str] = []
    for line in result.stdout.splitlines():
        item = line[3:].strip()
        if " -> " in item:
            item = item.split(" -> ", 1)[1].strip()
        if item:
            files.append(item)
    return files


def impacted_checks(file_path: str) -> set[str]:
    impacted: set[str] = set()
    for prefix, checks in RULES:
        if file_path == prefix.rstrip("/") or file_path.startswith(prefix):
            impacted.update(checks)
    return impacted


def run(root: Path, changed_files: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    if not changed_files:
        issues.append(ok("CHANGE_IMPACT_NONE", "", "No changed files detected"))
        return issues
    aggregate: set[str] = set()
    for file_path in changed_files:
        checks = impacted_checks(file_path)
        if checks:
            aggregate.update(checks)
            issues.append(warn("CHANGE_IMPACT_REVIEW", file_path, f"Changed file affects: {', '.join(sorted(checks))}", "Run the listed checks or document why they are not needed"))
        else:
            issues.append(warn("CHANGE_IMPACT_UNMAPPED", file_path, "Changed file is not mapped to checks", "Add a change-impact rule if this path is part of the maintained surface"))
    if aggregate:
        issues.append(warn("CHANGE_IMPACT_SUMMARY", "", f"Recommended checks: {', '.join(sorted(aggregate))}", "Run these checks before release"))
    return issues


def main() -> int:
    parser = make_parser("Report affected checks for changed files.")
    parser.add_argument("--changed-files", nargs="*", help="Changed file paths. Defaults to git status --short.")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    changed = args.changed_files if args.changed_files is not None else git_changed_files(root)
    issues = run(root, changed)
    if args.report:
        report_path = write_report(root, "check_change_impact", issues)
        issues.append(ok("REPORT_WRITTEN", rel(root, report_path), "Report written"))
    print_issues(issues, args.json)
    return exit_code(issues, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
