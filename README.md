# Learn Anything Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.2--beta-blue)](./CHANGELOG.md)
[![Locales](https://img.shields.io/badge/locales-en--US_|_zh--CN-blue)](./README.zh-CN.md)

A multilingual Agent Skill Pack that turns AI agents into guided learning coaches.

Instead of generating one-off explanations or dumping a folder of Markdown files, Learn Anything Skill helps an AI agent create a structured learning repository and immediately guide the user through the first learning session.

[中文说明](README.zh-CN.md)

## What is this?

Learn Anything Skill helps AI agents build structured learning systems for any domain.

It can create:

- domain maps
- concept breakdowns
- daily learning plans
- exercises
- quizzes
- flashcards
- progress tracking
- source tracking
- material-grounded learning plans
- final projects
- guided Day 1 learning sessions

Current release: **v0.2.2-beta**. See [release notes](./RELEASE_NOTES.md)
and [roadmap](./ROADMAP.md).

## Why it exists

Most AI learning conversations are temporary.
Most generated study plans are hard to continue.
Most learning repositories are useful, but beginners often do not know where to start.

This project solves that by combining:

1. A structured learning repository.
2. A guided learning session that starts immediately.
3. Progress tracking and review loops.
4. Source notes and freshness checks.
5. Support for user-provided PDFs, slides, notes, and documents.

## Key Feature: Guided Learning Mode

By default, after creating a learning repository, the agent does not stop at a file summary.

It immediately starts Day 1 in the chat:

- explains today's goal
- introduces the first concept in beginner-friendly language
- gives one small task
- provides a copyable answer template
- shows how the learner can tell whether the answer works
- asks the user to reply directly in the conversation
- updates progress after the user completes the task

For beginners, complete beginners, non-technical users, students, content
creators, writers, marketers, teachers, and people with no coding background,
Guided Learning Mode switches to an interactive beginner lesson:

- one plain-language idea for the day
- a scenario based on the learner's real goal
- I do: a fully worked example
- We do: one bad example and one better example
- You do: one tiny task, usually one workflow step

If the user only wants files, they can say:

```text
scaffold only
```

or:

```text
只创建项目，不要开始学习
```

## Example

User:

```text
I want to learn harness design.
My background: beginner.
Goal: understand the basic principles in 7 days and apply them to my content creation workflow.
Daily time: 1 hour.
```

Agent:

```text
Learning project created.

You do not need to open the files first. We will understand Day 1 here.

Today, learn just one sentence first:
A harness is a simple way to run the same workflow step again and check whether the result is good enough.

Put it into your real situation:
In a content workflow, you might use a harness to test one repeatable step, such as turning a topic idea into three article titles.

I do:
Workflow step: turn one topic idea into three article titles.
Expected output: three titles with a clear reader benefit.
Simple check: at least one title makes the reader immediately understand why they should click.

Bad example:
"Make my article better."
This is too broad. It does not say which step is being tested.

Better example:
"Take one topic idea and produce three article titles for middle-aged readers."
This is easier to test because the input, output, and audience are clear.

Your task:
Pick one small step from your own content creation workflow.

Copy and fill this template:

# My Day 1 Answer

1. My workflow step:

2. What I want this step to produce:

3. One simple way I can tell whether this step worked:

4. What I am still unsure about:

Please fill in the template above and send it to me directly.
```

## Core Features

### Guided Learning Mode

Create a learning repository and immediately start the first learning session.

Beginner-friendly sessions use an interactive lesson format: I do, We do, You
do. The agent gives a worked example, compares a bad example with a better
example, then asks for one small answer in chat.

### Domain Learning Repository

Generate a structured repository with maps, concepts, exercises, quizzes, projects, reviews, and progress tracking.

### Knowledge Reliability Layer

Track sources, claims, freshness risk, and unverified information.

This reduces hallucination risk, but does not guarantee absolute correctness.

### Material-Grounded Learning Mode

Build a learning plan from user-provided materials such as PDFs, PPTs, Markdown files, notes, manuals, and exported webpages.

### Multilingual Support

- English: en-US
- Simplified Chinese: zh-CN

### Multi-Agent / Multi-Platform Support

Designed for:

- Codex
- Claude Code
- Cursor
- ChatGPT
- generic file-based agents
- generic chat-only agents
- Coze / 扣子
- WorkBuddy
- Trae
- CodeBuddy

Platform support depends on each platform's file access, web access, workflow, and knowledge base capabilities.

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

### 1. Install it where your agent can read it

The simplest path is to place this repository in a directory your agent can
read:

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

Then connect it based on your agent:

- **Codex / Claude Code / Trae-style file agents**: open this directory or add
  it to the agent-readable workspace.
- **Agents with Skill support**: import this repository as a Skill or place it
  in the Skills directory.
- **Coze, WorkBuddy, CodeBuddy, and other Chinese agent platforms**: follow the
  adapter notes under `platforms/cn/`.
- **Chat-only agents**: copy the prompts from this repository when direct
  installation is not available.

### 2. Call it from the chat box

After installation, type:

> "AI Agents" is only an example. Replace it with the subject you actually want
> to learn, such as "Python", "nutrition", "photography", or "English writing".

```
Use learn-anything to create a learning project for "AI Agents".
My background: beginner.
My goal: understand the basics and build a small project in 30 days.
Daily time: 1 hour.
```

The agent should create the learning repository and then immediately start Day
1 in the chat. You do not need to open the generated Markdown files first.

If you already have PDFs, slides, notes, or course material, say:

```
Use learn-anything to create a learning project from my materials.
Prioritize the provided materials and mark anything that still needs verification.
```

If your agent cannot call the Skill by name but can read files, type:

> Again, replace "AI Agents" with your real learning subject.

```
Read learn-anything-skill/core/prompts/en-US/init-repo.md.
Create a learning repository for "AI Agents".
```

By default, repository creation continues into a guided Day 1 session. If you
only want files, say `scaffold only` or `generate files only`.

### 3. Continue learning

```
Continue with learn-anything. Read my progress and run today's learning session.
```

```
Continue with learn-anything. Review what I learned today and update my progress.
```

```
Continue with learn-anything. Give me a stage test. Ask questions first, then grade after I answer.
```

### Optional: use the command line

```bash
./scripts/new-domain.sh "Your Subject" en-US
```

For example:

```bash
./scripts/new-domain.sh "AI Agent" en-US
cd learn-ai-agent
```

See [docs/quick-start.md](./docs/quick-start.md) for the full guide.

## Multi-Platform Support

Learn Anything now includes a **Platform Adapter Layer** for platforms that cannot consume the native file-based Skill workflow directly.
Low-code platform support is experimental in this beta; validate each adapter in your own workspace before relying on it.

| Form | Target platforms | How it works |
| --- | --- | --- |
| File-based Agent / native Skill | Codex, Claude Code, Cursor, Trae, and other file-based agents that can read this repo | Reads `SKILL.md`, `core/`, `templates/`, `prompts/`, and `references/`; Codex uses `AGENTS.md`, Claude Code uses `CLAUDE.md`; writes the learning repo and starts guided learning directly |
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
