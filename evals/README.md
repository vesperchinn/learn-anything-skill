# Evals — Test Suite

Validation and behavior-policy tests for the Learn Anything Skill Pack.

**Coverage note**: Structural shell tests verify files, headings, and template
layout. `run_behavior_evals.py` does not call a real Agent. It makes the YAML
behavior cases executable by checking that must-pass policies are present across
SKILL.md, prompts, templates, references, adapters, and examples. These tests
are policy regression checks, not proof that a live multi-turn Agent completed
the learning loop. The v0.2.0 manual acceptance record is in
[`docs/acceptance-record-v0.2.0.md`](../docs/acceptance-record-v0.2.0.md);
live Agent outcome tests remain a v1.0 goal.

## Running Tests

```bash
# English locale tests (from repo root):
./evals/en-US/test-templates.sh
./evals/en-US/test-progress-format.sh
./evals/en-US/test-prompts.sh
python3 evals/run_behavior_evals.py --locale en-US

# Chinese locale tests (from repo root):
./evals/zh-CN/test-templates.sh
./evals/zh-CN/test-progress-format.sh
./evals/zh-CN/test-prompts.sh
python3 evals/run_behavior_evals.py --locale zh-CN

# Mock end-to-end smoke plus behavior gate:
python3 evals/run_e2e_evals.py --mode mock --locale en-US
python3 evals/run_e2e_evals.py --mode mock --locale zh-CN
```

## Test Descriptions

| Test | What it checks |
|------|---------------|
| `test-templates.sh` | Template directory structure is complete, all required files exist |
| `test-progress-format.sh` | progress.md has all 7 required sections in the correct language |
| `test-prompts.sh` | All core prompt files exist and contain required sections |
| `run_behavior_evals.py` | Executes YAML behavior cases as policy regression checks; does not call a live Agent |
| `run_e2e_evals.py --mode mock` | Scaffolds a repo, checks key files, and runs behavior evals |
| `factuality_cases.yaml` | Agents do not fabricate URLs, papers, benchmark data, version numbers, or source notes |
| `freshness_cases.yaml` | Generated modules include freshness risk and review intervals |
| `freshness_notice_cases.yaml` | Repository creation chat output includes a short Freshness Notice before Day 1 |
| `no_web_fallback_cases.yaml` | No-web mode produces unverified drafts and verification checklists |
| `high_stakes_cases.yaml` | Medical, legal, financial, and safety-critical topics include educational-use-only safeguards |
| `material_grounded_cases.yaml` | User materials are treated as primary sources; extraction issues and supplemental content are handled explicitly |

## Structure

```
evals/
├── README.md
├── run_behavior_evals.py           # executable behavior-policy checks
├── run_e2e_evals.py                # scaffold smoke + behavior gate
├── en-US/                          # English test suite
│   ├── test_cases.yaml             # 10 scenarios, 62 quality checks
│   ├── factuality_cases.yaml       # factuality and no-fabrication checks
│   ├── freshness_cases.yaml        # freshness risk checks
│   ├── freshness_notice_cases.yaml # repo-creation freshness notice checks
│   ├── no_web_fallback_cases.yaml  # no-web fallback checks
│   ├── high_stakes_cases.yaml      # high-stakes domain checks
│   ├── material_grounded_cases.yaml # material-grounded learning checks
│   ├── expected_outputs.md         # ✅ qualified vs ❌ unqualified examples
│   ├── test-templates.sh           # Template completeness (en-US headings)
│   ├── test-progress-format.sh     # Progress.md format (en-US headings)
│   └── test-prompts.sh             # Prompt file existence (en-US)
└── zh-CN/                          # Chinese test suite
    ├── test_cases.yaml             # 10 scenarios, 62 quality checks (zh-CN)
    ├── factuality_cases.yaml       # 事实准确性与禁止伪造检查
    ├── freshness_cases.yaml        # 时效性风险检查
    ├── freshness_notice_cases.yaml # 创建仓库后的时效性提醒检查
    ├── no_web_fallback_cases.yaml  # 无联网退化检查
    ├── high_stakes_cases.yaml      # 高风险领域检查
    ├── material_grounded_cases.yaml # 基于用户资料学习检查
    ├── expected_outputs.md         # ✅ qualified vs ❌ unqualified examples (zh-CN)
    ├── test-templates.sh           # Template completeness (zh-CN headings)
    ├── test-progress-format.sh     # Progress.md format (zh-CN headings)
    └── test-prompts.sh             # Prompt file existence (zh-CN)
```

## Adding Tests

Tests are simple shell scripts. Exit code 0 = pass, non-zero = fail. Output
that starts with `PASS:` or `FAIL:` is parsed by CI.

When adding a new test, create both an en-US and zh-CN version if the test
validates locale-specific content (e.g., section headings). For
locale-independent checks (e.g., file counts), a single test is sufficient.
