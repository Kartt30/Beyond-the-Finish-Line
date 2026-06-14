import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find all blocks of .pedigree-trigger and replace href="#" inside them with data-fullbody
def replacer(match):
    card_html = match.group(0)
    # Find data-fullbody="..."
    bg_match = re.search(r'data-fullbody="([^"]+)"', card_html)
    if bg_match:
        fullbody_url = bg_match.group(1)
        # Replace href="#" or href="" with href="<fullbody_url>"
        # specifically on the VIEW LINEAGE button
        card_html = re.sub(r'<a\s+href="[^"]*"\s+class="support-btn">VIEW LINEAGE</a>', 
                           f'<a href="{fullbody_url}" target="_blank" class="support-btn">VIEW LINEAGE</a>', 
                           card_html)
    return card_html

# Assuming cards start with <div class="support-card pedigree-trigger" and end with an anchor and some divs
# Let's just do a simpler search/replace based on splitting the file
segments = content.split('pedigree-trigger"')
for i in range(1, len(segments)):
    segment = segments[i]
    # find data-fullbody
    fb_match = re.search(r'data-fullbody="([^"]+)"', segment)
    if fb_match:
        url = fb_match.group(1)
        segment = re.sub(r'<a\s+href="[^"]*"\s+class="support-btn">VIEW LINEAGE</a>', 
                         f'<a href="{url}" target="_blank" class="support-btn">VIEW LINEAGE</a>', 
                         segment)
        segments[i] = segment

new_content = 'pedigree-trigger"'.join(segments)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Replaced links!")
