#!/bin/bash
# init-repo.sh — Initialize a learning repository from locale-aware templates.
# Called by the Codex skill when starting a new domain.
#
# Usage: ./init-repo.sh <domain-name> [locale]
#
# Delegates to the root scripts/new-domain.sh for actual scaffolding.

set -euo pipefail

DOMAIN="${1:-}"
LOCALE="${2:-en-US}"

if [ -z "$DOMAIN" ]; then
    echo "Usage: $0 <domain-name> [locale]"
    echo "Example: $0 \"AI Agent\""
    echo "Example: $0 \"AI Agent\" en-US"
    echo "Example: $0 \"营养学\" zh-CN"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
ROOT="$(cd "$SKILL_DIR/../../.." && pwd)"

exec "$ROOT/scripts/new-domain.sh" "$DOMAIN" "$LOCALE"
