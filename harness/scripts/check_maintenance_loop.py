#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from checklib import Issue, fail, ok, read_text, rel, run_check


REQUIRED_FILES = [
    "harness/contracts/maintenance-loop-contract.yaml",
    "references/en-US/maintenance-loop.md",
    "references/zh-CN/maintenance-loop.md",
    "prompts/en-US/maintenance-loop.md",
    "prompts/zh-CN/maintenance-loop.md",
    "evals/en-US/maintenance_loop_cases.yaml",
    "evals/zh-CN/maintenance_loop_cases.yaml",
    "harness/architecture/change-impact-matrix.md",
    "harness/architecture/release-gates.md",
    "harness/checklists/release-checklist.md",
]


def corpus(root: Path, paths: list[str]) -> str:
    return "\n".join(read_text(root / path) for path in paths if (root / path).exists())


def require_pattern(issues: list[Issue], root: Path, path: str, pattern: str, code: str, message: str, fix: str) -> None:
    file_path = root / path
    if not file_path.exists():
        issues.append(fail("MAINTENANCE_LOOP_FILE_MISSING", path, "Required maintenance loop file missing", "Add the missing file"))
        return
    if re.search(pattern, read_text(file_path), re.IGNORECASE | re.MULTILINE) is None:
        issues.append(fail(code, path, message, fix))


def require_corpus_pattern(issues: list[Issue], root: Path, paths: list[str], pattern: str, code: str, message: str, fix: str) -> None:
    text = corpus(root, paths)
    if re.search(pattern, text, re.IGNORECASE | re.MULTILINE) is None:
        issues.append(fail(code, ", ".join(paths), message, fix))


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []

    for item in REQUIRED_FILES:
        path = root / item
        if not path.exists():
            issues.append(fail("MAINTENANCE_LOOP_FILE_MISSING", item, "Required maintenance loop file missing", "Add the missing file"))
        elif path.stat().st_size == 0:
            issues.append(fail("MAINTENANCE_LOOP_FILE_EMPTY", item, "Required maintenance loop file is empty", "Define the maintenance loop content"))

    contract = "harness/contracts/maintenance-loop-contract.yaml"
    en_ref = "references/en-US/maintenance-loop.md"
    zh_ref = "references/zh-CN/maintenance-loop.md"
    en_prompt = "prompts/en-US/maintenance-loop.md"
    zh_prompt = "prompts/zh-CN/maintenance-loop.md"
    release_gates = "harness/architecture/release-gates.md"
    release_checklist = "harness/checklists/release-checklist.md"
    pr_checklist = "harness/checklists/pr-checklist.md"
    matrix = "harness/architecture/change-impact-matrix.md"
    eval_en = "evals/en-US/maintenance_loop_cases.yaml"
    eval_zh = "evals/zh-CN/maintenance_loop_cases.yaml"

    maintenance_docs = [contract, en_ref, zh_ref, en_prompt, zh_prompt, release_gates, release_checklist, pr_checklist]

    require_pattern(
        issues,
        root,
        contract,
        r"Maintenance Loop is maintainer-only|普通学习者|ordinary learner",
        "MAINTENANCE_LOOP_SCOPE_WEAK",
        "Contract does not clearly define maintainer-only scope",
        "State that Maintenance Loop is maintainer-only and excludes ordinary learner sessions",
    )
    require_pattern(
        issues,
        root,
        contract,
        r"release_blocked_until_closed:\s*true|范围未收口时不得|Do not tag or release while scope is unsettled",
        "MAINTENANCE_LOOP_SCOPE_FREEZE_MISSING",
        "Contract lacks release scope freeze rule",
        "Require release scope freeze before tag or release",
    )
    require_pattern(
        issues,
        root,
        contract,
        r"READY_WITH_WARNINGS.*human explanation|READY_WITH_WARNINGS.*人工解释",
        "MAINTENANCE_LOOP_WARNING_EXPLANATION_MISSING",
        "Contract does not require human explanation for READY_WITH_WARNINGS",
        "Require human explanation before release with warnings",
    )
    require_pattern(
        issues,
        root,
        contract,
        r"change-impact-matrix\.md",
        "MAINTENANCE_LOOP_MATRIX_REFERENCE_MISSING",
        "Contract does not reference the existing change-impact matrix",
        "Reference harness/architecture/change-impact-matrix.md",
    )

    require_corpus_pattern(
        issues,
        root,
        maintenance_docs,
        r"Scope Freeze|发布范围收口|scope freeze",
        "MAINTENANCE_LOOP_SCOPE_FREEZE_DOC_MISSING",
        "Maintenance docs lack release scope freeze rule",
        "Document file classification and scope freeze before release",
    )
    require_corpus_pattern(
        issues,
        root,
        maintenance_docs,
        r"messy worktree|工作区混乱|unreviewed changes|未审查变更|未收口",
        "MAINTENANCE_LOOP_DIRTY_RELEASE_RULE_MISSING",
        "Maintenance docs do not clearly block release from unsettled worktree state",
        "Block release when worktree is messy, unreviewed, or scope is unsettled",
    )
    require_corpus_pattern(
        issues,
        root,
        maintenance_docs,
        r"READY_WITH_WARNINGS.*(human explanation|人工解释)|warning.*human explanation",
        "MAINTENANCE_LOOP_READY_WARNINGS_RULE_MISSING",
        "Maintenance docs do not require human explanation for READY_WITH_WARNINGS",
        "Document the warning explanation requirement",
    )
    require_corpus_pattern(
        issues,
        root,
        maintenance_docs,
        r"ordinary learner|普通学习者|learner sessions|学习会话",
        "MAINTENANCE_LOOP_LEARNER_BOUNDARY_MISSING",
        "Maintenance docs do not clearly prohibit applying the loop to ordinary learner sessions",
        "State that Maintenance Loop does not apply to ordinary learner sessions",
    )
    require_corpus_pattern(
        issues,
        root,
        maintenance_docs,
        r"token cost|token 消耗|extra conversation rounds|额外对话轮次",
        "MAINTENANCE_LOOP_TOKEN_BOUNDARY_MISSING",
        "Maintenance docs do not forbid default learner token-cost increases",
        "State that the loop must not add default learner rounds or token cost",
    )
    require_corpus_pattern(
        issues,
        root,
        [en_ref, zh_ref, en_prompt, zh_prompt],
        r"Guided Learning Mode[\s\S]*Interactive Beginner Lesson Mode[\s\S]*Material-Grounded Learning Mode|Guided Learning Mode、Interactive Beginner Lesson Mode[\s\S]*Material-Grounded Learning Mode",
        "MAINTENANCE_LOOP_USER_FLOW_BOUNDARY_MISSING",
        "Maintenance docs do not protect the existing user learning modes",
        "Explicitly exclude Guided Learning Mode, Interactive Beginner Lesson Mode, and Material-Grounded Learning Mode from maintenance-loop behavior",
    )
    require_corpus_pattern(
        issues,
        root,
        [en_ref, zh_ref, matrix, release_gates, release_checklist],
        r"change-impact-matrix\.md|Change Impact Matrix|影响范围",
        "MAINTENANCE_LOOP_MATRIX_DOC_REFERENCE_MISSING",
        "Maintenance loop does not reference the existing change-impact matrix",
        "Link the loop to harness/architecture/change-impact-matrix.md",
    )
    require_corpus_pattern(
        issues,
        root,
        [release_gates, release_checklist, en_ref, zh_ref],
        r"RELEASE_NOTES\.md.*CHANGELOG\.md|CHANGELOG\.md.*RELEASE_NOTES\.md",
        "MAINTENANCE_LOOP_RELEASE_CHECKLIST_INCONSISTENT",
        "Release checklist alignment is missing CHANGELOG and RELEASE_NOTES requirements",
        "Keep Maintenance Loop release gate aligned with release checklist",
    )
    require_corpus_pattern(
        issues,
        root,
        [eval_en, eval_zh],
        r"must_state_maintainer_only[\s\S]*must_not_change_user_learning_flow[\s\S]*must_not_add_default_user_loop",
        "MAINTENANCE_LOOP_EVAL_SCOPE_CASE_MISSING",
        "Maintenance evals do not cover maintainer-only boundary",
        "Add eval cases for maintainer-only and no user-flow change",
    )
    require_corpus_pattern(
        issues,
        root,
        [eval_en, eval_zh],
        r"must_require_file_classification[\s\S]*must_require_staged_file_summary[\s\S]*must_pause_before_commit_or_release",
        "MAINTENANCE_LOOP_EVAL_SCOPE_FREEZE_CASE_MISSING",
        "Maintenance evals do not cover release scope freeze",
        "Add eval cases for file classification and pause before commit or release",
    )

    if not issues:
        issues.append(ok("MAINTENANCE_LOOP_OK", "", "Maintenance Loop contract, docs, prompts, evals, and release boundaries are present"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check maintainer-only Maintenance Loop.", check))
