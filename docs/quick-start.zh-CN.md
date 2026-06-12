# 快速开始指南

先安装，再用一句话开始你的第一个学习项目。

## 前提

- 你有一个支持文件读写的 AI Agent（推荐 Claude Code 或 Codex）
- 你有一个想学的领域

## 第一步：安装到你的 Agent

最简单的方式是把仓库放到 Agent 能读取的位置：

```bash
git clone https://github.com/vesperchinn/learn-anything-skill.git
cd learn-anything-skill
```

然后按你的 Agent 类型接入：

- **Codex / Claude Code / Trae 这类文件型 Agent**：打开这个目录，或把这个目录加入 Agent 可读取的工作区。
- **支持 Skill 的 Agent**：把整个仓库作为一个 Skill 导入或放到 Skills 目录。
- **Coze、WorkBuddy、CodeBuddy 等国产 Agent 平台**：参考 `platforms/cn/` 里的平台说明配置。
- **普通聊天 Agent**：不能真正安装时，就复制本仓库里的提示词使用。

## 第二步：在对话框里调用

安装好以后，直接输入：

> 下面的「AI Agent」只是示例。你可以换成任何想学的领域，比如「Python」「营养学」「摄影」「英语写作」。

```
使用 learn-anything，帮我为「AI Agent」创建一个中文学习项目。
我的背景：技术小白。
我的目标：30 天后能看懂 AI Agent 的基本原理，并做出一个小项目。
每天可学习：1 小时。
```

如果你想从自己的资料开始，输入：

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

## 第三步：每天怎么继续

```
继续使用 learn-anything，读取我的学习进度，安排今天的学习。
```

学习完输入：

```
继续使用 learn-anything，帮我复盘今天学到的内容，并更新学习进度。
```

第 7 天或学完一个阶段后输入：

```
继续使用 learn-anything，给我做一次阶段测试。先出题，等我回答后再评分。
```

## 可选：如果你会用命令

可以直接生成一个学习仓库：

```bash
./scripts/new-domain.sh "你想学的领域" zh-CN
```

例如：

```bash
./scripts/new-domain.sh "AI Agent" zh-CN
cd learn-ai-agent
```

## 基于自己的资料学习

如果你已有 PDF、PPT、笔记、文档导出或课程资料，直接告诉 Agent 文件位置，或把资料放到学习项目里。

Agent 应该把你的资料作为 primary source，并把无法读取的 PDF/PPT 内容记录为提取问题，而不是猜测。

---

就这么简单。你只需要在对话框里继续说“使用 learn-anything”，Agent 会按学习流程往下走。

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
