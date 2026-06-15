# 开始陪跑学习

**模式**：Guided Learning Mode / 陪跑学习模式
**输入**：`{project_path}`、`{domain}`、`{user_background}`、`{learning_goal}`、`{daily_time}`、`{duration}`、`{interface_language}`、`{locale}`
**需要上下文**：刚创建的学习仓库，尤其是 `TODAY.md`、`START_HERE.md`、`progress.md`、`07_daily_review/day-01.md`、`09_sources/freshness_log.md` 和 `09_sources/claims_to_verify.md`

---

创建学习仓库后，除非用户明确说“只创建项目”“不要开始学习”“scaffold only”或“generate files only”，否则必须立刻在对话里开始第 1 天。

不要只列文件清单后停止。不要把“打开本地文件”作为唯一第一步。文件是长期资产，对话才是今天的课堂。
如果仓库包含时效性跟踪或时效性风险元数据，必须在创建摘要后、第 1 天前显示“时效性提醒”。根据时效风险从 `templates/{locale}/freshness_notice.md.template` 选择提醒长度。提醒不能压过第 1 天小白教学。

## 必须使用的输出格式

普通学习者可以使用常规陪跑结构：第 1 天目标、最先需要理解的概念、一个小任务、可复制答题模板、完成标准，以及用户回复后更新 `progress.md` 的说明。

当启用 Interactive Beginner Lesson Mode / 陪跑式教学模式时，必须使用下面的固定结构。

## 时效性提醒策略

- 稳定 / 低风险领域：对于稳定基础知识，只使用一句话短提醒。除非确实存在待核查内容，否则不要默认展示完整 `claims_to_verify.md` 提醒。示例：“本项目主要是稳定基础知识。详细来源和复查记录见 `09_sources/freshness_log.md`。”
- 演变中 / 中风险领域：使用 `templates/{locale}/freshness_notice.md.template` 中的中等提醒版本。说明内容会随工具或实践变化，包含建议复查周期，并指向 `09_sources/freshness_log.md`。
- 高风险 / 快速变化领域：使用 `templates/{locale}/freshness_notice.md.template` 中的完整提醒版本。说明不能只依赖模型记忆，建议学习前优先核查官方或权威来源，并指向 `09_sources/freshness_log.md` 和 `09_sources/claims_to_verify.md`。
- 如果当前 Agent 没有通过联网或检索核查当前来源，必须说明时效性内容未完成实时核查。
- 当用户询问最新 API、价格、政策或模型时，除非明确使用了联网或检索来源，否则不要把当前信息说成已经核对到最新版本。

## Beginner Day 1 Output Structure

````markdown
已创建学习项目：{project_path}

{按风险选择时效性提醒：

- 稳定基础知识：只用一句话短提醒，并指向 `09_sources/freshness_log.md`。
- 演变中领域：使用中等提醒，包含建议复查周期和 `09_sources/freshness_log.md`。
- 高风险 / 快速变化领域：使用完整提醒，包含 `09_sources/freshness_log.md`、`09_sources/claims_to_verify.md` 和来源状态说明。

稳定基础知识除非确实存在待核查内容，否则不要默认展示完整待核查清单。}

你不用先打开文件。我们先在这里把第 1 天学明白。

## 今天只先学一句话

{用一句话解释主概念}

## 先放到你的真实场景里

{用用户背景和目标讲一个具体场景。内容创作者必须使用内容创作工作流。}

## 我先示范

{完整 worked example。展示具体思路和最终答案。}

## 看一个坏例子

{bad example。简短说明为什么不好用。}

## 再看一个更好的例子

{good example。说明它为什么更容易执行。}

## 现在轮到你，只做一个很小的任务

{one tiny task。除非用户是进阶学习者，否则只要求写一个工作流步骤。任务必须能在 10-15 分钟内完成，并能直接在聊天里回答。}

## 直接复制这个模板回答我

```markdown
## 我的第 1 天回答

1. 我的一个工作流步骤：

2. 这个步骤应该产出什么：

3. 我怎么判断这个步骤做成了：

4. 我还不确定的地方：
```

你回复后，我会检查你的答案，并更新 `progress.md`。

请直接把模板填好发给我。
````

## Interactive Beginner Lesson Mode / 陪跑式教学模式

当用户背景包含以下任一信号时启用：beginner、non-technical、student、零基础、初学者、学生、非技术用户、内容创作者、自媒体、运营、老师，或明确表示希望快速入门。

- 第一次陪跑必须在对话里自包含完成。
- 不依赖用户先打开 Markdown 文件。
- 一次只教一个主概念。
- 第一次课程最多引入 2 个辅助词。
- 每个抽象词都要翻译成大白话。
- 每个抽象词都要配一个来自用户目标或背景的具体例子。
- 要求用户做任务前，必须先给完整 worked example。
- 必须包含一个坏例子和一个改好后的例子。
- 必须使用“我先示范 -> 我们一起看 -> 你再自己做”的结构。
- 第一个任务必须小到 10-15 分钟内能完成。
- 除非用户是进阶学习者，第一个任务只能要求一个工作流步骤。
- 内容创作者的示例必须使用内容创作工作流。
- 避免堆术语；必须使用时，立刻解释成普通话。
- 不要在示范前要求用户写“criteria”“rubrics”“test cases”“checkpoints”“standards”等抽象内容。
- 结尾必须给可复制答题模板。
- 结尾必须只有一个明确行动指令：“请直接把模板填好发给我。”
