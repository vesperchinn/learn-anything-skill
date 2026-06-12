#!/usr/bin/env python3
"""Scan freshness_log.md for modules past their review date and report stale modules."""
import re
import sys
import argparse
from datetime import datetime, date
from pathlib import Path
from typing import Optional


def parse_freshness_log(log_path: Path) -> list[dict]:
    """Parse the freshness_log.md table and return module entries.

    Supports both English and Chinese template headers:
    | Module | Freshness Risk | Content Date | Next Review | Notes |
    | 模块 | 时效性风险 | 内容日期 | 下次复查 | 备注 |
    """
    if not log_path.is_file():
        print(f"Error: Freshness log not found at '{log_path}'")
        return []

    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def split_row(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip('|').split('|')]

    def normalized(value: str) -> str:
        return re.sub(r'\s+', ' ', value.strip().lower())

    def find_index(headers: list[str], names: set[str]) -> Optional[int]:
        for index, header in enumerate(headers):
            if normalized(header) in names:
                return index
        return None

    rows = [
        split_row(line)
        for line in content.splitlines()
        if line.lstrip().startswith('|') and not re.match(r'^\s*\|?\s*:?-{3,}', line)
    ]

    entries = []
    header_indexes = None

    for row in rows:
        lowered = [normalized(cell) for cell in row]
        if 'module' in lowered or '模块' in lowered:
            module_idx = find_index(row, {'module', 'module name', '模块', '模块名'})
            risk_idx = find_index(row, {'freshness risk', 'freshness tier', '时效性风险', '新鲜度风险'})
            content_date_idx = find_index(row, {'content date', 'created', 'created date', '内容日期', '创建日期'})
            next_review_idx = find_index(row, {'next review', 'review due', '下次复查', '下次审查'})
            if module_idx is not None and risk_idx is not None and next_review_idx is not None:
                header_indexes = (module_idx, risk_idx, content_date_idx, next_review_idx)
            continue

        if header_indexes is None:
            continue

        module_idx, risk_idx, content_date_idx, next_review_idx = header_indexes
        needed_indexes = [module_idx, risk_idx, next_review_idx]
        if any(index >= len(row) for index in needed_indexes):
            continue

        module_name = row[module_idx]
        freshness_risk = row[risk_idx]
        content_date_str = row[content_date_idx] if content_date_idx is not None and content_date_idx < len(row) else ''
        next_review_str = row[next_review_idx]

        if not module_name or module_name in {'—', '-'}:
            continue

        try:
            content_date = (
                datetime.strptime(content_date_str, '%Y-%m-%d').date()
                if re.fullmatch(r'\d{4}-\d{2}-\d{2}', content_date_str)
                else None
            )
            next_review_date = datetime.strptime(next_review_str, '%Y-%m-%d').date()
        except ValueError:
            continue

        entries.append({
            'module': module_name,
            'content_date': content_date,
            'freshness_risk': freshness_risk,
            'next_review': next_review_date,
        })

    return entries


def check_stale_modules(repo_dir: str) -> bool:
    """Check for stale modules in the repository. Returns True if no stale modules found."""
    repo_path = Path(repo_dir)
    if not repo_path.is_dir():
        print(f"Error: Directory '{repo_dir}' not found.")
        return False

    log_path = repo_path / '09_sources' / 'freshness_log.md'
    if not log_path.is_file():
        print(f"Error: No freshness log found at '{log_path}'.")
        print("  A learning repository with the Knowledge Reliability Layer must include this file.")
        return False

    today = date.today()
    print(f"Checking for stale modules as of {today}")
    print(f"Freshness log: {log_path}\n")

    entries = parse_freshness_log(log_path)
    if not entries:
        print("No module entries found in freshness log.")
        return True

    stale_modules = []
    upcoming_modules = []

    for entry in entries:
        days_until_review = (entry['next_review'] - today).days
        if days_until_review < 0:
            stale_modules.append({**entry, 'days_overdue': abs(days_until_review)})
        elif days_until_review <= 14:
            upcoming_modules.append({**entry, 'days_until': days_until_review})

    print(f"Total modules tracked: {len(entries)}")
    print(f"Stale modules (past review date): {len(stale_modules)}")
    print(f"Upcoming reviews (within 14 days): {len(upcoming_modules)}")

    if stale_modules:
        print(f"\n🔴 Stale modules requiring review:")
        for m in sorted(stale_modules, key=lambda x: -x['days_overdue']):
            print(f"  {m['module']}")
            print(f"    Risk: {m['freshness_risk']}")
            print(f"    Review was due: {m['next_review']} ({m['days_overdue']} days overdue)")

    if upcoming_modules:
        print(f"\n🟡 Upcoming reviews:")
        for m in sorted(upcoming_modules, key=lambda x: x['days_until']):
            print(f"  {m['module']}")
            print(f"    Risk: {m['freshness_risk']}")
            print(f"    Review due: {m['next_review']} (in {m['days_until']} days)")

    if not stale_modules and not upcoming_modules:
        print(f"\n✅ All modules are up to date.")

    if stale_modules:
        print(f"\n⚠️  {len(stale_modules)} module(s) need review.")
        return False

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check for stale modules past their review date in a learning repository."
    )
    parser.add_argument("repo_dir", help="Path to the learning repository")
    args = parser.parse_args()
    success = check_stale_modules(args.repo_dir)
    exit(0 if success else 1)
