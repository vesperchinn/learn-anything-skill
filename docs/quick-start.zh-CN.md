# 快速开始指南

5 分钟从零到第一个学习仓库。

## 前提

- 你有一个支持文件读写的 AI Agent（推荐 Claude Code 或 Codex）
- 你有一个想学的领域

## 第一步：克隆仓库

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

## 第二步：创建你的学习仓库

**用脚本（推荐）**：
```bash
./scripts/new-domain.sh "AI Agent"
cd learn-ai-agent
```

**手动**：复制 `templates/zh-CN/{{domain-slug}}/` 到你的工作目录。

## 第三步：告诉 Agent 开始工作

启动你的 AI Agent 在当前目录，然后输入：

```
请读取 learn-anything-skill/core/prompts/zh-CN/init-repo.md，
为「AI Agent」领域创建学习仓库。
我的背景：编程初级，每天 2 小时，目标 30 天后做出一个项目。
```

Agent 会创建所有文件。接下来：

```
请读取 learn-anything-skill/core/prompts/zh-CN/knowledge-map.md，
生成 AI Agent 的知识地图，写入 00_domain_map.md。
```

## 第四步：每天学习

每天打开这个目录，对 Agent 说：

```
请读取 progress.md，然后读取 learn-anything-skill/core/prompts/zh-CN/daily-session.md，
为我安排今天的学习。
```

学习完说：

```
请读取 learn-anything-skill/core/prompts/zh-CN/daily-review.md，
帮我做今天的复盘。
```

## 第五步：第 7 天测试

```
请读取 learn-anything-skill/core/prompts/zh-CN/stage-test.md，
对我进行阶段测试。先出题，等我回答后再评分。
```

## 可选：基于自己的资料学习

如果你已有 PDF、PPT、笔记、文档导出或课程资料，可以在创建学习仓库后使用
**Material-Grounded Learning Mode**：

1. 把文件放入 `learning_materials/raw/`，或告诉 Agent 文件位置。
2. 使用 `learn-anything-skill/prompts/zh-CN/material-intake.md`。
3. 使用 `learn-anything-skill/prompts/zh-CN/material-grounded-learning-repo.md`。

Agent 会把你的资料作为 primary source，并把无法读取的 PDF/PPT 内容记录为提取问题，而不是猜测。

---

就这么简单。30 天后，你会拥有一个完整的知识仓库和一个可展示的项目。

## 常见问题

**Q: 我的 Agent 不支持文件写入怎么办？**  
A: 参考 `adapters/generic-agent.md`，手动复制提示词结果到文件中。

**Q: 我能用 ChatGPT 吗？**  
A: 能，但需要手动管理文件。推荐至少用 Cursor 或 Claude Code 以获得完整体验。

**Q: 30 天太长，能加速吗？**  
A: 你可以通过增加每天的学习时间来压缩天数。快速通道模板计划在后续版本中推出。

**Q: 我能学任何领域吗？**  
A: 能。从编程到哲学、从营养学到投资，任何结构化知识领域都可以。

**Q: 我能用中文对话但学习仓库用英文吗？**  
A: 可以。在初始化时设置 `{interface_language}=中文`、`{learning_language}=English`。详见 `SKILL.md` § Language and Locale Policy。
