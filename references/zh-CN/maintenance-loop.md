# Maintenance Loop

Maintenance Loop 是维护者专用的修改与发布前检查循环。它不是学习功能，
不得改变 Guided Learning Mode、Interactive Beginner Lesson Mode 或
Material-Grounded Learning Mode 的默认学习行为。

## 边界

- 仅用于开发者维护、Codex 修改 Skill、发布前审查和多文件变更收口。
- 不用于普通学习者的学习会话。
- 不得新增默认学习循环、默认额外对话轮次或默认 token 消耗。
- 不得在用户未明确同意时自动继续学习会话。
- 不得把这套 loop 包装成用户学习卖点。

## 循环定义

1. 变更识别
2. 影响范围分析
3. 合同检查
4. 相关 eval 检查
5. harness 检查
6. 风险分类
7. 发布范围收口
8. 人工确认
9. commit / release

## 变更识别

维护前先识别本轮变更类型：

- SKILL.md change
- prompt change
- template change
- eval change
- harness change
- README / docs change
- platform adapter change
- reliability layer change
- material-grounding change
- release-only change

## 影响范围分析

以 `harness/architecture/change-impact-matrix.md` 作为影响范围来源。

必须检查：

| 变更类型 | 必须检查 |
| --- | --- |
| SKILL.md change | prompts、README、evals、adapters |
| prompt change | templates、examples、evals |
| template change | init scripts、examples、harness |
| reliability layer change | freshness notice、claim ledger、evals |
| material-grounding change | material prompts、templates、examples、evals |
| platform adapter change | capability matrix、platform package docs |
| README / docs change | 中英文同步和实际行为一致性 |

## 必跑检查

每轮维护至少运行：

```bash
python3 harness/scripts/run_all_checks.py --root . --report
```

涉及专项功能时运行对应检查：

```bash
python3 harness/scripts/check_guided_learning_mode.py --root . --report
python3 harness/scripts/check_freshness_notice.py --root . --report
python3 harness/scripts/check_material_grounding.py --root . --report
python3 harness/scripts/check_platform_adapters.py --root . --report
```

## 发布范围收口

发布前必须收口版本范围：

- 列出 tracked 修改文件。
- 列出 untracked 新文件。
- 分类哪些进入本版本。
- 分类哪些不进入本版本。
- 不确定文件必须暂停人工确认。
- 范围未收口时不得 tag 或 release。

## Commit Gate

commit 前必须确认：

- 没有敏感文件。
- 没有临时学习项目。
- 没有 `harness/reports/*.json`。
- 没有 `.env`、token 或 secret。
- 没有 PDF/PPT/Word 原始资料。
- 没有本地绝对路径泄露。
- 暂存文件属于本次版本范围。

## Release Gate

tag 或 release 前必须确认：

- 工作区干净，或未发布改动已 stash 并记录原因。
- tag 不存在。
- `RELEASE_NOTES.md` 已更新。
- `CHANGELOG.md` 已更新。
- harness 状态没有 `FAIL`。
- `READY_WITH_WARNINGS` 必须有人工解释。
- 工作区混乱或存在未审查变更时不得发布。

## 风险分类

- Low：纯文档修改，双语同步明确，且无行为变化。
- Medium：prompt、template、eval、adapter 或 harness 修改，范围清楚。
- High：SKILL.md、release gate、reliability、material-grounding 或平台行为修改。
- Blocked：范围不清、文件未审查、检查缺失、warning 无解释、tag 冲突、
  敏感资料或工作区发布状态混乱。

## 发布前收口模板

```text
Tracked 修改：

Untracked 新文件：

进入本版本：

不进入本版本：

需要人工确认的不确定文件：

Harness 状态：

READY_WITH_WARNINGS 解释：
```

所有不确定文件完成分类、所有 warning 有人工解释之前，不得 release。
