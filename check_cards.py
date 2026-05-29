import re
with open('c:/xampp/htdocs/andung/beyond-finish-line/index.html', encoding='utf-8') as f:
    text = f.read()
matches = list(re.finditer(r'<div\s+class="card"[\s\S]*?<h3>(.*?)<\/h3>[\s\S]*?class="btn(\d+)"', text))
print(f'Total cards: {len(matches)}')
for m in matches[-5:]:
    print(f'Name: {m.group(1)}, ID: {m.group(2)}')
