#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

def extract_title(file_path: Path) -> str:
    """Extract the first H1 title from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('# '):
                    return line.strip()[2:].strip()
    except Exception:
        pass
    return file_path.stem.replace('_', ' ').title()

def generate_index(repo_dir: str):
    """Generate an index.md linking to all files in the repository."""
    repo_path = Path(repo_dir)
    if not repo_path.is_dir():
        print(f"Error: Directory '{repo_dir}' not found.")
        return False
        
    index_content = ["# Learning Repository Index\n"]
    
    # Define order of directories
    ordered_dirs = [
        "01_core_concepts",
        "02_case_studies",
        "03_exercises",
        "04_projects",
        "05_flashcards",
        "06_quizzes",
        "07_daily_review"
    ]
    
    # Process root files first
    root_files = ["00_domain_map.md", "08_glossary.md", "09_resources.md"]
    index_content.append("## Core Documents\n")
    for rfile in root_files:
        path = repo_path / rfile
        if path.is_file():
            title = extract_title(path)
            index_content.append(f"- [{title}]({rfile})")
    index_content.append("")
            
    for d in ordered_dirs:
        dir_path = repo_path / d
        if not dir_path.is_dir():
            continue
            
        md_files = sorted([f for f in dir_path.iterdir() if f.is_file() and f.suffix == '.md' and not f.name.endswith('.answer-key.md')])
        if not md_files:
            continue
            
        # Format directory name for display
        dir_name = d.split('_', 1)[1].replace('_', ' ').title()
        index_content.append(f"## {dir_name}\n")
        
        for mf in md_files:
            title = extract_title(mf)
            rel_path = f"{d}/{mf.name}"
            index_content.append(f"- [{title}]({rel_path})")
            
        index_content.append("")
        
    index_path = repo_path / "index.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(index_content))
        
    print(f"✅ Index generated successfully at: {index_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate index.md for a learning repository.")
    parser.add_argument("repo_dir", help="Path to the learning repository")
    args = parser.parse_args()
    
    success = generate_index(args.repo_dir)
    exit(0 if success else 1)
