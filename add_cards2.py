import re
import os

chars = [
    {
        "id": 118,
        "name": "FUSAICHI PANDORA",
        "category": "medium",
        "color": "#e96b8e",
        "bgDark": "#753547",
        "speed": "A", "stamina": "B", "power": "B", "wit": "A",
        "date": "27 February",
        "quote": "A genius who plays by her own rules.",
        "desc": "Portrayed as a confident genius whose playful self-confidence masks her true dedication.",
        "link": "https://umamusu.wiki/Fusaichi_Pandora"
    },
    {
        "id": 119,
        "name": "GRAN ALEGRIA",
        "category": "mile",
        "color": "#59419b",
        "bgDark": "#2c204d",
        "speed": "S", "stamina": "C", "power": "A", "wit": "B",
        "date": "24 January",
        "quote": "I will prove my strength on the grandest stage.",
        "desc": "An overwhelming force on the mile, leaving the competition in awe.",
        "link": "https://umamusu.wiki/Gran_Alegria"
    },
    {
        "id": 120,
        "name": "HISHI MIRACLE",
        "category": "long",
        "color": "#60c5c6",
        "bgDark": "#306263",
        "speed": "B", "stamina": "A", "power": "B", "wit": "C",
        "date": "31 March",
        "quote": "Miracles happen when you believe, even if you take it easy.",
        "desc": "An easygoing runner who pulls off the most incredible upsets when it matters.",
        "link": "https://umamusu.wiki/Hishi_Miracle"
    },
    {
        "id": 121,
        "name": "HOKKO TARUMAE",
        "category": "dirt",
        "color": "#eb8c65",
        "bgDark": "#754632",
        "speed": "A", "stamina": "A", "power": "A", "wit": "C",
        "date": "26 May",
        "quote": "Bringing Tomakomai's charm to the whole world!",
        "desc": "A passionate local idol who rules the dirt tracks with an unyielding spirit.",
        "link": "https://umamusu.wiki/Hokko_Tarumae"
    },
    {
        "id": 122,
        "name": "K.S. MIRACLE",
        "category": "short",
        "color": "#235889",
        "bgDark": "#112c44",
        "speed": "A", "stamina": "C", "power": "B", "wit": "B",
        "date": "16 April",
        "quote": "Every run is a miracle I cherish with all my heart.",
        "desc": "A gentle yet resolute soul running to express her gratitude.",
        "link": "https://umamusu.wiki/K.S._Miracle"
    },
    {
        "id": 123,
        "name": "KATSURAGI ACE",
        "category": "medium",
        "color": "#111a43",
        "bgDark": "#080d21",
        "speed": "A", "stamina": "B", "power": "S", "wit": "B",
        "date": "24 April",
        "quote": "A brilliant ace that defies expectations.",
        "desc": "A fearless front-runner determined to create her own legend.",
        "link": "https://umamusu.wiki/Katsuragi_Ace"
    },
    {
        "id": 124,
        "name": "LOGOTYPE",
        "category": "mile",
        "color": "#352b2b",
        "bgDark": "#1a1515",
        "speed": "A", "stamina": "B", "power": "A", "wit": "B",
        "date": "10 March",
        "quote": "Leaving my mark with unquestionable strength.",
        "desc": "A steadfast champion whose presence commands the turf.",
        "link": "https://umamusu.wiki/Logotype"
    },
    {
        "id": 125,
        "name": "LUCKY LILAC",
        "category": "medium",
        "color": "#d78eb2",
        "bgDark": "#6b4759",
        "speed": "A", "stamina": "B", "power": "S", "wit": "B",
        "date": "3 April",
        "quote": "A blooming lilac that carries the luck of the draw.",
        "desc": "An elegant yet powerful presence whose grace captivates the audience.",
        "link": "https://umamusu.wiki/Lucky_Lilac"
    },
    {
        "id": 126,
        "name": "MARCHE LORRAINE",
        "category": "dirt",
        "color": "#713838",
        "bgDark": "#381c1c",
        "speed": "B", "stamina": "B", "power": "S", "wit": "B",
        "date": "4 February",
        "quote": "Taking on the world, one dirt track at a time.",
        "desc": "A trailblazing heroine who conquered the global dirt stage.",
        "link": "https://umamusu.wiki/Marche_Lorraine"
    },
    {
        "id": 127,
        "name": "NEO UNIVERSE",
        "category": "medium",
        "color": "#153965",
        "bgDark": "#0a1c32",
        "speed": "A", "stamina": "B", "power": "B", "wit": "S",
        "date": "21 May",
        "quote": "I can see the entire universe through my eyes.",
        "desc": "A mysterious intellect possessing insight beyond the stars.",
        "link": "https://umamusu.wiki/Neo_Universe"
    },
    {
        "id": 128,
        "name": "NO REASON",
        "category": "medium",
        "color": "#a2382e",
        "bgDark": "#511c17",
        "speed": "A", "stamina": "B", "power": "A", "wit": "C",
        "date": "18 May",
        "quote": "I don't need a reason to win.",
        "desc": "Driven by raw instinct and an unpredictable racing style.",
        "link": "https://umamusu.wiki/No_Reason"
    },
    {
        "id": 129,
        "name": "NORTH FLIGHT",
        "category": "mile",
        "color": "#344c80",
        "bgDark": "#1a2640",
        "speed": "S", "stamina": "C", "power": "A", "wit": "B",
        "date": "12 April",
        "quote": "A beautiful flight that rules the mile.",
        "desc": "The queen of the mile who glides elegantly to victory.",
        "link": "https://umamusu.wiki/North_Flight"
    },
    {
        "id": 130,
        "name": "RED DESIRE",
        "category": "medium",
        "color": "#c82828",
        "bgDark": "#641414",
        "speed": "A", "stamina": "B", "power": "A", "wit": "B",
        "date": "20 April",
        "quote": "My blazing desire outshines all rivals.",
        "desc": "Fierce and competitive, her burning passion fuels her speed.",
        "link": "https://umamusu.wiki/Red_Desire"
    },
    {
        "id": 131,
        "name": "ROYCE AND ROYCE",
        "category": "medium",
        "color": "#295f46",
        "bgDark": "#142f23",
        "speed": "B", "stamina": "A", "power": "B", "wit": "B",
        "date": "15 April",
        "quote": "Perseverance that stands the test of time.",
        "desc": "A reliable and elegant stayer whose dedication earns widespread respect.",
        "link": "https://umamusu.wiki/Royce_and_Royce"
    }
]

def main():
    filepath = 'c:/xampp/htdocs/andung/beyond-finish-line/index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Generate CSS
    css_content = "\n/* NEW CARDS FROM 118 */\n"
    for c in chars:
        # Hex to rgba roughly for background (I'll just use the hex or a semi-transparent version)
        # Using 0.92 opacity
        hex_color = c["color"].lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgba_str = f"rgba({rgb[0]},{rgb[1]},{rgb[2]},0.92)"
        
        # Decide text color based on background luminance roughly
        # For simplicity, if color is light, use black, else white. 
        # Most colors above are somewhat dark, so white is generally fine, but let's just use white.
        text_color = "white"

        css_content += f"""
.badge{c['id']} {{
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: {rgba_str};
  color: {text_color};
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
  color: {text_color};
  text-decoration: none;
  border-radius: 6px;
}}

.btn{c['id']}:hover {{
  background-color: {c['bgDark']};
  transform: scale(1.05);
}}
"""

    # Insert CSS before </style>
    if "</style>" in html:
        html = html.replace("</style>", css_content + "\n</style>")

    # 2. Generate HTML Cards
    html_cards = "\n"
    for c in chars:
        audio_file = c['name'].lower().replace(' ', '').replace('.', '')
        
        html_cards += f"""
<div class="card"
data-name="{c['name']}"
data-category="{c['category']}"
data-voice="voices/{audio_file}.mp3"
data-bg="linear-gradient(135deg,{c['color']},{c['bgDark']})"
data-speed="{c['speed']}"
data-stamina="{c['stamina']}"
data-power="{c['power']}"
data-wit="{c['wit']}"
data-date="{c['date']}"
data-quote="{c['quote']}"
data-img="https://i.pinimg.com/736x/00/00/00/placeholder.jpg"
data-desc="{c['desc']}"
data-color="{c['color']}"
>
  <div class="card-inner">
    <div class="favorite-btn">☆</div>
    <div class="badge{c['id']}">{c['category'].upper()}</div>

    <img loading="lazy" src="https://i.pinimg.com/736x/00/00/00/placeholder.jpg" />

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

    # Insert Cards before <!-- PAGINATION -->
    if "<!-- PAGINATION -->" in html:
        html = html.replace("<!-- PAGINATION -->", html_cards + "\n    <!-- PAGINATION -->")
    else:
        print("PAGINATION comment not found!")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Successfully updated index.html!")

if __name__ == '__main__':
    main()
