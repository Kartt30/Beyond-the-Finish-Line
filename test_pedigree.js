const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf8');
const dom = new JSDOM(html);
const document = dom.window.document;

// Simulate the logic to see if any exception is thrown
try {
  const pModal = document.getElementById('pedigreeModal');
  const pImg = document.getElementById('pedigreeModalImg');
  const pPlaceholder = document.getElementById('pedigreePlaceholder');
  const pTitle = document.getElementById('pedigreeModalTitle');
  const pDesc = document.getElementById('pedigreeModalDesc');
  const pBtn = document.getElementById('pedigreeModalBtn');

  document.querySelectorAll('.pedigree-trigger').forEach(card => {
      const title = card.getAttribute('data-title');
      const desc = card.querySelector('.support-info p').textContent;
      const bg = card.getAttribute('data-bg') || '#1a1a1a';
      const fullImg = card.getAttribute('data-fullbody');
      const thumbImg = card.querySelector('img').src;
      
      const themeColorElem = card.querySelector('.support-info h3');
      if (!themeColorElem) {
          console.log("Missing h3 for title: " + title);
      }
      const themeColor = themeColorElem.style.color;

      pTitle.textContent = title;
      pTitle.style.color = themeColor;
      pTitle.style.textShadow = `0 0 15px ${themeColor}`;
      pDesc.textContent = desc;
  });
  console.log("No JS errors simulated in the click handler.");
} catch (e) {
  console.error("Error found:", e);
}
