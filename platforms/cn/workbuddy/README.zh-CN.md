# WorkBuddy 适配包

本目录把 Learn Anything 设计成办公任务 Skill 调用包，适用于资料整理、学习计划、阶段报告、培训材料和知识复盘类任务。

## 推荐使用方式

| 场景 | 使用文件 |
| --- | --- |
| Skill 调用说明 | `skill-call-prompt.zh-CN.md` |
| 任务流 | `task-workflow.md` |
| 知识库上传 | `knowledge-base-package.md` |
| 文件处理 | `file-processing-rules.md` |
| 报告输出 | `report-output-template.md` |
| 发布检查 | `publishing-checklist.md` |

## 定位

WorkBuddy 版本不要求创建完整代码仓库。它应把学习过程包装成办公交付物：

- 学习资料登记表
- 学习计划报告
- 知识地图报告
- 每日学习任务单
- 阶段测评与错因分析
- 资料覆盖与待核查清单

## 能力边界

- 能读取上传文件时，按资料 Grounding 流程处理。
- 不能读取文件时，请用户粘贴文本、提供 OCR 或转换格式。
- 能生成文件时，输出报告；不能生成文件时，用 Markdown 正文输出。
- 无联网时，所有当前事实标记为未验证草稿。

