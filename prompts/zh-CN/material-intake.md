# 资料接收

**模式**：Material-Grounded Learning
**输入**：`{domain}`、`{material_paths}`、`{material_urls}`、`{agent_type}`、`{file_read_access}`、`{locale}`
**输出文件**：`learning_materials/material_manifest.md`、`learning_materials/extraction_issues.md`、`09_sources/sources.md`

---

你正在基于用户提供的资料准备学习仓库。

## 任务

在生成任何课程内容前，先收集、分类并记录学习资料。用户资料是本学习仓库的 primary source。

## 支持资料

- PDF
- PPT / PPTX
- Markdown
- TXT
- Word / DOCX
- HTML 或网页导出
- OCR 文本或用户粘贴文本

## 必须步骤

1. 将每个文件、URL 或粘贴文本块记录到 `learning_materials/material_manifest.md`。
2. 如果有文件访问能力，将原始文件复制或引用到 `learning_materials/raw/`。
3. 将可读文本提取到 `learning_materials/extracted/`。
4. 标记每份资料是否包含图表、截图、表格、图示、流程图或演讲备注。
5. 将无法读取、缺失或部分提取失败的内容记录到 `learning_materials/extraction_issues.md`。
6. 将每份用户资料同步登记到 `09_sources/sources.md`，Source Type 设为 `Material`，Tier 设为 `Primary`，Status 标记为已验证 / 部分提取 / unresolved。

## 无文件读取能力时的降级

如果 Agent 不能读取文件，不得声称已经读过资料。必须要求用户：

- 粘贴相关文本；
- 提供 OCR 结果；
- 将文件转换为 Markdown 或 TXT；
- 将幻灯片导出为文本和图片；
- 或只生成资料处理清单。

## 禁止

- 在资料索引完成前生成泛泛课程。
- 伪造页码、幻灯片编号、图表内容、引用或主题。
- 根据文件名推断视觉细节。
- 把外部知识当作资料内容。
- 不得跳过 `09_sources/sources.md`；用户资料也必须作为 source 追踪。

除非用户另有要求，输出使用 `{locale}` 对应语言。
