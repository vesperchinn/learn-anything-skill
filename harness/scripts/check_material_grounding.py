#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, read_text, run_check, warn


REQUIRED_PATHS = [
    "prompts/en-US/material-intake.md",
    "prompts/zh-CN/material-intake.md",
    "prompts/en-US/material-grounded-learning-repo.md",
    "prompts/zh-CN/material-grounded-learning-repo.md",
    "prompts/en-US/material-review-session.md",
    "prompts/zh-CN/material-review-session.md",
    "prompts/en-US/material-quiz-generation.md",
    "prompts/zh-CN/material-quiz-generation.md",
    "prompts/en-US/material-gap-analysis.md",
    "prompts/zh-CN/material-gap-analysis.md",
    "templates/en-US/material_manifest.md.template",
    "templates/zh-CN/material_manifest.md.template",
    "templates/en-US/material_index.md.template",
    "templates/zh-CN/material_index.md.template",
    "templates/en-US/material_coverage_map.md.template",
    "templates/zh-CN/material_coverage_map.md.template",
    "templates/en-US/material_learning_plan.md.template",
    "templates/zh-CN/material_learning_plan.md.template",
    "templates/en-US/extraction_issues.md.template",
    "templates/zh-CN/extraction_issues.md.template",
    "templates/en-US/material_quiz.md.template",
    "templates/zh-CN/material_quiz.md.template",
    "references/en-US/pdf-slide-handling.md",
    "references/zh-CN/pdf-slide-handling.md",
    "references/en-US/material-grounding-policy.md",
    "references/zh-CN/material-grounding-policy.md",
]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "material-grounding-contract.yaml")
    required_paths = sorted(set(REQUIRED_PATHS) | set(contract.get("required_paths", [])))
    contract_terms = contract.get("required_terms") or []
    corpus = ""
    for item in required_paths:
        path = root / item
        if not path.exists():
            issues.append(fail("MATERIAL_FILE_MISSING", item, "Material-grounding file missing", "Add the required material prompt, template, or reference"))
        else:
            corpus += "\n" + read_text(path)
    for item in ["README.md", "README.zh-CN.md"]:
        path = root / item
        if path.exists():
            corpus += "\n" + read_text(path)

    required_terms = ["PDF", "PPT", "slide", "page", "Supplemental", "extraction issue", "copyright"]
    zh_terms = ["页码", "幻灯片", "补充", "无法读取", "版权"]
    corpus_lower = corpus.lower()
    for term in contract_terms:
        if term.lower() not in corpus_lower:
            issues.append(warn("MATERIAL_CONTRACT_TERM_WEAK", "harness/contracts/material-grounding-contract.yaml", f"Contract term not found in material corpus: {term}", "Connect the contract term to a material prompt/reference or update the contract"))
    for term in required_terms:
        if term.lower() not in corpus_lower:
            issues.append(warn("MATERIAL_TERM_WEAK", "material grounding", f"Material corpus may not mention {term}", "Add explicit material-grounding wording"))
    for term in zh_terms:
        if term not in corpus:
            issues.append(warn("MATERIAL_ZH_TERM_WEAK", "material grounding", f"Chinese material corpus may not mention {term}", "Add explicit Chinese material-grounding wording"))
    if "fake page" not in corpus.lower() and "伪造页码" not in corpus and "编造页码" not in corpus:
        issues.append(fail("MATERIAL_FAKE_PAGE_RULE_MISSING", "material grounding", "No fake page/slide rule found", "Add explicit no fake page/slide number rule"))
    if "no-file" not in corpus.lower() and "不能读取文件" not in corpus and "无文件读取" not in corpus:
        issues.append(fail("MATERIAL_NO_FILE_FALLBACK_MISSING", "material grounding", "No file-access fallback found", "Add no-file-access fallback behavior"))

    if not issues:
        issues.append(ok("MATERIAL_GROUNDING_OK", "", "Material-grounding checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check material-grounded learning mode.", check))
