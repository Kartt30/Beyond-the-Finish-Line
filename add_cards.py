import re

chars = [
    { "id": 103, "name": "ADMIRE GROOVE", "quote": "Groove to the rhythm of victory.", "type": "MEDIUM", "stats": "SPD: A | STA: B | POW: B | GUTS: C | INT: B", "color": "#234990", "bg": "rgba(35,73,144,0.92)", "text_color": "white", "hover": "#1a366b", "link": "https://umamusu.wiki/Admire_Groove" },
    { "id": 104, "name": "AIR MESSIAH", "quote": "A messiah born of the sky, soaring ever higher.", "type": "MEDIUM", "stats": "SPD: B | STA: B | POW: B | GUTS: C | INT: A", "color": "#0c4f8d", "bg": "rgba(12,79,141,0.92)", "text_color": "white", "hover": "#083b6b", "link": "https://umamusu.wiki/Air_Messiah" },
    { "id": 105, "name": "BELIEVE", "quote": "Believe in the sprint that leads to glory.", "type": "SHORT", "stats": "SPD: S | STA: D | POW: A | GUTS: C | INT: C", "color": "#e5c158", "bg": "rgba(229,193,88,0.92)", "text_color": "black", "hover": "#b89a46", "link": "https://umamusu.wiki/Believe" },
    { "id": 106, "name": "BLAST ONEPIECE", "quote": "A blast of power that shatters all expectations.", "type": "LONG", "stats": "SPD: A | STA: A | POW: S | GUTS: B | INT: C", "color": "#3060a8", "bg": "rgba(48,96,168,0.92)", "text_color": "white", "hover": "#24487d", "link": "https://umamusu.wiki/Blast_Onepiece" },
    { "id": 107, "name": "BUBBLE GUM FELLOW", "quote": "Pop the bubble of doubt with unstoppable speed.", "type": "MILE", "stats": "SPD: A | STA: C | POW: B | GUTS: B | INT: B", "color": "#e1a1b1", "bg": "rgba(225,161,177,0.92)", "text_color": "black", "hover": "#b3808d", "link": "https://umamusu.wiki/Bubble_Gum_Fellow" },
    { "id": 108, "name": "CHRONO GENESIS", "quote": "Rewriting the genesis of champions with every stride.", "type": "LONG", "stats": "SPD: A | STA: A | POW: S | GUTS: A | INT: B", "color": "#999999", "bg": "rgba(153,153,153,0.92)", "text_color": "black", "hover": "#7a7a7a", "link": "https://umamusu.wiki/Chrono_Genesis" },
    { "id": 109, "name": "COPANO RICKEY", "quote": "Luck is on my side, let the feng shui guide the way!", "type": "DIRT", "stats": "SPD: A | STA: B | POW: A | GUTS: B | INT: A", "color": "#f18a20", "bg": "rgba(241,138,32,0.92)", "text_color": "white", "hover": "#c26d17", "link": "https://umamusu.wiki/Copano_Rickey" },
    { "id": 110, "name": "CURREN BOUQUETD'OR", "quote": "A golden bouquet for the one who graces the turf.", "type": "LONG", "stats": "SPD: A | STA: A | POW: B | GUTS: B | INT: B", "color": "#f16889", "bg": "rgba(241,104,137,0.92)", "text_color": "white", "hover": "#c2536e", "link": "https://umamusu.wiki/Curren_Bouquetd%27or" },
    { "id": 111, "name": "DARING HEART", "quote": "A daring heart fears no distance.", "type": "MILE", "stats": "SPD: A | STA: C | POW: B | GUTS: B | INT: B", "color": "#bb2020", "bg": "rgba(187,32,32,0.92)", "text_color": "white", "hover": "#941818", "link": "https://umamusu.wiki/Daring_Heart" },
    { "id": 112, "name": "DARING TACT", "quote": "Unyielding tactics forged by a Triple Crown determination.", "type": "MEDIUM", "stats": "SPD: A | STA: A | POW: A | GUTS: S | INT: B", "color": "#3b5e40", "bg": "rgba(59,94,64,0.92)", "text_color": "white", "hover": "#2e4a32", "link": "https://umamusu.wiki/Daring_Tact" },
    { "id": 113, "name": "DURAMENTE", "quote": "Play it loud, play it tough—a harsh and beautiful melody.", "type": "MEDIUM", "stats": "SPD: S | STA: A | POW: S | GUTS: B | INT: B", "color": "#161e38", "bg": "rgba(22,30,56,0.92)", "text_color": "white", "hover": "#0f1526", "link": "https://umamusu.wiki/Duramente" },
    { "id": 114, "name": "DURANDAL", "quote": "A holy sword cutting through the final stretch.", "type": "SHORT", "stats": "SPD: S | STA: C | POW: S | GUTS: B | INT: C", "color": "#b02a2a", "bg": "rgba(176,42,42,0.92)", "text_color": "white", "hover": "#8a2121", "link": "https://umamusu.wiki/Durandal" },
    { "id": 115, "name": "EPIPHANEIA", "quote": "A sudden revelation of absolute strength.", "type": "LONG", "stats": "SPD: A | STA: A | POW: A | GUTS: S | INT: B", "color": "#115933", "bg": "rgba(17,89,51,0.92)", "text_color": "white", "hover": "#0d4528", "link": "https://umamusu.wiki/Epiphaneia" },
    { "id": 116, "name": "ESPOIR CITY", "quote": "The city of hope gleams brightest on the dirt.", "type": "DIRT", "stats": "SPD: S | STA: C | POW: A | GUTS: B | INT: B", "color": "#152f6b", "bg": "rgba(21,47,107,0.92)", "text_color": "white", "hover": "#102554", "link": "https://umamusu.wiki/Espoir_City" },
    { "id": 117, "name": "FURIOSO", "quote": "Furious power thundering across the sand.", "type": "DIRT", "stats": "SPD: B | STA: A | POW: S | GUTS: S | INT: C", "color": "#2f1111", "bg": "rgba(47,17,17,0.92)", "text_color": "white", "hover": "#1a0909", "link": "https://umamusu.wiki/Furioso" }
]

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Badge CSS
    badges_css = ""
    for c in chars:
        badges_css += f"""
.badge{c['id']} {{
  position: absolute;
  top: 10px;
  right: 10px;
  background-color:{c['bg']};
  color:{c['text_color']};
  padding: 5px 10px;
  border-radius: 5px;
  font-family: "Times New Roman", Times, serif;
  font-weight: 900;
}}
"""
    badge_regex = re.compile(r'(\.badge102\s*\{[^}]+\})')
    html = badge_regex.sub(r'\1\n' + badges_css, html, count=1)

    # 2. Button CSS
    btns_css = ""
    for c in chars:
        btns_css += f"""
.btn{c['id']} {{
  display: inline-block;
  margin-top: auto;
  padding: 10px 15px;
  background-color: {c['color']};
  color: {c['text_color']};
  text-decoration: none;
  border-radius: 6px;
}}
"""
    btn_regex = re.compile(r'(\.btn102\s*\{\s*display:\s*inline-block;[^}]+border-radius:\s*6px;\s*\})')
    html = btn_regex.sub(r'\1\n' + btns_css, html, count=1)

    # 3. Hover CSS
    hover_css = ""
    for c in chars:
        hover_css += f"""
.btn{c['id']}:hover {{
  background-color: {c['hover']};
  transform: scale(1.05);
}}
"""
    hover_regex = re.compile(r'(\.btn102:hover\s*\{\s*background-color:[^}]+transform:[^}]+\})')
    html = hover_regex.sub(r'\1\n' + hover_css, html, count=1)

    # 4. List CSS 1 (around line 3300)
    # .btn102\n {
    added_list_1 = "\n".join([f".btn{i}" for i in range(103, 118)])
    html = html.replace('.btn102\n {', f'.btn102\n{added_list_1}\n {{')

    # 5. List CSS 2 (around line 3530)
    # .btn102 {  with preceding .btn101,
    added_list_2 = ",\n".join([f".btn{i}" for i in range(103, 118)])
    html = html.replace('.btn102 {', f'.btn102,\n{added_list_2} {{')

    # Now html cards
    html_cards = ""
    for c in chars:
        html_cards += f"""
        <div
          class="card"
          data-name="{c['name']}"
          data-type="{c['type']}"
          data-stats="{c['stats']}"
          data-color="{c['color']}"
        >
          <div class="card-inner">
            <div class="favorite-btn">☆</div>
            <div class="badge{c['id']}">{c['type']}</div>
            <img loading="lazy" src="https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" />
            <div class="overlay">
              <span>VIEW CHARACTER</span>
            </div>
            <div class="content">
              <h3>{c['name']}</h3>
              <p>{c['quote']}</p>
              <a href="{c['link']}" target="_blank" class="btn{c['id']}">DETAIL</a>
            </div>
          </div>
        </div>
"""
    # Insert cards at the end of the container
    # Find the SAKURA CHITOSE O card ending
    # <a\nhref="https://umamusu.wiki/Sakura_Chitose_O"\ntarget="_blank"\nclass="btn102"\n>DETAIL</a>\n\n</div>\n</div>\n</div>
    insertion_regex = re.compile(r'(<a\s*href="https://umamusu\.wiki/Sakura_Chitose_O"[^>]*>DETAIL</a>\s*</div>\s*</div>\s*</div>)')
    html = insertion_regex.sub(r'\1\n' + html_cards, html, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
