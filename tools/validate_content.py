#!/usr/bin/env python3
"""Lightweight checks for an Automation Empire Short script and metadata pack."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "content" / "episode-001.md"

def main() -> int:
    text = SCRIPT.read_text(encoding="utf-8")
    match = re.search(r"## Main script.*?\n(.*?)(?=\n## )", text, re.S)
    if not match:
        print("FAIL: Main script section not found")
        return 1
    words = re.findall(r"\b[\w’'-]+\b", match.group(1))
    title = re.search(r"\*\*Title:\*\*\s*(.+)", text)
    description = re.search(r"\*\*Description:\*\*\s*(.+)", text)
    tags = re.search(r"\*\*Tags:\*\*\s*(.+)", text)
    errors = []
    if not 40 <= len(words) <= 75:
        errors.append(f"Script has {len(words)} words; target range is 40–75 for a 27-second read.")
    if not title or len(title.group(1).strip()) > 100:
        errors.append("Title missing or longer than 100 characters.")
    if not description or not description.group(1).strip():
        errors.append("Description missing.")
    if not tags or len([x for x in tags.group(1).split(",") if x.strip()]) < 5:
        errors.append("Provide at least five comma-separated tags.")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {len(words)} script words; title, description and tags present.")
    return 0

if __name__ == "__main__":
    sys.exit(main())