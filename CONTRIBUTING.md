# Contributing

Thanks for your interest in improving Learn Anything Skill Pack!

## Ways to Contribute

- **New adapters**: Add support for a new AI Agent (e.g., Cody, Continue.dev, Aider)
- **New templates**: Create a domain-specific learning template (e.g., for programming languages, humanities, sciences)
- **Improved prompts**: Refine core prompts for better output quality or efficiency
- **New examples**: Share a complete learning repository for a domain you've studied
- **Bug fixes**: Fix issues in scripts, docs, or prompt logic
- **Translations**: Help translate prompts and docs to new locales, or improve existing zh-CN translations

## Development Setup

```bash
git clone https://github.com/vionlabs/learn-anything-skill.git
cd learn-anything-skill

# Run evals to verify everything is intact
./evals/en-US/test-templates.sh
./evals/en-US/test-progress-format.sh
./evals/en-US/test-prompts.sh

# Check for untranslated strings in English files
python3 scripts/check_untranslated_strings.py
```

## Pull Request Guidelines

1. For new prompts: keep the same variable conventions (`{domain}`,
   `{user_background}`, etc.) defined in `core/principles.md`. Place new
   prompts in both `core/prompts/en-US/` and `core/prompts/zh-CN/`.
2. For new adapters: follow the structure of `adapters/codex.md`
3. For new templates: include `.gitkeep` files in empty directories. Create
   both `templates/en-US/` and `templates/zh-CN/` versions.
4. Run `scripts/validate-repo.sh` on any template changes
5. Run `python3 scripts/check_untranslated_strings.py` to verify en-US files
   don't contain leftover CJK text
6. Update `CHANGELOG.md` under the next release section, or add an Unreleased section for post-release work

## Internationalization

This project uses locale directories for all content:

```
core/prompts/{locale}/     templates/{locale}/
references/{locale}/       examples/{locale}/
evals/{locale}/
```

When contributing content, create both `en-US` and `zh-CN` versions.
File names stay ASCII regardless of locale.

## Code Style

- Prompts: plain Markdown with `{variable}` placeholders
- Scripts: Shell scripts use `#!/bin/bash`, Python uses `#!/usr/bin/env python3`
- Documentation: English is the primary language. Chinese docs go in
  `*.zh-CN.md` files or `zh-CN/` subdirectories.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
