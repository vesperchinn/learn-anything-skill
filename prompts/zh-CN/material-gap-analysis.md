# 资料缺口分析

**模式**：Material-Grounded Learning
**输入**：`learning_materials/material_index.md`、`learning_materials/material_coverage_map.md`、`progress.md`
**输出文件**：更新后的 `material_coverage_map.md`、`claims_to_verify.md`、`extraction_issues.md`

---

分析用户资料覆盖了什么、缺了什么，以及哪些内容需要提取复核。

## 必须分析

1. 找出资料直接覆盖的概念。
2. 找出部分覆盖的概念。
3. 找出会影响学习目标的缺口。
4. 找出 unresolved extraction issues。
5. 为每个缺口建议：
   - 暂时忽略；
   - 向用户索取更好的资料；
   - 使用明确标记的 `Supplemental` 内容处理。

## 输出规则

- 更新 `learning_materials/material_coverage_map.md`。
- 对无法读取内容，更新 `learning_materials/extraction_issues.md`。
- 对外部补充主张，更新 `09_sources/claims_to_verify.md`。
- 不得把 supplemental 内容写成来自用户资料。
