# Trae Project Rules

## 读取顺序

1. 读取根目录 `SKILL.md`，理解学习流程。
2. 根据用户语言读取 `core/*.{locale}.md`。
3. 需要资料学习时读取 `prompts/{locale}/material-*.md`。
4. 需要模板时复制并填充 `templates/{locale}/`。
5. 需要可靠性规则时读取 `references/{locale}/source-quality-policy.md`、`freshness-policy.md`、`claim-verification-guide.md`。

## 文件写入

- 新建学习仓库使用 `learn-{domain_slug}/`。
- 不覆盖已有目录或用户文件。
- 修改 `progress.md` 前保留核心状态，完整历史写入 `progress-log.md`。
- 文件名保持 ASCII。
- 本地项目中的平台适配文件只写入 `platforms/`。

## 必须保留

- 学习闭环
- 资料 Grounding
- 来源记录
- 时效检查
- 防幻觉规则
- 无文件读取/无联网/无工作流降级说明

