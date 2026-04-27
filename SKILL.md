---
name: text-file-parser
description: Parses plain text files and extracts structured information such as emails, phone numbers, dates, URLs, dollar amounts, and a short content summary. Use this skill when the user asks to inspect, parse, summarize, or extract key fields from a text file.
---

# Text File Parser Skill

## When to use this skill

Use this skill when the user provides a plain text file and asks to extract useful structured information from it.

Good use cases include:
- Extract emails, phone numbers, dates, URLs, and dollar amounts
- Generate a short file summary
- Identify possible action items
- Create a clean parsing report from messy text

## When not to use this skill

Do not use this skill for:
- Image files
- PDF files
- Audio or video files
- Deep legal, medical, or financial interpretation
- Files that require private or sensitive judgment beyond basic parsing

## Expected inputs

The input should be a `.txt` file or pasted plain text.

## Script responsibility

The Python script handles deterministic parsing. It uses regular expressions to extract emails, phone numbers, URLs, dates, and dollar amounts. This is more reliable than asking the model to manually identify every field.

## Steps

1. Read the text file.
2. Run the parser script.
3. Extract structured fields.
4. Count basic file statistics.
5. Generate a short report.
6. Explain any limitations.

## Expected output format

The final output should include:

1. File overview
2. Extracted emails
3. Extracted phone numbers
4. Extracted dates
5. Extracted URLs
6. Extracted dollar amounts
7. Possible action items
8. Short summary
9. Limitations