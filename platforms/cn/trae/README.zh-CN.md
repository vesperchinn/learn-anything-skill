# Trae 适配包

Trae 适配面向文件型工程 Agent。它可以继续读取仓库中的 `SKILL.md`、`core/`、`templates/`、`prompts/`、`references/` 和脚本，但平台规则应放在本目录，不要把所有平台说明塞回 `SKILL.md`。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `project_rules.md` | 项目级规则 |
| `user_rules.md` | 用户级调用规则 |
| `agent-prompt.md` | Agent 工作提示 |
| `setup-guide.md` | 配置步骤 |
| `commands.md` | 常用命令 |

## 适配原则

- 保留原 Codex Skill，不删除、不重写。
- Trae 可以读取仓库文件时，优先使用原始模板和引用文件。
- 新增平台说明只放在 `platforms/cn/trae/`。
- 生成学习仓库时不得覆盖用户已有文件。
- 无联网时输出未验证草稿和待核查清单。

