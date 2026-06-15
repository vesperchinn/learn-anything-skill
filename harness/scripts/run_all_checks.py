#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from checklib import Issue, exit_code, make_parser, print_issues, rel, write_report


CHECKS = [
    "check_contracts.py",
    "check_skill_manifest.py",
    "check_repository_structure.py",
    "check_locale_parity.py",
    "check_change_impact.py",
    "check_prompt_template_linkage.py",
    "check_reference_linkage.py",
    "check_eval_coverage.py",
    "check_platform_adapters.py",
    "check_guided_learning_mode.py",
    "check_freshness_notice.py",
    "check_reliability_layer.py",
    "check_material_grounding.py",
    "check_source_notes.py",
    "check_unverified_claims.py",
    "check_stale_modules.py",
    "check_docs_consistency.py",
    "check_no_placeholder_files.py",
    "check_no_untranslated_strings.py",
    "check_script_contract.py",
    "check_release_readiness.py",
]

BEHAVIOR_EVAL_LOCALES = ["en-US", "zh-CN"]


def main() -> int:
    parser = make_parser("Run all read-only harness checks.")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    script_dir = Path(__file__).resolve().parent
    all_issues: list[Issue] = []

    for script in CHECKS:
        command = [sys.executable, str(script_dir / script), "--root", str(root), "--json"]
        result = subprocess.run(command, text=True, capture_output=True)
        if result.stdout.strip():
            try:
                payload = json.loads(result.stdout)
                for item in payload:
                    all_issues.append(Issue(**item))
            except json.JSONDecodeError:
                all_issues.append(Issue("CHECK_OUTPUT_INVALID", "FAIL", script, "Check did not return valid JSON", result.stdout[:400]))
        if result.stderr.strip():
            all_issues.append(Issue("CHECK_STDERR", "WARN", script, result.stderr.strip()[:500], "Review check stderr"))
        if result.returncode != 0 and not any(issue.severity == "FAIL" for issue in all_issues):
            all_issues.append(Issue("CHECK_FAILED", "FAIL", script, f"{script} exited with {result.returncode}", "Run the check directly for details"))

    for locale in BEHAVIOR_EVAL_LOCALES:
        command = [sys.executable, str(root / "evals" / "run_behavior_evals.py"), "--locale", locale]
        result = subprocess.run(command, text=True, capture_output=True, cwd=root)
        if result.returncode == 0:
            summary = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else "Behavior eval passed"
            all_issues.append(Issue("BEHAVIOR_EVAL_OK", "PASS", f"evals/{locale}", summary, ""))
        else:
            output = "\n".join((result.stdout + "\n" + result.stderr).strip().splitlines()[:12])
            all_issues.append(Issue("BEHAVIOR_EVAL_FAILED", "FAIL", f"evals/{locale}", output or f"{locale} behavior eval failed", "Run evals/run_behavior_evals.py for the locale and add missing CaseRequirement coverage"))

    has_fail = any(issue.severity == "FAIL" for issue in all_issues)
    has_warn = any(issue.severity == "WARN" for issue in all_issues)
    if has_fail:
        all_issues.append(Issue("HARNESS_STATUS", "FAIL", "", "NOT_READY", "Resolve FAIL items before release"))
    elif has_warn:
        all_issues.append(Issue("HARNESS_STATUS", "WARN", "", "READY_WITH_WARNINGS", "Review WARN items before release"))
    else:
        all_issues.append(Issue("HARNESS_STATUS", "PASS", "", "READY", ""))

    if args.report:
        report_path = write_report(root, "run_all_checks", all_issues)
        all_issues.append(Issue("REPORT_WRITTEN", "PASS", rel(root, report_path), "Report written", ""))
    print_issues(all_issues, args.json)
    return exit_code(all_issues, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
