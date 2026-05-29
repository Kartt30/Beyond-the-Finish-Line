import re

chars = [
    { "id": 132, "name": "SAMSON BIG", "quote": "I'll be a BIG Umamusume!", "type": "LONG", "stats": "SPD: C | STA: B | POW: B | GUTS: B | INT: C", "color": "#00BCD4", "bg": "rgba(0,188,212,0.92)", "text_color": "white", "hover": "#0097a7", "link": "https://umamusu.wiki/Samson_Big", "gradient": "linear-gradient(135deg, #00BCD4, #FFC0CB)" },
    { "id": 133, "name": "SATONO CROWN", "quote": "I will secure the crown for the Satono family.", "type": "MEDIUM", "stats": "SPD: A | STA: A | POW: S | GUTS: B | INT: B", "color": "#1b3a20", "bg": "rgba(27,58,32,0.92)", "text_color": "white", "hover": "#122615", "link": "https://umamusu.wiki/Satono_Crown", "gradient": "linear-gradient(135deg, #1b3a20, #d4af37)" },
    { "id": 134, "name": "SOUNDS OF EARTH", "quote": "The symphony of the earth resonates in my run.", "type": "LONG", "stats": "SPD: A | STA: A | POW: B | GUTS: A | INT: B", "color": "#654321", "bg": "rgba(101,67,33,0.92)", "text_color": "white", "hover": "#4a3118", "link": "https://umamusu.wiki/Sounds_of_Earth", "gradient": "linear-gradient(135deg, #654321, #ffffff)" },
    { "id": 135, "name": "TAP DANCE CITY", "quote": "Feel the rhythm of the tap dance on the turf!", "type": "MEDIUM", "stats": "SPD: S | STA: S | POW: B | GUTS: A | INT: C", "color": "#d32f2f", "bg": "rgba(211,47,47,0.92)", "text_color": "white", "hover": "#b71c1c", "link": "https://umamusu.wiki/Tap_Dance_City", "gradient": "linear-gradient(135deg, #d32f2f, #fbc02d)" },
    { "id": 136, "name": "TSURUMARU TSUYOSHI", "quote": "With strength and grace, I aim for the top.", "type": "MEDIUM", "stats": "SPD: A | STA: B | POW: A | GUTS: B | INT: B", "color": "#1976d2", "bg": "rgba(25,118,210,0.92)", "text_color": "white", "hover": "#0d47a1", "link": "https://umamusu.wiki/Tsurumaru_Tsuyoshi", "gradient": "linear-gradient(135deg, #1976d2, #e3f2fd)" },
    { "id": 137, "name": "VERXINA", "quote": "A brilliant performance requires a brilliant stage.", "type": "MILE", "stats": "SPD: A | STA: B | POW: B | GUTS: A | INT: S", "color": "#7b1fa2", "bg": "rgba(123,31,162,0.92)", "text_color": "white", "hover": "#4a148c", "link": "https://umamusu.wiki/Verxina", "gradient": "linear-gradient(135deg, #7b1fa2, #e1bee7)" },
    { "id": 138, "name": "VIVLOS", "quote": "Let's sparkle and shine on the world stage!", "type": "MEDIUM", "stats": "SPD: A | STA: B | POW: B | GUTS: B | INT: A", "color": "#03a9f4", "bg": "rgba(3,169,244,0.92)", "text_color": "white", "hover": "#0288d1", "link": "https://umamusu.wiki/Vivlos", "gradient": "linear-gradient(135deg, #03a9f4, #b3e5fc)" },
    { "id": 139, "name": "VICTOIRE PISA", "quote": "Victory is my only destination.", "type": "MEDIUM", "stats": "SPD: A | STA: A | POW: S | GUTS: S | INT: B", "color": "#0d47a1", "bg": "rgba(13,71,161,0.92)", "text_color": "white", "hover": "#002171", "link": "https://umamusu.wiki/Victoire_Pisa", "gradient": "linear-gradient(135deg, #0d47a1, #b71c1c)" },
    { "id": 140, "name": "WIN VARIATION", "quote": "Every variation of the race leads to my win.", "type": "LONG", "stats": "SPD: B | STA: S | POW: A | GUTS: B | INT: B", "color": "#388e3c", "bg": "rgba(56,142,60,0.92)", "text_color": "white", "hover": "#1b5e20", "link": "https://umamusu.wiki/Win_Variation", "gradient": "linear-gradient(135deg, #388e3c, #fbc02d)" },
    { "id": 141, "name": "WONDER ACUTE", "quote": "A wonder that acute senses can bring.", "type": "DIRT", "stats": "SPD: A | STA: B | POW: S | GUTS: A | INT: B", "color": "#e65100", "bg": "rgba(230,81,0,0.92)", "text_color": "white", "hover": "#bf360c", "link": "https://umamusu.wiki/Wonder_Acute", "gradient": "linear-gradient(135deg, #e65100, #5d4037)" },
    { "id": 142, "name": "YAMANIN ZEPHYR", "quote": "Like a gentle zephyr, I will breeze past you.", "type": "SHORT", "stats": "SPD: S | STA: C | POW: A | GUTS: B | INT: B", "color": "#81c784", "bg": "rgba(129,199,132,0.92)", "text_color": "black", "hover": "#388e3c", "link": "https://umamusu.wiki/Yamanin_Zephyr", "gradient": "linear-gradient(135deg, #81c784, #f1f8e9)" },
    { "id": 143, "name": "RULERSHIP", "quote": "To rule the turf is my royal duty.", "type": "LONG", "stats": "SPD: A | STA: S | POW: A | GUTS: A | INT: B", "color": "#000080", "bg": "rgba(0,0,128,0.92)", "text_color": "white", "hover": "#000066", "link": "https://umamusu.wiki/Rulership", "gradient": "linear-gradient(135deg, #000080, #ffd700)" },
    { "id": 144, "name": "KISEKI", "quote": "A miracle waiting to unfold.", "type": "LONG", "stats": "SPD: A | STA: S | POW: B | GUTS: S | INT: B", "color": "#4a148c", "bg": "rgba(74,20,140,0.92)", "text_color": "white", "hover": "#311b92", "link": "https://umamusu.wiki/Kiseki", "gradient": "linear-gradient(135deg, #4a148c, #000000)" }
]

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Generate CSS
    css_to_add = ""
    for c in chars:
        css_to_add += f"""
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
.btn{c['id']} {{
  display: inline-block;
  margin-top: auto;
  padding: 10px 15px;
  background-color: {c['color']};
  color: {c['text_color']};
  text-decoration: none;
  border-radius: 6px;
  font-family: "Times New Roman", Times, serif;
  font-weight: 900;
  transition: background-color 0.3s, transform 0.3s;
}}
.btn{c['id']}:hover {{
  background-color: {c['hover']};
  transform: scale(1.05);
}}
"""

    # Insert CSS right before </style>
    if "</style>" in html:
        html = html.replace("</style>", css_to_add + "\n</style>")

    # 2. Generate HTML Cards
    html_cards = ""
    for c in chars:
        html_cards += f"""
        <div
          class="card"
          data-name="{c['name']}"
          data-type="{c['type']}"
          data-stats="{c['stats']}"
          data-color="{c['color']}"
          data-bg="{c['gradient']}"
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

    # Insert Cards right after Royce and Royce
    # We find the end of ROYCE AND ROYCE
    import re
    match = re.search(r'class="btn131">DETAIL</a>\s*</div>\s*</div>\s*</div>', html)
    if match:
        insertion_point = match.end()
        html = html[:insertion_point] + "\n" + html_cards + html[insertion_point:]
        print("Cards successfully inserted!")
    else:
        print("Could not find the end of ROYCE AND ROYCE card.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
