#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, read_text, run_check, warn


REQUIRED_PATHS = [
    "prompts/en-US/start-guided-session.md",
    "prompts/zh-CN/start-guided-session.md",
    "references/en-US/guided-learning-mode.md",
    "references/zh-CN/guided-learning-mode.md",
    "templates/en-US/today.md.template",
    "templates/zh-CN/today.md.template",
    "templates/en-US/start_here.md.template",
    "templates/zh-CN/start_here.md.template",
    "templates/en-US/{{domain-slug}}/START_HERE.md",
    "templates/zh-CN/{{domain-slug}}/START_HERE.md",
    "templates/en-US/{{domain-slug}}/TODAY.md",
    "templates/zh-CN/{{domain-slug}}/TODAY.md",
    "templates/en-US/{{domain-slug}}/07_daily_review/day-01.md",
    "templates/zh-CN/{{domain-slug}}/07_daily_review/day-01.md",
    "evals/en-US/guided_learning_cases.yaml",
    "evals/zh-CN/guided_learning_cases.yaml",
]


def has_any(text: str, *terms: str) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "guided-learning-contract.yaml")
    required_paths = sorted(set(REQUIRED_PATHS) | set(contract.get("required_paths", [])))

    corpus = ""
    for item in required_paths:
        path = root / item
        if not path.exists():
            issues.append(fail("GUIDED_FILE_MISSING", item, "Guided Learning Mode file missing", "Add the required prompt, template, reference, or eval"))
        else:
            corpus += "\n" + read_text(path)

    skill = read_text(root / "SKILL.md")
    if "Guided Learning Mode" not in skill:
        issues.append(fail("GUIDED_SKILL_RULE_MISSING", "SKILL.md", "SKILL.md does not define Guided Learning Mode", "Add the default guided-session rule"))
    if not has_any(skill, "scaffold only", "generate files only") or not has_any(skill, "只创建项目", "不要开始学习"):
        issues.append(fail("GUIDED_SCAFFOLD_EXCEPTION_MISSING", "SKILL.md", "Scaffold-only exception is incomplete", "List explicit scaffold-only phrases"))

    prompt_corpus = "\n".join(
        read_text(root / path)
        for path in [
            "core/prompts/en-US/init-repo.md",
            "core/prompts/zh-CN/init-repo.md",
            "core/prompts/en-US/daily-session.md",
            "core/prompts/zh-CN/daily-session.md",
            "prompts/en-US/material-grounded-learning-repo.md",
            "prompts/zh-CN/material-grounded-learning-repo.md",
        ]
    )
    if not has_any(prompt_corpus, "do not stop after a file summary", "do not stop after file summary", "不得只输出文件清单", "不要只列文件清单"):
        issues.append(fail("GUIDED_PROMPT_STOP_RULE_MISSING", "core/prompts + prompts", "Prompts do not forbid stopping after file summary", "Add explicit no-file-summary-stop wording"))
    if not has_any(prompt_corpus, "start-guided-session.md"):
        issues.append(fail("GUIDED_PROMPT_START_LINK_MISSING", "core/prompts + prompts", "Prompts do not link to start-guided-session.md", "Reference the guided session prompt after repo creation"))

    docs = read_text(root / "README.md") + "\n" + read_text(root / "README.zh-CN.md")
    if not has_any(docs, "Guided Learning Mode", "陪跑学习模式"):
        issues.append(fail("GUIDED_README_SECTION_MISSING", "README.md / README.zh-CN.md", "README lacks Guided Learning Mode section", "Document default Day 1 start behavior"))
    if not has_any(docs, "You do not need to open", "不用先打开", "不用先翻"):
        issues.append(fail("GUIDED_README_NO_FILE_FIRST_MISSING", "README.md / README.zh-CN.md", "README does not tell users files are not the first step", "Explain that chat starts immediately"))

    evals = read_text(root / "evals/en-US/guided_learning_cases.yaml") + "\n" + read_text(root / "evals/zh-CN/guided_learning_cases.yaml")
    for term in [
        "must_not_stop_after_file_summary",
        "must_start_day_1_immediately",
        "must_include_answer_template",
        "must_not_start_guided_session",
        "must_create_material_repo",
    ]:
        if term not in evals:
            issues.append(fail("GUIDED_EVAL_TERM_MISSING", "evals/*/guided_learning_cases.yaml", f"Guided eval missing {term}", "Add expected behavior coverage"))

    required_terms = contract.get("required_terms") or []
    for term in required_terms:
        if term.lower() not in (skill + "\n" + corpus + "\n" + prompt_corpus + "\n" + docs).lower():
            issues.append(warn("GUIDED_CONTRACT_TERM_WEAK", "harness/contracts/guided-learning-contract.yaml", f"Contract term not found: {term}", "Connect the contract term to guided learning docs"))

    if not issues:
        issues.append(ok("GUIDED_LEARNING_MODE_OK", "", "Guided Learning Mode checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check Guided Learning Mode.", check))
