#!/usr/bin/env python3
"""Scan a learning repository for unverified claims and report a summary."""
import os
import re
import sys
import argparse
from pathlib import Path

UNVERIFIED_PATTERNS = [
    re.compile(r'\[unverified[^\]]*\]', re.IGNORECASE),
    re.compile(r'\[未验证[^\]]*\]'),
    re.compile(r'\bUnverified Draft\b', re.IGNORECASE),
    re.compile(r'未验证草稿'),
]

IGNORED_FILES = {
    Path('README.md'),
    Path('AGENTS.md'),
    Path('09_sources/source_quality_policy.md'),
}


def scan_unverified(repo_dir: str):
    repo_path = Path(repo_dir)
    if not repo_path.is_dir():
        print(f"Error: Directory '{repo_dir}' not found.")
        return False

    print(f"Scanning for unverified claims in: {repo_dir}")
    total_files = 0
    total_unverified = 0
    files_with_unverified = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                rel_path = file_path.relative_to(repo_path)
                if rel_path in IGNORED_FILES:
                    continue
                total_files += 1
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                matches = []
                for pattern in UNVERIFIED_PATTERNS:
                    matches.extend(pattern.findall(content))
                if matches:
                    total_unverified += len(matches)
                    files_with_unverified.append((str(rel_path), len(matches)))

    print(f"\nResults:")
    print(f"  Files scanned: {total_files}")
    print(f"  Unverified claims found: {total_unverified}")
    print(f"  Files with unverified claims: {len(files_with_unverified)}")

    if files_with_unverified:
        print(f"\nFiles containing unverified markers:")
        for path, count in sorted(files_with_unverified, key=lambda x: -x[1]):
            print(f"  {path}: {count} marker(s)")
        print(f"\n⚠️  {total_unverified} marker(s) need verification or source review.")
        return False
    else:
        print(f"\n✅ No unverified claims found.")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scan for unverified claims in a learning repository."
    )
    parser.add_argument("repo_dir", help="Path to the learning repository")
    args = parser.parse_args()
    success = scan_unverified(args.repo_dir)
    exit(0 if success else 1)
