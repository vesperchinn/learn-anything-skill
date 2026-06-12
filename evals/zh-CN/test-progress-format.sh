#!/bin/bash
# test-progress-format.sh — Verify progress.md has all required sections
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

PASS=0
FAIL=0

check_section() {
    local file="$1"
    local section="$2"
    if grep -q "^## $section" "$file" 2>/dev/null; then
        echo "PASS: Section '$section' found"
        PASS=$((PASS + 1))
    else
        echo "FAIL: Section '$section' NOT found in $file"
        FAIL=$((FAIL + 1))
    fi
}

check_line_count() {
    local file="$1"
    local max="$2"
    local count
    count=$(wc -l < "$file")
    if [ "$count" -le "$max" ]; then
        echo "PASS: Line count $count ≤ $max"
        PASS=$((PASS + 1))
    else
        echo "WARN: Line count $count exceeds $max (snapshot may be too large)"
    fi
}

echo "=== progress.md Format Test ==="
echo ""

# Test the template progress.md
TEMPLATE_FILE="$ROOT/templates/zh-CN/{{domain-slug}}/progress.md"
if [ -f "$TEMPLATE_FILE" ]; then
    echo "Testing: $TEMPLATE_FILE"
    check_section "$TEMPLATE_FILE" "当前状态"
    check_section "$TEMPLATE_FILE" "已完成模块"
    check_section "$TEMPLATE_FILE" "薄弱点"
    check_section "$TEMPLATE_FILE" "错题摘要"
    check_section "$TEMPLATE_FILE" "阶段测试成绩"
    check_section "$TEMPLATE_FILE" "项目进展"
    check_section "$TEMPLATE_FILE" "下一步"
    check_line_count "$TEMPLATE_FILE" 200
fi

# Test the example progress.md
EXAMPLE_FILE="$ROOT/examples/zh-CN/learn-ai-agent/progress.md"
if [ -f "$EXAMPLE_FILE" ]; then
    echo ""
    echo "Testing: $EXAMPLE_FILE"
    check_section "$EXAMPLE_FILE" "当前状态"
    check_section "$EXAMPLE_FILE" "已完成模块"
    check_section "$EXAMPLE_FILE" "薄弱点"
    check_section "$EXAMPLE_FILE" "错题摘要"
    check_section "$EXAMPLE_FILE" "阶段测试成绩"
    check_section "$EXAMPLE_FILE" "项目进展"
    check_section "$EXAMPLE_FILE" "下一步"
    check_line_count "$EXAMPLE_FILE" 200

    # Additional: check that weak points have error type tags
    if grep -qE '\[不懂概念\]|\[不会应用\]|\[表达不清\]|\[知识混淆\]' "$EXAMPLE_FILE"; then
        echo "PASS: Weak points contain error type tags"
        PASS=$((PASS + 1))
    else
        echo "FAIL: Weak points missing error type tags ([不懂概念]/[不会应用]/[表达不清]/[知识混淆])"
        FAIL=$((FAIL + 1))
    fi
fi

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="

if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
