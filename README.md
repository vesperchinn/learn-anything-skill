<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="Learn Anything Skill Pack — turn any AI agent into a guided learning coach that builds a structured learning repository and starts Day 1 with you in the chat">
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <a href="./CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.2.4--beta-blue" alt="Version 0.2.4-beta"></a>
  <a href="./README.zh-CN.md"><img src="https://img.shields.io/badge/locales-en--US_|_zh--CN-blue" alt="Locales: en-US and zh-CN"></a>
</p>

<p align="center">
  English · <a href="./README.zh-CN.md">中文说明</a>
</p>

A multilingual Agent Skill Pack that turns AI agents into guided learning coaches. Instead of one-off explanations or a dumped folder of Markdown files, the agent creates a structured learning repository for any subject — and immediately starts teaching Day 1 in the chat.

## See it in action

You type one message:

```text
Use learn-anything to create a learning project for "harness design".
My background: complete beginner, no technical background.
Goal: in 7 days, understand what a harness is and apply it to my content workflow.
Daily time: 1 hour.
```

The agent creates the learning repository — then starts teaching right in the conversation:

```text
Created learning project: ./learn-harness

You do not need to open the files first. We will understand Day 1 here.

Today, learn just one sentence first:
A harness is a repeatable way to run one workflow step
and check whether the result is good enough.

I do:    one topic idea → three article titles, with a simple check.
We do:   why "make my article better" is too broad to test.
You do:  pick one small step from your own workflow, fill the template.
```

No files to open first. Day 1 happens in the chat, and your answer updates `progress.md`. Full transcript: [examples/en-US/guided-learning-session.md](./examples/en-US/guided-learning-session.md). A complete generated repository: [examples/en-US/learn-ai-agent/](./examples/en-US/learn-ai-agent/).

If you only want the files, say `scaffold only` or `generate files only`.

## How it works

<p align="center">
  <img src="./assets/readme/workflow.svg" width="100%" alt="How it works: say the subject in chat, the agent builds a structured learning repository, Day 1 starts in the conversation, and progress keeps looping with reviews and tests">
</p>

The pack is built on five learning systems:

1. **Knowledge Map** — solves "I don't know what's in this field"
2. **Glossary** — solves "I don't understand the terminology"
3. **Exercise System** — solves "I thought I understood but I didn't"
4. **Project System** — solves "I learned a lot but can't apply it"
5. **Review System** — solves "I forgot it all and never fixed my mistakes"

See [references/en-US/learning-principles.md](./references/en-US/learning-principles.md).

## Quick start

### 1. Install it where your agent can read it

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

Then connect it based on your agent:

- **Codex / Claude Code / Trae-style file agents**: open this directory or add it to the agent-readable workspace.
- **Agents with Skill support**: import this repository as a Skill or place it in the Skills directory.
- **Coze, WorkBuddy, CodeBuddy, and other Chinese agent platforms**: follow the adapter notes under `platforms/cn/`.
- **Chat-only agents**: copy the prompts from this repository when direct installation is not available.

### 2. Call it from the chat box

> "harness design" is only an example. Replace it with the subject you actually want to learn — "Python", "nutrition", "photography", "English writing".

```text
Use learn-anything to create a learning project for "harness design".
My background: beginner.
My goal: understand the basics and build a small project in 14 days.
Daily time: 1 hour.
```

Already have PDFs, slides, notes, or course material? Say:

```text
Use learn-anything to create a learning project from my materials.
Prioritize the provided materials and mark anything that still needs verification.
```

If your agent cannot call the Skill by name but can read files:

```text
Read learn-anything-skill/core/prompts/en-US/init-repo.md.
Create a learning repository for "harness design".
```

### 3. Continue learning

```text
Continue with learn-anything. Read my progress and run today's learning session.
```

```text
Continue with learn-anything. Review what I learned today and update my progress.
```

```text
Continue with learn-anything. Give me a stage test. Ask questions first, then grade after I answer.
```

### Optional: use the command line

```bash
./scripts/new-domain.sh "Your Subject" en-US
```

See [docs/quick-start.md](./docs/quick-start.md) for the full guide.

## Why not just ask ChatGPT directly?

| Asking ChatGPT directly | Using Learn Anything Skill Pack |
|------------------------|-------------------------------|
| One-off conversations, knowledge doesn't stick | Everything is file-based, stored in a structured repository |
| AI tends to output explanatory prose | Built-in exercise + quiz + project systems ensure hands-on practice |
| No idea what you've learned or where you are | `progress.md` continuously tracks progress and weak points |
| Reinvent the method for every new domain | One Skill Pack, reusable forever |
| Wrong answer → "here's the right one" | Four-type error diagnosis → targeted remedial exercises |
| AI may sound confident without sources | Knowledge Reliability Layer tracks sources, unverified claims, and freshness risk |

## What's in the pack

### Guided Learning Mode

After creating the repository, the agent does not stop at a file summary — it starts Day 1 in the chat: today's goal, one beginner-friendly concept, one small task, a copyable answer template, and a way to check your own answer. Beginners get an interactive lesson format (I do → We do → You do). New projects include `START_HERE.md`, `TODAY.md`, and `07_daily_review/day-01.md` so the first step is always obvious.

### Knowledge Reliability Layer

- **Source-first policy**: claims should be backed by primary or authoritative sources; the agent must not fabricate URLs, papers, or benchmark results.
- **No source, no claim**: unsupported claims are marked `[unverified]` or moved to `09_sources/claims_to_verify.md`.
- **Freshness risk**: each module is tagged 🟢 Stable, 🟡 Evolving, or 🔴 Volatile, with a recommended review interval printed as a freshness notice when the project is created.
- **No-web fallback**: if the agent cannot browse, generated material is labeled **Unverified Draft** with a verification checklist.
- **High-stakes domains**: medical, legal, financial, safety-critical, and certification content requires an educational-use-only notice and authoritative sources first.

This reduces hallucination risk, but does not guarantee absolute correctness.

### Material-Grounded Learning Mode

Build the learning plan from your own PDFs, PPTs, Markdown files, notes, manuals, and exported webpages:

1. Put original files in `learning_materials/raw/`, or tell the agent where they are.
2. The agent registers and extracts the materials, then builds the map, plan, concepts, quizzes, and reviews from them.
3. `material_coverage_map.md` shows which modules are grounded, partially grounded, or supplemental; outside knowledge is labeled `Supplemental`, and extraction failures are recorded instead of guessed.

**Privacy note**: keep confidential documents, paid course materials, and copyrighted books out of public learning repositories; remove personal data before extraction.

### Multilingual

| Locale | Interface | Materials | Status |
|--------|-----------|-----------|--------|
| `en-US` | English | English | ✅ Complete |
| `zh-CN` | 中文 | 中文 | ✅ Complete |

`{interface_language}` and `{learning_language}` can be set independently — for example, chat in Chinese while building the learning repo in English. See [SKILL.md § Language and Locale Policy](./SKILL.md#language-and-locale-policy).

### Multi-platform

| Form | Target platforms | How it works |
| --- | --- | --- |
| File-based agent / native Skill | Codex, Claude Code, Cursor, Trae | Reads `SKILL.md`, `core/`, `templates/`, `prompts/`, and `references/`; writes the learning repo and starts guided learning directly |
| Platform package | Coze, WorkBuddy, CodeBuddy, generic low-code agents | Platform-specific prompts, knowledge-base packages, workflows, variables, and memory under `platforms/` |
| Chat-only package | Ordinary chat agents | Copies the core protocols and outputs path-labeled Markdown blocks |

Low-code platform support is experimental in this beta; validate each adapter in your own workspace before relying on it. See [platforms/README.md](./platforms/README.md) and [platforms/capability-matrix.md](./platforms/capability-matrix.md).

### Automation scripts

Python tools in `scripts/`: cross-platform repo scaffolding (`init_learning_repo.py`), TOC generation (`generate_index.py`), Anki flashcard export (`export_flashcards.py`), locale-bleed detection (`validate_locale.py`), and reliability checks for unverified claims, stale modules, and source notes. Scaffolding scripts support `--dry-run` and refuse to overwrite an existing learning directory.

### Maintenance harness

A read-only guard layer for maintainers lives in [harness/](./harness/): it catches structure drift, locale mismatch, platform adapter gaps, and reliability-rule gaps before release. Run all checks with:

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

## Repository layout

```
learn-anything-skill/
├── SKILL.md          # Skill entry point (routing file for agents)
├── core/             # Core prompts and platform-neutral protocols (en-US / zh-CN)
├── templates/        # Learning repo templates
├── references/       # Methodology references
├── examples/         # Complete example repositories and session transcripts
├── prompts/          # Material-grounded learning prompts
├── adapters/         # Cross-agent adaptation guides
├── platforms/        # Platform adapters (Coze / WorkBuddy / Trae / CodeBuddy …)
├── scripts/          # Automation scripts
├── harness/          # Maintenance checks for maintainers
├── evals/            # Test suites
└── docs/             # User documentation
```

## Documentation

- [Quick start guide](./docs/quick-start.md) · [User guide](./docs/user-guide.md)
- [Release notes](./RELEASE_NOTES.md) · [Roadmap](./ROADMAP.md) · [Changelog](./CHANGELOG.md)
- Agent adapters: [Codex](./adapters/codex.md) · [Claude Code](./adapters/claude-code.md) · [Cursor](./adapters/cursor.md) · [ChatGPT](./adapters/chatgpt.md) · [Generic](./adapters/generic-agent.md)

## Contributing

Contributions welcome — new adapters, templates, examples, or prompt improvements. See [CONTRIBUTING.md](./CONTRIBUTING.md) or [CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md).

## Acknowledgments

Inspired by [@GeekCatX](https://x.com/GeekCatX)'s article on using Codex to rapidly learn any field.

<p align="center">
  <a href="https://github.com/oil-oil/beautify-github-readme"><img src="./assets/readme/made-with-beautify.svg" width="300" alt="README made with beautify-github-readme"></a>
</p>

## License

MIT © 2026 Learn Anything Skill Pack Contributors
