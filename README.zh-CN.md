# Learn Anything Skill Pack

> 把 AI Agent 从「问答机器」变成「领域学习工程师」——一条命令启动一个完整的学习项目。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.1--beta-blue)](./CHANGELOG.md)
[![Locales](https://img.shields.io/badge/locales-en--US_|_zh--CN-blue)](./README.md)

[English](./README.md)

## 这是什么？

**Learn Anything Skill Pack** 是一个跨 AI Agent 的开源学习系统工具包。它包含核心提示词、学习仓库模板、Skill 定义、适配器和自动化脚本，让任意支持文件读写或提示词调用的 AI Agent（Codex / Claude Code / Cursor / ChatGPT 等）都能帮助用户：

- 5 分钟搭建一个结构化的「领域学习仓库」
- 生成知识地图，看清领域全貌
- 按 30 天计划每天学、练、测、复盘
- 自动诊断错误类型，针对性补救
- 每 7 天阶段测试，验证真实掌握程度
- 最终完成一个可展示的最小项目
- 基于自己的 PDF、PPT、Markdown、TXT、Word 文档和网页导出学习

当前版本：**v0.2.1-beta**。详见 [release notes](./docs/release-notes-v0.2.1-beta.md)
和 [roadmap](./ROADMAP.md)。

## 和直接问 ChatGPT 有什么不同？

| 直接问 ChatGPT | 用 Learn Anything Skill Pack |
|---------------|---------------------------|
| 一次性对话，知识不沉淀 | 所有内容文件化，存储在结构化仓库中 |
| AI 倾向于输出解释性文字 | 内置练习 + 测验 + 项目系统，确保动手 |
| 不知道自己学到哪了 | progress.md 持续追踪进度和薄弱点 |
| 每次学新领域要重新设计方法 | 一套 Skill Pack，反复复用 |
| 答错只给答案 | 四类错误诊断 + 针对性补救练习 |
| AI 容易自信但没有来源 | Knowledge Reliability Layer 会追踪来源、未验证主张和时效性风险 |

## 快速开始

### 1. 安装到你的 Agent

最简单的方式是先把这个仓库放到 Agent 能读取的位置：

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

然后按你的 Agent 类型接入：

- **Codex / Claude Code / Trae 这类文件型 Agent**：打开这个目录，或把这个目录加入 Agent 可读取的工作区。
- **支持 Skill 的 Agent**：把整个仓库作为一个 Skill 导入或放到 Skills 目录。
- **Coze、WorkBuddy、CodeBuddy 等国产 Agent 平台**：参考 `platforms/cn/` 里的平台说明，把提示词、知识库和 Workflow 按平台方式配置。
- **普通聊天 Agent**：不能真正安装时，就复制本仓库里的提示词使用。

### 2. 在对话框里调用

安装好以后，直接输入：

> 下面的「AI Agent」只是示例。你可以换成任何想学的领域，比如「Python」「营养学」「摄影」「英语写作」。

```
使用 learn-anything，帮我为「AI Agent」创建一个中文学习项目。
我的背景：技术小白。
我的目标：30 天后能看懂 AI Agent 的基本原理，并做出一个小项目。
每天可学习：1 小时。
```

Agent 会创建学习仓库，并立刻在对话里开始第 1 天。你不用先打开生成的一堆 Markdown 文件。

如果你已经有 PDF、PPT、笔记或课程资料，也可以直接说：

```
使用 learn-anything，基于我提供的资料创建一个学习项目。
请优先引用资料内容，并标记哪些内容还需要核实。
```

如果你的 Agent 不能识别 Skill 名称，但能读取文件，就输入：

> 同样，把「AI Agent」换成你真正想学的领域。

```
请读取 learn-anything-skill/core/prompts/zh-CN/init-repo.md，
为「AI Agent」领域创建一个学习仓库。
```

默认行为是：创建仓库后继续进入第 1 天陪跑学习。如果只想生成文件，可以说“只创建项目”“不要开始学习”或 `scaffold only`。

## 关键特性：陪跑学习模式

默认情况下，创建学习仓库后，Agent 不会只丢给你一堆文件路径。

它会立刻开始第 1 天学习：

- 告诉你今天学什么；
- 用小白能懂的话解释 2-3 个概念；
- 给一个很小的任务；
- 给可复制的作答模板；
- 告诉你完成标准；
- 让你直接在对话里回复；
- 根据你的答案更新 `progress.md`。

这对技术小白、学生、非开发者、内容创作者、运营、老师和自媒体用户更友好。你不用先打开一堆 Markdown 文件，也不用自己判断第一步该看哪里。

新学习项目会包含：

- `START_HERE.md`：小白用户入口说明
- `TODAY.md`：今天唯一学习入口
- `07_daily_review/day-01.md`：第 1 天安排、检查标准和复盘位置

如果你只想创建文件，可以明确说：

```text
只创建项目，不要开始学习。
```

只有你明确说“只创建项目”“不要开始学习”“scaffold only”或“generate files only”时，Agent 才可以只创建文件后停止。

### 3. 后续学习怎么叫 Agent

每天继续输入：

```
继续使用 learn-anything，读取我的学习进度，安排今天的学习。
```

```
继续使用 learn-anything，帮我复盘今天学到的内容，并更新学习进度。
```

```
继续使用 learn-anything，给我做一次阶段测试。先出题，等我回答后再评分。
```

### 可选：用命令快速生成

如果你会用终端，可以直接运行：

```bash
./scripts/new-domain.sh "你想学的领域" zh-CN
```

例如：

```bash
./scripts/new-domain.sh "AI Agent" zh-CN
```

```
cd learn-ai-agent
```

详细指南见 [docs/quick-start.zh-CN.md](./docs/quick-start.zh-CN.md)。

## 多平台支持

Learn Anything 现在包含 **Platform Adapter Layer**，用于把仓库型 Codex Skill 分发到不能直接读取 `SKILL.md` 的平台。低代码平台支持在本 beta 版本中标记为 experimental，正式依赖前需要在自己的平台环境中验证。

| 形态 | 适用平台 | 使用方式 |
| --- | --- | --- |
| Codex 原生 Skill | Codex、能读取本仓库的文件型 Agent | 读取 `SKILL.md`、`core/`、`templates/`、`prompts/`、`references/`，直接创建学习仓库 |
| 平台适配包 | 国产 Agent 平台：Coze、WorkBuddy、Trae、CodeBuddy、通用低代码 Agent | 使用 `platforms/` 下的平台说明、知识库包、工作流、变量、记忆和测试清单 |
| 聊天降级包 | 普通聊天 Agent | 复制核心协议和提示词，通过对话输出路径标记 Markdown |

详见 [platforms/README.md](./platforms/README.md)、[platforms/capability-matrix.md](./platforms/capability-matrix.md) 和 [dist/README.md](./dist/README.md)。

## 国产 Agent 平台适配说明

| 平台 | 适配目录 | 推荐形态 | 文件写入 | 主要限制 |
| --- | --- | --- | --- | --- |
| 扣子 Coze | [platforms/cn/coze/](./platforms/cn/coze/) | Bot + 知识库 + Workflow + 变量 + 记忆 | 通常不直接写本地文件 | 不能假设可读取 `SKILL.md`；需拆成 Prompt、KB、Workflow |
| WorkBuddy | [platforms/cn/workbuddy/](./platforms/cn/workbuddy/) | 办公任务 Skill + 报告输出 | 视平台任务能力而定 | 更适合报告、任务单、资料处理，不等同完整仓库工程 |
| Trae | [platforms/cn/trae/](./platforms/cn/trae/) | 文件型工程 Agent | 支持 | 可保留读取 `SKILL.md`、模板、提示词和引用文档 |
| CodeBuddy | [platforms/cn/codebuddy/](./platforms/cn/codebuddy/) | 代码/文档 Agent + 知识库 | 仓库连接时支持 | 需把 `references`、`templates`、`prompts` 打成知识库包 |
| 通用低代码 Agent | [platforms/cn/generic-lowcode-agent/](./platforms/cn/generic-lowcode-agent/) | System Prompt + Workflow + KB + State | 通常不支持 | 必须提供无文件读取、无联网、无工作流降级 |

不同平台能力不同，不能保证所有功能完全一致。文件型 Agent 可以创建和维护学习仓库；低代码平台通常只能通过知识库、工作流、变量、记忆和提示词模拟学习闭环；普通聊天 Agent 只能输出可复制保存的 Markdown。

## 用自己的资料学习

如果你已有课程 PDF、PPT、笔记、文档导出或网页导出，使用 **Material-Grounded Learning Mode**：

1. 将原始文件放入 `learning_materials/raw/`，或告诉 Agent 文件位置。
2. 使用 `prompts/{locale}/material-intake.md` 登记并提取资料。
3. 使用 `prompts/{locale}/material-grounded-learning-repo.md` 基于资料生成知识地图、学习计划、概念、测验、复盘和进度追踪。
4. 用 `material_coverage_map.md` 查看每个模块来自资料、部分来自资料，还是属于补充内容。

此模式下，用户资料是 primary source。外部知识必须标记为 `Supplemental`。如果 PDF/PPT 中的图表、截图、表格或流程图无法提取，就记录到 `learning_materials/extraction_issues.md`，不能猜测。

如果 Agent 没有文件读取能力，需要让用户粘贴文本、提供 OCR、转换为 Markdown/TXT、把幻灯片导出为文本和图片，或只生成资料处理清单。

### 隐私和版权提醒

不要把公司内部文档、合同、个人健康或财务记录、付费课程材料、未公开稿件、受版权保护的书籍放进公开学习仓库。敏感资料应放在私有仓库，提取前先移除个人信息，并确认你有权存储和转换这些材料。

## 目录结构

```
learn-anything-skill/
├── SKILL.md                    # Skill 入口（给 Agent 读的路由文件）
├── README.md                   # 英文首页
├── README.zh-CN.md             # 中文首页（你在这里）
├── core/                       # 核心提示词（Agent 无关）
│   ├── prompts/
│   │   ├── en-US/              #   13 个英文提示词模块
│   │   └── zh-CN/              #   13 个中文提示词模块
│   ├── *-protocol.*.md         #   平台无关协议
│   └── principles.md           #   学习原则
├── templates/                  # 学习仓库模板
│   ├── en-US/                  #   英文
│   └── zh-CN/                  #   中文
├── references/                 # 学习方法论文档
│   ├── en-US/                  #   英文
│   └── zh-CN/                  #   中文
├── examples/                   # 完整示例仓库
│   ├── en-US/learn-ai-agent/   #   英文示例
│   └── zh-CN/learn-ai-agent/   #   中文示例
├── adapters/                   # 跨 Agent 适配说明
├── platforms/                  # 平台适配层（Coze / WorkBuddy / Trae / CodeBuddy 等）
├── dist/                       # 发行包清单和构建说明
├── prompts/                    # 基于资料学习的提示词
├── skills/codex/               # Codex / Claude Code 原生 Skill
├── scripts/                    # 自动化脚本
├── evals/                      # 测试用例
│   ├── en-US/                  #   英文测试
│   └── zh-CN/                  #   中文测试
└── docs/                       # 用户文档
```

## 自动化 Python 脚本

我们在 `scripts/` 目录下提供了一套 Python 工具来增强你的学习体验：

- `init_learning_repo.py`: 支持 Windows/Mac/Linux 的跨平台脚手架工具。
- `generate_index.py`: 动态扫描整个学习仓库，自动生成一份带有大纲链接的 `index.md`。
- `export_flashcards.py`: 自动抽取闪卡内容，并导出为 Anki 可直接导入的 CSV 格式。
- `validate_locale.py`: 启发式语言检测工具，防止学习仓库中出现“语言溢出”（如英文材料混入中文）。
- `check_unverified_claims.py`: 检查 `[未验证]`、`[unverified]` 和未验证草稿标记。
- `check_stale_modules.py`: 检查 `09_sources/freshness_log.md` 中是否有超过复查日期的模块。
- `check_source_notes.py`: 检查学习模块是否包含来源注释、时效性风险、待验证主张、最后验证日期和建议复查间隔。

两个创建仓库脚本都支持 `--dry-run`，并且不会覆盖已经存在的
`learn-{domain-slug}` 目录。

## Maintenance Harness

维护防护层位于 [harness/](./harness/)。它不是新学习功能，而是用于日常维护和发布前检查，帮助发现结构缺失、locale 不一致、平台适配缺口、资料学习规则缺失、来源与时效规则缺失等问题。

运行全部只读检查：

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

报告写入 `harness/reports/`，文件名带时间戳，不覆盖旧报告。`PASS` 表示通过，`WARN` 表示需要人工确认，`FAIL` 表示发布前必须处理。

修改 `SKILL.md` 前，查看 [change-impact-matrix.md](./harness/architecture/change-impact-matrix.md)，并运行 `check_skill_manifest.py`、`check_docs_consistency.py`、`check_eval_coverage.py`。新增平台适配前，使用 [platform-adapter-checklist.md](./harness/checklists/platform-adapter-checklist.md)。发布前使用 [release-checklist.md](./harness/checklists/release-checklist.md) 和 [release-gates.md](./harness/architecture/release-gates.md)。

## 事实准确性、时效性和幻觉风险

Learn Anything 为生成的学习仓库加入了 Knowledge Reliability Layer：

- **来源优先**：事实主张应优先依据权威来源。Agent 不得伪造 URL、论文、发布日期、官方文档或 benchmark。
- **无来源不下结论**：缺少来源的主张必须标记为 `[未验证]`，或写入 `09_sources/claims_to_verify.md`。
- **时效性风险**：每个模块标记为 🟢 稳定、🟡 演变中或 🔴 易变，并给出建议复查间隔。
- **无联网退化**：如果 Agent 不能联网，生成内容必须标记为 **未验证草稿**，并生成待验证清单。
- **高风险领域**：医疗、法律、金融、安全关键、网络安全和职业认证内容必须加入仅供教育用途声明，并优先使用权威来源。
- **私密或受版权保护资料**：除非已经获得授权并移除敏感信息，否则不要放入公开仓库。

## 支持的 Agent

| Agent | 支持程度 | 适配说明 |
|-------|---------|---------|
| **Codex** | 完整支持（原生 Skill） | [codex.md](./adapters/codex.md) |
| **Claude Code** | 有文档化流程（CLAUDE.md） | [claude-code.md](./adapters/claude-code.md) |
| **Cursor** | 有文档化流程（.cursorrules） | [cursor.md](./adapters/cursor.md) |
| **ChatGPT** | 复制粘贴提示词 | [chatgpt.md](./adapters/chatgpt.md) |
| **通用 Agent** | 手动复制提示词 | [generic-agent.md](./adapters/generic-agent.md) |

## 平台能力差异

| 能力 | Codex / Trae / 文件型 Agent | Coze / WorkBuddy / CodeBuddy 知识库模式 | 普通聊天 Agent |
| --- | --- | --- | --- |
| 读取仓库文件 | 支持 | 通常不支持或需上传知识库 | 不支持 |
| 写入学习仓库 | 支持 | 通常输出报告或平台内容 | 不支持 |
| 资料学习 | 可读取本地文件 | 通过上传文件或知识库 | 需要粘贴文本/OCR |
| 来源记录 | 写入 `09_sources/` | 写入报告、变量或记忆 | 写入对话摘要 |
| 工作流 | 由 Agent 执行 | 平台 Workflow | 手动多轮对话 |
| 降级方式 | 文件不可用时输出代码块 | 无插件时转为知识库/报告模式 | 输出 `learning_state` 和 Markdown 块 |

## 学习方法论

本 Skill Pack 基于五个系统的核心理念：

1. **知识地图** — 解决「不知道这个领域有什么」
2. **术语表** — 解决「听不懂专业词」
3. **练习系统** — 解决「以为懂了其实没懂」
4. **项目系统** — 解决「学了很多但不会用」
5. **复盘系统** — 解决「学完就忘、错了不改」

详见 [references/zh-CN/learning-principles.md](./references/zh-CN/learning-principles.md)。

## 国际化

| Locale | 对话语言 | 学习材料 | 状态 |
|--------|---------|---------|------|
| `en-US` | English | English | ✅ 完整 |
| `zh-CN` | 中文 | 中文 | ✅ 完整 |

`{interface_language}` 和 `{learning_language}` 可以独立设置。
例如：「用中文对话，但学习仓库用英文」。

详见 [SKILL.md § Language and Locale Policy](./SKILL.md#language-and-locale-policy)。

## 贡献

欢迎贡献新适配器、模板、示例或改进提示词。详见
[CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md)，英文版见
[CONTRIBUTING.md](./CONTRIBUTING.md)。

## 致谢

灵感源自 [@GeekCatX](https://x.com/GeekCatX) 的文章《如何使用 Codex 快速入门任何一个领域》。

## 许可证

MIT © 2026 Learn Anything Skill Pack Contributors
