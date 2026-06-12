# Learn Anything Skill Pack

> Turn any AI agent from a Q&A bot into a domain learning engineer — a structured system for mastering any field.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0--beta-blue)](./CHANGELOG.md)
[![Locales](https://img.shields.io/badge/locales-en--US_|_zh--CN-blue)](./README.zh-CN.md)

[中文说明](./README.zh-CN.md)

## What is this?

**Learn Anything Skill Pack** is an open-source, cross-AI-agent learning system
toolkit. It bundles core prompts, learning repository templates, Skill
definitions, adapters, and automation scripts so that any AI agent with file
read/write or prompt-invocation capabilities (Codex, Claude Code, Cursor,
ChatGPT, and others) can help users:

- Scaffold a structured "domain learning repository" in 5 minutes
- Generate a knowledge map that shows the full landscape of a field
- Follow a 30-day plan with daily learn → practice → test → review cycles
- Get automatic error diagnosis with targeted remediation
- Pass a stage test every 7 days that verifies real understanding
- Complete a demonstrable capstone project
- Learn from your own PDFs, slide decks, Markdown, TXT, Word docs, and webpage exports

Current release: **v0.2.0-beta**. See [release notes](./docs/release-notes-v0.2.0.md)
and [roadmap](./ROADMAP.md).

## How is this different from asking ChatGPT directly?

| Asking ChatGPT directly | Using Learn Anything Skill Pack |
|------------------------|-------------------------------|
| One-off conversations, knowledge doesn't stick | Everything is file-based, stored in a structured repository |
| AI tends to output explanatory prose | Built-in exercise + quiz + project systems ensure hands-on practice |
| No idea what you've learned or where you are | `progress.md` continuously tracks progress and weak points |
| Reinvent the method for every new domain | One Skill Pack, reusable forever |
| Wrong answer → "here's the right one" | Four-type error diagnosis → targeted remedial exercises |
| AI may sound confident without sources | Knowledge Reliability Layer tracks sources, unverified claims, and freshness risk |

## Quick Start

### If the Skill is already installed in your agent

Type this in the chat box:

```
Use learn-anything to create a learning project for "AI Agents".
My background: beginner.
My goal: understand the basics and build a small project in 30 days.
Daily time: 1 hour.
```

The agent should create the learning repository, domain map, plan, daily
sessions, reviews, quizzes, and project practice from the Skill workflow.

If you already have PDFs, slides, notes, or course material, say:

```
Use learn-anything to create a learning project from my materials.
Prioritize the provided materials and mark anything that still needs verification.
```

### If the Skill is not installed yet

Put this repository somewhere your agent can read:

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

Then type:

```
Read learn-anything-skill/core/prompts/en-US/init-repo.md.
Create a learning repository for "AI Agents".
```

### If you prefer a command

```bash
./scripts/new-domain.sh "AI Agent" en-US
```

### How to continue

```
Continue with learn-anything. Read my progress and run today's learning session.
```

```
Continue with learn-anything. Review what I learned today and update my progress.
```

```
Continue with learn-anything. Give me a stage test. Ask questions first, then grade after I answer.
```

See [docs/quick-start.md](./docs/quick-start.md) for the full guide.

## Multi-Platform Support

Learn Anything now includes a **Platform Adapter Layer** for platforms that cannot consume the native Codex `SKILL.md` directly.
Low-code platform support is experimental in this beta; validate each adapter in your own workspace before relying on it.

| Form | Target platforms | How it works |
| --- | --- | --- |
| Native Codex Skill | Codex and file-based agents that can read this repo | Reads `SKILL.md`, `core/`, `templates/`, `prompts/`, and `references/`; writes the learning repo directly |
| Platform package | Coze, WorkBuddy, Trae, CodeBuddy, generic low-code agents | Uses platform-specific prompts, knowledge-base packages, workflows, variables, memory, and test checklists under `platforms/` |
| Chat-only package | Ordinary chat agents | Copies the core protocols and outputs path-labeled Markdown blocks |

See [platforms/README.md](./platforms/README.md), [platforms/capability-matrix.md](./platforms/capability-matrix.md), and [dist/README.md](./dist/README.md).

## Chinese Agent Platform Adapters

| Platform | Adapter | Recommended form | File writing | Main limitation |
| --- | --- | --- | --- | --- |
| Coze | [platforms/cn/coze/](./platforms/cn/coze/) | Bot + knowledge base + workflow + variables + memory | Usually no local file writing | Do not assume it can read `SKILL.md`; split into prompt, KB, workflow |
| WorkBuddy | [platforms/cn/workbuddy/](./platforms/cn/workbuddy/) | Office task Skill + report output | Depends on task environment | Best for reports, task sheets, and material processing |
| Trae | [platforms/cn/trae/](./platforms/cn/trae/) | File-based engineering Agent | Yes | Can preserve direct repo reading |
| CodeBuddy | [platforms/cn/codebuddy/](./platforms/cn/codebuddy/) | Code/document Agent + knowledge base | Yes when repo-connected | Package `references`, `templates`, and `prompts` into a KB |
| Generic low-code Agent | [platforms/cn/generic-lowcode-agent/](./platforms/cn/generic-lowcode-agent/) | System prompt + workflow + KB + state | Usually no | Needs explicit fallback for no file read, no web, or no workflow |

Capabilities differ by platform, product version, workspace policy, and enabled connectors. File-based agents can create and maintain a learning repository. Low-code platforms usually approximate the workflow through knowledge bases, workflows, variables, memory, and prompts. Chat-only agents can only output copyable Markdown and compact state summaries.

## Learn From Your Own Materials

If you already have course PDFs, slide decks, notes, documentation exports, or
webpage exports, use **Material-Grounded Learning Mode**:

1. Put original files in `learning_materials/raw/`, or tell the agent where the files are.
2. Run `prompts/{locale}/material-intake.md` to register and extract the materials.
3. Run `prompts/{locale}/material-grounded-learning-repo.md` to build the knowledge map, plan, concepts, quizzes, reviews, and progress tracking from those materials.
4. Use `material_coverage_map.md` to see which modules are grounded in the materials, partially grounded, or supplemental.

In this mode, user-provided materials are the primary source. Outside knowledge
must be labeled `Supplemental`. If a PDF/PPT chart, screenshot, table, or
flowchart cannot be extracted, the issue is recorded in
`learning_materials/extraction_issues.md` rather than guessed.

If the agent cannot read files, paste the text, provide OCR, convert the files
to Markdown/TXT, export slides as text plus images, or ask for a material
processing checklist.

### Privacy and Copyright Note

Do not put confidential company documents, contracts, private health or
financial records, paid course materials, unpublished manuscripts, or copyrighted
books into a public learning repository. Keep sensitive materials in a private
repo, remove personal data before extraction, and make sure you have the right
to store and transform the material.

## Directory Structure

```
learn-anything-skill/
├── SKILL.md                    # Skill entry point (routing file for agents)
├── README.md                   # English homepage (you are here)
├── README.zh-CN.md             # Chinese homepage
├── core/                       # Core prompts (agent-agnostic)
│   ├── prompts/
│   │   ├── en-US/              #   13 English prompt modules
│   │   └── zh-CN/              #   13 Chinese prompt modules
│   ├── *-protocol.*.md         #   Platform-neutral protocols
│   └── principles.md           #   Learning principles
├── templates/                  # Learning repo templates
│   ├── en-US/                  #   English (default)
│   └── zh-CN/                  #   Chinese
├── references/                 # Methodology references
│   ├── en-US/                  #   English
│   └── zh-CN/                  #   Chinese
├── examples/                   # Complete example repositories
│   ├── en-US/learn-ai-agent/   #   English example
│   └── zh-CN/learn-ai-agent/   #   Chinese example
├── adapters/                   # Cross-agent adaptation guides
├── platforms/                  # Platform adapters (Coze / WorkBuddy / Trae / CodeBuddy, etc.)
├── dist/                       # Distribution manifests and build notes
├── prompts/                    # Material-grounded learning prompts
├── skills/codex/               # Legacy wrapper / compatibility files
├── scripts/                    # Automation scripts
├── evals/                      # Test suites
│   ├── en-US/                  #   English eval cases
│   └── zh-CN/                  #   Chinese eval cases
└── docs/                       # User documentation
```

## Python Automation Scripts

We provide a suite of Python tools in the `scripts/` directory to enhance your learning experience:

- `init_learning_repo.py`: Cross-platform repository scaffolding (Windows/Mac/Linux).
- `generate_index.py`: Dynamically generates a Table of Contents (`index.md`) for your learning repository.
- `export_flashcards.py`: Extracts flashcards into an Anki-compatible CSV file.
- `validate_locale.py`: Detects "language bleed" (e.g. Chinese text in an English repo) using character heuristics.
- `check_unverified_claims.py`: Finds `[unverified]` and unverified-draft markers that still need review.
- `check_stale_modules.py`: Checks `09_sources/freshness_log.md` for modules past their review date.
- `check_source_notes.py`: Ensures learning modules include Source Notes, Freshness Risk, Claims to Verify, Last Verified, and Recommended Review Interval.

Both scaffolding scripts support `--dry-run` and refuse to overwrite an existing
`learn-{domain-slug}` directory.

## Maintenance Harness

The read-only maintenance guard layer lives in [harness/](./harness/). It is not a new learning feature; it helps maintainers catch structure drift, locale mismatch, platform adapter gaps, material-grounding gaps, and reliability-rule gaps before release.

Run all checks:

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

Reports are written to `harness/reports/` with timestamped filenames and never overwrite older reports. `PASS` means OK, `WARN` means human review is needed, and `FAIL` means the issue should be resolved before release.

Before changing `SKILL.md`, review [change-impact-matrix.md](./harness/architecture/change-impact-matrix.md) and run `check_skill_manifest.py`, `check_docs_consistency.py`, and `check_eval_coverage.py`. Before adding a platform adapter, use [platform-adapter-checklist.md](./harness/checklists/platform-adapter-checklist.md). Before release, use [release-checklist.md](./harness/checklists/release-checklist.md) and [release-gates.md](./harness/architecture/release-gates.md).

## Factuality, Freshness, and Hallucination Risk

Learn Anything includes a Knowledge Reliability Layer for generated learning repositories:

- **Source-first policy**: claims should be backed by primary or authoritative sources. The agent must not fabricate URLs, papers, publication dates, official documents, or benchmark results.
- **No source, no claim**: unsupported claims are marked `[unverified]` or moved to `09_sources/claims_to_verify.md`.
- **Freshness risk**: each module is tagged as 🟢 Stable, 🟡 Evolving, or 🔴 Volatile, with a recommended review interval.
- **No-web fallback**: if the agent cannot browse or search, generated material is labeled **Unverified Draft** and a verification checklist is produced.
- **High-stakes domains**: medical, legal, financial, safety-critical, cybersecurity, and certification content requires an educational-use-only notice and authoritative sources first.
- **Private or copyrighted materials**: keep them out of public repositories unless you have permission and have removed sensitive data.

## Supported Agents

| Agent | Support Level | Adapter |
|-------|-------------|---------|
| **Codex** | Full (native Skill) | [codex.md](./adapters/codex.md) |
| **Claude Code** | Documented workflow (CLAUDE.md) | [claude-code.md](./adapters/claude-code.md) |
| **Cursor** | Documented workflow (.cursorrules) | [cursor.md](./adapters/cursor.md) |
| **ChatGPT** | Copy-paste prompts | [chatgpt.md](./adapters/chatgpt.md) |
| **Generic Agent** | Manual prompt copy | [generic-agent.md](./adapters/generic-agent.md) |

## Platform Capability Differences

| Capability | Codex / Trae / file agents | Coze / WorkBuddy / CodeBuddy KB mode | Chat-only agents |
| --- | --- | --- | --- |
| Read repository files | Yes | Usually no, unless uploaded to KB | No |
| Write learning repo files | Yes | Usually report or platform output only | No |
| Learn from materials | Direct file reading | Upload or knowledge base | Pasted text/OCR |
| Source records | `09_sources/` files | Reports, variables, or memory | Conversation summary |
| Workflow | Agent execution | Platform workflow | Manual multi-turn chat |
| Fallback | Path-labeled blocks when files are unavailable | KB/report mode when plugins are unavailable | `learning_state` plus Markdown blocks |

## Learning Methodology

This Skill Pack is built on five core systems:

1. **Knowledge Map** — solves "I don't know what's in this field"
2. **Glossary** — solves "I don't understand the terminology"
3. **Exercise System** — solves "I thought I understood but I didn't"
4. **Project System** — solves "I learned a lot but can't apply it"
5. **Review System** — solves "I forgot it all and never fixed my mistakes"

See [references/en-US/learning-principles.md](./references/en-US/learning-principles.md).

## Internationalization

| Locale | Interface | Materials | Status |
|--------|-----------|-----------|--------|
| `en-US` | English | English | ✅ Complete |
| `zh-CN` | 中文 | 中文 | ✅ Complete |

The `{interface_language}` and `{learning_language}` can be set independently.
For example: "Chat in Chinese but build the learning repo in English."

See [SKILL.md § Language and Locale Policy](./SKILL.md#language-and-locale-policy).

## Contributing

Contributions welcome — new adapters, templates, examples, or prompt
improvements. See [CONTRIBUTING.md](./CONTRIBUTING.md) or
[CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md).

## Acknowledgments

Inspired by [@GeekCatX](https://x.com/GeekCatX)'s article on using Codex to
rapidly learn any field.

## License

MIT © 2026 Learn Anything Skill Pack Contributors
