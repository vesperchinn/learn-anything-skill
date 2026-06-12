# v0.1.0 - Initial Public Release

## What is learn-anything-skill

Learn Anything Skill Pack is a multilingual Agent Skill Pack that helps AI
agents turn a subject into a structured learning repository with plans,
concepts, exercises, reviews, projects, flashcards, and source tracking.

## Key Features

- Codex-native `SKILL.md` workflow
- English and Simplified Chinese prompts, templates, examples, and references
- Learning repository scaffolding scripts
- Platform adapter packages for file-based agents, knowledge-base workflows,
  and chat-only fallback use
- Maintenance harness for release checks and policy consistency

## Supported Platforms

- Codex and file-based agents can use the repository-oriented workflow.
- Trae and similar file-based environments can adapt the same files and
  templates.
- Coze, WorkBuddy, CodeBuddy, and generic low-code agents can use the platform
  adapter materials with reduced capabilities.
- Chat-only agents can use copied prompts and produce Markdown output, but they
  do not provide the same file, workflow, or source-management behavior.

Different platforms expose different file access, web access, workflow, memory,
and knowledge-base capabilities. Users should validate the adapter in their own
platform before relying on it.

## Reliability and Source Tracking

The Knowledge Reliability Layer tracks source quality, unverified claims,
freshness risk, and no-web fallback states. It is designed to reduce
hallucination risk, not to eliminate it. High-stakes or time-sensitive topics
still require source review by the user.

## Material-Grounded Learning

Material-Grounded Learning Mode helps agents learn from user-provided PDFs,
slides, notes, documents, or exported webpages by creating material indexes,
coverage maps, extraction issue logs, and material-based learning plans.

Users should only provide materials they have permission to use and should avoid
uploading private or sensitive files to platforms they do not trust.

## Known Limitations

- Low-code and chat-only platforms may not support direct file writing.
- Web access, source verification, memory, and workflow automation depend on
  the platform.
- Behavior evals check policy and structure; they are not proof that every live
  agent will behave identically.
- The project reduces hallucination risk through structure and source tracking,
  but it does not guarantee factual correctness.

## Next Steps

- Collect real-world adapter feedback from Codex, Trae, Coze, WorkBuddy, and
  CodeBuddy users.
- Add more complete material-grounded examples.
- Expand adapter-specific troubleshooting.
- Continue improving release checks and bilingual documentation parity.
