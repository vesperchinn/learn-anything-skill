# 学习 {{domain}}

这是一个用于系统掌握 **{{domain}}** 的结构化学习仓库。由 [Learn Anything Skill Pack](https://github.com/vionlabs/learn-anything-skill) 生成。

## 如何使用本仓库

本仓库专为与 AI 智能体（Codex、Claude Code、Cursor 等）配合使用而设计，AI 将充当您的专属学习工程师。

### 每日学习流程

1. 在终端打开此目录
2. 启动您的 AI 智能体
3. 说出：**"请读取 progress.md 并开始今天的学习"**
4. 完成任务并提交答案
5. 说出：**"来做每日复盘"**

### 仓库结构说明

```
├── README.md               # 本文件 — 使用说明
├── AGENTS.md               # AI 教学规则 — 智能体行为规范
├── CLAUDE.md               # Claude Code 使用的等价教学规则
├── 00_domain_map.md        # 知识地图 — 该领域完整知识结构
├── 01_core_concepts/       # 核心概念 — 每个核心概念的详细拆解
├── 02_case_studies/        # 案例分析 — 真实世界案例与示例
├── 03_exercises/           # 练习题库 — 动手实践练习
├── 04_projects/            # 项目实战 — 项目设计及交付物
├── 05_flashcards/          # 知识压缩卡 — 生成的记忆卡片
├── 06_quizzes/             # 测验题库 — 测验题目与阶段测试
├── 07_daily_review/        # 每日复盘 — 每日学习记录
├── 08_glossary.md          # 术语表 — 持续更新的术语定义
├── 09_resources.md         # 推荐资源 — 书籍、课程、工具、社区
├── learning_materials/      # 用户提供的 PDF、PPT、文档、网页导出和提取记录
├── 09_sources/             # 来源、事实主张验证和时效性追踪
├── progress.md             # 进度快照 — 当前状态概览（≤ 200 行）
└── progress-log.md         # 完整历史 — 学习的完整日志
```

### 学习原则

- **先全局，后细节** — 在深入每个细节之前，先理解整体框架
- **学 → 练 → 输出 → 测** — 每天循环四个环节
- **20-60-20 法则** — 先聚焦关键的 20%，略过中间 60%，高级 20% 留待后期
- **最小可行项目** — 目标是做出东西，而不只是阅读资料

### 知识可靠性

- `09_sources/sources.md` 记录学习过程中使用的信息源。
- `09_sources/source_quality_policy.md` 定义来源层级和禁止伪造规则。
- `09_sources/claim_ledger.md` 跟踪事实主张及其验证状态。
- `09_sources/claims_to_verify.md` 列出仍需权威来源核验的主张。
- `09_sources/freshness_log.md` 记录模块时效性风险和复查日期。

如果 AI Agent 无法联网，新生成内容必须视为 **未验证草稿**。重要主张在使用前需要对照权威来源核验。

### 用自己的资料学习

将 PDF、PPT、Markdown、TXT、Word 文档或网页导出放入 `learning_materials/raw/`。AI Agent 应先把可读内容提取到 `learning_materials/extracted/`，建立 `material_index.md`，再基于这些资料生成知识地图和学习计划。外部解释必须标记为 `Supplemental`，无法读取的内容记录到 `learning_materials/extraction_issues.md`。

### 进度追踪

- `progress.md` 是您的仪表盘 — 每天查看以了解当前状态
- `progress-log.md` 是完整历史 — 需要回顾全程时查阅
- 阶段测试每 7 天进行一次 — 这是对学习效果的检验
