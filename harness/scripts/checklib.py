#!/usr/bin/env python3
"""Shared helpers for read-only harness checks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Iterable


PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


@dataclass
class Issue:
    code: str
    severity: str
    file: str
    message: str
    suggested_fix: str


def make_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    parser.add_argument("--report", action="store_true", help="Write a timestamped report.")
    return parser


def repo_path(root: Path, *parts: str) -> Path:
    return root.joinpath(*parts)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def ok(code: str, file: str, message: str = "OK") -> Issue:
    return Issue(code, PASS, file, message, "")


def warn(code: str, file: str, message: str, suggested_fix: str) -> Issue:
    return Issue(code, WARN, file, message, suggested_fix)


def fail(code: str, file: str, message: str, suggested_fix: str) -> Issue:
    return Issue(code, FAIL, file, message, suggested_fix)


def markdown_files(root: Path, paths: Iterable[str]) -> list[Path]:
    files: list[Path] = []
    for item in paths:
        path = root / item
        if path.is_file() and path.suffix.lower() in {".md", ".markdown"}:
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def all_text_files(root: Path) -> list[Path]:
    allowed = {".md", ".txt", ".yaml", ".yml", ".py", ".sh", ".template"}
    ignored_parts = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ignored_parts.intersection(path.parts):
            continue
        if path.name == ".DS_Store":
            continue
        if path.suffix in allowed or path.name.endswith(".md.template"):
            files.append(path)
    return sorted(files)


def parse_front_matter(text: str) -> tuple[dict[str, str], str] | tuple[None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    raw = text[4:end].strip()
    body = text[end + 4 :]
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip().strip("\"'")
        elif current_key:
            data[current_key] = (data[current_key] + " " + line.strip()).strip()
    return data, body


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def ascii_ratio(text: str) -> float:
    letters = [ch for ch in text if ch.isalpha()]
    if not letters:
        return 0.0
    ascii_letters = [ch for ch in letters if ord(ch) < 128]
    return len(ascii_letters) / len(letters)


def find_path_mentions(text: str) -> list[str]:
    pattern = r"(?:[`(])?((?:core|prompts|templates|references|adapters|platforms|evals|docs|dist|scripts)/[A-Za-z0-9_./{}-]+(?:\.md|\.template|\.yaml|\.yml|\.py|\.sh)?)(?:[`)]?)?"
    return [match.group(1).rstrip(".,)") for match in re.finditer(pattern, text)]


def load_contract_lists(root: Path, filename: str) -> dict[str, list[str]]:
    """Load top-level YAML list values without requiring PyYAML."""
    path = root / "harness" / "contracts" / filename
    if not path.exists():
        return {}
    data: dict[str, list[str]] = {}
    current_key: str | None = None
    for raw_line in read_text(path).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line and not raw_line.startswith(" ") and ":" in raw_line:
            key, rest = raw_line.split(":", 1)
            current_key = key.strip()
            if rest.strip() == "":
                data.setdefault(current_key, [])
            continue
        if current_key and raw_line.startswith("  - "):
            data.setdefault(current_key, []).append(raw_line.strip()[2:].strip())
    return data


def load_platform_contract_paths(root: Path) -> dict[str, list[str]]:
    """Parse platform -> paths from the simple platform contract shape."""
    path = root / "harness" / "contracts" / "platform-adapter-contract.yaml"
    if not path.exists():
        return {}
    platforms: dict[str, list[str]] = {}
    in_platforms = False
    current_platform: str | None = None
    in_paths = False
    for raw_line in read_text(path).splitlines():
        if raw_line.startswith("platforms:"):
            in_platforms = True
            continue
        if in_platforms and raw_line and not raw_line.startswith(" "):
            break
        if not in_platforms:
            continue
        platform_match = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", raw_line)
        if platform_match:
            current_platform = platform_match.group(1)
            platforms.setdefault(current_platform, [])
            in_paths = False
            continue
        if current_platform and raw_line.strip() == "paths:":
            in_paths = True
            continue
        if current_platform and in_paths and raw_line.startswith("      - "):
            platforms[current_platform].append(raw_line.strip()[2:].strip())
    return platforms


def write_report(root: Path, script_name: str, issues: list[Issue]) -> Path:
    report_dir = root / "harness" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = report_dir / f"{timestamp}-{script_name}.json"
    counter = 1
    while path.exists():
        path = report_dir / f"{timestamp}-{script_name}-{counter}.json"
        counter += 1
    payload = {
        "script": script_name,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "issues": [asdict(issue) for issue in issues],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def print_issues(issues: list[Issue], as_json: bool) -> None:
    if as_json:
        print(json.dumps([asdict(issue) for issue in issues], ensure_ascii=False, indent=2))
        return
    for issue in issues:
        location = f" {issue.file}" if issue.file else ""
        print(f"{issue.severity} {issue.code}{location}: {issue.message}")
        if issue.suggested_fix:
            print(f"  fix: {issue.suggested_fix}")


def exit_code(issues: list[Issue], strict: bool) -> int:
    if any(issue.severity == FAIL for issue in issues):
        return 1
    if strict and any(issue.severity == WARN for issue in issues):
        return 1
    return 0


def run_check(description: str, check: Callable[[Path], list[Issue]]) -> int:
    parser = make_parser(description)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    issues = check(root)
    if not issues:
        issues = [ok("NO_ISSUES", "", "No issues found")]
    if args.report:
        report_path = write_report(root, Path(sys.argv[0]).stem, issues)
        issues.append(ok("REPORT_WRITTEN", rel(root, report_path), "Report written"))
    print_issues(issues, args.json)
    return exit_code(issues, args.strict)
