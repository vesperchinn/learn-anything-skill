#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, read_text, run_check


PROMPT_PATHS = [
    "core/prompts/en-US/init-repo.md",
    "core/prompts/zh-CN/init-repo.md",
    "core/prompts/en-US/full-workflow.md",
    "core/prompts/zh-CN/full-workflow.md",
    "prompts/en-US/start-guided-session.md",
    "prompts/zh-CN/start-guided-session.md",
    "prompts/en-US/material-grounded-learning-repo.md",
    "prompts/zh-CN/material-grounded-learning-repo.md",
]

TEMPLATE_PATHS = [
    "templates/en-US/freshness_notice.md.template",
    "templates/zh-CN/freshness_notice.md.template",
]

EVAL_PATHS = [
    "evals/en-US/freshness_notice_cases.yaml",
    "evals/zh-CN/freshness_notice_cases.yaml",
]

README_PATHS = ["README.md", "README.zh-CN.md"]

ORDER_CHECK_PATHS = [
    "prompts/en-US/start-guided-session.md",
    "prompts/zh-CN/start-guided-session.md",
    "examples/en-US/freshness-notice-session.md",
    "examples/zh-CN/freshness-notice-session.md",
]

REQUIRED_TEMPLATE_FIELDS = [
    "{{freshness_risk_label}}",
    "{{highest_freshness_risk}}",
    "{{recommended_review_interval}}",
    "{{freshness_log_path}}",
    "{{claims_to_verify_path}}",
    "{{source_status}}",
    "{{verification_disclaimer}}",
]


def has_any(text: str, *patterns: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE | re.MULTILINE) for pattern in patterns)


def read_existing(root: Path, paths: list[str]) -> str:
    parts: list[str] = []
    for item in paths:
        path = root / item
        if path.exists():
            parts.append(read_text(path))
    return "\n".join(parts)


def first_match_index(text: str, patterns: list[str]) -> int:
    positions = [match.start() for pattern in patterns for match in [re.search(pattern, text, re.IGNORECASE | re.MULTILINE)] if match]
    return min(positions) if positions else -1


def first_match_after(text: str, patterns: list[str], start: int) -> int:
    segment = text[start:]
    offset = first_match_index(segment, patterns)
    return start + offset if offset >= 0 else -1


def has_ordered_markers(text: str) -> bool:
    creation = first_match_index(
        text,
        [
            r"Created learning project",
            r"Learning project created",
            r"repository creation summary",
            r"创建摘要",
            r"已创建学习项目",
        ],
    )
    notice = first_match_after(text, [r"Freshness Notice", r"时效性提醒"], creation) if creation >= 0 else -1
    day1 = first_match_after(text, [r"Day 1", r"第 1 天", r"Today, learn", r"今天只先学"], notice) if notice >= 0 else -1
    return creation >= 0 and notice > creation and day1 > notice


def named_section(text: str, heading_patterns: list[str]) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not any(re.search(pattern, line, re.IGNORECASE) for pattern in heading_patterns):
            continue
        section_lines = [line]
        for following in lines[index + 1 :]:
            if re.match(r"^\s*#{1,3}\s+", following) or re.match(r"^\s*-\s+(stable|evolving|high-risk|稳定|演变中|高风险)", following, re.IGNORECASE):
                break
            section_lines.append(following)
        return "\n".join(section_lines)
    return ""


def forbidden_term_found(text: str, term: str) -> bool:
    pattern = re.escape(term)
    for match in re.finditer(pattern, text, re.IGNORECASE):
        context = text[max(0, match.start() - 20) : match.end() + 20].lower()
        if term.lower() == "fully verified" and re.search(r"\bnot\s+fully\s+verified\b", context):
            continue
        if term.lower() == "real-time verified" and re.search(r"\bnot\s+real-time\s+verified\b", context):
            continue
        return True
    return False


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "freshness-notice-contract.yaml")
    required_paths = sorted(
        set(contract.get("required_paths", []))
        | set(PROMPT_PATHS)
        | set(TEMPLATE_PATHS)
        | set(EVAL_PATHS)
        | set(README_PATHS)
        | {"SKILL.md"}
    )

    for item in required_paths:
        if not (root / item).exists():
            issues.append(fail("FRESHNESS_NOTICE_FILE_MISSING", item, "Required Freshness Notice file missing", "Add the required file or update the contract"))

    skill = read_text(root / "SKILL.md") if (root / "SKILL.md").exists() else ""
    if not has_any(skill, r"Freshness Notice in Chat Output"):
        issues.append(fail("FRESHNESS_NOTICE_SKILL_RULE_MISSING", "SKILL.md", "SKILL.md does not require Freshness Notice in chat output", "Add the chat-output rule under Guided Learning Mode or Knowledge Reliability Layer"))
    if not has_any(skill, r"chat output", r"conversation", r"对话"):
        issues.append(fail("FRESHNESS_NOTICE_CHAT_RULE_MISSING", "SKILL.md", "Freshness Notice is not tied to chat output", "Require the notice in repository creation chat output"))

    for item in TEMPLATE_PATHS:
        path = root / item
        if not path.exists():
            continue
        text = read_text(path)
        for field in REQUIRED_TEMPLATE_FIELDS:
            if field not in text:
                issues.append(fail("FRESHNESS_NOTICE_TEMPLATE_FIELD_MISSING", item, f"Template missing field {field}", "Add all required template fields"))

    for item in PROMPT_PATHS:
        path = root / item
        if not path.exists():
            continue
        text = read_text(path)
        if "freshness_notice.md.template" not in text:
            issues.append(fail("FRESHNESS_NOTICE_PROMPT_TEMPLATE_LINK_MISSING", item, "Prompt does not reference the Freshness Notice template", "Reference templates/{locale}/freshness_notice.md.template"))
        if not has_any(text, r"Freshness Notice", r"时效性提醒"):
            issues.append(fail("FRESHNESS_NOTICE_PROMPT_RULE_MISSING", item, "Prompt does not mention Freshness Notice", "Add the required chat-output notice rule"))

    prompt_corpus = read_existing(root, PROMPT_PATHS)
    if not has_any(prompt_corpus, r"material-grounded-learning-repo", r"基于资料"):
        issues.append(fail("FRESHNESS_NOTICE_MATERIAL_FLOW_MISSING", "prompts/*/material-grounded-learning-repo.md", "Material-grounded flow is not covered", "Add Freshness Notice to material-grounded repository creation"))

    eval_corpus = read_existing(root, EVAL_PATHS)
    for term in [
        "fund_investing_beginner_notice",
        "openai_api_fast_changing_notice",
        "basic_algebra_short_notice",
        "must_include_freshness_notice_in_chat",
        "must_not_claim_absolute_accuracy",
        "must_start_day_1_after_notice",
    ]:
        if term not in eval_corpus:
            issues.append(fail("FRESHNESS_NOTICE_EVAL_CASE_MISSING", "evals/*/freshness_notice_cases.yaml", f"Eval missing {term}", "Add the required Freshness Notice eval coverage"))

    readme_corpus = read_existing(root, README_PATHS)
    if not has_any(readme_corpus, r"Freshness Notice", r"时效性提醒"):
        issues.append(fail("FRESHNESS_NOTICE_README_SECTION_MISSING", "README.md / README.zh-CN.md", "README does not document chat Freshness Notice", "Add a short Freshness Notice section"))
    if not has_any(readme_corpus, r"created.*chat", r"创建学习仓库.*对话"):
        issues.append(fail("FRESHNESS_NOTICE_README_BEHAVIOR_MISSING", "README.md / README.zh-CN.md", "README does not say the notice is shown during repository creation", "Document that the chat output includes the notice"))

    production_corpus = "\n".join([skill, prompt_corpus, readme_corpus, read_existing(root, TEMPLATE_PATHS)])
    if "09_sources/freshness_log.md" not in production_corpus:
        issues.append(fail("FRESHNESS_NOTICE_LOG_PATH_MISSING", "Freshness Notice files", "Freshness Notice does not include 09_sources/freshness_log.md", "Add the freshness log path to rules and templates"))
    if not has_any(production_corpus, r"09_sources/claims_to_verify\.md"):
        issues.append(fail("FRESHNESS_NOTICE_CLAIMS_PATH_MISSING", "Freshness Notice files", "High-risk Freshness Notice does not include 09_sources/claims_to_verify.md", "Add claims_to_verify path for high-risk or verification-needed content"))
    if not has_any(production_corpus, r"finance|investment|medical|health|legal|policy|tax|immigration|AI tools|APIs|software libraries|pricing|benchmarks|exam policies|platform rules|market data"):
        issues.append(fail("FRESHNESS_NOTICE_HIGH_RISK_SCOPE_MISSING", "SKILL.md", "High-stakes / fast-changing domain scope is incomplete", "List the mandatory high-risk and fast-changing domains"))
    if not has_any(production_corpus, r"no-web|no-retrieval|web or retrieval|没有联网|实时检索|未完成实时核查"):
        issues.append(fail("FRESHNESS_NOTICE_NO_WEB_DISCLAIMER_MISSING", "Freshness Notice files", "No-web or no-retrieval disclaimer is missing", "Add a disclaimer for unverified current sources"))

    risk_patterns = {
        "stable": r"stable foundational|Stable / low-risk|Low-risk / Stable|稳定基础知识|稳定 / 低风险|低风险 / 稳定",
        "evolving": r"evolving|medium-risk|Medium-risk|演变中|中风险",
        "high-risk": r"high-risk|fast-changing|High-risk / Fast-changing|高风险|快速变化|高时效",
    }
    for tier, pattern in risk_patterns.items():
        if not has_any(production_corpus, pattern):
            issues.append(fail("FRESHNESS_NOTICE_RISK_TIER_MISSING", "Freshness Notice files", f"Missing {tier} Freshness Notice tier", "Document stable, evolving, and high-risk notice variants"))

    stable_sections = "\n".join(
        named_section(read_text(root / item), [r"Stable", r"Low-risk", r"稳定", r"低风险"])
        for item in PROMPT_PATHS + TEMPLATE_PATHS
        if (root / item).exists()
    )
    if has_any(stable_sections, r"Claims to verify:\s*`?09_sources/claims_to_verify\.md", r"待核查内容：`?09_sources/claims_to_verify\.md", r"must include.*claims_to_verify", r"必须.*claims_to_verify"):
        issues.append(fail("FRESHNESS_NOTICE_STABLE_OVERWARN", "Freshness Notice stable tier", "Stable tier appears to require the full claims-to-verify block", "Use only a short stable notice unless actual claims require verification"))

    high_risk_sections = "\n".join(
        named_section(read_text(root / item), [r"High-risk", r"fast-changing", r"高风险", r"快速变化"])
        for item in PROMPT_PATHS + TEMPLATE_PATHS
        if (root / item).exists()
    )
    if "09_sources/claims_to_verify.md" not in high_risk_sections and "{{claims_to_verify_path}}" not in high_risk_sections:
        issues.append(fail("FRESHNESS_NOTICE_HIGH_RISK_CLAIMS_MISSING", "Freshness Notice high-risk tier", "High-risk tier does not require claims_to_verify.md", "Include claims_to_verify.md in high-risk / fast-changing notices"))

    ordered_examples = [
        item
        for item in ORDER_CHECK_PATHS
        if (root / item).exists() and has_ordered_markers(read_text(root / item))
    ]
    if not ordered_examples:
        issues.append(fail("FRESHNESS_NOTICE_ORDER_MISSING", "prompts or examples", "No prompt or example shows creation summary -> Freshness Notice -> Day 1 order", "Add an example or structure with that order"))

    for term in contract.get("forbidden_terms", []):
        if term and forbidden_term_found(production_corpus, term):
            issues.append(fail("FRESHNESS_NOTICE_OVERCLAIM", "Freshness Notice files", f"Overclaiming phrase found: {term}", "Remove guarantees of complete accuracy or full trustworthiness"))

    if not issues:
        issues.append(ok("FRESHNESS_NOTICE_OK", "", "Freshness Notice checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check Freshness Notice chat output.", check))
