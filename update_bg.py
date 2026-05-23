import re

gradients = {
    "ADMIRE GROOVE": 'linear-gradient(135deg, #a1c4fd, #234990)',
    "AIR MESSIAH": 'linear-gradient(135deg, #f6d365, #0c4f8d)',
    "BELIEVE": 'linear-gradient(135deg, #fdfbfb, #e5c158)',
    "BLAST ONEPIECE": 'linear-gradient(135deg, #ff9a9e, #3060a8)',
    "BUBBLE GUM FELLOW": 'linear-gradient(135deg, #fbc2eb, #e1a1b1)',
    "CHRONO GENESIS": 'linear-gradient(135deg, #cfd9df, #999999)',
    "COPANO RICKEY": 'linear-gradient(135deg, #f6d365, #f18a20)',
    "CURREN BOUQUETD'OR": 'linear-gradient(135deg, #ffccd5, #f16889)',
    "DARING HEART": 'linear-gradient(135deg, #ff758c, #bb2020)',
    "DARING TACT": 'linear-gradient(135deg, #d4fc79, #3b5e40)',
    "DURAMENTE": 'linear-gradient(135deg, #e6b980, #161e38)',
    "DURANDAL": 'linear-gradient(135deg, #fad0c4, #b02a2a)',
    "EPIPHANEIA": 'linear-gradient(135deg, #96fbc4, #115933)',
    "ESPOIR CITY": 'linear-gradient(135deg, #e0c3fc, #152f6b)',
    "FURIOSO": 'linear-gradient(135deg, #f5576c, #2f1111)'
}

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    for name, grad in gradients.items():
        # Look for the data-color="..." part for each card to insert data-bg right after it
        # Note: the user's name is in data-name="NAME"
        # Since we generated it as:
        # data-name="{name}"
        # data-type="..."
        # data-stats="..."
        # data-color="..."
        
        pattern = re.compile(rf'(data-name="{name}"\s*\n\s*data-type="[^"]+"\s*\n\s*data-stats="[^"]+"\s*\n\s*data-color="[^"]+")')
        html = pattern.sub(rf'\1\n          data-bg="{grad}"', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
