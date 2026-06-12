# Learn Anything Skill Pack

> 把 AI Agent 从「问答机器」变成「领域学习工程师」——一条命令启动一个完整的学习项目。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-blue)](./CHANGELOG.md)
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

当前版本：**v0.2.0**。详见 [release notes](./docs/release-notes-v0.2.0.md)
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

### 1. 安装

```bash
git clone https://github.com/vionlabs/learn-anything-skill.git
cd learn-anything-skill
```

### 2. 用你的 AI Agent 初始化学习仓库

**Codex / Claude Code 用户**：在终端中进入工作目录，启动 Agent，然后输入：

```
请读取 learn-anything-skill/core/prompts/zh-CN/init-repo.md，
为「AI Agent」领域创建一个学习仓库。
```

**其他 Agent 用户**：复制 `core/prompts/zh-CN/init-repo.md` 的内容，替换 `{domain}` 变量，粘贴给 Agent。

### 3. 开始学习

按顺序使用 `core/prompts/{locale}/` 下的提示词：

```
init-repo.md        →  创建仓库（Day 0）
knowledge-map.md    →  生成知识地图（Day 0）
learning-plan.md    →  制定 30 天计划（Day 0）
daily-session.md    →  每天学习（Day 1-30）
daily-review.md     →  每天复盘（Day 1-30）
stage-test.md       →  每 7 天阶段测试
project-design.md   →  最后 7 天设计项目
```

详细指南见 [docs/quick-start.zh-CN.md](./docs/quick-start.zh-CN.md)。

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

欢迎贡献新适配器、模板、示例或改进提示词。详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 致谢

灵感源自 [@GeekCatX](https://x.com/GeekCatX) 的文章《如何使用 Codex 快速入门任何一个领域》。

## 许可证

MIT © 2026 Learn Anything Skill Pack Contributors
