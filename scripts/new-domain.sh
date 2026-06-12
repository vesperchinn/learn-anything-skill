#!/bin/bash
# new-domain.sh — Scaffold a new learning repository from locale-aware templates.
#
# Usage:
#   ./scripts/new-domain.sh <domain-name> [locale]
#   ./scripts/new-domain.sh --dry-run <domain-name> [locale]
#   ./scripts/new-domain.sh "AI Agent"
#   ./scripts/new-domain.sh "AI Agent" en-US
#   ./scripts/new-domain.sh "营养学" zh-CN
#
# Output:
#   A new directory learn-<domain-slug>/ with the standard learning repo structure.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DRY_RUN=0

if [ "${1:-}" = "--dry-run" ]; then
    DRY_RUN=1
    shift
fi

if [ $# -lt 1 ]; then
    echo "Usage: $0 <domain-name> [locale]"
    echo "Usage: $0 --dry-run <domain-name> [locale]"
    echo "Example: $0 \"AI Agent\""
    echo "Example: $0 --dry-run \"AI Agent\" en-US"
    echo "Example: $0 \"AI Agent\" en-US"
    echo "Example: $0 \"营养学\" zh-CN"
    exit 1
fi

DOMAIN="$1"
LOCALE="${2:-en-US}"

# Validate locale
if [ "$LOCALE" != "en-US" ] && [ "$LOCALE" != "zh-CN" ]; then
    echo "Error: Unsupported locale '$LOCALE'. Use 'en-US' or 'zh-CN'."
    exit 1
fi

TEMPLATE_DIR="$PROJECT_ROOT/templates/$LOCALE/{{domain-slug}}"

# Validate template exists and is complete
if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "Error: Template directory not found: $TEMPLATE_DIR"
    exit 1
fi

REQUIRED_FILES=(
    "README.md"
    "AGENTS.md"
    "CLAUDE.md"
    "progress.md"
    "progress-log.md"
    "00_domain_map.md"
    "08_glossary.md"
    "09_resources.md"
    "learning_materials/material_manifest.md"
    "learning_materials/material_index.md"
    "learning_materials/material_coverage_map.md"
    "learning_materials/material_learning_plan.md"
    "learning_materials/extraction_issues.md"
    "09_sources/sources.md"
    "09_sources/source_quality_policy.md"
    "09_sources/claim_ledger.md"
    "09_sources/claims_to_verify.md"
    "09_sources/freshness_log.md"
)
REQUIRED_DIRS=("01_core_concepts" "02_case_studies" "03_exercises" "04_projects" "05_flashcards" "06_quizzes" "07_daily_review" "learning_materials" "learning_materials/raw" "learning_materials/extracted" "09_sources")
MISSING_FILES=()

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$TEMPLATE_DIR/$file" ]; then
        MISSING_FILES+=("$file")
    fi
done

if [ ${#MISSING_FILES[@]} -gt 0 ]; then
    echo "Error: Template is incomplete. Missing files:"
    for file in "${MISSING_FILES[@]}"; do
        echo "  - $file"
    done
    echo ""
    echo "Template directory: $TEMPLATE_DIR"
    exit 1
fi

DOMAIN_FOR_SLUG=$(printf '%s' "$DOMAIN" \
  | sed 's/++/ plus-plus/g' \
  | sed 's/#/ sharp/g' \
  | sed 's/&/ and /g')
DOMAIN_SLUG=$(echo "$DOMAIN_FOR_SLUG" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')
# Fallback for non-Latin domain names (e.g., Chinese, Japanese)
# Append short timestamp to avoid collisions between multiple Chinese domains
if [ -z "$DOMAIN_SLUG" ]; then
    DOMAIN_SLUG="my-domain-$(date +%s)"
fi
TARGET_DIR="./learn-$DOMAIN_SLUG"

if [ -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' already exists."
    exit 1
fi

echo "Creating learning repository for: $DOMAIN"
echo "Locale: $LOCALE"
echo "Target directory: $TARGET_DIR"

if [ "$DRY_RUN" -eq 1 ]; then
    echo ""
    echo "Dry run only. No files will be created."
    echo "The script would copy this template:"
    echo "  $TEMPLATE_DIR"
    echo "It would create these required files:"
    for file in "${REQUIRED_FILES[@]}"; do
        echo "  - $file"
    done
    echo "It would create these required directories:"
    for dir in "${REQUIRED_DIRS[@]}"; do
        echo "  - $dir/"
    done
    exit 0
fi

# Clean up on failure
trap 'echo -e "\nError: Script failed. Cleaning up $TARGET_DIR..."; rm -rf "$TARGET_DIR"' ERR INT TERM

# Copy template
cp -r "$TEMPLATE_DIR" "$TARGET_DIR"

# Escape special characters in domain for sed replacement
ESCAPED_DOMAIN=$(printf '%s' "$DOMAIN" | sed 's/[\/&]/\\&/g')

# Replace domain placeholders in files
# Use a portable sed in-place approach that works on both macOS and Linux.
if command -v gsed &> /dev/null; then
    # GNU sed (installed via Homebrew on macOS, or native on Linux)
    find "$TARGET_DIR" -type f -name "*.md" -exec gsed -i "s/{{domain}}/$ESCAPED_DOMAIN/g" {} +
elif sed --version 2>/dev/null | grep -q 'GNU'; then
    # GNU sed on Linux
    find "$TARGET_DIR" -type f -name "*.md" -exec sed -i "s/{{domain}}/$ESCAPED_DOMAIN/g" {} +
else
    # BSD sed (macOS default)
    find "$TARGET_DIR" -type f -name "*.md" -exec sed -i '' "s/{{domain}}/$ESCAPED_DOMAIN/g" {} +
fi

# Remove trap upon success before verification
trap - ERR INT TERM

# Verify the result has all required files
echo ""
echo "Verifying output..."
VERIFY_FAIL=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$TARGET_DIR/$file" ]; then
        echo "  FAIL: Missing $file"
        VERIFY_FAIL=1
    else
        echo "  OK: $file"
    fi
done

# Check required subdirectories exist
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$TARGET_DIR/$dir" ]; then
        echo "  FAIL: Missing directory $dir/"
        VERIFY_FAIL=1
    else
        echo "  OK: $dir/"
    fi
done

if [ "$VERIFY_FAIL" -eq 1 ]; then
    echo ""
    echo "Error: Scaffold verification failed. The generated repository is incomplete."
    echo "Template source: $TEMPLATE_DIR"
    exit 1
fi

echo ""
echo "Done! Learning repository created at: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Start your AI agent in this directory"
echo "  3. Use core/prompts/$LOCALE/knowledge-map.md to generate the knowledge map"
echo "  4. Use core/prompts/$LOCALE/learning-plan.md to create the 30-day plan"
echo ""
echo "Happy learning!"
