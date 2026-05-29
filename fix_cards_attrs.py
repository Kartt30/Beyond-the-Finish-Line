import re

chars = [
    { "id": 132, "name": "SAMSON BIG", "quote": "I'll be a BIG Umamusume!", "type": "LONG", "stats": "SPD: C | STA: B | POW: B | GUTS: B | INT: C", "color": "#00BCD4", "bg": "rgba(0,188,212,0.92)", "text_color": "white", "hover": "#0097a7", "link": "https://umamusu.wiki/Samson_Big", "gradient": "linear-gradient(135deg, #00BCD4, #FFC0CB)", "desc": "A small umamusume with BIG dreams." },
    { "id": 133, "name": "SATONO CROWN", "quote": "I will secure the crown for the Satono family.", "type": "MEDIUM", "stats": "SPD: A | STA: A | POW: S | GUTS: B | INT: B", "color": "#1b3a20", "bg": "rgba(27,58,32,0.92)", "text_color": "white", "hover": "#122615", "link": "https://umamusu.wiki/Satono_Crown", "gradient": "linear-gradient(135deg, #1b3a20, #d4af37)", "desc": "A determined runner bearing the Satono name." },
    { "id": 134, "name": "SOUNDS OF EARTH", "quote": "The symphony of the earth resonates in my run.", "type": "LONG", "stats": "SPD: A | STA: A | POW: B | GUTS: A | INT: B", "color": "#654321", "bg": "rgba(101,67,33,0.92)", "text_color": "white", "hover": "#4a3118", "link": "https://umamusu.wiki/Sounds_of_Earth", "gradient": "linear-gradient(135deg, #654321, #ffffff)", "desc": "A stayer whose runs are like a majestic symphony." },
    { "id": 135, "name": "TAP DANCE CITY", "quote": "Feel the rhythm of the tap dance on the turf!", "type": "MEDIUM", "stats": "SPD: S | STA: S | POW: B | GUTS: A | INT: C", "color": "#d32f2f", "bg": "rgba(211,47,47,0.92)", "text_color": "white", "hover": "#b71c1c", "link": "https://umamusu.wiki/Tap_Dance_City", "gradient": "linear-gradient(135deg, #d32f2f, #fbc02d)", "desc": "A front-runner who dominates with rhythm." },
    { "id": 136, "name": "TSURUMARU TSUYOSHI", "quote": "With strength and grace, I aim for the top.", "type": "MEDIUM", "stats": "SPD: A | STA: B | POW: A | GUTS: B | INT: B", "color": "#1976d2", "bg": "rgba(25,118,210,0.92)", "text_color": "white", "hover": "#0d47a1", "link": "https://umamusu.wiki/Tsurumaru_Tsuyoshi", "gradient": "linear-gradient(135deg, #1976d2, #e3f2fd)", "desc": "A graceful competitor striving for greatness." },
    { "id": 137, "name": "VERXINA", "quote": "A brilliant performance requires a brilliant stage.", "type": "MILE", "stats": "SPD: A | STA: B | POW: B | GUTS: A | INT: S", "color": "#7b1fa2", "bg": "rgba(123,31,162,0.92)", "text_color": "white", "hover": "#4a148c", "link": "https://umamusu.wiki/Verxina", "gradient": "linear-gradient(135deg, #7b1fa2, #e1bee7)", "desc": "An elegant umamusume seeking the ultimate stage." },
    { "id": 138, "name": "VIVLOS", "quote": "Let's sparkle and shine on the world stage!", "type": "MEDIUM", "stats": "SPD: A | STA: B | POW: B | GUTS: B | INT: A", "color": "#03a9f4", "bg": "rgba(3,169,244,0.92)", "text_color": "white", "hover": "#0288d1", "link": "https://umamusu.wiki/Vivlos", "gradient": "linear-gradient(135deg, #03a9f4, #b3e5fc)", "desc": "A sparkling talent with global ambitions." },
    { "id": 139, "name": "VICTOIRE PISA", "quote": "Victory is my only destination.", "type": "MEDIUM", "stats": "SPD: A | STA: A | POW: S | GUTS: S | INT: B", "color": "#0d47a1", "bg": "rgba(13,71,161,0.92)", "text_color": "white", "hover": "#002171", "link": "https://umamusu.wiki/Victoire_Pisa", "gradient": "linear-gradient(135deg, #0d47a1, #b71c1c)", "desc": "A dedicated athlete laser-focused on victory." },
    { "id": 140, "name": "WIN VARIATION", "quote": "Every variation of the race leads to my win.", "type": "LONG", "stats": "SPD: B | STA: S | POW: A | GUTS: B | INT: B", "color": "#388e3c", "bg": "rgba(56,142,60,0.92)", "text_color": "white", "hover": "#1b5e20", "link": "https://umamusu.wiki/Win_Variation", "gradient": "linear-gradient(135deg, #388e3c, #fbc02d)", "desc": "A versatile runner who adapts to any situation." },
    { "id": 141, "name": "WONDER ACUTE", "quote": "A wonder that acute senses can bring.", "type": "DIRT", "stats": "SPD: A | STA: B | POW: S | GUTS: A | INT: B", "color": "#e65100", "bg": "rgba(230,81,0,0.92)", "text_color": "white", "hover": "#bf360c", "link": "https://umamusu.wiki/Wonder_Acute", "gradient": "linear-gradient(135deg, #e65100, #5d4037)", "desc": "A veteran dirt runner with sharp instincts." },
    { "id": 142, "name": "YAMANIN ZEPHYR", "quote": "Like a gentle zephyr, I will breeze past you.", "type": "SHORT", "stats": "SPD: S | STA: C | POW: A | GUTS: B | INT: B", "color": "#81c784", "bg": "rgba(129,199,132,0.92)", "text_color": "black", "hover": "#388e3c", "link": "https://umamusu.wiki/Yamanin_Zephyr", "gradient": "linear-gradient(135deg, #81c784, #f1f8e9)", "desc": "A swift runner moving like the wind." },
    { "id": 143, "name": "RULERSHIP", "quote": "To rule the turf is my royal duty.", "type": "LONG", "stats": "SPD: A | STA: S | POW: A | GUTS: A | INT: B", "color": "#000080", "bg": "rgba(0,0,128,0.92)", "text_color": "white", "hover": "#000066", "link": "https://umamusu.wiki/Rulership", "gradient": "linear-gradient(135deg, #000080, #ffd700)", "desc": "A majestic umamusume born to rule." },
    { "id": 144, "name": "KISEKI", "quote": "A miracle waiting to unfold.", "type": "LONG", "stats": "SPD: A | STA: S | POW: B | GUTS: S | INT: B", "color": "#008080", "bg": "rgba(0,128,128,0.92)", "text_color": "white", "hover": "#004d4d", "link": "https://umamusu.wiki/Kiseki", "gradient": "linear-gradient(135deg, #008080, #ffffff)", "desc": "An artistic soul creating miraculous stories." }
]

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find SAMSON BIG block
    match = re.search(r'(<div\s+class="card"\s+data-name="SAMSON BIG"[\s\S]*?class="btn144">DETAIL</a>\s*</div>\s*</div>\s*</div>)', html)
    if not match:
        print("Block not found!")
        return

    old_block = match.group(1)

    html_cards = ""
    for c in chars:
        stats_match = re.search(r'SPD: (.*?) \| STA: (.*?) \| POW: (.*?) \| GUTS: (.*?) \| INT: (.*)', c['stats'])
        spd = stats_match.group(1) if stats_match else "C"
        sta = stats_match.group(2) if stats_match else "C"
        pow = stats_match.group(3) if stats_match else "C"
        wit = stats_match.group(5) if stats_match else "C"
        
        html_cards += f"""
<div class="card"
data-name="{c['name']}"
data-category="{c['type'].lower()}"
data-voice=""
data-bg="{c['gradient']}"
data-speed="{spd}"
data-stamina="{sta}"
data-power="{pow}"
data-wit="{wit}"
data-date="TBA"
data-quote="{c['quote']}"
data-img="https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg"
data-desc="{c['desc']}"
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
</div>"""

    html = html.replace(old_block, html_cards)

    # Fix Kiseki CSS colors
    html = html.replace('background-color:rgba(74,20,140,0.92);', 'background-color:rgba(0,128,128,0.92);')
    html = html.replace('background-color: #4a148c;', 'background-color: #008080;')
    html = html.replace('background-color: #311b92;', 'background-color: #004d4d;')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Cards fixed and colors updated!")

if __name__ == '__main__':
    main()
