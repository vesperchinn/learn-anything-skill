# Learn Anything Skill Pack — 产品架构设计

> 基于《如何使用 Codex 快速入门任何一个领域》(GeekCatX, 2026-06-08) 构建的跨 Agent 开源学习 Skill 产品包。

**修订记录**：
| 版本 | 日期 | 修订内容 |
|------|------|----------|
| v1.0 | 2026-06-11 | 初稿 |
| v1.1 | 2026-06-11 | 根据审查意见修订：progress.md 拆分为快照+日志、新增 resume-session.md 和 concept-relationship.md、validate-repo.sh 提至 MVP、CLAUDE.md 显式映射、变量表加 agent_type、附录 A 补上下文预算、minimal 模板补 resources 文件 |

---

## 1. 产品定义

**Learn Anything Skill Pack** 是一个**跨 AI Agent 的可复用学习系统工具包**。它不是单一提示词，而是一套由核心提示词、模板文件、Skill 定义、适配器和自动化脚本组成的完整产品，让任意支持文件读写或提示词调用的 AI Agent（Codex / Cursor / Windsurf / Copilot / 通用 LLM）都能帮助用户快速搭建个人领域学习系统。

一句话定位：

> 把 AI Agent 从「问答机器」变成「领域学习工程师」——一条命令启动一个完整的学习项目。

---

## 2. 解决的问题

| 痛点 | 现状 | 本产品方案 |
|------|------|-----------|
| **碎片化学习** | 每次问 AI 都是孤立对话，知识不沉淀 | 所有学习内容文件化、版本化，存储在结构化学习仓库中 |
| **只学不练** | AI 倾向于输出解释性文字，缺乏练习设计 | 内置练习系统、测验系统、项目系统，确保「学→练→测→输出」闭环 |
| **无进度追踪** | 不知道自己学了什么、薄弱点在哪 | progress.md（状态快照）+ progress-log.md（完整日志）持续记录学习轨迹、错题、薄弱点 |
| **无法复用** | 每次学新领域都要重新设计方法 | 一套 Skill Pack，学任何领域都直接套用 |
| **Agent 锁定** | 学习方法绑定特定 Agent 格式 | 适配器层实现跨 Agent 兼容 |
| **只输入不输出** | 学了很多但做不出东西 | 内置最小可展示项目引导 + 每日可交付任务 |
| **错误不诊断** | 答错只给答案，不分析错误类型 | 四类错误诊断：概念不清 / 不会应用 / 表达不清 / 知识混淆 |

---

## 3. 目标用户

| 用户画像 | 典型场景 | 核心需求 |
|----------|----------|----------|
| **快速入门者** | 想用 30 天了解一个新领域（如 AI Agent、Web3、营养学） | 结构化学习路径 + 最小必要知识筛选 |
| **内容创作者** | 需要快速研究一个主题并产出文章/视频脚本 | 知识地图 + 核心概念拆解 + 可交付输出 |
| **独立开发者** | 需要快速掌握新技术栈并做出 MVP | 项目引导 + 练习系统 + 验收标准 |
| **研究者** | 需要系统梳理跨学科领域知识 | 概念关系图谱 + 文献案例库 + 术语表 |
| **学生** | 应对考试或课程项目 | 测验系统 + 错题诊断 + 阶段测试 + 记忆卡片 |

---

## 4. 核心能力矩阵

### 4.1 学习仓库创建

- 一条指令初始化标准化的领域学习目录结构
- 自动生成 README.md、AGENTS.md / CLAUDE.md
- 支持自定义模板（极简版 / 标准版 / 深度版）

### 4.2 知识地图生成

- 领域定义：这个领域解决什么问题
- 费曼解释：小学生也能听懂的一句话
- Top 20 核心概念及其关系
- 概念分类：必须先懂的 20% / 暂时跳过的 60% / 以后深入的 20%
- 易混淆概念对比表
- 5 阶段学习路径 + 每阶段可交付作品
- 最小必要知识清单 + 暂不需要学的内容

### 4.3 核心概念拆解

- 每个概念：一句话解释 + 生活类比 + 技术解释 + 真实案例
- 概念间关系图谱
- 前置依赖标注（学 B 必须先学 A）

### 4.4 30 天学习计划

- 按周拆分阶段目标
- 每天：学习 + 练习 + 输出 + 测验 四段式
- 每 7 天一次阶段测试
- 根据 progress.md 动态调整

### 4.5 每日学习循环

```
复习昨日 5 个关键点 → 检查薄弱点 → 学习今日 3 个核心概念
→ 5 道检测题 → 60 分钟小任务 → 验收 → 复盘 → 更新 progress.md（快照）
→ 追加 progress-log.md → 生成压缩卡 → 安排明日任务
```

### 4.6 进度追踪系统（progress.md + progress-log.md）

**设计原则**：快照与日志分离，防止单文件膨胀导致 Agent 上下文超限。

**progress.md（当前状态快照，限制 ≤200 行）**：
- 当前天数 / 总天数
- 已完成模块清单（含完成日期）
- 当前薄弱点 Top 5（按优先级排序，含错误类型）
- 错题本摘要（最近 20 道错题）
- 下一步学习计划（未来 3 天）
- 学习时间累计
- 阶段测试成绩历史

**progress-log.md（完整历史日志，追加写入）**：
- 每日学习记录（日期 + 学习内容 + 掌握程度 + 耗时）
- 完整错题本（不删减）
- 每日复盘总结
- 阶段测试详细结果
- 项目进展记录

**读取策略**：
- `daily-session.md`、`daily-review.md`：读 progress.md（快照）
- `resume-session.md`：读 progress.md + 最近 3 条 progress-log 条目
- `stage-test.md`：读 progress.md + 本阶段 progress-log
- 完整日志分析（如需）：读 progress-log.md

**progress.md 格式模板**（`validate-repo.sh` 的校验基准）：

```markdown
# 学习进度快照

## 当前状态
- 天数: 5 / 30
- 阶段: 第一阶段（第 1-7 天）
- 上次学习: 2026-06-15

## 已完成模块
- [x] 01 - 什么是 AI Agent (Day 1)
- [x] 02 - Agent 架构组成 (Day 2)
- [x] 03 - Tool Use 机制 (Day 3)
- [x] 04 - 记忆与上下文 (Day 4)
- [ ] 05 - 规划与推理 (当前)

## 薄弱点（按优先级）
1. [不会应用] Tool Use 的实际代码编写 (出现 3 次)
2. [知识混淆] ReAct vs Plan-and-Execute 的适用场景 (出现 2 次)

## 错题摘要（最近 20 条）
| # | 日期 | 题目 | 错误类型 | 状态 |
|----|------|------|----------|------|
| 1 | D3 | Tool 定义格式 | 不会应用 | 已补救 |
| 2 | D4 | 记忆类型区分 | 知识混淆 | 待重测 |

## 阶段测试成绩
| 阶段 | 日期 | 得分 | 主要问题 |
|------|------|------|----------|
| - | - | - | 尚未进行 |

## 项目进展
- 状态: 未开始
- 预计开始: Day 22

## 下一步（未来 3 天）
- Day 5: 规划与推理 → 练习设计一个 ReAct Agent
- Day 6: 多 Agent 协作 → 对比单 Agent vs 多 Agent
- Day 7: 阶段测试一（Day 1-6 内容）
```

**validate-repo.sh 的 progress.md 校验规则**：

| 检查项 | 规则 | 违规级别 |
|--------|------|----------|
| 文件存在 | `progress.md` 必须存在于仓库根目录 | ERROR |
| 行数上限 | ≤ 200 行（超过说明快照膨胀，需截断旧错题到 progress-log.md） | WARNING |
| 必需标题 | 必须包含 7 个二级标题：`## 当前状态`、`## 已完成模块`、`## 薄弱点`、`## 错题摘要`、`## 阶段测试成绩`、`## 项目进展`、`## 下一步` | ERROR |
| 状态字段 | `## 当前状态` 下必须包含 `天数:` `阶段:` `上次学习:` 三行 | ERROR |
| 薄弱点格式 | `## 薄弱点` 下每条必须包含错误类型标签：`[不懂概念]` / `[不会应用]` / `[表达不清]` / `[知识混淆]` | WARNING |
| 错题表格 | `## 错题摘要` 下必须有合法的 Markdown 表格（表头含 `#\|日期\|题目\|错误类型\|状态`） | WARNING |

### 4.7 错误诊断（四类）

| 错误类型 | 含义 | 补救策略 |
|----------|------|----------|
| **不懂概念** | 根本不知道这个概念是什么 | 回到定义 + 费曼解释 + 生活类比 |
| **不会应用** | 知道概念但不会用 | 场景应用题 + 案例模仿 |
| **表达不清** | 心里懂但说不出来 | 费曼输出练习 + 口头解释录音 |
| **知识混淆** | 把 A 概念和 B 概念混了 | 对比表 + 区分练习 + 并排案例 |

### 4.8 领域压缩卡

- 格式：一句话解释 + 5 关键词 + 3 应用场景 + 2 常见误区 + 1 经典案例 + 1 自测题 + 知识连接 + 最易忘点 + 复习建议
- 存储：`05_flashcards/` 目录
- 30 天积累个人知识卡片库

### 4.9 阶段测试系统

- 每 7 天一次
- 格式：10 选择题 + 5 概念解释 + 3 场景应用 + 1 综合项目题
- 「先出题不给答案 → 用户回答 → 评分 → 诊断 → 补救练习」
- 结果写入 progress.md（快照）+ progress-log.md（详细记录），重排后续计划

### 4.10 最小可展示项目引导

- 根据用户基础和领域设计 MVP
- 输出：项目名称 + 介绍 + 核心功能 + 所需知识点 + 每日任务 + 验收标准
- 低代码方案备选
- 进阶方向建议
- 项目验收清单：能运行 / 能展示 / 能解释 / 能迭代

---

## 5. 开源仓库目录结构

```
learn-anything-skill/
│
├── README.md                          # 项目说明、快速开始、徽章
├── LICENSE                            # MIT
├── CHANGELOG.md                       # 版本变更记录
├── ARCHITECTURE.md                    # 本架构文档
├── CONTRIBUTING.md                    # 贡献指南
│
├── core/                              # 🧠 核心提示词（Agent 无关）
│   ├── prompts/                       # 按 locale 分层的提示词
│   │   ├── en-US/                     # 英文提示词（13 个）
│   │   └── zh-CN/                     # 中文提示词（13 个）
│   │
│   └── principles.md                  # 学习原则定义（全局引用）
│
├── templates/                         # 📁 学习仓库模板（按 locale 分层）
│   ├── en-US/                         # 英文模板（30天深度学习）
│   │   └── {{domain-slug}}/
│   │       ├── README.md
│   │       ├── AGENTS.md
│   │       ├── 00_domain_map.md
│   │       ├── 01_core_concepts/
│   │       ├── 02_case_studies/
│   │       ├── 03_exercises/
│   │       ├── 04_projects/
│   │       ├── 05_flashcards/
│   │       ├── 06_quizzes/
│   │       ├── 07_daily_review/
│   │       ├── 08_glossary.md
│   │       ├── 09_resources.md
│   │       ├── progress.md
│   │       └── progress-log.md
│   │
│   └── zh-CN/                         # 中文模板（30天深度学习）
│       └── {{domain-slug}}/
│           └── (同上结构，中文内容)
│
├── skills/                            # 🔌 Agent 原生 Skill 定义
│   ├── codex/                         # Codex / Claude Code Skills
│   │   └── domain-learning-master/
│   │       ├── SKILL.md               # Codex Skill 主文件
│   │       ├── AGENTS.md              # 学习仓库中使用的 AGENTS.md 模板
│   │       ├── CLAUDE.md              # Claude Code 用户的项目规则模板
│   │       ├── references/
│   │       │   ├── learning-principles.md
│   │       │   ├── error-types.md
│   │       │   └── project-patterns.md
│   │       ├── scripts/
│   │       │   ├── init-repo.sh           # 初始化仓库脚本
│   │       │   ├── update-progress.py     # 更新进度
│   │       │   └── generate-flashcard.py  # 生成压缩卡 HTML/PDF
│   │       └── templates/
│   │           ├── concept-template.md
│   │           ├── exercise-template.md
│   │           └── daily-review-template.md
│   │
│   ├── cursor/                        # Cursor Rules
│   │   └── .cursorrules              # Cursor 项目规则文件
│   │
│   ├── windsurf/                      # Windsurf Rules
│   │   └── .windsurfrules
│   │
│   └── copilot/                       # GitHub Copilot Instructions
│       └── .github/
│           └── copilot-instructions.md
│
├── adapters/                          # 🔄 跨 Agent 适配器
│   ├── README.md                      # 适配器使用说明
│   ├── codex.md                       # Codex 适配说明
│   ├── claude-code.md                 # Claude Code 适配说明
│   ├── cursor.md                      # Cursor 适配说明
│   ├── chatgpt.md                     # ChatGPT 适配说明
│   ├── generic-agent.md               # 通用 Agent 适配（手动复制粘贴）
│   └── legacy/                        # 旧版适配器（仅供参考）
│
├── scripts/                           # 🛠 自动化脚本
│   ├── install.sh                     # 一键安装（v1.0）
│   ├── new-domain.sh                  # 创建新领域学习仓库
│   ├── validate-repo.sh               # 校验仓库结构完整性 + progress.md 格式合规
│   ├── progress-analyzer.py           # 分析 progress.md 生成可视化报告
│   ├── flashcard-exporter.py          # 导出压缩卡为 Anki/PDF
│   └── quiz-generator.py              # 从概念文件自动生成测验题
│
├── examples/                          # 📚 示例学习仓库
│   ├── learn-ai-agent/                # 示例：学习 AI Agent
│   │   ├── README.md
│   │   ├── AGENTS.md
│   │   ├── 00_domain_map.md
│   │   ├── 01_core_concepts/
│   │   │   ├── 01-what-is-agent.md
│   │   │   ├── 02-agent-architecture.md
│   │   │   └── 03-tool-use.md
│   │   ├── 02_case_studies/
│   │   │   └── auto-gpt-case.md
│   │   ├── 03_exercises/
│   │   │   └── design-a-simple-agent.md
│   │   ├── 04_projects/
│   │   │   └── personal-research-agent/
│   │   ├── 05_flashcards/
│   │   ├── 06_quizzes/
│   │   ├── 07_daily_review/
│   │   ├── 08_glossary.md
│   │   ├── progress.md
│   │   └── progress-log.md
│   │
│   ├── learn-prompt-engineering/      # 示例：学习提示词工程
│   └── learn-nutrition/               # 示例：学习营养学
│
├── docs/                              # 📖 文档
│   ├── quick-start.md                 # 5 分钟快速开始
│   ├── user-guide.zh-CN.md                  # 用户手册
│   ├── agent-comparison.md            # 各 Agent 能力对比
│   ├── learning-methodology.md        # 学习方法论说明
│   ├── faq.md                         # 常见问题
│   └── images/                        # 文档配图
│       └── workflow.png
│
└── tests/                             # 🧪 测试
    ├── test-prompts.sh                # 提示词完整性测试
    ├── test-templates.sh              # 模板文件完整性测试
    └── test-scripts.sh                # 脚本功能测试
```

---

## 6. 组件分层说明

### 6.1 Core Prompts（核心提示词）— Agent 无关

这是产品的大脑。所有核心提示词以纯 Markdown 编写，使用 `{变量}` 形式的替换标记。任何 Agent 都可以直接使用（手动替换变量），或由适配器自动注入。

**设计原则**：
- 每个 prompt 文件是一个独立可用的指令单元
- 使用 `{domain}` `{user_background}` `{daily_time}` `{duration}` `{learning_goal}` `{final_artifact}` `{interface_language}` `{learning_language}` 等标准化变量
- 包含明确的输入期望和输出格式
- 引用 `principles.md` 中的共享学习原则

### 6.2 Templates（模板文件）— 文件系统

预定义的学习仓库目录结构。使用 `{{domain-slug}}` 作为模板目录名。分三个级别：
- **minimal**：7 天速通版，适合简单领域或快速浏览
- **standard**：30 天深度学习版（默认推荐）
- **deep**：90 天研究级，适合学术研究者

### 6.3 Skills（Agent 原生 Skill）— Agent 相关

针对不同 Agent 的原生 Skill / Rule 格式定义：
- **Codex/Claude Code**：SKILL.md + AGENTS.md + 子目录
- **Cursor**：.cursorrules（项目级规则文件）
- **Windsurf**：.windsurfrules
- **Copilot**：.github/copilot-instructions.md

### 6.4 Adapters（适配器）— 桥接层

将 Core Prompts 转换/包装为不同 Agent 的原生格式。每个适配器说明：
- 该 Agent 的能力边界（是否支持文件读写、命令执行、长指令等）
- 变量注入方式
- 已知限制和替代方案

### 6.5 Scripts（脚本）— 自动化层

辅助脚本，可以被 Agent 调用或用户手动运行：
- Shell 脚本：仓库初始化、环境检查
- Python 脚本：进度分析、卡片导出、测验生成
- 所有脚本输出纯文本或标准格式，方便 Agent 读取

### 6.6 Examples（示例项目）— 参考实现

展示完整使用效果的示例学习仓库。每个示例对应一个真实领域，展示从初始化到完成项目的全过程记录。

---

## 7. 学习状态机设计

```
                        ┌───────────────────────┐
                        │    INTERRUPTED         │  用户中断 N 天后返回
                        │    (中断)               │
                        │  resume-session.md     │
                        │  读取 progress.md      │
                        │  + 最近 3 天日志        │
                        └───────────┬───────────┘
                                    │ 重建状态
                                    ▼
                 ┌─────────────┐
                 │   INIT      │  创建学习仓库
                 │ (初始化)     │
                 └──────┬──────┘
                        │ init-repo.md
                        ▼
                 ┌─────────────┐
                 │  MAP_READY  │  知识地图生成完毕
                 │ (地图就绪)   │
                 └──────┬──────┘
                        │ knowledge-map.md + concept-breakdown.md
                        ▼
                 ┌─────────────┐
                 │  PLAN_READY │  30天计划生成完毕
                 │ (计划就绪)   │
                 └──────┬──────┘
                        │ learning-plan.md
                        ▼
            ┌───────────────────────┐
            │    IN_PROGRESS        │  每日循环
            │    (学习中)            │◄──────────────────────┐
            │                       │                       │
            │  每日:                  │                       │
            │  daily-session.md     │                       │
            │       ↓               │                       │
            │  daily-review.md      │                       │
            │       ↓               │                       │
            │  flashcard-generate.md│                       │
            │       ↓               │                       │
            │  update progress.md   │                       │
            │  (snapshot, ≤200行)    │                       │
            │  append progress-log  │                       │
            └───────┬───────────────┘                       │
                    │                                       │
                    │ 每 7 天: stage-test.md                │
                    ├─ 通过 ─────────────────────────────────┤
                    │                                       │
                    ├─ 未通过 (STAGE_TEST_FAILED)            │
                    │  诊断 → 补救 → 重排计划 ───────────────┘
                    │
                    │ 最后 7 天: project-design.md
                    ▼
            ┌───────────────────────┐
            │    PROJECT_DONE       │
            │    (项目完成)          │
            └───────────────────────┘
```

**关键状态转换说明**：

| 转换 | 触发条件 | 处理方式 |
|------|----------|----------|
| `INIT → MAP_READY` | `init-repo.md` 执行完毕，仓库结构就位 | 正常推进 |
| `MAP_READY → PLAN_READY` | 知识地图 + 概念拆解完成 | 正常推进 |
| `PLAN_READY → IN_PROGRESS` | 30 天学习计划生成完毕 | 正常推进 |
| `IN_PROGRESS → IN_PROGRESS`（每日） | `daily-session.md` + `daily-review.md` 完成 | 更新 progress.md 快照，追加 progress-log.md |
| `IN_PROGRESS → IN_PROGRESS`（阶段测试通过） | `stage-test.md` 得分 ≥ 及格线 | 继续推进 |
| `IN_PROGRESS → IN_PROGRESS`（阶段测试未通过）| `stage-test.md` 得分 < 及格线 | 诊断薄弱点 → 补救练习 → 重排后续计划 → 重新测试 |
| `INTERRUPTED → IN_PROGRESS` | 用户停止学习 N 天后返回，调用 `resume-session.md` | 读取 progress.md 快照 + 最近 3 天 progress-log 条目 → 重建状态 → 跳过已掌握内容 → 生成当日任务 |
| `IN_PROGRESS → PROJECT_DONE` | 学习天数达标 + 项目验收通过 | 最终复盘，归档仓库 |

---

## 8. 提示词变量标准

所有 Core Prompts 统一使用以下变量：

| 变量 | 说明 | 示例 |
|------|------|------|
| `{domain}` | 学习领域名称 | AI Agent |
| `{domain_slug}` | 领域名 URL 友好格式 | ai-agent |
| `{user_background}` | 用户当前基础 | 编程初级 / 零基础 / 有 Python 经验 |
| `{daily_time}` | 每天可用学习时间 | 2小时 |
| `{duration}` | 学习周期（天） | 30 |
| `{learning_goal}` | 学习目标 | 做出一个可展示的作品 |
| `{final_artifact}` | 期望最终产出 | 一个自动整理资料的 Agent |
| `{template_level}` | 模板级别 | minimal / standard / deep |
| `{day_number}` | 当前天数 | 3 |
| `{interface_language}` | 对话语言 | English / 中文 |
| `{learning_language}` | 学习材料语言 | English / 中文 |
| `{locale}` | 语言包标识 | en-US / zh-CN |
| `{agent_type}` | 当前使用的 Agent 类型 | codex / cursor / windsurf / generic |

`{agent_type}` 用于在 Core Prompts 中根据 Agent 能力差异调整行为：
- `codex`：生成可执行的 shell 命令、文件写入指令
- `cursor` / `windsurf`：生成文件编辑指令，避免依赖 CLI 专用能力
- `generic`：生成手动复制粘贴的完整内容块，不假设任何自动化能力

---

## 9. MVP vs v1.0 功能边界

### MVP（v0.1.0）— 核心闭环可运行

**目标**：一个人用 Codex/Claude Code 能跑通完整学习流程。

| 模块 | MVP 范围 | 排期 |
|------|----------|------|
| Core Prompts | 12 个核心提示词（+concept-relationship +resume-session） | P0 |
| progress.md 设计 | 拆为 progress.md（快照 ≤200 行）+ progress-log.md（完整日志） | P0 |
| Templates | standard 模板完成（含 progress.md + progress-log.md） | P0 |
| Skills | Codex SKILL.md + AGENTS.md + CLAUDE.md | P0 |
| Scripts | `new-domain.sh` + `validate-repo.sh` | P0 |
| Adapters | Codex 适配说明（含 AGENTS.md vs CLAUDE.md 差异说明） | P0 |
| Examples | `learn-ai-agent` 一个完整示例 | P0 |
| Docs | quick-start.md + user-guide.zh-CN.md（中文） | P0 |
| Tests | 模板完整性检查 + validate-repo.sh 自测 | P0 |

**MVP 不包含**：
- ❌ Cursor / Windsurf / Copilot 适配器
- ❌ minimal 和 deep 模板
- ❌ Python 脚本（progress-analyzer / flashcard-exporter / quiz-generator）
- ❌ 多语言支持
- ❌ 社区贡献模板
- ❌ CI/CD
- ❌ `install.sh` 一键安装

### v1.0 — 跨 Agent 完整产品

| 模块 | v1.0 新增 | 排期 |
|------|-----------|------|
| Templates | minimal + deep 模板 | P1 |
| Skills | Cursor / Windsurf / Copilot Skill 定义 | P1 |
| Adapters | 全部 5 个适配器文档 | P1 |
| Scripts | 全部 Python 辅助脚本 | P1 |
| Examples | 新增 2 个示例（提示词工程 + 营养学） | P1 |
| Docs | agent-comparison.md + faq.md + 英文文档 | P1 |
| Installer | `install.sh` 一键安装 | P1 |
| Tests | 完整测试套件 | P1 |
| 多语言 | i18n 框架 + 英文版 prompts | P2 |
| 社区 | CONTRIBUTING.md + 模板贡献规范 | P2 |

---

## 10. 开发计划

### Phase 0：基础架构搭建（2-3 天）

```
Week 1
├── Day 1-2: 创建仓库结构，编写 README.md、LICENSE、ARCHITECTURE.md
├── Day 2-3: 编写 principles.md（学习原则），定义变量标准
```

**交付物**：
- [ ] 仓库初始化，目录结构就位
- [ ] README.md（项目介绍 + 徽章 + 快速开始入口）
- [ ] ARCHITECTURE.md（本架构文档）
- [ ] LICENSE（MIT）
- [ ] core/principles.md

### Phase 1：Core Prompts（4-5 天）

```
Week 1-2
├── Day 3-4: 编写核心提示词 Part 1
│   ├── init-repo.md
│   ├── knowledge-map.md
│   ├── concept-breakdown.md
│   ├── concept-relationship.md
│   └── learning-plan.md
├── Day 5-6: 编写核心提示词 Part 2
│   ├── daily-session.md
│   ├── daily-review.md
│   ├── error-diagnosis.md
│   ├── stage-test.md
│   ├── flashcard-generate.md
│   └── project-design.md
├── Day 7: 编写特殊提示词
│   ├── resume-session.md（中断恢复）
│   └── full-workflow.md（聚合所有流程）
```

**交付物**：
- [ ] 12 个核心提示词文件
- [ ] full-workflow.md 聚合入口
- [ ] 所有提示词变量一致性检查
- [ ] 上下文窗口预算标注（每个 prompt 标注需要的传入文件 + 预估总 token）

### Phase 2：Templates + Codex Skill（3-4 天）

```
Week 2-3
├── Day 8-9: 创建 standard 模板
│   ├── 目录结构和初始文件
│   ├── README.md 模板
│   ├── AGENTS.md 模板（学习仓库规则）
│   ├── progress.md 模板（快照格式，≤200 行上限）
│   └── progress-log.md 模板（日志追加格式）
├── Day 10-11: 创建 Codex Skill
│   ├── SKILL.md
│   ├── AGENTS.md（Codex 项目级规则）
│   ├── CLAUDE.md（Claude Code 用户级规则模板）
│   ├── references/
│   ├── scripts/ (init-repo.sh)
│   └── templates/
├── Day 12: 创建辅助脚本
│   ├── new-domain.sh
│   └── validate-repo.sh（仓库结构 + progress.md 格式校验）
```

**交付物**：
- [ ] templates/en-US/ 完整模板（含 progress.md + progress-log.md）
- [ ] skills/codex/domain-learning-master/ 完整 Skill（含 CLAUDE.md）
- [ ] scripts/new-domain.sh + validate-repo.sh

### Phase 3：示例 + 文档（3-4 天）

```
Week 3-4
├── Day 13-15: 创建 learn-ai-agent 示例仓库
│   ├── 跑通完整流程
│   ├── 记录真实 progress.md
│   ├── 生成真实的 flashcard、quiz、review
│   └── 完成一个最小可展示项目
├── Day 16-17: 编写文档
│   ├── docs/quick-start.md
│   ├── docs/user-guide.zh-CN.md
│   └── 更新 README.md
```

**交付物**：
- [ ] examples/learn-ai-agent/ 完整示例
- [ ] docs/quick-start.md
- [ ] docs/user-guide.zh-CN.md
- [ ] 更新 README.md

### Phase 4：测试 + 发布 MVP（2-3 天）

```
Week 4
├── Day 18-19: 测试
│   ├── 模板完整性测试
│   ├── 提示词一致性测试
│   ├── 在 Codex 中实际运行完整流程
│   └── 修复 bug
├── Day 20-21: 发布
│   ├── CHANGELOG.md
│   ├── Git tag v0.1.0
│   └── 发布到 GitHub
```

**交付物**：
- [ ] 测试通过
- [ ] CHANGELOG.md
- [ ] v0.1.0 Release

### Phase 5：v1.0 扩展（3-4 周）

```
Week 5-8
├── 适配器：Cursor / Windsurf / Copilot / Generic LLM
├── 模板：minimal + deep
├── 脚本：Python 辅助脚本
├── 示例：+2 个领域
├── 文档：英文版 + FAQ + Agent 对比
├── 安装器：install.sh
└── v1.0.0 Release
```

---

## 11. 关键设计决策

### 决策 1：Core Prompts 使用纯 Markdown 而非 JSON/YAML

**理由**：Markdown 可以被任何 Agent 直接读取和理解，无需解析器。JSON Schema 虽然结构化，但增加了 Agent 的理解负担，且不同 Agent 对 JSON 的支持程度不一。Markdown 是 AI 最擅长理解的自然格式。

### 决策 2：模板使用文件系统目录而非 Docker/DevContainer

**理由**：目标用户包含非技术用户（学生、内容创作者）。学习仓库的本质是 Markdown 文件 + 目录结构，不需要容器化。保持极简降低使用门槛。

### 决策 3：以 AGENTS.md 为规范命名，CLAUDE.md 为显式镜像

**理由**：AGENTS.md 是 Codex 的项目级长期指令文件，也是原文的核心设计。但在 Claude Code 中，`CLAUDE.md` 有独立的读取逻辑和优先级（全局 `~/.claude/CLAUDE.md` + 项目级 `CLAUDE.md`），与 `AGENTS.md` 不完全等价。

**处理方式**：
- `skills/codex/domain-learning-master/` 中同时维护 `AGENTS.md` 和 `CLAUDE.md`，内容等价但适配各自格式
- `adapters/codex.md` 中明确说明两者的差异与推荐用法：
  - **仅 Codex 用户** → 使用 `AGENTS.md`
  - **Claude Code 用户** → 使用 `CLAUDE.md`（支持全局 + 项目级叠加）
  - **同时使用两者** → 两个文件都写入，内容保持同步
- 其他 Agent 适配器负责映射到各自的规则文件格式

### 决策 4：状态不依赖外部数据库

**理由**：整个学习系统的状态全部存储在文件系统（progress.md 及各目录文件）。这使得：
- 跨 Agent 兼容（不需要共享数据库）
- Git 友好（所有状态可版本控制）
- 备份简单（就是文件拷贝）
- Agent 通过读写文件即可获取和更新状态

### 决策 5：Scripts 独立于 Agent，通过 CLI 调用

**理由**：脚本是可选的增强功能，不是核心依赖。Agent 通过执行命令调用脚本，读取其输出。这使得脚本可以被任何支持命令执行的 Agent 使用，也可以被用户手动运行。

---

## 12. 风险与缓解

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| 不同 Agent 能力差异大 | 提示词在某些 Agent 上效果差 | 适配器层记录每个 Agent 的已知限制和替代方案 |
| Agent 上下文窗口限制 | 长提示词 + 大量文件无法一次加载 | Core Prompts 设计为模块化，每个可独立使用；提供 minimal 模板 |
| progress.md 膨胀 | 每日追加导致文件过大，Agent 读取超限 | progress.md 严格限制 ≤200 行（仅当前状态快照）；完整日志写入 progress-log.md；每日复盘只读最近 3 天日志 |
| Agent 指令遵循不稳定 | 输出格式不一致 | 提示词中使用明确格式约束 + 输出示例 |
| 领域知识质量依赖 Agent 基础能力 | 冷门领域知识可能不准 | 提示词中强调「如不确定请标注」+ 鼓励用户交叉验证 |
| 用户学习动力衰减 | 30 天计划难以坚持 | 每日任务控制在 60 分钟内 + 强调可交付成果的正反馈 |
| Agent 生态快速变化 | 适配器可能很快过时 | 适配器设计为独立文件，社区可快速更新 |

---

## 13. 成功指标

- **可用性**：一个新用户能在 5 分钟内创建第一个学习仓库（从安装到第一天任务生成）
- **完整性**：30 天学习路径覆盖从知识地图到可展示项目的完整闭环
- **跨 Agent**：至少支持 3 种不同的 AI Agent 跑通核心流程
- **社区**：有外部贡献者提交适配器 / 模板 / 示例
- **复用性**：用户能在一个月内用同一套 Skill Pack 学习 2+ 个不同领域

---

## 附录 A：Core Prompts 详细规格（含上下文预算）

| Prompt 文件 | 输入 | 输出 | Prompt 自身 | 需传入的上下文文件 | 典型总上下文 |
|-------------|------|------|------------|-------------------|-------------|
| `init-repo.md` | domain + background | 目录结构 + README + AGENTS.md | ~500 tokens | 无 | ~500 tokens |
| `knowledge-map.md` | domain | 10 项知识地图内容 | ~800 tokens | 无 | ~800 tokens |
| `concept-breakdown.md` | domain + concepts list | 每个概念的结构化拆解 | ~600 tokens | 00_domain_map.md | ~2,000 tokens |
| `concept-relationship.md` | concept A + concept B | 对比表 + 依赖图 + 混淆诊断 | ~400 tokens | 01_core_concepts/ 下相关文件 | ~2,500 tokens |
| `learning-plan.md` | domain + background + time | 30 天每日计划表 | ~700 tokens | 00_domain_map.md + 01_core_concepts/ | ~3,000 tokens |
| `daily-session.md` | day_number | 当日学习内容 | ~600 tokens | progress.md + 昨日 review + 对应概念文件 | ~3,500 tokens |
| `daily-review.md` | 今日学习内容 + 用户表现 | 复盘 + 更新 progress.md | ~400 tokens | progress.md + 今日 session 输出 | ~3,000 tokens |
| `error-diagnosis.md` | 用户错误答案 | 错误类型 + 补救策略 | ~400 tokens | 相关概念文件 | ~2,000 tokens |
| `stage-test.md` | 已学模块范围 | 完整测试卷（先不出答案） | ~500 tokens | progress.md + 本阶段概念文件 | ~4,000 tokens |
| `flashcard-generate.md` | 今日/本周内容 | 压缩卡 (Markdown) | ~300 tokens | 相关概念 + progress.md 薄弱点 | ~2,500 tokens |
| `project-design.md` | domain + background + time | 项目设计方案 | ~500 tokens | 00_domain_map.md + progress.md | ~2,500 tokens |
| `resume-session.md` | 无（完全从文件系统重建） | 恢复后的当日任务 | ~500 tokens | progress.md + 最近 3 天 progress-log | ~2,000 tokens |
| `full-workflow.md` | 所有变量 | 聚合启动指令 | ~1,000 tokens | 无（仅引用其他 prompt） | ~1,000 tokens |

> **设计约束**：所有 prompt 的「典型总上下文」均控制在 4,000 tokens 以内，确保即使在 8K 上下文窗口的 Agent 上也能留出足够空间给 Agent 的输出和对话历史。对于 minimal 模板用户（可能使用更小上下文的 Agent），建议分两步调用：先传入 progress.md 快照，再传入当日概念文件。

---

## 附录 B：参考文章核心洞察

原文章《如何使用 Codex 快速入门任何一个领域》(GeekCatX) 的核心洞察：

1. **Codex ≠ 问答机器**：Codex 的核心差异是文件读写 + 命令执行 + AGENTS.md 长期规则，这让它从「一次性对话」升级为「持续学习工程系统」
2. **五个系统理论**：知识地图 + 术语表 + 练习系统 + 项目系统 + 复盘系统
3. **最小必要知识**：先学会必须懂的 20%，跳过 60%，深入 20%
4. **考官模式**：学习最快的人是被检测最多的，AI 应该扮演考官而不仅是老师
5. **领域压缩**：不是堆资料，而是压缩领域——用压缩卡、费曼解释、最小概念集
6. **AGENTS.md 是灵魂**：不是普通笔记，而是写给 AI 的「长期规则文件」
7. **ChatGPT + Codex 分工**：ChatGPT 负责讲明白，Codex 负责工程化、文件化、项目化
