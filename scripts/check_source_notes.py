#!/usr/bin/env python3
"""Scan learning content files for required reliability footer sections."""
import os
import re
import sys
import argparse
from pathlib import Path

ROOT_FILES = [
    '00_domain_map.md',
]

TARGET_DIRS = [
    '01_core_concepts',
    '02_case_studies',
    '03_exercises',
    '04_projects',
    '05_flashcards',
    '06_quizzes',
    '07_daily_review',
]

REQUIRED_PATTERNS = {
    'Source Notes': re.compile(r'^#{2,4}\s+(Source\s+Notes|来源注释)', re.MULTILINE | re.IGNORECASE),
    'Freshness Risk': re.compile(r'(Freshness\s+Risk|时效性风险)', re.IGNORECASE),
    'Claims to Verify': re.compile(r'^#{2,4}\s+(Claims\s+to\s+Verify|待验证主张)', re.MULTILINE | re.IGNORECASE),
    'Last Verified': re.compile(r'(Last\s+Verified|最后验证日期|最后验证)', re.IGNORECASE),
    'Recommended Review Interval': re.compile(r'(Recommended\s+Review\s+Interval|建议复查间隔)', re.IGNORECASE),
}

PLACEHOLDER_PATTERNS = [
    re.compile(r'To be generated', re.IGNORECASE),
    re.compile(r'will be populated', re.IGNORECASE),
    re.compile(r'待生成'),
    re.compile(r'将在.*填充'),
]


def check_source_notes(repo_dir: str) -> bool:
    """Check that content files have the required reliability footer.

    Returns True if all files have source notes, False otherwise.
    """
    repo_path = Path(repo_dir)
    if not repo_path.is_dir():
        print(f"Error: Directory '{repo_dir}' not found.")
        return False

    print(f"Scanning for reliability footer sections in: {repo_dir}")
    print(f"Target directories: {', '.join(TARGET_DIRS)}\n")

    total_files = 0
    files_complete = 0
    files_with_missing_sections = []

    candidates = []
    for root_file in ROOT_FILES:
        path = repo_path / root_file
        if path.is_file():
            candidates.append(path)

    for target_dir in TARGET_DIRS:
        dir_path = repo_path / target_dir
        if not dir_path.is_dir():
            print(f"  ⏭️  Skipping '{target_dir}' (directory not found)")
            continue

        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md'):
                    candidates.append(Path(root) / file)

    for file_path in sorted(candidates):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if any(pattern.search(content) for pattern in PLACEHOLDER_PATTERNS):
            continue

        total_files += 1

        missing = [
            label
            for label, pattern in REQUIRED_PATTERNS.items()
            if not pattern.search(content)
        ]
        if missing:
            rel_path = file_path.relative_to(repo_path)
            files_with_missing_sections.append((str(rel_path), missing))
        else:
            files_complete += 1

    print(f"Results:")
    print(f"  Files scanned: {total_files}")
    print(f"  Files with complete reliability footer: {files_complete}")
    print(f"  Files with missing footer sections: {len(files_with_missing_sections)}")

    if files_with_missing_sections:
        print(f"\nFiles missing required reliability footer sections:")
        for path, missing in files_with_missing_sections:
            print(f"  ❌ {path}: {', '.join(missing)}")
        print(f"\n⚠️  {len(files_with_missing_sections)} file(s) need a complete footer.")
        print("  Required fields: Source Notes, Freshness Risk, Claims to Verify,")
        print("  Last Verified, Recommended Review Interval.")
        return False
    elif total_files == 0:
        print(f"\n⏭️  No content files found to check.")
        return True
    else:
        print(f"\n✅ All {total_files} content files have complete reliability footers.")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check that learning content files have reliability footer sections."
    )
    parser.add_argument("repo_dir", help="Path to the learning repository")
    args = parser.parse_args()
    success = check_source_notes(args.repo_dir)
    exit(0 if success else 1)
