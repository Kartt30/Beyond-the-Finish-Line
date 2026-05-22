const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
const extracted = fs.readFileSync('extracted.txt', 'utf8');

const regex = /({\s*name:"BELNO LIGHT"[\s\S]*?})([\s\S]*?)];/;

if(regex.test(html)) {
  html = html.replace(regex, `$1${extracted}\n];`);
  fs.writeFileSync('index.html', html);
  console.log("Success");
} else {
  console.log("Failed to find target string");
}
