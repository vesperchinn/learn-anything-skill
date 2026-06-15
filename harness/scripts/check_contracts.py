#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, load_contract_lists, load_platform_contract_paths, ok, run_check, warn


CONTRACTS = [
    "skill-contract.yaml",
    "locale-contract.yaml",
    "learning-repo-contract.yaml",
    "reliability-contract.yaml",
    "material-grounding-contract.yaml",
    "platform-adapter-contract.yaml",
    "eval-contract.yaml",
    "script-contract.yaml",
    "guided-learning-contract.yaml",
    "freshness-notice-contract.yaml",
    "maintenance-loop-contract.yaml",
]


def check_required_paths(root: Path, contract_name: str, issues: list[Issue]) -> None:
    contract = load_contract_lists(root, contract_name)
    for key in ("required_paths", "required_files"):
        for item in contract.get(key, []):
            if not (root / item).exists():
                issues.append(fail("CONTRACT_REQUIRED_PATH_MISSING", f"harness/contracts/{contract_name}", f"Contract points to missing path: {item}", "Add the path or update the contract"))


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract_dir = root / "harness" / "contracts"
    for name in CONTRACTS:
        path = contract_dir / name
        if not path.exists():
            issues.append(fail("CONTRACT_FILE_MISSING", f"harness/contracts/{name}", "Contract file missing", "Add the contract file"))
            continue
        if path.stat().st_size == 0:
            issues.append(fail("CONTRACT_EMPTY", f"harness/contracts/{name}", "Contract file is empty", "Define contract content"))
        check_required_paths(root, name, issues)

    platform_paths = load_platform_contract_paths(root)
    if not platform_paths:
        issues.append(fail("CONTRACT_PLATFORM_PARSE_FAILED", "harness/contracts/platform-adapter-contract.yaml", "Could not parse platform paths", "Keep platform contract in the supported simple YAML shape"))
    for platform, paths in platform_paths.items():
        if not paths:
            issues.append(fail("CONTRACT_PLATFORM_NO_PATHS", platform, "Platform has no required paths", "Add adapter paths to platform contract"))
        for item in paths:
            if not (root / item).exists():
                issues.append(fail("CONTRACT_PLATFORM_PATH_MISSING", item, f"Platform contract points to missing file for {platform}", "Add the adapter file or update contract"))

    # The lightweight parser intentionally handles simple top-level lists only.
    if not load_contract_lists(root, "script-contract.yaml").get("forbidden_patterns"):
        issues.append(warn("CONTRACT_LIST_PARSE_WEAK", "harness/contracts/script-contract.yaml", "Could not parse forbidden_patterns from script contract", "Keep top-level list shape for machine-read contract fields"))

    if not issues:
        issues.append(ok("CONTRACTS_OK", "", "Contracts are present and point to existing files"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check harness contracts.", check))
