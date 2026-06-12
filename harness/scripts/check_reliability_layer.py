#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, read_text, run_check, warn


REQUIRED_PATHS = [
    "templates/en-US/sources.md.template",
    "templates/zh-CN/sources.md.template",
    "templates/en-US/source_notes.md.template",
    "templates/zh-CN/source_notes.md.template",
    "templates/en-US/claim_ledger.md.template",
    "templates/zh-CN/claim_ledger.md.template",
    "templates/en-US/claims_to_verify.md.template",
    "templates/zh-CN/claims_to_verify.md.template",
    "templates/en-US/freshness_log.md.template",
    "templates/zh-CN/freshness_log.md.template",
    "references/en-US/source-quality-policy.md",
    "references/zh-CN/source-quality-policy.md",
    "references/en-US/freshness-policy.md",
    "references/zh-CN/freshness-policy.md",
    "references/en-US/high-stakes-domain-policy.md",
    "references/zh-CN/high-stakes-domain-policy.md",
    "references/en-US/claim-verification-guide.md",
    "references/zh-CN/claim-verification-guide.md",
]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "reliability-contract.yaml")
    required_paths = sorted(set(REQUIRED_PATHS) | set(contract.get("required_paths", [])))
    corpus = ""
    for item in required_paths:
        path = root / item
        if not path.exists():
            issues.append(fail("RELIABILITY_FILE_MISSING", item, "Reliability file missing", "Add the required reliability template or reference"))
        else:
            corpus += "\n" + read_text(path)

    contract_terms = contract.get("required_terms") or []
    required_terms = [
        ("Source Notes",),
        ("Freshness Risk",),
        ("Claims to Verify",),
        ("Last Verified",),
        ("no-web", "no web", "无联网"),
        ("high-stakes", "高风险"),
    ]
    zh_terms = [("来源",), ("时效",), ("待核查", "待验证"), ("无联网",), ("高风险",), ("伪造", "编造")]
    corpus_lower = corpus.lower()
    for term in contract_terms:
        if term.lower() not in corpus_lower:
            issues.append(warn("RELIABILITY_CONTRACT_TERM_WEAK", "harness/contracts/reliability-contract.yaml", f"Contract term not found in reliability corpus: {term}", "Connect the contract term to a reliability document or update the contract"))
    for terms in required_terms:
        if not any(term.lower() in corpus_lower for term in terms):
            issues.append(warn("RELIABILITY_TERM_WEAK", "reliability layer", f"Reliability corpus may not mention {'/'.join(terms)}", "Add explicit reliability wording"))
    for terms in zh_terms:
        if not any(term in corpus for term in terms):
            issues.append(warn("RELIABILITY_ZH_TERM_WEAK", "reliability layer", f"Chinese reliability corpus may not mention {'/'.join(terms)}", "Add explicit Chinese reliability wording"))

    fake_terms = ["fabricate", "伪造", "编造"]
    if not any(term in corpus_lower or term in corpus for term in fake_terms):
        issues.append(fail("RELIABILITY_FAKE_CITATION_RULE_MISSING", "references/", "No fake-citation prohibition found", "Add explicit no-fabricated-citation rules"))

    if not issues:
        issues.append(ok("RELIABILITY_LAYER_OK", "", "Reliability layer checks passed"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check reliability layer.", check))
