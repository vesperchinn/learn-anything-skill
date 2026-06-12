#!/usr/bin/env python3
import os
import re
import sys
import time
import shutil
import argparse
from pathlib import Path

def sanitize_slug(domain: str) -> str:
    """Generate a safe URL-friendly slug from the domain name."""
    # Handle special characters common in tech
    slug = domain.replace('C++', 'c-plus-plus')
    slug = slug.replace('C#', 'c-sharp')
    slug = slug.replace('+', ' plus ')
    slug = slug.replace('#', ' sharp ')
    slug = slug.replace('&', ' and ')
    slug = slug.replace('/', ' ')
    
    # Convert to lowercase
    slug = slug.lower()
    
    # Replace any non-alphanumeric character with a hyphen
    slug = re.sub(r'[^a-z0-9]', '-', slug)
    
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    
    # Trim hyphens from start and end
    slug = slug.strip('-')
    
    # Fallback for entirely non-Latin domains
    if not slug:
        slug = f"my-domain-{int(time.time())}"
        
    return slug

def init_repo(domain: str, locale: str = "en-US", dry_run: bool = False):
    project_root = Path(__file__).resolve().parent.parent
    template_dir = project_root / "templates" / locale / "{{domain-slug}}"
    
    if not template_dir.is_dir():
        print(f"Error: Template directory not found: {template_dir}", file=sys.stderr)
        sys.exit(1)
        
    domain_slug = sanitize_slug(domain)
    target_dir = Path.cwd() / f"learn-{domain_slug}"
    
    if target_dir.exists():
        print(f"Error: Directory '{target_dir}' already exists.", file=sys.stderr)
        sys.exit(1)

    required_files = [
        "README.md",
        "AGENTS.md",
        "CLAUDE.md",
        "progress.md",
        "progress-log.md",
        "00_domain_map.md",
        "08_glossary.md",
        "09_resources.md",
        "learning_materials/material_manifest.md",
        "learning_materials/material_index.md",
        "learning_materials/material_coverage_map.md",
        "learning_materials/material_learning_plan.md",
        "learning_materials/extraction_issues.md",
        "09_sources/sources.md",
        "09_sources/source_quality_policy.md",
        "09_sources/claim_ledger.md",
        "09_sources/claims_to_verify.md",
        "09_sources/freshness_log.md",
    ]
    required_dirs = [
        "01_core_concepts",
        "02_case_studies",
        "03_exercises",
        "04_projects",
        "05_flashcards",
        "06_quizzes",
        "07_daily_review",
        "learning_materials",
        "learning_materials/raw",
        "learning_materials/extracted",
        "09_sources",
    ]

    print(f"Creating learning repository for: {domain}")
    print(f"Locale: {locale}")
    print(f"Target directory: {target_dir}")

    if dry_run:
        print("\nDry run only. No files will be created.")
        print("The script would copy this template:")
        print(f"  {template_dir}")
        print("It would create these required files:")
        for req_file in required_files:
            print(f"  - {req_file}")
        print("It would create these required directories:")
        for req_dir in required_dirs:
            print(f"  - {req_dir}/")
        return

    try:
        shutil.copytree(template_dir, target_dir)

        # Replace placeholders
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = Path(root) / file
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    content = content.replace("{{domain}}", domain)
                    content = content.replace("{{domain-slug}}", domain_slug)

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)

    except Exception as e:
        print(f"\nError: Script failed. Cleaning up {target_dir}...", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        if target_dir.exists():
            shutil.rmtree(target_dir)
        sys.exit(1)

    print("\nVerifying output...")
    verify_fail = False

    for req_file in required_files:
        if not (target_dir / req_file).is_file():
            print(f"  FAIL: Missing {req_file}")
            verify_fail = True
        else:
            print(f"  OK: {req_file}")

    for req_dir in required_dirs:
        if not (target_dir / req_dir).is_dir():
            print(f"  FAIL: Missing directory {req_dir}/")
            verify_fail = True
        else:
            print(f"  OK: {req_dir}/")
            
    if verify_fail:
        print("\nError: Scaffold verification failed. The generated repository is incomplete.", file=sys.stderr)
        sys.exit(1)
        
    print(f"\nDone! Learning repository created at: {target_dir}\n")
    print("Next steps:")
    print(f"  1. cd {target_dir.name}")
    print(f"  2. Start your AI agent in this directory")
    print(f"  3. Use core/prompts/{locale}/knowledge-map.md to generate the knowledge map")
    print(f"  4. Use core/prompts/{locale}/learning-plan.md to create the 30-day plan")
    print("\nHappy learning!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new learning repository.")
    parser.add_argument("domain", help="The learning domain (e.g., 'AI Agent', 'C++')")
    parser.add_argument("--locale", default="en-US", choices=["en-US", "zh-CN"],
                        help="The template locale (default: en-US)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be created without writing files")
    args = parser.parse_args()

    init_repo(args.domain, args.locale, args.dry_run)
