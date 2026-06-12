# 贡献指南

感谢你愿意改进 Learn Anything Skill Pack。

本项目的代码、目录名和主要开发约定以 English 为主；中文文档、提示词和平台适配同样是一等内容。提交贡献时，请尽量保持中英文版本同步。

## 可以贡献什么

- **新平台适配器**：为新的 AI Agent、低代码平台或知识库平台补充使用说明。
- **新模板**：为编程、人文、科学、商业等领域补充学习仓库模板。
- **提示词改进**：提升核心提示词的清晰度、稳定性或可执行性。
- **示例仓库**：提供一个完整、可参考的学习项目。
- **Bug 修复**：修复脚本、文档、提示词逻辑或平台包问题。
- **翻译与本地化**：补全新 locale，或改进现有 zh-CN 内容。

## 本地检查

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill

./evals/en-US/test-templates.sh
./evals/en-US/test-progress-format.sh
./evals/en-US/test-prompts.sh

python3 scripts/check_untranslated_strings.py
python3 harness/scripts/run_all_checks.py --root . --report
```

如果修改了中文内容，也建议运行对应的 zh-CN 检查：

```bash
./evals/zh-CN/test-templates.sh
./evals/zh-CN/test-progress-format.sh
./evals/zh-CN/test-prompts.sh
```

## Pull Request 要求

1. 新增提示词时，保持 `{domain}`、`{user_background}` 等变量命名一致，并同时提供 `core/prompts/en-US/` 和 `core/prompts/zh-CN/` 版本。
2. 新增平台适配器时，参考 `adapters/codex.md` 和 `platforms/` 下已有平台结构。
3. 新增模板时，保留空目录中的 `.gitkeep`，并同时提供 `templates/en-US/` 和 `templates/zh-CN/` 版本。
4. 修改模板后，运行 `scripts/validate-repo.sh`。
5. 修改英文文档后，运行 `python3 scripts/check_untranslated_strings.py`，避免英文文件残留中文。
6. 修改资料驱动学习、来源记录、平台适配或发布说明时，同时检查 README、docs、examples、evals 和 harness 相关文件是否需要同步。
7. 在 `CHANGELOG.md` 的下一版本区域记录用户可见变化；如果还没有对应区域，可以新增 `Unreleased`。

## 国际化规则

项目使用 locale 目录管理内容：

```
core/prompts/{locale}/     templates/{locale}/
references/{locale}/       examples/{locale}/
evals/{locale}/
```

新增内容时，请尽量提供 `en-US` 和 `zh-CN` 两个版本。文件名保持 ASCII，正文按对应 locale 编写。

## 文档与提示词风格

- 提示词使用 Markdown，并保留 `{variable}` 变量标记。
- Shell 脚本使用 `#!/bin/bash`，Python 脚本使用 `#!/usr/bin/env python3`。
- 中文文档放在 `*.zh-CN.md` 文件或 `zh-CN/` 目录。
- 不要承诺完全消除幻觉、百分百正确或自动保证学习效果；使用有边界的描述。
- 涉及 PDF、PPT、私密资料、付费课程或版权材料时，保留隐私和版权提醒。

## 许可证

提交贡献即表示你同意你的贡献以 MIT License 授权。
