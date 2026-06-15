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


def cn_platform_files(platform: str) -> tuple[str, ...]:
    base = f"platforms/cn/{platform}"
    files = {
        "coze": (
            f"{base}/README.zh-CN.md",
            f"{base}/bot-prompt.zh-CN.md",
            f"{base}/workflow-blueprint.md",
            f"{base}/knowledge-base-package.md",
            f"{base}/variables-schema.md",
            f"{base}/memory-schema.md",
            f"{base}/material-upload-flow.md",
            f"{base}/reliability-flow.md",
            f"{base}/publishing-checklist.md",
        ),
        "workbuddy": (
            f"{base}/README.zh-CN.md",
            f"{base}/skill-call-prompt.zh-CN.md",
            f"{base}/task-workflow.md",
            f"{base}/knowledge-base-package.md",
            f"{base}/file-processing-rules.md",
            f"{base}/report-output-template.md",
            f"{base}/publishing-checklist.md",
        ),
        "trae": (
            f"{base}/README.zh-CN.md",
            f"{base}/project_rules.md",
            f"{base}/user_rules.md",
            f"{base}/agent-prompt.md",
            f"{base}/setup-guide.md",
            f"{base}/commands.md",
        ),
        "codebuddy": (
            f"{base}/README.zh-CN.md",
            f"{base}/knowledge-base-upload-guide.md",
            f"{base}/agent-rules.md",
            f"{base}/setup-guide.md",
            f"{base}/test-checklist.md",
        ),
        "generic-lowcode-agent": (
            f"{base}/README.zh-CN.md",
            f"{base}/system-prompt.zh-CN.md",
            f"{base}/workflow-template.md",
            f"{base}/knowledge-base-template.md",
            f"{base}/state-schema.md",
            f"{base}/fallback-mode.md",
        ),
    }
    return files[platform]


def base_learning_files(locale: str) -> tuple[str, ...]:
    return (
        "SKILL.md",
        f"core/prompts/{locale}/init-repo.md",
        f"core/prompts/{locale}/knowledge-map.md",
        f"core/prompts/{locale}/concept-breakdown.md",
        f"core/prompts/{locale}/daily-session.md",
        f"core/prompts/{locale}/daily-review.md",
        f"core/prompts/{locale}/error-diagnosis.md",
        f"core/prompts/{locale}/stage-test.md",
        f"core/prompts/{locale}/project-design.md",
        f"core/prompts/{locale}/resume-session.md",
        f"templates/{locale}/{{{{domain-slug}}}}/progress.md",
        f"templates/{locale}/{{{{domain-slug}}}}/AGENTS.md",
        f"templates/{locale}/{{{{domain-slug}}}}/CLAUDE.md",
        f"examples/{locale}/learn-ai-agent/progress.md",
    )


def guided_learning_files(locale: str) -> tuple[str, ...]:
    return (
        "SKILL.md",
        f"prompts/{locale}/start-guided-session.md",
        f"references/{locale}/guided-learning-mode.md",
        f"core/prompts/{locale}/init-repo.md",
        f"core/prompts/{locale}/daily-session.md",
        f"core/prompts/{locale}/daily-review.md",
        f"prompts/{locale}/material-grounded-learning-repo.md",
        f"templates/{locale}/today.md.template",
        f"templates/{locale}/start_here.md.template",
        f"templates/{locale}/{{{{domain-slug}}}}/START_HERE.md",
        f"templates/{locale}/{{{{domain-slug}}}}/TODAY.md",
        f"templates/{locale}/{{{{domain-slug}}}}/07_daily_review/day-01.md",
        f"examples/{locale}/guided-learning-session.md",
        "README.md",
        "README.zh-CN.md",
        "adapters/codex.md",
        "adapters/claude-code.md",
        "adapters/cursor.md",
        "adapters/chatgpt.md",
    )


def requirements(locale: str) -> dict[tuple[str, str], CaseRequirement]:
    common = base_files(locale)
    material = material_files(locale)
    base_learning = base_learning_files(locale)
    guided = guided_learning_files(locale)
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
        ("base_learning", "TC01"): CaseRequirement(
            files=base_learning,
            evidence=(r"Domain|领域", r"Background|基础|背景", r"daily_time|每天|每日", r"final_artifact|最终", r"interface_language", r"learning_language"),
            input_patterns=(r"learn|学习", r"nutrition|营养学"),
            forbidden_patterns=(r"knowledge map|知识地图", r"assumes defaults|默认值"),
        ),
        ("base_learning", "TC02"): CaseRequirement(
            files=base_learning,
            evidence=(r"README\.md", r"AGENTS\.md", r"CLAUDE\.md", r"progress\.md", r"progress-log\.md", r"01_core_concepts", r"09_sources"),
            input_patterns=(r"AI Agent", r"beginner|初学者"),
            forbidden_patterns=(r"Missing any required|缺少任何", r"directory listing|目录列表"),
        ),
        ("base_learning", "TC03"): CaseRequirement(
            files=base_learning,
            evidence=(r"knowledge map|知识地图", r"Feynman|费曼", r"20-60-20", r"What NOT to learn|不要学什么", r"learning order|学习顺序"),
            input_patterns=(r"knowledge-map\.md|知识地图", r"00_domain_map\.md"),
            forbidden_patterns=(r"Missing any|缺少", r"empty|为空"),
        ),
        ("base_learning", "TC04"): CaseRequirement(
            files=base_learning,
            evidence=(r"One-line|一句话", r"Life Analogy|生活类比", r"Technical|技术", r"Real-world Case|真实案例", r"Common Pitfall|常见误区", r"Exercise|练习"),
            input_patterns=(r"concept-breakdown\.md", r"01_core_concepts|概念文件"),
            forbidden_patterns=(r"Missing any|缺少", r"pure prose|纯文字"),
        ),
        ("base_learning", "TC05"): CaseRequirement(
            files=base_learning,
            evidence=(r"review|复习", r"learn|学习", r"practice|练习", r"output|输出", r"answers|答案", r"acceptance criteria|验收标准"),
            input_patterns=(r"Day 3|第 3 天", r"daily-session\.md"),
            forbidden_patterns=(r"prose-only|只有文字", r"reveals quiz answers|给出了答案"),
        ),
        ("base_learning", "TC06"): CaseRequirement(
            files=base_learning,
            evidence=(r"\[concept-gap\]", r"\[application-failure\]", r"\[expression-unclear\]", r"\[knowledge-confusion\]", r"remedial|补救"),
            input_patterns=(r"tool schema|Tool schema", r"name|名称", r"description|描述"),
            forbidden_patterns=(r"without diagnosing|未诊断", r"generic remediation|通用补救"),
        ),
        ("base_learning", "TC07"): CaseRequirement(
            files=base_learning,
            evidence=(r"examiner|考官", r"100", r"wait|等待", r"06_quizzes", r"weak points|薄弱点"),
            input_patterns=(r"stage-test\.md", r"Stage 1|第 1 阶段"),
            forbidden_patterns=(r"gives answers|给出答案", r"grades before|提前评分"),
        ),
        ("base_learning", "TC08"): CaseRequirement(
            files=base_learning,
            evidence=(r"progress\.md", r"progress-log\.md", r"07_daily_review", r"append|追加", r"Error|错题|错误"),
            input_patterns=(r"daily-review\.md", r"review|复盘"),
            forbidden_patterns=(r"not updated|没有更新", r"overwritten|覆盖"),
        ),
        ("base_learning", "TC09"): CaseRequirement(
            files=base_learning,
            evidence=(r"capstone|结业|最终项目", r"7-day|7 天", r"acceptance criteria|验收标准", r"no-code|无代码|低代码", r"weak points|薄弱点"),
            input_patterns=(r"project-design\.md", r"personal research assistant|个人研究助手"),
            forbidden_patterns=(r"No 7-day|没有 7 天", r"No acceptance|没有验收"),
        ),
        ("base_learning", "TC10"): CaseRequirement(
            files=base_learning,
            evidence=(r"progress\.md", r"progress-log\.md", r"warm-up|热身", r"continue|继续", r"review|复习"),
            input_patterns=(r"two weeks|两周", r"continue|继续"),
            forbidden_patterns=(r"without checking progress|不检查 progress", r"from day 1|第 1 天重新"),
        ),
        ("guided_learning", "create_repo_starts_day_1"): CaseRequirement(
            files=guided,
            evidence=(
                r"Guided Learning Mode|陪跑学习模式",
                r"do not stop after (a )?file summary|不得只输出文件清单|不要只列文件清单",
                r"start Day 1|开始第 1 天|第 1 天",
                r"today'?s? learning goal|今日目标|第 1 天目标",
                r"beginner-friendly|清楚解释|直白解释|陪跑式教学模式",
                r"one small task|一个小任务|一个聊天小任务",
                r"answer template|作答模板|复制这个模板",
                r"completion criteria|完成标准",
                r"reply (directly )?in chat|聊天里回复|直接发给我",
                r"progress\.md",
            ),
            input_patterns=(r"harness", r"technical beginner|刚开始接触|零基础", r"7 days|7 天", r"1 hour|1 小时"),
            forbidden_patterns=(r"only lists generated files|只列出生成文件|file summary.*stops|文件清单后停止",),
        ),
        ("guided_learning", "explicit_scaffold_only"): CaseRequirement(
            files=guided,
            evidence=(r"scaffold only", r"generate files only", r"只创建项目", r"不要开始学习", r"must_not_start_guided_session|scaffold-only"),
            input_patterns=(r"scaffold only|只创建", r"Do not start learning|不要开始学习"),
            forbidden_patterns=(r"starts a guided Day 1|仍启动第 1 天|despite.*scaffold-only",),
        ),
        ("guided_learning", "non_technical_user"): CaseRequirement(
            files=guided,
            evidence=(r"content creator|内容创作者", r"no code|cannot code|不会代码", r"Beginner-Friendly Guided Mode", r"content workflow|内容工作流|用户目标", r"Do not require code|不要求写代码|不要求用户写代码"),
            input_patterns=(r"content creator|内容创作者", r"cannot code|不会代码", r"prompt evaluation"),
            forbidden_patterns=(r"write code as the default task|默认要求.*写代码|multiple major tasks|多个主要任务",),
        ),
        ("guided_learning", "complete_beginner_content_creator_interactive_lesson"): CaseRequirement(
            files=guided,
            evidence=(
                r"Interactive Beginner Lesson Mode",
                r"complete beginner",
                r"no coding background",
                r"content creation workflow|content workflow",
                r"You do not need to open the files first",
                r"Today, learn just one sentence first|one plain",
                r"fully worked example|worked example",
                r"bad example",
                r"better example|improved example",
                r"one workflow step",
                r"answer template|Copy this template",
                r"send it to me directly|reply directly",
            ),
            input_patterns=(r"harness design", r"complete beginner", r"content creation workflow", r"Daily time: 1 hour"),
            forbidden_patterns=(r"three abstract concepts|3 concepts", r"write three or more workflow steps", r"open Markdown files first"),
        ),
        ("guided_learning", "material_learning_mode"): CaseRequirement(
            files=guided,
            evidence=(r"material index|资料索引|material_index", r"start guided|start Day 1|开始第 1 天|陪跑学习", r"do not need to open the files first|不用先翻文件|不用先打开文件", r"material-grounded|基于资料"),
            input_patterns=(r"PDF", r"uploaded|上传"),
            forbidden_patterns=(r"stops after material_manifest|material_index.*file summary|文件清单后停止|requires.*open files|要求用户先打开文件",),
        ),
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
        ("freshness_notice", "fund_investing_beginner_notice"): CaseRequirement(
            files=common
            + readmes
            + (
                f"prompts/{locale}/start-guided-session.md",
                f"templates/{locale}/freshness_notice.md.template",
                f"core/prompts/{locale}/init-repo.md",
            ),
            evidence=(
                r"Freshness Notice|时效性提醒",
                r"09_sources/freshness_log\.md",
                r"09_sources/claims_to_verify\.md",
                r"finance|investment|金融|投资",
                r"final professional advice|最终专业建议|not.*final.*advice|不要.*最终建议",
                r"Day 1|第 1 天",
            ),
            input_patterns=(r"基金投资|fund investing", r"理财小白|beginner", r"40 分钟|40 minutes"),
            forbidden_patterns=(r"guaranteed accuracy|完全准确|final investment advice|最终投资建议|stops before starting Day 1|没有继续进入第 1 天",),
        ),
        ("freshness_notice", "openai_api_fast_changing_notice"): CaseRequirement(
            files=common
            + readmes
            + (
                f"prompts/{locale}/start-guided-session.md",
                f"templates/{locale}/freshness_notice.md.template",
                f"core/prompts/{locale}/init-repo.md",
            ),
            evidence=(
                r"Freshness Notice|时效性提醒",
                r"AI tools|APIs|API",
                r"official|authoritative|官方|权威",
                r"source status|Overall freshness status|整体时效状态|Last Verified|最后验证",
                r"not fully verified|未完成实时核查|no-web|no-retrieval|没有联网",
                r"09_sources/freshness_log\.md",
            ),
            input_patterns=(r"OpenAI API", r"beginner", r"1 hour"),
            forbidden_patterns=(r"latest without source|最新.*没有来源|claims latest|声称最新",),
        ),
        ("freshness_notice", "basic_algebra_short_notice"): CaseRequirement(
            files=common
            + (
                f"prompts/{locale}/start-guided-session.md",
                f"templates/{locale}/freshness_notice.md.template",
            ),
            evidence=(
                r"stable foundational|稳定基础知识",
                r"Keep it short|提醒不能压过|short Freshness Notice|简短",
                r"Day 1|第 1 天",
            ),
            input_patterns=(r"basic algebra", r"beginner", r"30 minutes"),
            forbidden_patterns=(r"high-risk warning|高风险.*基础代数|overwarn|过度警告",),
        ),
        ("freshness_notice", "material_grounded_freshness_notice"): CaseRequirement(
            files=common
            + material
            + (
                f"prompts/{locale}/start-guided-session.md",
                f"templates/{locale}/freshness_notice.md.template",
            ),
            evidence=(
                r"Freshness Notice|时效性提醒",
                r"primary source|primary sources|主要来源|用户资料是 primary source",
                r"Supplemental",
                r"claims_to_verify\.md",
                r"Day 1|第 1 天",
            ),
            input_patterns=(r"PDF", r"PPT", r"45 minutes|45 分钟|45分钟"),
            forbidden_patterns=(
                r"external background knowledge as if it came from the PDF or PPT|外部背景知识说成来自 PDF 或 PPT",
                r"omits Supplemental|没有标记为 Supplemental",
                r"stops before starting Day 1|没有继续进入第 1 天",
            ),
        ),
        ("freshness_notice", "no_web_no_retrieval_fallback_notice"): CaseRequirement(
            files=common
            + (
                f"prompts/{locale}/start-guided-session.md",
                f"templates/{locale}/freshness_notice.md.template",
                f"core/prompts/{locale}/init-repo.md",
            ),
            evidence=(
                r"no-web|no-retrieval|web or retrieval|没有联网|实时检索|检索",
                r"not fully verified|未完成实时核查",
                r"official|authoritative|官方|权威",
                r"09_sources/freshness_log\.md",
                r"Day 1|第 1 天",
            ),
            input_patterns=(r"no web access|没有联网", r"no retrieval access|实时检索能力|没有实时检索"),
            forbidden_patterns=(
                r"verified current information without web or retrieval access|没有联网或检索也已经核查当前信息",
                r"omits.*not fully verified|没有说明.*未完成实时核查",
                r"omits 09_sources/freshness_log\.md|缺少 09_sources/freshness_log\.md",
            ),
        ),
        ("freshness_notice", "realtime_claim_trap_notice"): CaseRequirement(
            files=common
            + (
                f"prompts/{locale}/start-guided-session.md",
                f"templates/{locale}/freshness_notice.md.template",
                "harness/contracts/freshness-notice-contract.yaml",
            ),
            evidence=(
                r"latest|current|最新|当前",
                r"web or retrieval|联网|检索",
                r"official|authoritative|官方|权威",
                r"09_sources/claims_to_verify\.md",
                r"guaranteed latest|latest verified|已实时核查|已确认最新",
            ),
            input_patterns=(r"latest API|最新 API", r"pricing|价格", r"policy|政策", r"model|模型"),
            forbidden_patterns=(
                r"latest verified without explicit web or retrieval sources|没有明确联网或检索来源时说 latest verified",
                r"guaranteed latest|保证准确",
                r"fully verified or real-time verified|已实时核查或已确认最新",
            ),
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
        ("platform_coze", "coze_no_skill_md_dependency"): CaseRequirement(
            files=cn_platform_files("coze"),
            evidence=(r"bot-prompt\.zh-CN\.md", r"知识库", r"workflow|工作流", r"variables|变量", r"memory|记忆", r"checklist|检查清单", r"不能假设.*SKILL\.md|不要假设.*SKILL\.md"),
            input_patterns=(r"扣子|Coze", r"不能读取仓库文件|不能读取.*文件"),
            forbidden_patterns=(r"读取仓库根目录 SKILL\.md|直接读取 SKILL\.md|没有知识库|没有.*工作流"),
        ),
        ("platform_coze", "coze_material_grounding"): CaseRequirement(
            files=cn_platform_files("coze"),
            evidence=(r"资料 ID|material_id|material", r"上传|知识库", r"Grounded|Partially grounded|Supplemental", r"extraction issue|提取问题"),
            input_patterns=(r"PDF|资料", r"学习计划"),
            forbidden_patterns=(r"未读取资料就总结|编造页码|编造.*图表|编造.*资料内容"),
        ),
        ("platform_coze", "coze_reliability_fallback"): CaseRequirement(
            files=cn_platform_files("coze"),
            evidence=(r"未验证草稿|Unverified Draft", r"claims_to_verify|待核查", r"单 Bot 降级|无工作流", r"learning_state"),
            input_patterns=(r"没有联网|无联网", r"没有工作流|无工作流"),
            forbidden_patterns=(r"声称已核查最新事实|没有状态摘要"),
        ),
        ("platform_workbuddy", "workbuddy_task_skill_form"): CaseRequirement(
            files=cn_platform_files("workbuddy"),
            evidence=(r"skill-call-prompt\.zh-CN\.md", r"报告", r"task-workflow\.md|任务流", r"file-processing-rules\.md|文件处理", r"report-output-template\.md|报告输出", r"验收标准"),
            input_patterns=(r"培训资料|资料", r"30 天|阶段报告"),
            forbidden_patterns=(r"聊天式学习建议|没有报告输出模板"),
        ),
        ("platform_workbuddy", "workbuddy_file_processing"): CaseRequirement(
            files=cn_platform_files("workbuddy"),
            evidence=(r"文件 ID|资料 ID|ID", r"PDF|PPT|Word", r"表格|图示|备注", r"extraction issue|提取问题", r"位置|页码|幻灯片"),
            input_patterns=(r"PDF", r"PPT", r"Word", r"学习计划"),
            forbidden_patterns=(r"把图表当普通文本处理|无法读取时仍总结内容"),
        ),
        ("platform_workbuddy", "workbuddy_reliability_report"): CaseRequirement(
            files=cn_platform_files("workbuddy"),
            evidence=(r"未验证草稿|Unverified Draft", r"Source Notes|来源", r"Freshness Risk|时效", r"Claims to Verify|待核查", r"不伪造|不得伪造"),
            input_patterns=(r"阶段学习报告|阶段.*报告", r"不能联网|无联网"),
            forbidden_patterns=(r"声称已联网确认|缺少待核查清单"),
        ),
        ("platform_trae", "trae_reads_repository_files"): CaseRequirement(
            files=cn_platform_files("trae"),
            evidence=(r"SKILL\.md", r"core/", r"templates/", r"prompts/", r"references/", r"project_rules\.md", r"agent-prompt\.md", r"不要把所有平台说明塞回 `?SKILL\.md`?|不把平台说明塞进 SKILL\.md"),
            input_patterns=(r"Trae", r"本仓库|学习仓库"),
            forbidden_patterns=(r"忽略仓库文件|只复制低代码提示词|删除或重写 Codex Skill"),
        ),
        ("platform_trae", "trae_file_write_safety"): CaseRequirement(
            files=cn_platform_files("trae"),
            evidence=(r"检查目标目录|目录.*存在|已存在", r"不覆盖|不要覆盖", r"progress\.md", r"progress-log\.md", r"ASCII"),
            input_patterns=(r"learn-ai-agent", r"目录可能已存在"),
            forbidden_patterns=(r"覆盖已有学习仓库|删除用户内容"),
        ),
        ("platform_trae", "trae_fallbacks"): CaseRequirement(
            files=cn_platform_files("trae"),
            evidence=(r"OCR|粘贴文本|格式转换", r"未验证草稿|Unverified Draft", r"待核查|claims_to_verify", r"不编造|不得伪造"),
            input_patterns=(r"资料路径不可读|不可读", r"不能联网|无联网"),
            forbidden_patterns=(r"声称已读取不可读资料|写成已验证事实"),
        ),
        ("platform_codebuddy", "codebuddy_kb_package"): CaseRequirement(
            files=cn_platform_files("codebuddy"),
            evidence=(r"core/", r"references/zh-CN/", r"templates/zh-CN/", r"prompts/zh-CN/", r"知识库分组|分组"),
            input_patterns=(r"CodeBuddy", r"知识库"),
            forbidden_patterns=(r"只上传 SKILL\.md|没有模板或提示词分组"),
        ),
        ("platform_codebuddy", "codebuddy_repo_or_kb_mode"): CaseRequirement(
            files=cn_platform_files("codebuddy"),
            evidence=(r"仓库连接模式", r"知识库模式", r"不假装|不能读取本地仓库", r"learning_state", r"grounding|资料"),
            input_patterns=(r"CodeBuddy", r"只能用知识库|不能读取本地仓库"),
            forbidden_patterns=(r"要求读取本地 SKILL\.md|缺少降级说明"),
        ),
        ("platform_codebuddy", "codebuddy_behavior_rules"): CaseRequirement(
            files=cn_platform_files("codebuddy"),
            evidence=(r"资料.*登记|material", r"未验证草稿|无联网", r"不伪造|不得伪造", r"阶段测试|答案"),
            input_patterns=(r"上传资料|资料", r"无联网"),
            forbidden_patterns=(r"未核查事实写成确定结论|编造资料内容"),
        ),
        ("platform_generic_lowcode", "generic_lowcode_package_complete"): CaseRequirement(
            files=cn_platform_files("generic-lowcode-agent"),
            evidence=(r"system-prompt\.zh-CN\.md", r"workflow-template\.md", r"knowledge-base-template\.md", r"state-schema\.md", r"fallback-mode\.md"),
            input_patterns=(r"低代码 Agent|低代码.*平台", r"Learn Anything"),
            forbidden_patterns=(r"只有系统提示词|没有知识库上传说明"),
        ),
        ("platform_generic_lowcode", "generic_lowcode_learning_loop"): CaseRequirement(
            files=cn_platform_files("generic-lowcode-agent"),
            evidence=(r"intake|采集|画像", r"知识地图|学习计划", r"练习|任务", r"阶段测试|评分", r"复盘|learning_state"),
            input_patterns=(r"低代码 Agent", r"AI Agent"),
            forbidden_patterns=(r"泛泛学习建议|没有练习或任务"),
        ),
        ("platform_generic_lowcode", "generic_lowcode_fallbacks"): CaseRequirement(
            files=cn_platform_files("generic-lowcode-agent"),
            evidence=(r"粘贴|OCR|Markdown", r"未验证草稿", r"system prompt|系统提示词", r"learning_state"),
            input_patterns=(r"不能读文件|不能联网|没有长期记忆"),
            forbidden_patterns=(r"假装读过文件|没有状态摘要"),
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
