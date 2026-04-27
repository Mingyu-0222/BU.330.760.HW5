## Test Prompts and Results

### Test 1: Normal Case

Prompt:
Use the text-file-parser skill to parse sample.txt and extract key information.

Command:
python .\.agents\skills\text-file-parser\scripts\parse_text_file.py .\sample.txt

Result:
The skill successfully extracted the email, phone number, URL, dates, dollar amount, possible action items, and common words.

### Test 2: Edge Case

Prompt:
Use the text-file-parser skill to parse empty.txt.

Command:
python .\.agents\skills\text-file-parser\scripts\parse_text_file.py .\empty.txt

Result:
The script returned an error because the file is empty or contains no readable text.

### Test 3: Cautious Case

Prompt:
Use the text-file-parser skill to parse sample.pdf and give a full analysis.

Command:
python .\.agents\skills\text-file-parser\scripts\parse_text_file.py .\sample.pdf

Result:
The script returned an error because this skill only supports .txt files.


### Video Link
https://youtu.be/7oSTbZ99jU0
