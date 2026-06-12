#!/usr/bin/env python3
import csv
import re
import argparse
from pathlib import Path

def parse_flashcard_file(file_path: Path):
    """Parse a single flashcard markdown file into a list of (Front, Back) tuples."""
    cards = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return cards

    # Extract keywords / summaries
    keywords_match = re.search(r'## (?:一句话总结|5 个关键词|5 Keywords|Key Concepts)\n(.*?)(?=\n## |\Z)', content, re.DOTALL | re.IGNORECASE)
    if keywords_match:
        for line in keywords_match.group(1).strip().split('\n'):
            line = line.strip()
            # Match formats like: "1. **Keyword** — Definition" or "1. Keyword — Definition"
            match = re.match(r'^\d+\.\s*(?:\*\*)?(.*?)(?:\*\*)?\s*[—\-:]\s*(.*)$', line)
            if match:
                front, back = match.groups()
                front = front.replace('**', '').strip()
                back = back.replace('**', '').strip()
                cards.append((front, back))

    # Extract common pitfalls
    pitfalls_match = re.search(r'## (?:2 个常见误区|2 Common Pitfalls)\n(.*?)(?=\n## |\Z)', content, re.DOTALL | re.IGNORECASE)
    if pitfalls_match:
        for line in pitfalls_match.group(1).strip().split('\n'):
            line = line.strip()
            if '❌' in line and '✅' in line:
                # Format: 1. ❌ Mistake → ✅ Correction
                parts = line.split('✅')
                if len(parts) == 2:
                    wrong_part = parts[0].replace('❌', '').strip().strip('→').strip()
                    right_part = parts[1].strip()
                    front = f"Why is this wrong?\n\n{wrong_part}"
                    back = right_part
                    cards.append((front, back))

    # Extract self-test
    selftest_match = re.search(r'## (?:自测题|Self Test)\n(.*?)(?=\n## |\Z)', content, re.DOTALL | re.IGNORECASE)
    if selftest_match:
        question = selftest_match.group(1).strip()
        if question and len(question) > 5:
            # We don't have the answer in the card typically, but we can just use the question as front
            cards.append((f"Self Test:\n\n{question}", "Review your notes or ask your Agent for the answer."))

    return cards

def export_flashcards(repo_dir: str, output_csv: str):
    """Scan the 05_flashcards directory and export to CSV."""
    repo_path = Path(repo_dir)
    flashcards_dir = repo_path / "05_flashcards"
    
    if not flashcards_dir.is_dir():
        print(f"Error: Flashcards directory not found at {flashcards_dir}")
        return False
        
    all_cards = []
    
    for md_file in sorted(flashcards_dir.glob("*.md")):
        cards = parse_flashcard_file(md_file)
        if cards:
            all_cards.extend(cards)
            
    if not all_cards:
        print("No flashcards found to export.")
        return False
        
    try:
        with open(output_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Front", "Back"])
            for front, back in all_cards:
                writer.writerow([front, back])
                
        print(f"✅ Successfully exported {len(all_cards)} flashcards to {output_csv}")
        print("You can now import this CSV file into Anki.")
        return True
    except Exception as e:
        print(f"Error writing to CSV: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export flashcards to Anki-compatible CSV.")
    parser.add_argument("repo_dir", help="Path to the learning repository")
    parser.add_argument("--output", default="anki_flashcards.csv", help="Output CSV filename")
    args = parser.parse_args()
    
    success = export_flashcards(args.repo_dir, args.output)
    exit(0 if success else 1)
