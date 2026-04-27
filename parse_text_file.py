import re
import sys
from pathlib import Path
from collections import Counter


def extract_patterns(text):
    emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    phones = re.findall(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
    urls = re.findall(r'https?://[^\s]+|www\.[^\s]+', text)
    dollar_amounts = re.findall(r'\$\s?\d+(?:,\d{3})*(?:\.\d{2})?', text)

    dates = re.findall(
        r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|'
        r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4})\b',
        text,
        flags=re.IGNORECASE
    )

    return {
        "emails": sorted(set(emails)),
        "phones": sorted(set(phones)),
        "urls": sorted(set(urls)),
        "dates": sorted(set(dates)),
        "dollar_amounts": sorted(set(dollar_amounts))
    }


def find_action_items(text):
    lines = text.splitlines()
    keywords = ["must", "need to", "should", "action", "deadline", "submit", "send", "complete", "required"]
    action_lines = []

    for line in lines:
        clean_line = line.strip()
        if any(keyword in clean_line.lower() for keyword in keywords):
            action_lines.append(clean_line)

    return action_lines[:10]


def basic_stats(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    line_count = len(text.splitlines())
    character_count = len(text)

    common_words = Counter(
        word for word in words
        if len(word) > 3
    ).most_common(10)

    return {
        "word_count": word_count,
        "line_count": line_count,
        "character_count": character_count,
        "common_words": common_words
    }


def generate_report(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("This parser only supports .txt files.")

    text = path.read_text(encoding="utf-8", errors="replace")

    if not text.strip():
        raise ValueError("The file is empty or contains no readable text.")

    patterns = extract_patterns(text)
    actions = find_action_items(text)
    stats = basic_stats(text)

    print("# Text File Parsing Report")
    print()
    print("## File Overview")
    print(f"File name: {path.name}")
    print(f"Word count: {stats['word_count']}")
    print(f"Line count: {stats['line_count']}")
    print(f"Character count: {stats['character_count']}")
    print()

    print("## Extracted Information")
    for key, values in patterns.items():
        label = key.replace("_", " ").title()
        print(f"### {label}")
        if values:
            for value in values:
                print(f"- {value}")
        else:
            print("- None found")
        print()

    print("## Possible Action Items")
    if actions:
        for item in actions:
            print(f"- {item}")
    else:
        print("- None found")
    print()

    print("## Common Words")
    for word, count in stats["common_words"]:
        print(f"- {word}: {count}")
    print()

    print("## Limitations")
    print("This script performs rule based parsing. It may miss unusual formats or extract false positives from messy text.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/parse_text_file.py path/to/file.txt")
        sys.exit(1)

    try:
        generate_report(sys.argv[1])
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)