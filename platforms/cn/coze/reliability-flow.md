# Coze Reliability Flow

## 每次生成前

- 判断是否涉及当前事实、数字、版本、价格、考试、法律、医疗、金融、安全或模型能力。
- 如果涉及且 `web_access != available`，标记为未验证草稿。
- 检索 `core/reliability-protocol.zh-CN.md` 和 `references/zh-CN/source-quality-policy.md`。

## 每次生成中

- 不写伪造 URL、DOI、论文、日期、法规、benchmark。
- 对无法核查的内容标记 `[未验证]`。
- 对用户资料内容保留资料 ID 和位置。
- 对外部补充内容标记 `Supplemental`。

## 每次生成后

输出：

- Source Notes
- Freshness Risk
- Claims to Verify
- Last Verified
- Recommended Review Interval

并更新：

- `claims_to_verify`
- `open_risks`
- `source_policy`

