#!/bin/bash
# test-prompts.sh — Verify all core prompt files exist and are well-formed
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
PROMPTS="$ROOT/core/prompts/zh-CN"
MATERIAL_PROMPTS="$ROOT/prompts/zh-CN"
PASS=0
FAIL=0

# Required prompt files (MVP set)
REQUIRED=(
    "init-repo.md"
    "knowledge-map.md"
    "concept-breakdown.md"
    "concept-relationship.md"
    "learning-plan.md"
    "daily-session.md"
    "daily-review.md"
    "error-diagnosis.md"
    "stage-test.md"
    "flashcard-generate.md"
    "project-design.md"
    "resume-session.md"
    "full-workflow.md"
)

MATERIAL_REQUIRED=(
    "material-intake.md"
    "material-grounded-learning-repo.md"
    "material-review-session.md"
    "material-quiz-generation.md"
    "material-gap-analysis.md"
)

echo "=== Core Prompts Test ==="
echo ""

for prompt in "${REQUIRED[@]}"; do
    file="$PROMPTS/$prompt"
    if [ -f "$file" ]; then
        # Check it has a title (# heading)
        if grep -q '^# ' "$file"; then
            echo "PASS: $prompt (has title)"
            PASS=$((PASS + 1))
        else
            echo "FAIL: $prompt — missing level-1 heading"
            FAIL=$((FAIL + 1))
        fi
    else
        echo "WARN: $prompt — file not yet created (MVP-in-progress)"
    fi
done

for prompt in "${MATERIAL_REQUIRED[@]}"; do
    file="$MATERIAL_PROMPTS/$prompt"
    if [ -f "$file" ]; then
        if grep -q '^# ' "$file"; then
            echo "PASS: material/$prompt (has title)"
            PASS=$((PASS + 1))
        else
            echo "FAIL: material/$prompt — missing level-1 heading"
            FAIL=$((FAIL + 1))
        fi
    else
        echo "FAIL: material/$prompt — file not found"
        FAIL=$((FAIL + 1))
    fi
done

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="

if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
