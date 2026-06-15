# Maintenance Loop Prompt

对象：Codex 和维护者专用。

不要把这个 prompt 用于普通学习者会话。除非维护者明确要求修改用户端行为，
否则不得改变 Guided Learning Mode、Interactive Beginner Lesson Mode、
Material-Grounded Learning Mode、Day 1 规则、progress 规则或默认 token 消耗。

## Start Maintenance Loop

维护者开始修改 Skill 时使用：

```text
本轮要修改什么？
属于哪个模块？
会影响哪些文件？
需要跑哪些检查？
哪些用户学习流程必须保持不变？
```

必须输出：

```text
变更类型：
影响模块：
可能受影响文件：
需要运行的检查：
用户流程边界：
风险级别：
是否需要人工确认：
```

## Pre-commit Loop

暂存或 commit 前使用：

```text
哪些文件已暂存？
哪些文件未暂存？
哪些文件不应提交？
是否需要 scope freeze？
```

必须输出：

```text
已暂存文件：
未暂存文件：
Untracked 新文件：
不进入本次提交：
Scope freeze 状态：
阻塞文件：
是否允许 commit：
```

如果范围不清、暂存文件不属于本版本、存在敏感文件、存在临时学习项目、
暂存了 `harness/reports/*.json`、暂存了 PDF/PPT/Word 原始资料，或维护文件中
泄露本地绝对路径，则禁止 commit。

## Pre-release Loop

tag 或 release 前使用：

```text
版本号是什么？
CHANGELOG 是否更新？
RELEASE_NOTES 是否更新？
tag 是否存在？
工作区是否干净？
```

必须输出：

```text
版本号：
CHANGELOG 状态：
RELEASE_NOTES 状态：
Tag 状态：
工作区状态：
Harness 状态：
READY_WITH_WARNINGS 解释：
是否允许 release：
```

存在未审查变更、工作区混乱、tag 已存在、release notes 缺失、changelog 缺失、
harness 有 `FAIL`，或 `READY_WITH_WARNINGS` 没有人工解释时，禁止 release。

## Post-release Loop

release 后使用：

```text
Release 是否成功？
GitHub 页面是否更新？
是否需要恢复 stash？
是否需要创建下一轮 TODO？
```

必须输出：

```text
Release 结果：
GitHub 页面状态：
Stash 状态：
下一轮 TODO：
后续负责人：
```
