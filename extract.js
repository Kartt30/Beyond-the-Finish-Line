const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const regex = /<div[^>]*class="[^"]*card[^"]*"[\s\S]*?data-name="([^"]+)"[\s\S]*?data-quote="([^"]+)"[\s\S]*?data-img="([^"]+)"/g;
let match;
let started = false;
let output = [];
while ((match = regex.exec(html)) !== null) {
  if (match[1] === "TAMAMO CROSS") started = true;
  if (started) {
    output.push(`{\n  name:"${match[1]}",\n  quote:"${match[2]}",\n  img:"${match[3]}"\n}`);
  }
  if (match[1] === "SAKURA CHITOSE O") break;
}
fs.writeFileSync('extracted.txt', ',\n' + output.join(',\n'));
