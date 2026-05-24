import re

with open('c:/xampp/htdocs/andung/beyond-finish-line/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = list(re.finditer(r'<div class="card"', content))
if matches:
    print(f'Found {len(matches)} cards.')
    last_match = matches[-1]
    print(f'Last card starts at index {last_match.start()}')
    print(content[last_match.start():last_match.start()+500])
else:
    print("No cards found with exact match.")
