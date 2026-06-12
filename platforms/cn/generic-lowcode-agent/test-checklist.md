# Generic Low-Code Agent Test Checklist

- [ ] System prompt 已使用 `system-prompt.zh-CN.md`。
- [ ] Workflow 已按 `workflow-template.md` 配置，或已启用无工作流降级。
- [ ] Knowledge base 已上传 `knowledge-base-template.md` 中列出的核心协议、提示词、模板和引用文档。
- [ ] State schema 已按 `state-schema.md` 配置，或每轮输出 `learning_state`。
- [ ] 无文件读取时要求粘贴文本、OCR 或 Markdown/TXT 转换。
- [ ] 无联网时输出未验证草稿和待核查清单。
- [ ] 用户资料先登记和索引，不假装读取不可访问文件。
- [ ] 阶段测试先出题，等待用户提交后再评分。
- [ ] 每轮输出下一步任务和当前状态摘要。
