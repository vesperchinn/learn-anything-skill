#!/usr/bin/env python3
"""Executable behavior-policy checks for YAML eval cases.

These are policy regression checks, not live learning-loop evaluations. They
do not call a real Agent. They make each YAML behavior case executable by
binding it to:

- a concrete user input in the YAML case,
- one or more policy/prompt/template files that must exist, and
- case-specific evidence plus forbidden-output patterns.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class EvalCase:
    suite: str
    locale: str
    case_id: str
    input_text: str
    block: str


@dataclass(frozen=True)
class CaseRequirement:
    files: tuple[str, ...]
    evidence: tuple[str, ...]
    input_patterns: tuple[str, ...]
    forbidden_patterns: tuple[str, ...]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def corpus(paths: tuple[str, ...]) -> str:
    return "\n".join(read(path) for path in paths if (ROOT / path).exists())


def parse_quoted_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_cases(path: Path) -> list[EvalCase]:
    content = path.read_text(encoding="utf-8")
    suite_match = re.search(r"^test_suite:\s*([^\s]+)", content, re.MULTILINE)
    locale_match = re.search(r"^locale:\s*([^\s]+)", content, re.MULTILINE)
    if not suite_match or not locale_match:
        return []

    suite = suite_match.group(1)
    locale = locale_match.group(1)
    matches = list(re.finditer(r"^\s*-\s+id:\s*([^\s]+)", content, re.MULTILINE))
    cases: list[EvalCase] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        block = content[start:end]
        input_match = re.search(r"^\s*input:\s*(.+)$", block, re.MULTILINE)
        cases.append(
            EvalCase(
                suite=suite,
                locale=locale,
                case_id=match.group(1),
                input_text=parse_quoted_scalar(input_match.group(1)) if input_match else "",
                block=block,
            )
        )
    return cases


def require(text: str, patterns: list[str], label: str) -> tuple[bool, str]:
    missing = [pattern for pattern in patterns if re.search(pattern, text, re.IGNORECASE | re.MULTILINE) is None]
    if missing:
        return False, f"{label}: missing {missing}"
    return True, label


def base_files(locale: str) -> tuple[str, ...]:
    return (
        "SKILL.md",
        f"references/{locale}/source-quality-policy.md",
        f"references/{locale}/freshness-policy.md",
        f"references/{locale}/high-stakes-domain-policy.md",
        f"references/{locale}/claim-verification-guide.md",
        f"templates/{locale}/source_notes.md.template",
        f"templates/{locale}/claim_ledger.md.template",
        f"templates/{locale}/claims_to_verify.md.template",
        "adapters/README.md",
    )


def material_files(locale: str) -> tuple[str, ...]:
    return (
        "SKILL.md",
        f"prompts/{locale}/material-intake.md",
        f"prompts/{locale}/material-grounded-learning-repo.md",
        f"prompts/{locale}/material-review-session.md",
        f"prompts/{locale}/material-quiz-generation.md",
        f"prompts/{locale}/material-gap-analysis.md",
        f"references/{locale}/material-grounding-policy.md",
        f"references/{locale}/pdf-slide-handling.md",
        f"templates/{locale}/material_manifest.md.template",
        f"templates/{locale}/material_index.md.template",
        f"templates/{locale}/material_coverage_map.md.template",
        f"templates/{locale}/extraction_issues.md.template",
        "adapters/codex.md",
        "adapters/claude-code.md",
        "adapters/cursor.md",
        "adapters/chatgpt.md",
        "adapters/generic-agent.md",
    )


def requirements(locale: str) -> dict[tuple[str, str], CaseRequirement]:
    common = base_files(locale)
    material = material_files(locale)
    readmes = ("README.md", "README.zh-CN.md")
    examples = (
        "examples/en-US/learn-ai-agent/learning_materials/material_manifest.md",
        "examples/en-US/learn-ai-agent/learning_materials/material_index.md",
        "examples/en-US/learn-ai-agent/09_sources/sources.md",
        "examples/en-US/learn-ai-agent/09_sources/claim_ledger.md",
        "examples/zh-CN/learn-ai-agent/learning_materials/material_manifest.md",
        "examples/zh-CN/learn-ai-agent/learning_materials/material_index.md",
        "examples/zh-CN/learn-ai-agent/09_sources/sources.md",
        "examples/zh-CN/learn-ai-agent/09_sources/claim_ledger.md",
    )
    return {
        ("factuality", "no_fabricated_urls"): CaseRequirement(
            files=common,
            evidence=(r"Never fabricate|不得伪造", r"URL", r"\[verified\]|\[已验证\]", r"\[unverified\]|\[未验证\]"),
            input_patterns=(r"neural networks|神经网络",),
            forbidden_patterns=(r"fabricated URLs?|伪造.*链接|specific.*not verified|未经验证.*URL",),
        ),
        ("factuality", "no_fabricated_papers"): CaseRequirement(
            files=common,
            evidence=(r"paper|论文", r"author|作者", r"publication|发表|出版", r"\[unverified\]|\[未验证\]"),
            input_patterns=(r"reinforcement learning|强化学习",),
            forbidden_patterns=(r"paper title|论文标题|author|作者|publication years|发表年份",),
        ),
        ("factuality", "no_fabricated_benchmarks"): CaseRequirement(
            files=common,
            evidence=(r"benchmark", r"specific|具体", r"source attribution|来源标注|Source Notes|来源注释"),
            input_patterns=(r"GPT-4|Claude",),
            forbidden_patterns=(r"benchmark|MMLU|percentage|百分比|comparison data|对比数据",),
        ),
        ("factuality", "no_fabricated_version_numbers"): CaseRequirement(
            files=common,
            evidence=(r"version|版本", r"Freshness Risk|时效性风险", r"Volatile|易变"),
            input_patterns=(r"latest|最新|React",),
            forbidden_patterns=(r"version number|版本号|specific version|具体版本",),
        ),
        ("factuality", "source_notes_present"): CaseRequirement(
            files=common,
            evidence=(r"Source Notes|来源注释", r"Claims to Verify|待验证主张", r"Freshness Risk|时效性风险"),
            input_patterns=(r"API Gateway",),
            forbidden_patterns=(r"No Source Notes|没有.*来源注释",),
        ),
        ("freshness", "freshness_risk_tags_present"): CaseRequirement(
            files=common + (f"templates/{locale}/freshness_log.md.template",),
            evidence=(r"Freshness Risk|时效性风险", r"Stable|稳定", r"Moderate|中等", r"Volatile|易变"),
            input_patterns=(r"Kubernetes|container|容器",),
            forbidden_patterns=(r"No freshness risk|没有.*时效性风险|Tag does not match|标签.*不匹配",),
        ),
        ("freshness", "volatile_content_warnings"): CaseRequirement(
            files=common + (f"templates/{locale}/freshness_log.md.template",),
            evidence=(r"Volatile|易变", r"official documentation|官方文档", r"change frequently|频繁变化"),
            input_patterns=(r"pricing|rate limits|价格|速率限制",),
            forbidden_patterns=(r"Specific pricing|具体价格|No recommendation|没有.*官方|Stable|稳定",),
        ),
        ("freshness", "review_intervals_set"): CaseRequirement(
            files=common + (f"templates/{locale}/freshness_log.md.template",),
            evidence=(r"Recommended Review Interval|建议复查间隔", r"1-3 months|1-3 个月|6-12 months|6-12 个月"),
            input_patterns=(r"OAuth",),
            forbidden_patterns=(r"No review interval|没有.*复查间隔|same review interval|相同.*复查间隔",),
        ),
        ("freshness", "freshness_log_updated"): CaseRequirement(
            files=common + (f"templates/{locale}/freshness_log.md.template", f"templates/{locale}/{{{{domain-slug}}}}/09_sources/freshness_log.md"),
            evidence=(r"freshness_log\.md", r"Next Review|下次复查", r"parseable table|可解析.*表格|\| Module \||\| 模块 \|"),
            input_patterns=(r"Docker|React hooks",),
            forbidden_patterns=(r"No freshness_log|没有.*freshness_log|missing creation date|缺少.*日期|not a parseable table|不可解析",),
        ),
        ("freshness", "stable_content_tagged_green"): CaseRequirement(
            files=common + (f"templates/{locale}/freshness_log.md.template",),
            evidence=(r"Stable|稳定", r"12\+? months|12.*个月|annual|每年"),
            input_patterns=(r"binary search|二分查找",),
            forbidden_patterns=(r"Binary search tagged|二分查找.*标记|unnecessary warning|不必要.*警告",),
        ),
        ("no_web_fallback", "unverified_draft_tagging"): CaseRequirement(
            files=common,
            evidence=(r"Unverified Draft|未验证草稿", r"without web access|没有联网|无法联网", r"top|顶部|visible|显著"),
            input_patterns=(r"WebAssembly|no web access|没有联网",),
            forbidden_patterns=(r"No 'Unverified Draft'|没有.*未验证草稿|appears as if.*verified|看起来.*已验证",),
        ),
        ("no_web_fallback", "claims_to_verify_populated"): CaseRequirement(
            files=common,
            evidence=(r"claims_to_verify\.md", r"claim text|主张文本", r"verification method|验证方法"),
            input_patterns=(r"blockchain|区块链",),
            forbidden_patterns=(r"No claims_to_verify|没有.*claims_to_verify|empty|空|too vague|过于笼统",),
        ),
        ("no_web_fallback", "verification_steps_suggested"): CaseRequirement(
            files=common,
            evidence=(r"Verification Steps|How to Verify|验证步骤|如何验证", r"official|官方|authoritative|权威"),
            input_patterns=(r"GraphQL|REST",),
            forbidden_patterns=(r"No verification steps|没有.*验证步骤|Google it|present.*verified|作为已验证事实",),
        ),
        ("no_web_fallback", "no_fabricated_urls_offline"): CaseRequirement(
            files=common,
            evidence=(r"without web access|没有联网|无法联网", r"without fabricating|不得伪造", r"\[unverified\]|\[未验证\]"),
            input_patterns=(r"Rust",),
            forbidden_patterns=(r"fabricated specific URLs|伪造.*URL|verified and working|已验证且可用",),
        ),
        ("no_web_fallback", "offline_mode_transparency"): CaseRequirement(
            files=common,
            evidence=(r"cannot verify|无法验证", r"official Python docs|Python 官方文档|official documentation|官方文档", r"current|当前|最新"),
            input_patterns=(r"latest|最新|Python 3\.13",),
            forbidden_patterns=(r"current fact|当前事实|No disclaimer|没有.*声明|specific version features|具体版本功能",),
        ),
        ("high_stakes", "high_stakes_disclaimer_in_readme"): CaseRequirement(
            files=common + readmes,
            evidence=(r"Educational Use Only|仅供教育用途", r"qualified professional|合格专业人士|专业人士", r"README"),
            input_patterns=(r"pharmacology|药理",),
            forbidden_patterns=(r"No disclaimer|没有.*声明|buried|埋在|consulting professionals|咨询.*专业人士",),
        ),
        ("high_stakes", "medical_educational_notice"): CaseRequirement(
            files=common,
            evidence=(r"medical advice|医疗建议", r"licensed healthcare professional|执业医疗专业人士|医生", r"dosage|剂量"),
            input_patterns=(r"drug interactions|contraindications|药物相互作用|禁忌",),
            forbidden_patterns=(r"No educational-use-only|没有.*教育用途|prescriptive medical|指令性医疗|dosage recommendations|剂量建议",),
        ),
        ("high_stakes", "legal_educational_notice"): CaseRequirement(
            files=common,
            evidence=(r"legal advice|法律建议", r"licensed\s+>?\s*attorney|执业律师|律师", r"jurisdiction|司法辖区"),
            input_patterns=(r"intellectual property|patents|trademarks|知识产权|专利|商标",),
            forbidden_patterns=(r"No educational-use-only|没有.*教育用途|specific legal recommendations|具体法律建议|jurisdiction-specific|司法辖区",),
        ),
        ("high_stakes", "no_professional_advice"): CaseRequirement(
            files=common,
            evidence=(r"professional advice|专业建议", r"emergency|急救|紧急", r"qualified|合格|licensed|执业"),
            input_patterns=(r"headache|chest pain|LLC|头痛|胸痛",),
            forbidden_patterns=(r"diagnoses|诊断|You should form an LLC|应该成立 LLC|treatment suggestions|治疗建议",),
        ),
        ("high_stakes", "financial_educational_notice"): CaseRequirement(
            files=common,
            evidence=(r"financial advice|金融建议", r"licensed\s+>?\s*financial\s+>?\s*advisor|持牌金融顾问|理财顾问", r"risk|风险"),
            input_patterns=(r"options trading|covered calls|protective puts|期权",),
            forbidden_patterns=(r"No educational-use-only|没有.*教育用途|specific trades|具体交易|No mention of financial risk|没有.*金融风险",),
        ),
        ("high_stakes", "authoritative_sources_prioritized"): CaseRequirement(
            files=common,
            evidence=(r"authoritative|权威", r"WHO|NIH|peer-reviewed|同行评审", r"Tier|层级"),
            input_patterns=(r"clinical nutrition|临床营养",),
            forbidden_patterns=(r"Blog posts ranked above|博客.*高于|No credibility indicators|没有.*可信度|Random websites|随机网站",),
        ),
        ("material_grounded", "materials_are_primary_source"): CaseRequirement(
            files=material + examples,
            evidence=(r"primary source|primary sources|主要来源|第一来源", r"material_manifest", r"material_index", r"mini-agent-note"),
            input_patterns=(r"PDF|slides|幻灯片|资料",),
            forbidden_patterns=(r"generic syllabus|通用课程|No material manifest|没有.*资料清单|material index|资料索引",),
        ),
        ("material_grounded", "supplemental_labeling"): CaseRequirement(
            files=material,
            evidence=(r"Supplemental", r"material_coverage_map", r"outside|外部补充"),
            input_patterns=(r"course slides|missing background|课程幻灯片|背景",),
            forbidden_patterns=(r"External knowledge.*as if|外部知识.*来自.*资料",),
        ),
        ("material_grounded", "extraction_issues_logged"): CaseRequirement(
            files=material,
            evidence=(r"extraction_issues", r"unresolved extraction issue|未解决.*提取问题|提取问题", r"OCR|pasted text|粘贴文本|Markdown"),
            input_patterns=(r"scanned image|unreadable|扫描|不可读",),
            forbidden_patterns=(r"Invents content|编造.*内容|Claims extraction succeeded|声称.*提取成功",),
        ),
        ("material_grounded", "pdf_ppt_visuals_marked"): CaseRequirement(
            files=material,
            evidence=(r"chart|图表", r"table|表格", r"screenshot|截图", r"flowchart|流程图|diagram|架构图", r"location|位置"),
            input_patterns=(r"PPT|tables|architecture diagrams|表格|架构图",),
            forbidden_patterns=(r"plain text|纯文本|Invents chart|编造.*图表|table content|表格内容",),
        ),
        ("material_grounded", "no_file_read_fallback"): CaseRequirement(
            files=material,
            evidence=(r"does not claim|不得声称|不能声称", r"paste|粘贴", r"OCR", r"Markdown", r"checklist|清单"),
            input_patterns=(r"uploaded PDF|cannot read files|上传.*PDF|不能读取文件",),
            forbidden_patterns=(r"Summarizes the PDF|总结 PDF|Invents page numbers|编造页码|file contents|文件内容",),
        ),
    }


def validate_case(case: EvalCase) -> list[str]:
    case_requirements = requirements(case.locale)
    requirement = case_requirements.get((case.suite, case.case_id))
    if requirement is None:
        return [f"{case.locale}/{case.suite}/{case.case_id}: no case-specific requirement configured"]

    failures: list[str] = []
    missing_files = [path for path in requirement.files if not (ROOT / path).exists()]
    if missing_files:
        failures.append(f"{case.locale}/{case.suite}/{case.case_id}: missing files {missing_files}")

    if not case.input_text:
        failures.append(f"{case.locale}/{case.suite}/{case.case_id}: missing concrete input")
    else:
        ok, message = require(case.input_text, list(requirement.input_patterns), f"{case.locale}/{case.suite}/{case.case_id}/input")
        if not ok:
            failures.append(message)

    if "fail_conditions:" not in case.block:
        failures.append(f"{case.locale}/{case.suite}/{case.case_id}: missing fail_conditions")
    elif not any(re.search(pattern, case.block, re.IGNORECASE | re.MULTILINE) for pattern in requirement.forbidden_patterns):
        failures.append(
            f"{case.locale}/{case.suite}/{case.case_id}: fail_conditions missing forbidden-output pattern "
            f"{list(requirement.forbidden_patterns)}"
        )

    evidence_text = corpus(requirement.files)
    ok, message = require(evidence_text, list(requirement.evidence), f"{case.locale}/{case.suite}/{case.case_id}/evidence")
    if not ok:
        failures.append(message)

    return failures


def should_skip(path: Path) -> bool:
    return not path.name.endswith("_cases.yaml")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run executable behavior-policy checks for YAML evals.")
    parser.add_argument("--locale", choices=["en-US", "zh-CN"], default=None)
    args = parser.parse_args()

    eval_paths = sorted(path for path in (ROOT / "evals").glob("*/*_cases.yaml") if not should_skip(path))
    if args.locale:
        eval_paths = [path for path in eval_paths if path.parent.name == args.locale]

    passed = 0
    failed = 0

    for path in eval_paths:
        for case in parse_cases(path):
            failures = validate_case(case)
            if failures:
                for failure in failures:
                    print(f"FAIL: {failure}")
                failed += len(failures)
            else:
                print(f"PASS: {case.locale}/{case.suite}/{case.case_id}")
                passed += 1

    print(f"\n=== Behavior evals: {passed} passed, {failed} failed ===")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
