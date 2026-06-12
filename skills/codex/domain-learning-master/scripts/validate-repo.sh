#!/bin/bash
# validate-repo.sh — Check learning repository structure and progress.md format.
# Usage: ./validate-repo.sh <repo-path> [locale]
set -euo pipefail

REPO="${1:-.}"
LOCALE="${2:-}"

PASS=0
FAIL=0

check_file() {
    if [ -f "$REPO/$1" ]; then
        PASS=$((PASS + 1))
    else
        echo "FAIL: missing $1"
        FAIL=$((FAIL + 1))
    fi
}

check_dir() {
    if [ -d "$REPO/$1" ]; then
        PASS=$((PASS + 1))
    else
        echo "FAIL: missing $1/"
        FAIL=$((FAIL + 1))
    fi
}

check_section() {
    if grep -q "^## $2" "$REPO/$1" 2>/dev/null; then
        PASS=$((PASS + 1))
    else
        echo "FAIL: $1 missing section '$2'"
        FAIL=$((FAIL + 1))
    fi
}

# Auto-detect locale from progress.md if not specified
if [ -z "$LOCALE" ]; then
    if [ -f "$REPO/progress.md" ]; then
        if grep -q "^## 当前状态" "$REPO/progress.md" 2>/dev/null; then
            LOCALE="zh-CN"
        else
            LOCALE="en-US"
        fi
    else
        LOCALE="en-US"
    fi
fi

echo "=== Validating: $REPO (locale: $LOCALE) ==="

# Structure
for d in 01_core_concepts 02_case_studies 03_exercises 04_projects 05_flashcards 06_quizzes 07_daily_review learning_materials learning_materials/raw learning_materials/extracted 09_sources; do
    check_dir "$d"
done

for f in README.md AGENTS.md 00_domain_map.md progress.md progress-log.md 08_glossary.md 09_resources.md learning_materials/material_manifest.md learning_materials/material_index.md learning_materials/material_coverage_map.md learning_materials/material_learning_plan.md learning_materials/extraction_issues.md 09_sources/sources.md 09_sources/source_quality_policy.md 09_sources/claim_ledger.md 09_sources/claims_to_verify.md 09_sources/freshness_log.md; do
    check_file "$f"
done

# progress.md sections (locale-aware)
if [ "$LOCALE" = "zh-CN" ]; then
    SECTIONS=("当前状态" "已完成模块" "薄弱点" "错题摘要" "阶段测试成绩" "项目进展" "下一步")
else
    SECTIONS=("Current Status" "Completed Modules" "Weak Points" "Error Summary" "Stage Test Scores" "Project Progress" "Next Steps")
fi

for s in "${SECTIONS[@]}"; do
    check_section "progress.md" "$s"
done

# Line count check
if [ -f "$REPO/progress.md" ]; then
    LINES=$(wc -l < "$REPO/progress.md")
    if [ "$LINES" -le 200 ]; then
        PASS=$((PASS + 1))
    else
        echo "WARN: progress.md has $LINES lines (>200)"
    fi
fi

echo "=== $PASS passed, $FAIL failed ==="
[ "$FAIL" -eq 0 ] || exit 1
