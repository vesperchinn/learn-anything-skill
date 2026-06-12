# 用户指南

Learn Anything Skill Pack 完整使用手册。

## 目录

1. [核心概念](#核心概念)
2. [学习流程详解](#学习流程详解)
3. [提示词使用指南](#提示词使用指南)
4. [进度追踪](#进度追踪)
5. [错误诊断](#错误诊断)
6. [项目设计](#项目设计)
7. [跨 Agent 使用](#跨-agent-使用)
8. [常见问题](#常见问题)

## 核心概念

Learn Anything Skill Pack 的目标是让 AI Agent 成为你的「领域学习工程师」——不是让它给你讲知识，而是让它帮你搭建一个**可运行、可迭代、可复盘的学习系统**。

### 五个系统

```
知识地图 → 术语表 → 练习系统 → 项目系统 → 复盘系统
```

### 学习节奏

- **每天**: 学习 3 个概念 → 5 道检测题 → 60 分钟小任务 → 复盘
- **每周**: 阶段测试（10 选择 + 5 概念 + 3 场景 + 1 综合题）
- **最终**: 7 天完成一个可展示的最小项目

### 三个知识层级

- **20% 必须先懂**：决定能否入门
- **60% 暂时跳过**：现在学了也用不上
- **20% 以后深入**：做项目后再回来补

## 学习流程详解

> 提示词文件按语言分目录存放。中文用户使用 `core/prompts/zh-CN/`，英文用户使用 `core/prompts/en-US/`。以下统一用 `{locale}` 表示。

### Phase 0: 初始化 (Day 0)

使用 `core/prompts/{locale}/init-repo.md` 创建学习仓库。Agent 会生成：
- 标准化目录结构（10 个目录 + 核心文件）
- README.md（仓库使用说明）
- AGENTS.md（Agent 行为规则）
- progress.md（进度快照模板）

### Phase 1: 知识地图 (Day 0)

使用 `core/prompts/{locale}/knowledge-map.md` 生成知识全景图：
- 领域定义和费曼解释
- Top 20 核心概念
- 概念关系图谱
- 20-60-20 分类
- 易混淆概念对比
- 最小必要知识清单

### Phase 2: 概念拆解

使用 `core/prompts/{locale}/concept-breakdown.md` 为每个核心概念生成详细文件：
- 一句话解释
- 生活类比
- 技术解释
- 真实案例
- 练习

### Phase 3: 30 天计划

使用 `core/prompts/{locale}/learning-plan.md` 生成每日计划。

### Phase 4: 每日循环 (Day 1-30)

每天两个环节：
1. **学习会话**（`core/prompts/{locale}/daily-session.md`）：复习 → 学新概念 → 练习 → 60 分钟任务
2. **每日复盘**（`core/prompts/{locale}/daily-review.md`）：总结 → 错误分析 → 更新进度 → 安排明天

### Phase 5: 阶段测试 (每 7 天)

考官模式——Agent 变成严格考官，先出题、等你回答、再评分和诊断。

使用 `core/prompts/{locale}/stage-test.md`。

### Phase 6: 项目 (最后 7 天)

使用 `core/prompts/{locale}/project-design.md` 设计最小可展示项目。

## 进度追踪

### progress.md（快照）
- Agent 每次必读
- 保持 ≤ 200 行
- 包含：当前天数、已完成模块、薄弱点、错题摘要、测试成绩、项目进展、下一步

### progress-log.md（日志）
- 追加写入，不删减
- 每日详细记录：学习内容、掌握程度、错误分析、复盘

## 错误诊断

当你答错时，Agent 会先判断错误类型再给答案：

| 类型 | 含义 | 补救 |
|------|------|------|
| 不懂概念 | 根本不知道概念是什么 | 回到定义 + 类比 |
| 不会应用 | 知道概念但不会用 | 场景题 + 模仿 |
| 表达不清 | 心里懂但说不出来 | 费曼输出练习 |
| 知识混淆 | A 和 B 搞混了 | 对比表 + 区分练习 |

详见 `core/prompts/{locale}/error-diagnosis.md`。

## 项目设计

项目的标准：
- 能运行（不只是文档）
- 能展示（可以给别人看）
- 能解释（你能说清楚设计决策）
- 能迭代（有明确的改进方向）

详见 `references/{locale}/project-patterns.md` 获取 5 种项目模式。

## 跨 Agent 使用

| Agent | 适配说明 |
|-------|---------|
| Codex | `adapters/codex.md` — 原生 Skill 支持 |
| Claude Code | `adapters/claude-code.md` — 通过 CLAUDE.md 集成 |
| Cursor | `adapters/cursor.md` — 通过 .cursorrules 集成 |
| ChatGPT | `adapters/chatgpt.md` — 复制粘贴提示词 |
| 通用 Agent | `adapters/generic-agent.md` — 手动复制提示词 |

> 旧版适配文件已移至 `adapters/legacy/`，仅供参考，不再维护。

## 常见问题

**Q: 我中途停了几天，怎么恢复？**
A: 用 `core/prompts/{locale}/resume-session.md`。Agent 会读 progress.md + 最近日志重建状态。

**Q: 阶段测试不及格怎么办？**
A: Agent 会自动诊断薄弱点，生成 3 个补救练习，重排后续 3 天计划，3 天后重测。

**Q: 能把学习仓库分享给别人吗？**
A: 可以。整个仓库就是一套 Markdown 文件，Git push 或打包发送即可。

**Q: 中文对话但英文仓库，怎么设置？**
A: 在采集阶段告诉 Agent："用中文跟我对话，但学习资料用英文"。Agent 会设置 `{interface_language}=中文`、`{learning_language}=English`，对话用中文，仓库文件用英文。

**Q: 当前支持哪些脚本工具？**
A: 当前 `scripts/` 提供以下工具：
- `new-domain.sh` / `init_learning_repo.py` — 创建学习仓库（支持跨平台）
- `validate-repo.sh` — 验证学习仓库结构
- `validate_locale.py` — 启发式算法检测语言溢出
- `generate_index.py` — 动态生成学习目录索引 (index.md)
- `export_flashcards.py` — 将闪卡导出为 Anki 兼容的 CSV 格式
- `detect_language.py` / `check_untranslated_strings.py` — 语言检测与开发检查工具
