#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from checklib import Issue, fail, load_platform_contract_paths, ok, read_text, run_check, warn


PLATFORMS = {
    "codex": ["adapters/codex.md", "SKILL.md"],
    "claude-code": ["adapters/claude-code.md"],
    "cursor": ["adapters/cursor.md"],
    "chatgpt": ["adapters/chatgpt.md"],
    "generic-agent": ["adapters/generic-agent.md"],
    "coze": [
        "platforms/cn/coze/README.zh-CN.md",
        "platforms/cn/coze/bot-prompt.zh-CN.md",
        "platforms/cn/coze/workflow-blueprint.md",
        "platforms/cn/coze/knowledge-base-package.md",
        "platforms/cn/coze/variables-schema.md",
        "platforms/cn/coze/memory-schema.md",
        "platforms/cn/coze/material-upload-flow.md",
        "platforms/cn/coze/reliability-flow.md",
        "platforms/cn/coze/publishing-checklist.md",
    ],
    "workbuddy": [
        "platforms/cn/workbuddy/README.zh-CN.md",
        "platforms/cn/workbuddy/skill-call-prompt.zh-CN.md",
        "platforms/cn/workbuddy/task-workflow.md",
        "platforms/cn/workbuddy/knowledge-base-package.md",
        "platforms/cn/workbuddy/state-schema.md",
        "platforms/cn/workbuddy/file-processing-rules.md",
        "platforms/cn/workbuddy/report-output-template.md",
        "platforms/cn/workbuddy/publishing-checklist.md",
    ],
    "trae": [
        "platforms/cn/trae/README.zh-CN.md",
        "platforms/cn/trae/project_rules.md",
        "platforms/cn/trae/user_rules.md",
        "platforms/cn/trae/agent-prompt.md",
        "platforms/cn/trae/setup-guide.md",
        "platforms/cn/trae/commands.md",
    ],
    "codebuddy": [
        "platforms/cn/codebuddy/README.zh-CN.md",
        "platforms/cn/codebuddy/knowledge-base-upload-guide.md",
        "platforms/cn/codebuddy/workflow-template.md",
        "platforms/cn/codebuddy/state-schema.md",
        "platforms/cn/codebuddy/agent-rules.md",
        "platforms/cn/codebuddy/setup-guide.md",
        "platforms/cn/codebuddy/test-checklist.md",
    ],
    "generic-lowcode-agent": [
        "platforms/cn/generic-lowcode-agent/README.zh-CN.md",
        "platforms/cn/generic-lowcode-agent/system-prompt.zh-CN.md",
        "platforms/cn/generic-lowcode-agent/workflow-template.md",
        "platforms/cn/generic-lowcode-agent/knowledge-base-template.md",
        "platforms/cn/generic-lowcode-agent/state-schema.md",
        "platforms/cn/generic-lowcode-agent/fallback-mode.md",
        "platforms/cn/generic-lowcode-agent/test-checklist.md",
    ],
}


LOWCODE = ["coze", "workbuddy", "codebuddy", "generic-lowcode-agent"]
REQUIRED_LOWCODE_TERMS = [
    ("fallback", "降级"),
    ("无联网", "不能联网", "no web"),
    ("无法读取", "不能读取", "no file"),
    ("知识库", "knowledge base"),
]

CAPABILITY_PATTERNS = {
    "README": ("readme",),
    "prompt_or_rules": ("prompt", "rules"),
    "workflow_or_task_flow": ("workflow", "task-workflow", "commands"),
    "knowledge_base": ("knowledge",),
    "state_or_variables": ("schema", "variables", "memory", "state"),
    "fallback": ("fallback", "readme", "prompt", "rules"),
    "reliability": ("reliability", "rules", "prompt"),
    "material": ("material", "file-processing", "knowledge", "rules"),
    "checklist": ("checklist",),
}

CAPABILITY_TERMS = {
    "fallback": ("fallback", "降级", "无法读取", "无联网", "no web", "no-file"),
    "reliability": ("reliability", "来源", "时效", "未验证", "claims", "freshness"),
    "material": ("material", "资料", "PDF", "PPT", "OCR", "上传"),
}

RISKY_SKILL_DEPENDENCY_PATTERNS = [
    re.compile(r"直接读取.{0,16}SKILL\.md"),
    re.compile(r"读取.{0,16}根目录.{0,8}SKILL\.md"),
    re.compile(r"执行.{0,16}SKILL\.md"),
]
NEGATION_TERMS = ["不要", "不能", "不得", "不可", "不应", "不要假设", "不能假设", "do not", "cannot", "must not"]

COZE_README_FALLBACKS = {
    "file": ("没有文件读取", "无文件读取", "无法读取资料", "不能读取文件"),
    "web": ("没有联网", "无联网", "不能联网"),
    "workflow": ("没有工作流", "单 Bot 降级", "无工作流"),
}


def split_statements(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"[\n。；;!?]+", text) if part.strip()]


def has_risky_skill_dependency(text: str) -> bool:
    for statement in split_statements(text.replace("`", "")):
        if any(pattern.search(statement) for pattern in RISKY_SKILL_DEPENDENCY_PATTERNS):
            lower = statement.lower()
            if not any(term in statement or term in lower for term in NEGATION_TERMS):
                return True
    return False


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    platforms = load_platform_contract_paths(root) or PLATFORMS
    for platform, paths in platforms.items():
        corpus = ""
        for item in paths:
            path = root / item
            if not path.exists():
                issues.append(fail("PLATFORM_FILE_MISSING", item, f"{platform} adapter file missing", "Add the required adapter file"))
            else:
                corpus += "\n" + read_text(path)
        if platform in LOWCODE:
            existing_names = [Path(item).name.lower() for item in paths if (root / item).exists()]
            for capability, patterns in CAPABILITY_PATTERNS.items():
                if capability == "knowledge_base" and platform == "trae":
                    continue
                if not any(any(pattern in name for pattern in patterns) for name in existing_names):
                    issues.append(warn("PLATFORM_CAPABILITY_FILE_WEAK", platform, f"{platform} may lack a dedicated file for {capability}", "Add a dedicated adapter file or document the capability in README"))
            for capability, terms in CAPABILITY_TERMS.items():
                matched_files = [root / item for item in paths if (root / item).exists() and any(pattern in Path(item).name.lower() for pattern in CAPABILITY_PATTERNS.get(capability, ()))]
                if matched_files:
                    matched_text = "\n".join(read_text(path) for path in matched_files)
                    matched_lower = matched_text.lower()
                    if not any(term in matched_text or term.lower() in matched_lower for term in terms):
                        issues.append(warn("PLATFORM_CAPABILITY_CONTENT_WEAK", platform, f"{platform} {capability} files lack expected terms", "Add explicit behavior to the dedicated adapter file"))
        if platform in LOWCODE:
            corpus_lower = corpus.lower()
            for terms in REQUIRED_LOWCODE_TERMS:
                if not any(term in corpus or term.lower() in corpus_lower for term in terms):
                    issues.append(warn("PLATFORM_FALLBACK_WEAK", platform, f"{platform} adapter may not mention {'/'.join(terms)}", "Add explicit low-code fallback behavior"))
            if platform != "trae" and has_risky_skill_dependency(corpus):
                issues.append(fail("PLATFORM_CODEX_DEPENDENCY", platform, f"{platform} may depend on direct SKILL.md reading", "Split platform runtime into prompt, KB, workflow, and state docs"))
            if platform == "coze":
                readme_path = root / "platforms/cn/coze/README.zh-CN.md"
                if readme_path.exists():
                    readme = read_text(readme_path)
                    for capability, terms in COZE_README_FALLBACKS.items():
                        if not any(term in readme for term in terms):
                            issues.append(fail("PLATFORM_ENTRYPOINT_FALLBACK_MISSING", "platforms/cn/coze/README.zh-CN.md", f"Coze README missing {capability} fallback", "Document this fallback in the adapter entrypoint README"))

    if not (root / "platforms/capability-matrix.md").exists():
        issues.append(fail("PLATFORM_CAPABILITY_MATRIX_MISSING", "platforms/capability-matrix.md", "Capability matrix missing", "Add platform capability matrix"))

    if not issues:
        issues.append(ok("PLATFORM_ADAPTERS_OK", "", "Platform adapter checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check platform adapters.", check))
