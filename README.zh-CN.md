<p align="center">
  <img src="./assets/readme/hero.zh-CN.svg" width="100%" alt="Learn Anything Skill Pack — 把 AI Agent 变成陪跑式学习教练：先搭建结构化学习仓库，再立刻在对话里开始第 1 天课程">
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <a href="./CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.2.4--beta-blue" alt="Version 0.2.4-beta"></a>
  <a href="./README.md"><img src="https://img.shields.io/badge/locales-en--US_|_zh--CN-blue" alt="Locales: en-US and zh-CN"></a>
</p>

<p align="center">
  <a href="./README.md">English</a> · 中文
</p>

一个跨 AI Agent 的开源学习系统工具包：让 Agent 不再只做一次性问答，而是为任意领域搭建一个结构化的学习仓库，并立刻在对话里带你开始第 1 天课程。

## 看看实际效果

你只发一条消息：

```text
使用 learn-anything，帮我为「AI Agent」创建一个中文学习项目。
我的背景：刚开始接触这个领域。
我的目标：14 天后能看懂 AI Agent 的基本原理，并做出一个小项目。
每天可学习：1 小时。
```

Agent 会创建学习仓库——然后立刻在对话里开始上课：

```text
已创建学习项目：./learn-ai-agent

你不用先打开文件，我们直接在对话里学完第 1 天。

今天先只学一句话：
Agent 是一个能自己调用工具、分步骤完成目标的 AI 系统。

我先示范：一个选题 → 三个文章标题，并给出检查标准。
对比讲解：为什么「帮我把文章写好」这种提法太模糊。
你来做：从你自己的工作流里挑一小步，填好作答模板。
```

不用先打开一堆 Markdown 文件。第 1 天就在对话里进行，你的回答会更新 `progress.md`。完整对话记录见 [examples/zh-CN/guided-learning-session.md](./examples/zh-CN/guided-learning-session.md)，完整的学习仓库示例见 [examples/zh-CN/learn-ai-agent/](./examples/zh-CN/learn-ai-agent/)。

如果你只想生成文件，可以说「只创建项目」「不要开始学习」或 `scaffold only`。

## 它是怎么工作的

<p align="center">
  <img src="./assets/readme/workflow.zh-CN.svg" width="100%" alt="工作方式：在对话里说出想学的主题，Agent 搭建结构化学习仓库，第 1 天课程立刻在对话里开始，随后通过复盘与测试让进度持续滚动">
</p>

整个工具包建立在五个学习系统之上：

1. **知识地图** —— 解决「这个领域到底有什么」
2. **术语表** —— 解决「看不懂术语」
3. **练习系统** —— 解决「以为懂了其实没懂」
4. **项目系统** —— 解决「学了很多却用不出来」
5. **复习系统** —— 解决「全忘了、错题没人管」

详见 [references/zh-CN/learning-principles.md](./references/zh-CN/learning-principles.md)。

## 快速开始

### 1. 安装到你的 Agent

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

然后按你的 Agent 类型接入：

- **Codex / Claude Code / Trae 这类文件型 Agent**：打开这个目录，或把它加入 Agent 可读取的工作区。
- **支持 Skill 的 Agent**：把整个仓库作为一个 Skill 导入，或放到 Skills 目录。
- **Coze、WorkBuddy、CodeBuddy 等国产 Agent 平台**：参考 `platforms/cn/` 里的平台说明配置提示词、知识库和 Workflow。
- **普通聊天 Agent**：不能真正安装时，直接复制本仓库里的提示词使用。

### 2. 在对话框里调用

> 「AI Agent」只是示例。你可以换成任何想学的领域，比如「Python」「营养学」「摄影」「英语写作」。

```text
使用 learn-anything，帮我为「AI Agent」创建一个中文学习项目。
我的背景：刚开始接触这个领域。
我的目标：14 天后能看懂 AI Agent 的基本原理，并做出一个小项目。
每天可学习：1 小时。
```

已经有 PDF、PPT、笔记或课程资料？直接说：

```text
使用 learn-anything，基于我提供的资料创建一个学习项目。
请优先引用资料内容，并标记哪些内容还需要核实。
```

如果你的 Agent 不能识别 Skill 名称，但能读取文件：

```text
请读取 learn-anything-skill/core/prompts/zh-CN/init-repo.md，
为「AI Agent」领域创建一个学习仓库。
```

### 3. 继续学习

```text
继续使用 learn-anything。读取我的进度，开始今天的学习。
```

```text
继续使用 learn-anything。复盘我今天学的内容，并更新我的进度。
```

```text
继续使用 learn-anything。给我一次阶段测试，先提问，等我回答后再评分。
```

### 可选：命令行方式

```bash
./scripts/new-domain.sh "你的主题" zh-CN
```

完整指南见 [docs/quick-start.zh-CN.md](./docs/quick-start.zh-CN.md)。

## 和直接问 ChatGPT 有什么不同？

| 直接问 ChatGPT | 用 Learn Anything Skill Pack |
|---------------|---------------------------|
| 一次性对话，知识不沉淀 | 所有内容文件化，存储在结构化仓库中 |
| AI 倾向于输出解释性文字 | 内置练习 + 测验 + 项目系统，确保动手 |
| 不知道自己学到哪了 | `progress.md` 持续追踪进度和薄弱点 |
| 每次学新领域要重新设计方法 | 一套 Skill Pack，反复复用 |
| 答错只给答案 | 四类错误诊断 + 针对性补救练习 |
| AI 容易自信但没有来源 | Knowledge Reliability Layer 会追踪来源、未验证主张和时效性风险 |

## 工具包里有什么

### 陪跑学习模式

创建学习仓库后，Agent 不会只丢给你一堆文件路径——它会立刻开始第 1 天：提示时效性风险、讲一个核心概念、给一个很小的任务、给可复制的作答模板，并告诉你怎么判断答案能不能用。遇到零基础用户时，会自动切换为「我先示范 → 坏例子/好例子 → 你再自己做」的陪跑式教学。新项目会包含 `START_HERE.md`、`TODAY.md` 和 `07_daily_review/day-01.md`，让第一步永远明确。

### 知识可靠性层

- **来源优先**：主张应有一手或权威来源支撑；Agent 不得编造 URL、论文、发布日期或 benchmark 结果。
- **无来源、不主张**：没有来源的内容标记为 `[unverified]`，或移入 `09_sources/claims_to_verify.md`。
- **时效性风险**：每个模块标记为 🟢 稳定、🟡 演进中、🔴 易过期，并在创建项目时打印时效提示和建议复查周期。
- **无网降级**：Agent 无法联网时，生成内容标记为「未验证草稿」，并附核实清单。
- **高风险领域**：医疗、法律、金融、安全、认证类内容要求教育用途声明，并优先使用权威来源。

这套机制能降低幻觉风险，但不保证绝对正确。

### 基于自有资料的学习模式

用你自己的 PDF、PPT、Markdown、笔记、手册和网页导出来构建学习计划：

1. 把原始文件放进 `learning_materials/raw/`，或告诉 Agent 文件位置。
2. Agent 会登记并提取资料内容，再基于资料构建知识地图、计划、概念讲解、测验和复盘。
3. `material_coverage_map.md` 标明哪些模块完全基于资料、部分基于资料或属于补充；资料之外的知识一律标记为 `Supplemental`，提取失败的内容会被记录而不是猜测。

**隐私提示**：不要把公司机密文件、付费课程资料和受版权保护的书籍放进公开的学习仓库；提取前请先移除个人数据。

### 多语言支持

| 语言 | 界面 | 学习材料 | 状态 |
|------|------|----------|------|
| `en-US` | English | English | ✅ 完整 |
| `zh-CN` | 中文 | 中文 | ✅ 完整 |

`{interface_language}` 和 `{learning_language}` 可以独立设置——比如「用中文对话，但学习仓库用英文」。详见 [SKILL.md § Language and Locale Policy](./SKILL.md#language-and-locale-policy)。

### 多平台支持

| 形态 | 目标平台 | 工作方式 |
| --- | --- | --- |
| 文件型 Agent / 原生 Skill | Codex、Claude Code、Cursor、Trae | 直接读取 `SKILL.md`、`core/`、`templates/`、`prompts/`、`references/`，写出学习仓库并开始陪跑 |
| 平台适配包 | Coze、WorkBuddy、CodeBuddy、通用低代码 Agent | 使用 `platforms/` 下的平台提示词、知识库、Workflow、变量和记忆 |
| 纯聊天适配包 | 普通聊天 Agent | 复制核心协议，输出带路径标签的 Markdown 块 |

低代码平台支持在本 beta 中仍为实验性质，依赖前请在你自己的工作区验证。详见 [platforms/README.md](./platforms/README.md) 和 [platforms/capability-matrix.md](./platforms/capability-matrix.md)。

### 自动化脚本

`scripts/` 目录下的 Python 工具：跨平台仓库脚手架（`init_learning_repo.py`）、目录索引生成（`generate_index.py`）、Anki 记忆卡导出（`export_flashcards.py`）、语言混杂检测（`validate_locale.py`），以及未验证主张、过期模块和来源记录的可靠性检查。脚手架脚本支持 `--dry-run`，且不会覆盖已存在的学习目录。

### 维护 Harness

面向维护者的只读检查层位于 [harness/](./harness/)：在发布前捕捉结构漂移、语言不一致、平台适配缺口和可靠性规则缺口。运行全部检查：

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

## 目录结构

```
learn-anything-skill/
├── SKILL.md          # Skill 入口（Agent 的路由文件）
├── core/             # 核心提示词与平台中立协议（en-US / zh-CN）
├── templates/        # 学习仓库模板
├── references/       # 方法论参考
├── examples/         # 完整示例仓库与对话记录
├── prompts/          # 资料驱动学习提示词
├── adapters/         # 跨 Agent 适配指南
├── platforms/        # 平台适配（Coze / WorkBuddy / Trae / CodeBuddy …）
├── scripts/          # 自动化脚本
├── harness/          # 维护者检查工具
├── evals/            # 测试套件
└── docs/             # 用户文档
```

## 文档

- [快速开始](./docs/quick-start.zh-CN.md) · [用户指南](./docs/user-guide.zh-CN.md)
- [Release notes](./RELEASE_NOTES.md) · [Roadmap](./ROADMAP.md) · [Changelog](./CHANGELOG.md)
- Agent 适配：[Codex](./adapters/codex.md) · [Claude Code](./adapters/claude-code.md) · [Cursor](./adapters/cursor.md) · [ChatGPT](./adapters/chatgpt.md) · [通用](./adapters/generic-agent.md)

## 参与贡献

欢迎贡献——新的适配器、模板、示例或提示词改进。见 [CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md) 或 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 致谢

灵感来自 [@GeekCatX](https://x.com/GeekCatX) 关于用 Codex 快速学习任意领域的文章。

<p align="center">
  <a href="https://github.com/oil-oil/beautify-github-readme"><img src="./assets/readme/made-with-beautify.svg" width="300" alt="README made with beautify-github-readme"></a>
</p>

## 许可证

MIT © 2026 Learn Anything Skill Pack Contributors
