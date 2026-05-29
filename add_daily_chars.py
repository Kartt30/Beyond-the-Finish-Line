import re

chars = [
    { "name": "SAMSON BIG", "quote": "I'll be a BIG Umamusume!", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "SATONO CROWN", "quote": "I will secure the crown for the Satono family.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "SOUNDS OF EARTH", "quote": "The symphony of the earth resonates in my run.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "TAP DANCE CITY", "quote": "Feel the rhythm of the tap dance on the turf!", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "TSURUMARU TSUYOSHI", "quote": "With strength and grace, I aim for the top.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "VERXINA", "quote": "A brilliant performance requires a brilliant stage.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "VIVLOS", "quote": "Let's sparkle and shine on the world stage!", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "VICTOIRE PISA", "quote": "Victory is my only destination.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "WIN VARIATION", "quote": "Every variation of the race leads to my win.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "WONDER ACUTE", "quote": "A wonder that acute senses can bring.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "YAMANIN ZEPHYR", "quote": "Like a gentle zephyr, I will breeze past you.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "RULERSHIP", "quote": "To rule the turf is my royal duty.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" },
    { "name": "KISEKI", "quote": "A miracle waiting to unfold.", "img": "https://i.pinimg.com/736x/42/6b/09/426b09f0b3063c9f7f32a19db7e89f53.jpg" }
]

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix CSS overflow on .daily-character
    # Add box-sizing: border-box; to .daily-character
    css_pattern = r'(\.daily-character\s*\{[\s\S]*?padding:[\s\S]*?)(border-bottom: 1px solid rgba\(255,255,255,0\.07\);)'
    if "box-sizing: border-box;" not in html:
        # Actually a safer replace:
        old_css = """.daily-character{

  width:100%;

  margin:0;

  padding:36px 20px 28px;

  text-align:center;

  color:white;

  border-bottom: 1px solid rgba(255,255,255,0.07);

}"""
        new_css = """.daily-character{
  box-sizing: border-box;
  width:100%;
  margin:0;
  padding:36px 20px 28px;
  text-align:center;
  color:white;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}"""
        html = html.replace(old_css, new_css)
        
        # fallback if exact match fails
        html = re.sub(r'(\.daily-character\s*\{)', r'\1\n  box-sizing: border-box;', html, count=1)

    # 2. Append to dailyCharacters array
    # Find the end of ROYCE AND ROYCE
    # },
    # {
    #   name:"ROYCE AND ROYCE",
    #   quote:"Perseverance that stands the test of time.",
    #   img:"https://i.pinimg.com/736x/f4/98/89/f49889651996963c4866f779654c4e6a.jpg"
    # }
    # ];
    
    match = re.search(r'(name:"ROYCE AND ROYCE"[\s\S]*?img:".*?"\s*\n\})', html)
    if match:
        insertion_str = ",\n"
        for i, c in enumerate(chars):
            insertion_str += f"""{{
  name:"{c['name']}",
  quote:"{c['quote']}",
  img:"{c['img']}"
}}"""
            if i < len(chars) - 1:
                insertion_str += ",\n"
        
        html = html.replace(match.group(1), match.group(1) + insertion_str)
        print("dailyCharacters array updated.")
    else:
        print("ROYCE AND ROYCE not found in array.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
