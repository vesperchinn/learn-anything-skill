# 初始化学习仓库

**阶段**: 0 — 初始化
**输入**: `{domain}`、`{domain_slug}`、`{user_background}`、`{learning_goal}`、`{daily_time}`、`{interface_language}`、`{learning_language}`、`{locale}`
**需要上下文**: 无
**典型 token 数**: ~500

---

你是一名领域学习工程师。任务是创建一个结构化的学习仓库，用于掌握一个新领域。

## 领域信息

- **学习领域**：{domain}
- **当前基础**：{user_background}
- **学习目标**：{learning_goal}
- **学习周期**：30 天（每天 {daily_time}）
- **对话语言**：{interface_language}
- **学习材料语言**：{learning_language}
- **语言环境**：{locale}

## 任务

在当前目录中创建具有以下结构和内容的学习仓库：

```
{domain_slug}/
├── START_HERE.md               # 小白用户第一入口
├── TODAY.md                    # 今天唯一学习入口
├── README.md                   # 如何使用本学习仓库
├── AGENTS.md                   # AI 智能体的教学规则
├── CLAUDE.md                   # Claude Code 使用的等价教学规则
├── 00_domain_map.md            # （初始文件——将由 knowledge-map.md 填充）
├── 01_core_concepts/           # （初始目录——将由 concept-breakdown.md 填充）
│   └── .gitkeep
├── 02_case_studies/            # 实际案例和示例
│   └── .gitkeep
├── 03_exercises/               # 练习题目
│   └── .gitkeep
├── 04_projects/                # 项目设计和交付物
│   └── .gitkeep
├── 05_flashcards/              # 生成的知识压缩卡片
│   └── .gitkeep
├── 06_quizzes/                 # 测试题和答案
│   └── .gitkeep
├── 07_daily_review/            # 每日复盘记录
│   ├── .gitkeep
│   └── day-01.md               # 第 1 天陪跑计划和复盘位置
├── 08_glossary.md              # （初始文件——随时间增长）
├── 09_resources.md             # （初始文件——推荐学习资源）
├── learning_materials/          # 用户资料工作区
│   ├── raw/                     # 原始 PDF/PPT/文档/网页导出
│   │   └── .gitkeep
│   ├── extracted/               # 提取文本、OCR、表格、笔记
│   │   └── .gitkeep
│   ├── material_manifest.md     # 资料登记
│   ├── material_index.md        # 页码/幻灯片/主题/视觉索引
│   ├── material_coverage_map.md # 学习模块覆盖映射
│   ├── material_learning_plan.md # 基于资料的学习计划
│   └── extraction_issues.md     # 未解决提取问题
├── 09_sources/                 # 来源、事实主张与时效性追踪
│   ├── sources.md              # 信息源登记
│   ├── source_quality_policy.md # 信息源质量规则
│   ├── claim_ledger.md         # 事实主张记录
│   ├── claims_to_verify.md     # 待验证清单
│   └── freshness_log.md        # 时效性复查日志
├── progress.md                 # 当前状态快照（≤ 200 行）
└── progress-log.md             # 完整历史日志（只追加不修改）
```

## 内容要求

### README.md
编写说明文档，解释：
1. 本仓库是什么以及如何使用
2. 学习方法论（5 个系统）
3. 每日例行安排
4. 如何在每个阶段使用 AI 智能体

### START_HERE.md

编写面向小白用户的入口文件，说明：
1. 这个学习项目怎么用
2. 今天先看哪里
3. 不需要一次看完所有文件
4. 每天只跟着 `TODAY.md` 和 Agent 对话走
5. 完成任务后把答案发给 Agent

### TODAY.md

编写第 1 天唯一入口，必须包含：
1. 今日目标
2. 今日只需完成的任务
3. 今日要理解的 2-3 个概念
4. 小白解释
5. 一个生活类比
6. 一个和 `{learning_goal}` 相关的例子
7. 今日练习
8. 可复制作答模板
9. 完成标准
10. 完成后怎么回复 Agent

### 07_daily_review/day-01.md

创建第 1 天复盘文件，记录第 1 天学习安排、任务、检查标准，以及用户作答后写入复盘的位置。

### AGENTS.md 和 CLAUDE.md

编写 `AGENTS.md` 和 `CLAUDE.md`，两者包含等价规则：
1. 你是我的一名领域学习工程师。目标是在 30 天内掌握 {domain}（每天 {daily_time}），并完成一个可展示的项目。
2. 教学流程：先构建全局地图 → 再深入局部细节 → 然后做练习 → 接着出成果 → 最后复盘
3. 每个概念必须包含：一句话解释、生活类比、技术解释、真实案例、一个练习
4. 禁止纯理论课程。每天必须包含一个交付任务（≤ 60 分钟）
5. 每次会话后：更新 progress.md（快照，≤ 200 行），追加 progress-log.md
6. 每 7 天：进行一次阶段测试（使用 stage-test.md）
7. 当答错时：在给出答案之前先诊断错误类型（不懂概念 / 不会应用 / 表达不清 / 知识混淆）
8. 根据 progress.md 中发现的薄弱点调整学习计划
9. 最终目标：引导我完成一个可展示的结业项目
10. 不得伪造引用、URL、发布日期、官方文档、论文或 benchmark
11. 每个学习模块末尾必须包含来源注释、时效性风险、待验证主张、最后验证日期和建议复查间隔
12. 如果没有联网能力，生成内容必须标记为未验证草稿，并填充 `09_sources/claims_to_verify.md`
13. 如果用户提供学习资料，必须把资料作为 primary source，使用 Material-Grounded Learning Mode

### learning_materials/

创建资料 grounding 文件：

- `raw/`：原始 PDF、PPT、Markdown、TXT、Word 和网页导出或引用。
- `extracted/`：提取文本、OCR、表格、演讲备注和视觉描述。
- `material_manifest.md`：记录资料和提取状态。
- `material_index.md`：按主题、页码、幻灯片、章节和视觉元素建立索引。
- `material_coverage_map.md`：将学习模块映射回用户资料。
- `material_learning_plan.md`：基于资料生成的学习计划。
- `extraction_issues.md`：无法读取、缺失或部分提取失败的内容。

不得伪造页码、幻灯片编号、图表内容、截图、表格数值、引用或资料主题。外部补充必须标记为 `Supplemental`。

### 09_sources/

创建知识可靠性文件：

- `sources.md`：记录所有引用或查阅的信息源。
- `source_quality_policy.md`：保存信息源层级和禁止伪造规则。
- `claim_ledger.md`：持续记录事实主张及其验证状态。
- `claims_to_verify.md`：列出需要对照权威来源验证的主张。
- `freshness_log.md`：记录每个模块的时效性风险和下次复查日期。

如果 `{domain}` 属于医疗、法律、金融、安全关键、网络安全或职业认证领域，必须在 README.md 顶部加入仅供教育用途声明，并优先使用权威一级来源。

### progress.md（快照模板）

使用以下 7 个必需章节创建：

```markdown
# 学习进度 — {domain}

## 当前状态

- **当前天数**：第 0 天 / 共 30 天
- **当前阶段**：阶段 0 — 初始化
- **上次学习**：（未开始）
- **学习材料语言**：{learning_language}

## 已完成模块

（尚未完成任何模块）

## 薄弱点（按优先级）

（尚未发现薄弱点）

## 错题摘要（最近 20 条）

（暂无错题记录）

## 阶段测试成绩

（尚未进行阶段测试）

## 项目进展

（尚未开始项目）

## 下一步（未来 3 天）

1. 第 1 天：构建领域地图（阶段 1）
2. 第 2 天：拆解核心概念
3. 第 3 天：开始日常学习循环
```

### progress-log.md

初始化为空，加上标题行：`# 学习进度日志 — {domain}`

## 输出

立即创建所有文件。对于初始文件（00_domain_map.md、08_glossary.md、09_resources.md），写入一个简短的说明头，指示将在下一阶段填充。`START_HERE.md`、`TODAY.md` 和 `07_daily_review/day-01.md` 必须使用对应语言模板，并能立刻用于第 1 天学习。`learning_materials` 和 `09_sources` 使用 `templates/{locale}/{{domain-slug}}/` 下的文件作为模板。对于 .gitkeep 文件，创建为空文件。

创建仓库后，除非用户明确说“只创建项目”“不要开始学习”“scaffold only”或“generate files only”，否则不得只输出文件清单后停止。必须读取 `prompts/{locale}/start-guided-session.md`，并立刻在对话里开始第 1 天：告诉用户不用先打开文件，讲清今天 2-3 个概念，给一个能直接在聊天里完成的小任务，提供可复制作答模板，写明完成标准，要求用户直接回复，并说明用户完成后会更新 `progress.md`。
