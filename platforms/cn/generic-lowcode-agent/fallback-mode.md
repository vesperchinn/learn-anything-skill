# Generic Low-Code Fallback Mode

## 无文件读取

- 不声称已读取用户资料。
- 要求用户粘贴文本、提供 OCR、转换 Markdown/TXT 或上传到知识库。
- 只输出资料处理清单，不生成资料内容总结。

## 无文件写入

输出路径标记 Markdown：

````markdown
### Save as: learn-{domain_slug}/README.md
```markdown
内容
```
````

## 无联网

- 标记 `状态：未验证草稿`。
- 所有当前、数字、版本、政策、考试、医疗、法律、金融、安全相关主张进入待核查清单。
- 给出建议核查来源，但不伪造链接。

## 无工作流

用一条 system prompt 执行。每次只完成一个阶段，并在末尾说明下一阶段需要用户输入什么。

## 无记忆

每轮输出 `learning_state`，并提示用户下次继续时粘贴。

## 无知识库

把核心协议压缩进 system prompt。输出更短，但仍必须保留学习闭环、资料规则、来源规则和降级说明。

