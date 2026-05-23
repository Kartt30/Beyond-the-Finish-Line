import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    def replacer(match):
        name = match.group(1)
        dtype = match.group(2)
        rest = match.group(3)
        
        cat = dtype.lower()
        if cat == "short":
            cat = "sprint"
            
        return f'class="card category-{cat}"\n          data-name="{name}"\n          data-category="{cat}"\n          data-type="{dtype}"\n{rest}>'
    
    pattern = re.compile(r'class="card"\s*\n\s*data-name="([^"]+)"\s*\n\s*data-type="([^"]+)"\s*\n(.*?)>', re.DOTALL)
    html = pattern.sub(replacer, html)

    dirt_btn = """    <button class="filter-btn" data-filter="dirt">
      DIRT
    </button>
"""
    btn_regex = re.compile(r'(<button class="filter-btn" data-filter="long">.*?</button>\s*\n)(.*?</div>)', re.DOTALL)
    
    # Only replace if dirt button is not there
    if 'data-filter="dirt"' not in html:
        html = btn_regex.sub(r'\1' + dirt_btn + r'\2', html, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
