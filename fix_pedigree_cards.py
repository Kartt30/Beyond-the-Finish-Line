import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the vibrant backgrounds for the outer modal
vibrant_bgs = {
    "SCIENTIFIC INHERITANCE": "linear-gradient(135deg, rgba(255, 60, 0, 0.9), rgba(255, 215, 0, 0.8))",
    "THE LEGENDARY SISTERS": "linear-gradient(135deg, rgba(138, 43, 226, 0.9), rgba(100, 149, 237, 0.8))",
    "THE GOLDEN CHAOS": "linear-gradient(135deg, rgba(255, 215, 0, 0.9), rgba(218, 165, 32, 0.8))",
    "IMPERIAL DYNASTY": "linear-gradient(135deg, rgba(0, 0, 139, 0.9), rgba(65, 105, 225, 0.8))",
    "THE MEJIRO NOBLES": "linear-gradient(135deg, rgba(0, 100, 0, 0.9), rgba(46, 139, 87, 0.8))",
    "SILENCE & SPELL": "linear-gradient(135deg, rgba(147, 112, 219, 0.9), rgba(255, 105, 180, 0.8))",
    "THE EMPRESS'S LEGACY": "linear-gradient(135deg, rgba(139, 0, 0, 0.9), rgba(178, 34, 34, 0.8))",
    "THE ROYAL TUTOR": "linear-gradient(135deg, rgba(10, 132, 97, 0.9), rgba(255, 134, 249, 0.8))",
    "THE REBELLIOUS SPIRIT": "linear-gradient(135deg, rgba(43, 43, 43, 0.9), rgba(12, 2, 98, 0.8))",
    "THE SUNDAY SUCCESSORS": "linear-gradient(135deg, rgba(95, 28, 157, 0.9), rgba(255, 215, 0, 0.8))",
    "THE GALACTIC ECHO": "linear-gradient(135deg, rgba(0, 31, 63, 0.9), rgba(13, 71, 161, 0.8))",
    "THE SAKURA SPEED": "linear-gradient(135deg, rgba(255, 0, 0, 0.9), rgba(255, 255, 255, 0.8))",
    "THE JUNGLE'S PRIDE": "linear-gradient(135deg, rgba(121, 85, 72, 0.9), rgba(255, 235, 59, 0.8))",
    "THE PACIFIC SIBLINGS": "linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(0, 31, 63, 0.8))",
    "THE SATONO LEGACY": "linear-gradient(135deg, rgba(27, 94, 32, 0.9), rgba(251, 192, 45, 0.8))",
    "HARSH MELODY": "linear-gradient(135deg, rgba(0, 0, 0, 0.9), rgba(255, 0, 0, 0.8))"
}

segments = content.split('pedigree-trigger"')
for i in range(1, len(segments)):
    segment = segments[i]
    title_match = re.search(r'data-title="([^"]+)"', segment)
    if title_match:
        title = title_match.group(1)
        if title in vibrant_bgs:
            new_bg = vibrant_bgs[title]
            segment = re.sub(r'data-bg="[^"]+"', f'data-bg="{new_bg}"', segment)
        segments[i] = segment

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('pedigree-trigger"'.join(segments))
    
print("Updated backgrounds")
