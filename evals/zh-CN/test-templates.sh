#!/bin/bash
# test-templates.sh — Verify standard template completeness
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
TEMPLATE="$ROOT/templates/zh-CN/{{domain-slug}}"
PASS=0
FAIL=0

check_file() {
    if [ -f "$1" ]; then
        echo "PASS: $2"
        PASS=$((PASS + 1))
    else
        echo "FAIL: $2 — missing: $1"
        FAIL=$((FAIL + 1))
    fi
}

check_dir() {
    if [ -d "$1" ]; then
        echo "PASS: $2"
        PASS=$((PASS + 1))
    else
        echo "FAIL: $2 — missing: $1"
        FAIL=$((FAIL + 1))
    fi
}

echo "=== Template Structure Test ==="
echo ""

# Root template files
check_file "$TEMPLATE/README.md"        "Template README.md"
check_file "$TEMPLATE/START_HERE.md"    "Template START_HERE.md"
check_file "$TEMPLATE/TODAY.md"         "Template TODAY.md"
check_file "$TEMPLATE/AGENTS.md"        "Template AGENTS.md"
check_file "$TEMPLATE/CLAUDE.md"        "Template CLAUDE.md"
check_file "$TEMPLATE/00_domain_map.md" "Template 00_domain_map.md"
check_file "$TEMPLATE/progress.md"      "Template progress.md"
check_file "$TEMPLATE/progress-log.md"  "Template progress-log.md"
check_file "$TEMPLATE/08_glossary.md"    "Template 08_glossary.md"
check_file "$TEMPLATE/09_resources.md"   "Template 09_resources.md"
check_file "$TEMPLATE/learning_materials/material_manifest.md"      "Template learning_materials/material_manifest.md"
check_file "$TEMPLATE/learning_materials/material_index.md"         "Template learning_materials/material_index.md"
check_file "$TEMPLATE/learning_materials/material_coverage_map.md"  "Template learning_materials/material_coverage_map.md"
check_file "$TEMPLATE/learning_materials/material_learning_plan.md" "Template learning_materials/material_learning_plan.md"
check_file "$TEMPLATE/learning_materials/extraction_issues.md"      "Template learning_materials/extraction_issues.md"
check_file "$TEMPLATE/09_sources/sources.md"               "Template 09_sources/sources.md"
check_file "$TEMPLATE/09_sources/source_quality_policy.md" "Template 09_sources/source_quality_policy.md"
check_file "$TEMPLATE/09_sources/claim_ledger.md"          "Template 09_sources/claim_ledger.md"
check_file "$TEMPLATE/09_sources/claims_to_verify.md"      "Template 09_sources/claims_to_verify.md"
check_file "$TEMPLATE/09_sources/freshness_log.md"         "Template 09_sources/freshness_log.md"
check_file "$TEMPLATE/07_daily_review/day-01.md"           "Template 07_daily_review/day-01.md"

# Subdirectories
check_dir "$TEMPLATE/01_core_concepts"  "Template 01_core_concepts/"
check_dir "$TEMPLATE/02_case_studies"   "Template 02_case_studies/"
check_dir "$TEMPLATE/03_exercises"      "Template 03_exercises/"
check_dir "$TEMPLATE/04_projects"       "Template 04_projects/"
check_dir "$TEMPLATE/05_flashcards"     "Template 05_flashcards/"
check_dir "$TEMPLATE/06_quizzes"        "Template 06_quizzes/"
check_dir "$TEMPLATE/07_daily_review"   "Template 07_daily_review/"
check_dir "$TEMPLATE/learning_materials" "Template learning_materials/"
check_dir "$TEMPLATE/learning_materials/raw" "Template learning_materials/raw/"
check_dir "$TEMPLATE/learning_materials/extracted" "Template learning_materials/extracted/"
check_dir "$TEMPLATE/09_sources"        "Template 09_sources/"

# .gitkeep in empty dirs
for dir in 01_core_concepts 02_case_studies 03_exercises 04_projects 05_flashcards 06_quizzes 07_daily_review; do
    check_file "$TEMPLATE/$dir/.gitkeep" "Template $dir/.gitkeep"
done
check_file "$TEMPLATE/learning_materials/raw/.gitkeep" "Template learning_materials/raw/.gitkeep"
check_file "$TEMPLATE/learning_materials/extracted/.gitkeep" "Template learning_materials/extracted/.gitkeep"

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="

if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
