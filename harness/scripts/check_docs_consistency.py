#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from checklib import Issue, fail, ok, read_text, run_check, warn


FORBIDDEN = ["completely avoid hallucinations", "fully eliminate hallucinations", "完全避免幻觉", "彻底杜绝幻觉"]
EXAGGERATED_PATTERNS = [
    re.compile(r"\b(completely|fully|entirely|totally)\s+\w*\s*(avoid|eliminate|prevent|remove|stop)s?\s+\w*\s*hallucinations?\b", re.IGNORECASE),
    re.compile(r"\b(eliminate|prevent|remove|stop)s?\s+\w*\s*(all|any|every|ai)?\s*\w*\s*hallucinations?\b", re.IGNORECASE),
    re.compile(r"(完全|彻底|百分百|100%)\s*(避免|消除|杜绝|防止).{0,8}(幻觉|胡编|编造)", re.IGNORECASE),
]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    docs = ["README.md", "README.zh-CN.md", "SKILL.md", "platforms/README.md", "platforms/capability-matrix.md"]
    corpus = ""
    for item in docs:
        path = root / item
        if not path.exists():
            issues.append(fail("DOC_FILE_MISSING", item, "Important doc missing", "Restore or update doc contract"))
        else:
            corpus += "\n" + read_text(path)

    terms = ["Material-Grounded", "Knowledge Reliability", "Coze", "WorkBuddy", "Trae", "CodeBuddy"]
    for term in terms:
        if term not in corpus:
            issues.append(warn("DOC_TERM_WEAK", "docs", f"Docs may not mention {term}", "Review docs for terminology consistency"))

    for item in ["README.md", "README.zh-CN.md"]:
        path = root / item
        if path.exists():
            raw_text = read_text(path)
            text = raw_text.lower()
            for term in FORBIDDEN:
                if term.lower() in text:
                    issues.append(fail("DOC_EXAGGERATED_CLAIM", item, f"Exaggerated claim found: {term}", "Replace with bounded reliability wording"))
            for pattern in EXAGGERATED_PATTERNS:
                if pattern.search(raw_text):
                    issues.append(fail("DOC_EXAGGERATED_CLAIM", item, "Exaggerated hallucination guarantee found", "Replace absolute guarantees with bounded reliability wording"))
                    break

    for item in ["core/prompts/en-US/init-repo.md", "core/prompts/zh-CN/init-repo.md"]:
        if not (root / item).exists():
            issues.append(fail("DOC_QUICK_START_TARGET_MISSING", item, "Quick start referenced prompt missing", "Update quick start or restore prompt"))

    if not issues:
        issues.append(ok("DOCS_CONSISTENCY_OK", "", "Docs consistency checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check docs consistency.", check))
