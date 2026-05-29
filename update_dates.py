dates = {
    "SAMSON BIG": "14 April",
    "SATONO CROWN": "10 March",
    "SOUNDS OF EARTH": "12 April",
    "TAP DANCE CITY": "16 March",
    "TSURUMARU TSUYOSHI": "6 April",
    "VERXINA": "5 March",
    "VIVLOS": "9 April",
    "VICTOIRE PISA": "31 March",
    "WIN VARIATION": "10 April",
    "WONDER ACUTE": "14 March",
    "YAMANIN ZEPHYR": "27 May",
    "RULERSHIP": "22 March",
    "KISEKI": "13 May"
}

import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    for name, date in dates.items():
        pattern = re.compile(rf'(data-name="{name}"[\s\S]*?data-date=)"TBA"')
        html = pattern.sub(rf'\1"{date}"', html, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Dates updated!")

if __name__ == '__main__':
    main()
