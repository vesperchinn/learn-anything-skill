# Trae Commands

## 初始化学习仓库

```bash
./scripts/new-domain.sh "AI Agent" zh-CN
```

## Python 初始化

```bash
python3 scripts/init_learning_repo.py --domain "AI Agent" --locale zh-CN --dry-run
```

## 生成索引

```bash
python3 scripts/generate_index.py learn-ai-agent
```

## 检查未验证主张

```bash
python3 scripts/check_unverified_claims.py learn-ai-agent
```

## 检查过时模块

```bash
python3 scripts/check_stale_modules.py learn-ai-agent
```

## 检查来源注释

```bash
python3 scripts/check_source_notes.py learn-ai-agent
```

## 平台包 dry-run

```bash
python3 scripts/build_platform_packages.py --platform trae --locale zh-CN
```

