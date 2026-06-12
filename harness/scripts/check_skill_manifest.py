#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from checklib import Issue, fail, load_contract_lists, ok, parse_front_matter, read_text, run_check, warn


REQUIRED_SECTIONS = [
    "Do Not Use When",
    "Workflow",
    "Language and Locale Policy",
    "Source-First Reliability Policy",
    "Material-Grounded Learning Mode",
    "Agent Capability Fallback",
    "Safety and Source Rules",
    "Privacy",
]

FORBIDDEN = [
    "completely avoid hallucinations",
    "fully eliminate hallucinations",
    "完全避免幻觉",
    "彻底杜绝幻觉",
]


def check(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    contract = load_contract_lists(root, "skill-contract.yaml")
    required_sections = contract.get("required_sections") or REQUIRED_SECTIONS
    forbidden_terms = contract.get("forbidden_terms") or FORBIDDEN
    path = root / "SKILL.md"
    if not path.exists():
        return [fail("SKILL_MISSING", "SKILL.md", "SKILL.md is missing", "Restore SKILL.md")]

    text = read_text(path)
    front_matter, body = parse_front_matter(text)
    if front_matter is None:
        issues.append(fail("SKILL_FRONT_MATTER_MISSING", "SKILL.md", "YAML front matter is missing", "Add --- YAML front matter with name and description"))
    else:
        for field in ("name", "description"):
            if not front_matter.get(field):
                issues.append(fail("SKILL_FIELD_MISSING", "SKILL.md", f"Missing front matter field: {field}", f"Add `{field}` to SKILL.md front matter"))
        description = front_matter.get("description", "")
        if len(description) > 1200:
            issues.append(warn("SKILL_DESCRIPTION_LONG", "SKILL.md", "Description is long for trigger metadata", "Shorten description while preserving trigger coverage"))

    for section in required_sections:
        if section not in body and section not in text:
            issues.append(fail("SKILL_SECTION_MISSING", "SKILL.md", f"Missing required section or equivalent: {section}", "Add or rename the section so the contract is explicit"))

    lower = text.lower()
    for term in forbidden_terms:
        if term.lower() in lower:
            issues.append(fail("SKILL_EXAGGERATED_CLAIM", "SKILL.md", f"Exaggerated guarantee found: {term}", "Replace absolute guarantee with bounded reliability wording"))

    if not issues:
        issues.append(ok("SKILL_MANIFEST_OK", "SKILL.md", "Skill manifest and required sections look valid"))
    return issues


if __name__ == "__main__":
    raise SystemExit(run_check("Check native Skill manifest.", check))
