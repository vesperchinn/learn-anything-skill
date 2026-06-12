#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path

def is_cjk_char(char: str) -> bool:
    """Check if character is a CJK character (Chinese/Japanese/Korean)."""
    val = ord(char)
    # Basic CJK Unified Ideographs block
    if 0x4E00 <= val <= 0x9FFF:
        return True
    # CJK Compatibility Ideographs
    if 0xF900 <= val <= 0xFAFF:
        return True
    # Halfwidth and Fullwidth Forms
    if 0xFF00 <= val <= 0xFFEF:
        return True
    return False

def analyze_file_locale(file_path: Path) -> dict:
    """Analyze text file and return character counts."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    total_alpha = 0
    total_cjk = 0
    
    for char in content:
        if char.isalpha() and char.isascii():
            total_alpha += 1
        elif is_cjk_char(char):
            total_cjk += 1
            
    total_meaningful = total_alpha + total_cjk
    if total_meaningful == 0:
        return {"file": str(file_path.name), "cjk_ratio": 0.0, "total": 0}
        
    return {"file": str(file_path.name), "cjk_ratio": total_cjk / total_meaningful, "total": total_meaningful}

def validate_directory(repo_dir: str, target_locale: str):
    """Validate that the directory content aligns with the expected locale.
    
    Note: This uses a simple CJK character ratio heuristic suitable for smoke
    testing rather than rigorous linguistic analysis.
    """
    repo_path = Path(repo_dir)
    if not repo_path.is_dir():
        print(f"Error: Directory '{repo_dir}' not found.")
        return False
        
    print(f"Validating locale '{target_locale}' for repository: {repo_dir}")
    issues_found = 0
    
    # Thresholds
    # For en-US: CJK ratio should be very low (e.g. < 5%)
    # For zh-CN: CJK ratio should be significant (e.g. > 10% as code/english still exists)
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.md'):
                stats = analyze_file_locale(Path(root) / file)
                
                if stats["total"] < 50:
                    continue # Skip very small files
                    
                ratio = stats["cjk_ratio"]
                
                if target_locale == "en-US" and ratio > 0.05:
                    print(f"  [WARNING] Language Bleed in {stats['file']}: CJK ratio is {ratio:.1%} (Expected < 5%)")
                    issues_found += 1
                elif target_locale == "zh-CN" and ratio < 0.05:
                    print(f"  [WARNING] Insufficient translation in {stats['file']}: CJK ratio is {ratio:.1%} (Expected > 5%)")
                    issues_found += 1

    if issues_found == 0:
        print(f"✅ Validation passed. Repository matches locale '{target_locale}'.")
        return True
    else:
        print(f"❌ Validation failed. Found {issues_found} potential language bleed issues.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate generated learning repo against target locale.")
    parser.add_argument("repo_dir", help="Path to the learning repository")
    parser.add_argument("locale", choices=["en-US", "zh-CN"], help="Target locale to validate against")
    args = parser.parse_args()
    
    success = validate_directory(args.repo_dir, args.locale)
    exit(0 if success else 1)
