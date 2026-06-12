#!/usr/bin/env python3
"""Check English locale files for leftover Chinese text.

Scans all files under the en-US locale directories (prompts, templates,
references, examples, evals) and reports any line containing CJK characters.
Useful as a CI check or pre-commit hook to ensure English files haven't
accidentally retained Chinese text.

Usage:
    python3 scripts/check_untranslated_strings.py
    python3 scripts/check_untranslated_strings.py --dir core/prompts/en-US
    python3 scripts/check_untranslated_strings.py --exclude "stage-test-1.md"

Exit code 0 = clean (no CJK found in en-US files).
Exit code 1 = found CJK characters (files printed to stdout).
"""

import argparse
import os
import sys
from pathlib import Path


# Unicode ranges for CJK characters
CJK_RANGES = [
    (0x4E00, 0x9FFF),    # CJK Unified Ideographs
    (0x3400, 0x4DBF),    # CJK Unified Ideographs Extension A
    (0xF900, 0xFAFF),    # CJK Compatibility Ideographs
    (0x3000, 0x303F),    # CJK Symbols and Punctuation
    (0xFF00, 0xFFEF),    # Halfwidth and Fullwidth Forms
    (0x2F00, 0x2FDF),    # Kangxi Radicals
    (0x2E80, 0x2EFF),    # CJK Radicals Supplement
]

# Lines that legitimately contain CJK (e.g., as examples of what NOT to do,
# or in locale comparison tables) — we allow these specific patterns
ALLOWED_PATTERNS = [
    # Comparison tables showing both locales side by side
    "zh-CN",
    # Intentional CJK in English docs (e.g., "NOT 当前状态")
    "当前状态",
    "已完成模块",
    "薄弱点",
    "错题摘要",
    "阶段测试成绩",
    "项目进展",
    "下一步",
    "不懂概念",
    "不会应用",
    "表达不清",
    "知识混淆",
    "解释",
    "示例",
    "练习",
    "检查",
    "复盘",
    # Chinese adapter docs or references to zh-CN files
    "中文",
]


def has_cjk(line: str) -> bool:
    """Check if a line contains CJK characters."""
    for ch in line:
        cp = ord(ch)
        for lo, hi in CJK_RANGES:
            if lo <= cp <= hi:
                return True
    return False


def is_allowed_cjk(line: str) -> bool:
    """Check if the CJK on this line is an allowed pattern.

    A line is allowed if ALL CJK substrings on it match known allowed patterns
    (e.g., comparison tables showing what NOT to do, or references to zh-CN).
    """
    # Extract CJK segments from the line
    cjk_segments = []
    current = []
    for ch in line:
        cp = ord(ch)
        is_cjk = any(lo <= cp <= hi for lo, hi in CJK_RANGES)
        if is_cjk:
            current.append(ch)
        else:
            if current:
                cjk_segments.append("".join(current))
                current = []
    if current:
        cjk_segments.append("".join(current))

    if not cjk_segments:
        return True  # No CJK at all — allowed

    # Check each CJK segment against the allowed list
    for segment in cjk_segments:
        allowed = False
        for allowed_pattern in ALLOWED_PATTERNS:
            if segment in allowed_pattern or allowed_pattern in segment:
                allowed = True
                break
        if not allowed:
            return False

    return True


def check_file(filepath: Path) -> list[tuple[int, str]]:
    """Check a single file for unallowed CJK characters.

    Returns a list of (line_number, line_content) tuples for violations.
    """
    violations = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if has_cjk(line) and not is_allowed_cjk(line):
                    violations.append((i, line.rstrip("\n")))
    except UnicodeDecodeError:
        print(f"WARNING: Could not read {filepath} as UTF-8", file=sys.stderr)
    except Exception as e:
        print(f"WARNING: Error reading {filepath}: {e}", file=sys.stderr)

    return violations


def find_en_us_dirs(root: Path) -> list[Path]:
    """Find all en-US locale directories under root."""
    en_us_dirs = []
    for dirpath, dirnames, _ in os.walk(root):
        if os.path.basename(dirpath) == "en-US":
            en_us_dirs.append(Path(dirpath))
    return en_us_dirs


def main():
    parser = argparse.ArgumentParser(
        description="Check English locale files for leftover Chinese text."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=None,
        help="Specific directory to check (default: all en-US dirs under repo root)",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        default=None,
        help="Comma-separated file names to exclude from the check",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Disable allowed-pattern whitelist (report ALL CJK occurrences)",
    )
    args = parser.parse_args()

    # Determine repo root (parent of scripts/)
    repo_root = Path(__file__).resolve().parent.parent

    excludes = set()
    if args.exclude:
        excludes = {name.strip() for name in args.exclude.split(",")}

    if args.dir:
        target_dirs = [Path(args.dir)]
    else:
        target_dirs = find_en_us_dirs(repo_root)

    if not target_dirs:
        print("No en-US directories found.", file=sys.stderr)
        sys.exit(0)

    total_violations = 0
    files_checked = 0
    files_with_violations = 0

    for en_us_dir in sorted(target_dirs):
        if not en_us_dir.exists():
            continue

        for filepath in sorted(en_us_dir.rglob("*")):
            if not filepath.is_file():
                continue
            if filepath.name in excludes:
                continue
            # Skip non-text files
            if filepath.suffix in (".png", ".jpg", ".gif", ".pdf", ".gitkeep"):
                continue

            files_checked += 1
            violations = check_file(filepath)

            if args.strict:
                # In strict mode, report ALL CJK (ignore allowed patterns)
                strict_violations = []
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            if has_cjk(line):
                                strict_violations.append((i, line.rstrip("\n")))
                except Exception:
                    pass
                violations = strict_violations

            if violations:
                files_with_violations += 1
                rel_path = filepath.relative_to(repo_root)
                print(f"\n{'=' * 60}")
                print(f"FILE: {rel_path}")
                print(f"{'=' * 60}")
                for line_no, content in violations:
                    print(f"  L{line_no}: {content[:120]}")
                    total_violations += 1

    print(f"\n{'=' * 60}")
    print(f"Summary: {files_checked} files checked, "
          f"{files_with_violations} files with issues, "
          f"{total_violations} total violations")

    if total_violations > 0:
        print(f"\nTo see what's allowed, run with --strict to report ALL CJK.")
        print(f"Allowed patterns: {', '.join(ALLOWED_PATTERNS)}")
        sys.exit(1)
    else:
        print("✅ All en-US files are clean (no unallowed CJK text).")
        sys.exit(0)


if __name__ == "__main__":
    main()
