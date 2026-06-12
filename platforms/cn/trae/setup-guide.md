# Trae Setup Guide

## 推荐配置

1. 打开 `learn-anything-skill` 仓库。
2. 将 `platforms/cn/trae/project_rules.md` 作为项目规则。
3. 将 `platforms/cn/trae/user_rules.md` 作为用户规则或快捷提示。
4. 使用 `platforms/cn/trae/agent-prompt.md` 启动学习任务。
5. 需要创建学习仓库时，优先使用 `scripts/new-domain.sh` 或 `scripts/init_learning_repo.py`。

## 验证

- Agent 能读取 `SKILL.md`。
- Agent 能读取 `core/learning-protocol.zh-CN.md`。
- Agent 能列出 `templates/zh-CN/`。
- Agent 能读取 `references/zh-CN/source-quality-policy.md`。
- Agent 能在 dry-run 下执行脚本。

