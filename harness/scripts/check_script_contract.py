#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, read_text, rel, run_check, warn


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "script-contract.yaml")
    required_flags = contract.get("required_cli_flags") or ["--root", "--json", "--strict", "--report"]
    forbidden_patterns = contract.get("forbidden_patterns") or ["rm -rf", "git reset --hard", "git clean", "os.remove(", "shutil.rmtree("]

    for path in sorted((root / "harness/scripts").glob("check_*.py")) + [root / "harness/scripts/run_all_checks.py"]:
        text = read_text(path)
        r = rel(root, path)
        if path.name != "check_script_contract.py":
            for pattern in forbidden_patterns:
                if pattern in text:
                    issues.append(fail("SCRIPT_FORBIDDEN_PATTERN", r, f"Forbidden pattern found: {pattern}", "Remove dangerous or destructive behavior from harness scripts"))
        help_result = subprocess.run([sys.executable, str(path), "--help"], text=True, capture_output=True)
        help_text = help_result.stdout + help_result.stderr
        if help_result.returncode != 0:
            issues.append(fail("SCRIPT_HELP_FAILED", r, "Script --help failed", "Fix argument parser or imports"))
            continue
        for flag in required_flags:
            if flag not in help_text:
                issues.append(fail("SCRIPT_FLAG_MISSING", r, f"Required flag missing: {flag}", "Use checklib.make_parser or add the required flag"))
        if "write_text(" in text and "--report" not in text and "write_report(" not in text:
            issues.append(warn("SCRIPT_WRITE_REVIEW", r, "Script writes files outside the shared report path", "Confirm writes are opt-in and never overwrite user files"))

    if not issues:
        issues.append(ok("SCRIPT_CONTRACT_OK", "", "Harness scripts satisfy the script contract"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check harness script contract.", check))
