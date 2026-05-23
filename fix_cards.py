import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

targets = [
    "ADMIRE GROOVE", "AIR MESSIAH", "BELIEVE", "BLAST ONEPIECE", 
    "BUBBLE GUM FELLOW", "CHRONO GENESIS", "COPANO RICKEY", "CURREN BOUQUETD'OR", 
    "DARING HEART", "DARING TACT", "DURAMENTE", "DURANDAL", "EPIPHANEIA", 
    "ESPOIR CITY", "FURIOSO"
]

for target in targets:
    pattern = r'<div\s+class="card category-[^"]+"\s+data-name="' + re.escape(target) + r'"[^>]*>'
    
    match = re.search(pattern, content)
    if not match:
        print(f"Could not find {target}")
        continue
    
    div_tag = match.group(0)
    
    cat_match = re.search(r'data-category="([^"]+)"', div_tag)
    cat = cat_match.group(1) if cat_match else ""
    
    color_match = re.search(r'data-color="([^"]+)"', div_tag)
    color = color_match.group(1) if color_match else ""
    
    bg_match = re.search(r'data-bg="([^"]+)"', div_tag)
    bg = bg_match.group(1) if bg_match else ""
    
    stats_match = re.search(r'data-stats="([^"]+)"', div_tag)
    stats = stats_match.group(1) if stats_match else ""
    
    try:
        spd = re.search(r'SPD:\s*([A-Z\+]+)', stats).group(1) if stats else ""
        sta = re.search(r'STA:\s*([A-Z\+]+)', stats).group(1) if stats else ""
        pow = re.search(r'POW:\s*([A-Z\+]+)', stats).group(1) if stats else ""
        wit = re.search(r'INT:\s*([A-Z\+]+)', stats).group(1) if stats else ""
    except Exception as e:
        print(f"Error parsing stats for {target}: {e}")
        spd, sta, pow, wit = "", "", "", ""
    
    start_idx = match.end()
    end_idx = content.find('</a>', start_idx) + 50
    inner_block = content[start_idx:end_idx]
    
    img_match = re.search(r'<img[^>]*src="([^"]+)"', inner_block)
    img_src = img_match.group(1) if img_match else ""
    
    quote_match = re.search(r'<p>([^<]+)</p>', inner_block)
    quote = quote_match.group(1) if quote_match else ""

    voice_name = target.lower().replace(" ", "").replace("'", "")
    voice = f"voices/{voice_name}.mp3"

    new_div_tag = f"""<div class="card category-{cat}"
data-name="{target}"
data-category="{cat}"
data-voice="{voice}"
data-bg="{bg}"
data-speed="{spd}"
data-stamina="{sta}"
data-power="{pow}"
data-wit="{wit}"
data-date="Unknown"
data-quote="{quote}"
data-img="{img_src}"
data-desc="{quote}"
data-color="{color}"
>"""
    
    content = content[:match.start()] + new_div_tag + content[match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
