#!/usr/bin/env python3
"""Build platform-specific distribution packages.

Default mode is dry-run. Use --execute to copy files. Existing files are never
overwritten.
"""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


COMMON_CORE = [
    "core/learning-protocol.{locale}.md",
    "core/reliability-protocol.{locale}.md",
    "core/material-grounding-protocol.{locale}.md",
    "core/state-schema.{locale}.md",
    "core/output-contract.{locale}.md",
]


PLATFORM_FILES = {
    "coze": [
        "platforms/cn/coze/README.zh-CN.md",
        "platforms/cn/coze/bot-prompt.zh-CN.md",
        "platforms/cn/coze/workflow-blueprint.md",
        "platforms/cn/coze/knowledge-base-package.md",
        "platforms/cn/coze/variables-schema.md",
        "platforms/cn/coze/memory-schema.md",
        "platforms/cn/coze/material-upload-flow.md",
        "platforms/cn/coze/reliability-flow.md",
        "platforms/cn/coze/publishing-checklist.md",
        "dist/coze-package-manifest.md",
    ],
    "workbuddy": [
        "platforms/cn/workbuddy/README.zh-CN.md",
        "platforms/cn/workbuddy/skill-call-prompt.zh-CN.md",
        "platforms/cn/workbuddy/task-workflow.md",
        "platforms/cn/workbuddy/knowledge-base-package.md",
        "platforms/cn/workbuddy/file-processing-rules.md",
        "platforms/cn/workbuddy/report-output-template.md",
        "platforms/cn/workbuddy/publishing-checklist.md",
        "dist/workbuddy-package-manifest.md",
    ],
    "trae": [
        "platforms/cn/trae/README.zh-CN.md",
        "platforms/cn/trae/project_rules.md",
        "platforms/cn/trae/user_rules.md",
        "platforms/cn/trae/agent-prompt.md",
        "platforms/cn/trae/setup-guide.md",
        "platforms/cn/trae/commands.md",
        "dist/trae-package-manifest.md",
    ],
    "codebuddy": [
        "platforms/cn/codebuddy/README.zh-CN.md",
        "platforms/cn/codebuddy/knowledge-base-upload-guide.md",
        "platforms/cn/codebuddy/agent-rules.md",
        "platforms/cn/codebuddy/setup-guide.md",
        "platforms/cn/codebuddy/test-checklist.md",
    ],
    "chat-only": [
        "platforms/global/chat-only/README.md",
        "dist/chat-only-package-manifest.md",
    ],
}


REFERENCE_SETS = {
    "zh-CN": [
        "references/zh-CN/learning-principles.md",
        "references/zh-CN/error-types.md",
        "references/zh-CN/project-patterns.md",
        "references/zh-CN/source-quality-policy.md",
        "references/zh-CN/freshness-policy.md",
        "references/zh-CN/claim-verification-guide.md",
        "references/zh-CN/high-stakes-domain-policy.md",
        "references/zh-CN/material-grounding-policy.md",
        "references/zh-CN/pdf-slide-handling.md",
        "templates/zh-CN/concept-template.md",
        "templates/zh-CN/source_notes.md.template",
        "templates/zh-CN/material_manifest.md.template",
        "templates/zh-CN/material_index.md.template",
        "templates/zh-CN/material_coverage_map.md.template",
        "templates/zh-CN/material_learning_plan.md.template",
        "prompts/zh-CN/material-intake.md",
        "prompts/zh-CN/material-grounded-learning-repo.md",
        "prompts/zh-CN/material-review-session.md",
        "prompts/zh-CN/material-quiz-generation.md",
        "prompts/zh-CN/material-gap-analysis.md",
    ],
    "en-US": [
        "references/en-US/learning-principles.md",
        "references/en-US/error-types.md",
        "references/en-US/project-patterns.md",
        "references/en-US/source-quality-policy.md",
        "references/en-US/freshness-policy.md",
        "references/en-US/claim-verification-guide.md",
        "references/en-US/high-stakes-domain-policy.md",
        "references/en-US/material-grounding-policy.md",
        "references/en-US/pdf-slide-handling.md",
        "templates/en-US/concept-template.md",
        "templates/en-US/source_notes.md.template",
        "templates/en-US/material_manifest.md.template",
        "templates/en-US/material_index.md.template",
        "templates/en-US/material_coverage_map.md.template",
        "templates/en-US/material_learning_plan.md.template",
        "prompts/en-US/material-intake.md",
        "prompts/en-US/material-grounded-learning-repo.md",
        "prompts/en-US/material-review-session.md",
        "prompts/en-US/material-quiz-generation.md",
        "prompts/en-US/material-gap-analysis.md",
    ],
}


@dataclass(frozen=True)
class PackagePlan:
    platform: str
    locale: str
    destination: Path
    files: list[Path]
    missing: list[Path]


def resolve_files(platform: str, locale: str) -> tuple[list[Path], list[Path]]:
    rel_paths = [item.format(locale=locale) for item in COMMON_CORE]
    rel_paths += PLATFORM_FILES[platform]
    rel_paths += REFERENCE_SETS[locale]
    rel_paths += ["dist/package-manifest.md", "platforms/capability-matrix.md"]

    files: list[Path] = []
    missing: list[Path] = []
    seen: set[Path] = set()
    for rel_path in rel_paths:
        path = REPO_ROOT / rel_path
        if path in seen:
            continue
        seen.add(path)
        if path.exists():
            files.append(path)
        else:
            missing.append(path)
    return files, missing


def create_plan(args: argparse.Namespace) -> PackagePlan:
    destination = args.output_dir / f"{args.platform}-{args.locale}"
    files, missing = resolve_files(args.platform, args.locale)
    return PackagePlan(args.platform, args.locale, destination, files, missing)


def relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def display_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def package_doc(plan: PackagePlan) -> str:
    file_list = "\n".join(f"- `{relative(path)}`" for path in plan.files)
    missing_list = "\n".join(f"- `{relative(path)}`" for path in plan.missing) or "- None"
    return f"""# {plan.platform} {plan.locale} Package

Generated package manifest.

## Source files

{file_list}

## Missing optional files

{missing_list}

## Runtime notes

- Existing files must not be overwritten.
- Low-code platforms should use adapter files, core protocols, knowledge-base documents, variables, and workflow instructions.
- Codex native Skill files remain in the source repository and are not required for low-code runtime unless the platform can read repository files directly.
"""


def print_plan(plan: PackagePlan) -> None:
    print(f"Platform: {plan.platform}")
    print(f"Locale: {plan.locale}")
    print(f"Destination: {display_path(plan.destination)}")
    print(f"Files: {len(plan.files)}")
    for path in plan.files:
        print(f"  + {relative(path)}")
    if plan.missing:
        print("Missing optional files:")
        for path in plan.missing:
            print(f"  ! {relative(path)}")


def ensure_no_overwrite(plan: PackagePlan) -> None:
    targets = [plan.destination / "PACKAGE.md"]
    targets += [plan.destination / relative(path) for path in plan.files]
    existing = [path for path in targets if path.exists()]
    if existing:
        formatted = "\n".join(f"  - {path}" for path in existing)
        raise SystemExit(f"Refusing to overwrite existing files:\n{formatted}")


def execute(plan: PackagePlan) -> None:
    ensure_no_overwrite(plan)
    plan.destination.mkdir(parents=True, exist_ok=True)

    package_path = plan.destination / "PACKAGE.md"
    package_path.write_text(package_doc(plan), encoding="utf-8")

    for source in plan.files:
        target = plan.destination / relative(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    print(f"Wrote package: {display_path(plan.destination)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform",
        required=True,
        choices=sorted(PLATFORM_FILES),
        help="Target platform package.",
    )
    parser.add_argument(
        "--locale",
        default="zh-CN",
        choices=sorted(REFERENCE_SETS),
        help="Locale package to include.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "dist" / "packages",
        help="Package output directory.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Write files. Without this flag the command is a dry-run.",
    )
    args = parser.parse_args()
    if not args.output_dir.is_absolute():
        args.output_dir = REPO_ROOT / args.output_dir

    plan = create_plan(args)
    print_plan(plan)

    if not args.execute:
        print("Dry-run only. Add --execute to write the package.")
        return 0

    execute(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
