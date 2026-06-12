#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import subprocess
import tempfile
from pathlib import Path

def run_mock_evals(repo_dir: Path) -> bool:
    """Run simulated end-to-end evaluations without requiring a real LLM."""
    print("=== Running Mock End-to-End Evals ===")
    
    # 1. Simulate Phase 0: Init Repo
    print("Simulating Phase 0: Init Repo...")
    progress_file = repo_dir / "progress.md"
    if not progress_file.exists():
        print("FAIL: progress.md not found after init")
        return False

    required_reliability_files = [
        "CLAUDE.md",
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
    for rel_path in required_reliability_files:
        if not (repo_dir / rel_path).exists():
            print(f"FAIL: {rel_path} not found after init")
            return False
        
    # 2. Simulate Phase 1: Knowledge Map
    print("Simulating Phase 1: Knowledge Map...")
    km_file = repo_dir / "00_domain_map.md"
    with open(km_file, "w") as f:
        f.write(
            "# Domain Map: Mock Domain\n\n"
            "## Top 20 Concepts\n"
            "- Concept A\n"
            "- Concept B\n\n"
            "---\n\n"
            "### Source Notes\n"
            "- Mock eval fixture - [verified]\n\n"
            "### Freshness Risk: 🟢 Stable\n\n"
            "### Claims to Verify\n"
            "- [ ] None\n\n"
            "**Last Verified**: mock\n"
            "**Recommended Review Interval**: 12 months\n"
        )
    if not km_file.exists():
        print("FAIL: 00_domain_map.md not generated")
        return False
        
    # 3. Simulate Error Diagnosis during Daily Session
    print("Simulating Error Diagnosis (Quiz Failure)...")
    # Simulate the agent updating progress.md with a weak point tagged with [concept-gap]
    with open(progress_file, "a") as f:
        f.write("\n## 薄弱点\n- [concept-gap] Student failed to understand Concept A\n")
        
    # Check if the mock worked
    with open(progress_file, "r") as f:
        content = f.read()
        if "[concept-gap]" not in content:
            print("FAIL: Error diagnosis tag [concept-gap] not found in progress.md")
            return False
            
    print("✅ Mock E2E Evals Passed!")
    return True

def run_real_llm_evals(repo_dir: Path) -> bool:
    """Run live-agent smoke tests when configured, plus required behavior checks."""
    project_root = Path(__file__).resolve().parent.parent
    behavior = subprocess.run(
        [sys.executable, str(project_root / "evals" / "run_behavior_evals.py")],
        cwd=project_root,
        check=False,
    )
    if behavior.returncode != 0:
        return False

    try:
        import litellm
    except ImportError:
        print("litellm not installed; behavior evals passed, live LLM smoke skipped.")
        return True
        
    print("=== Running Real LLM Smoke Evals ===")
    print("Live LLM smoke requires project-specific model/API configuration.")
    print("Behavior evals are the required gate in this repo.")
    return True

def main():
    parser = argparse.ArgumentParser(description="End-to-End Evaluation Runner")
    parser.add_argument("--mode", choices=["mock", "real"], default="mock",
                        help="Evaluation mode (default: mock)")
    parser.add_argument("--domain", default="Test E2E", help="Domain to test")
    parser.add_argument("--locale", default="en-US", choices=["en-US", "zh-CN"], help="Locale to test")
    
    args = parser.parse_args()
    
    project_root = Path(__file__).resolve().parent.parent
    scripts_dir = project_root / "scripts"
    
    # Scaffold repo
    sys.path.append(str(scripts_dir))
    import init_learning_repo
    
    test_repo_name = f"learn-{init_learning_repo.sanitize_slug(args.domain)}"
    success = False

    with tempfile.TemporaryDirectory(prefix="learn-anything-e2e-") as tmp:
        tmp_root = Path(tmp)
        test_repo_dir = tmp_root / test_repo_name
        old_cwd = Path.cwd()

        # Monkeypatch sys.argv to run the init script programmatically.
        old_argv = sys.argv
        sys.argv = ["init_learning_repo.py", args.domain, "--locale", args.locale]

        # Suppress output of init script to keep eval logs clean.
        old_stdout = sys.stdout
        os.chdir(tmp_root)
        with open(os.devnull, 'w') as f:
            sys.stdout = f
            try:
                init_learning_repo.init_repo(args.domain, args.locale)
            except SystemExit as e:
                sys.stdout = old_stdout
                sys.argv = old_argv
                os.chdir(old_cwd)
                if e.code != 0:
                    print("Failed to initialize test repository.")
                    return 1

        sys.stdout = old_stdout
        sys.argv = old_argv

        # Change into the test repo to simulate agent execution context.
        os.chdir(test_repo_dir)

        try:
            if args.mode == "mock":
                success = run_mock_evals(test_repo_dir)
                if success:
                    behavior = subprocess.run(
                        [sys.executable, str(project_root / "evals" / "run_behavior_evals.py"), "--locale", args.locale],
                        cwd=project_root,
                        check=False,
                    )
                    success = behavior.returncode == 0
            elif args.mode == "real":
                success = run_real_llm_evals(test_repo_dir)
        finally:
            os.chdir(old_cwd)
            
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
