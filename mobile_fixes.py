css_to_add = """
/* ---- MOBILE TWEAKS ---- */
@media (max-width: 768px) {
  /* Fix Character of the Day texts overflowing */
  .daily-character h2 {
    font-size: 22px !important;
    white-space: normal;
    word-break: break-word;
    letter-spacing: 1px !important;
  }
  .daily-character h3 {
    font-size: 24px !important;
    white-space: normal;
    word-break: break-word;
  }
  
  /* Fix Filter menu position overlapping image */
  .filter-menu {
    position: relative !important;
    top: auto !important;
    left: auto !important;
    margin: 20px auto !important;
    display: flex;
    justify-content: center;
    width: 100%;
    z-index: 999;
  }
  
  /* Dropdown wrapper positioning fix for relative parent */
  .filter-dropdown {
    top: 50px !important;
    left: auto !important;
  }
  
  /* Fix search box input width */
  .search-box input {
    width: 90% !important;
    font-size: 16px !important;
  }
}
"""

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    if "/* ---- MOBILE TWEAKS ---- */" not in html:
        html = html.replace("</style>", css_to_add + "\n</style>")
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Mobile tweaks added!")
    else:
        print("Mobile tweaks already exist.")

if __name__ == '__main__':
    main()
