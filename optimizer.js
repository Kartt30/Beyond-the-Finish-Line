const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

let changed = false;

// 1. Lazy load
if (html.includes('<img src=')) {
  html = html.replace(/<img\s+src=/g, '<img loading="lazy" src=');
  changed = true;
}

// 2. CSS Opt
if (html.includes('.card {') && html.includes('position: relative;')) {
  html = html.replace(/\.card\s*\{\s*position:\s*relative;/g, '.card { content-visibility: auto; contain-intrinsic-size: 320px 450px; position: relative;');
  changed = true;
}

// 3. Particles
if (html.includes('value: 70,')) {
  html = html.replace(/value:\s*70,/g, 'value: window.innerWidth <= 768 ? 20 : 70,');
  changed = true;
}

// 4. Lenis
if (html.includes('const lenis = new Lenis({') && !html.includes('isMobileDevice')) {
  html = html.replace('const lenis = new Lenis({', 'const isMobileDevice = window.innerWidth <= 768;\nconst lenis = new Lenis({\n  smoothTouch: false,');
  
  html = html.replace('requestAnimationFrame(raf);\n</script>', 'if (!isMobileDevice) { requestAnimationFrame(raf); } else { lenis.destroy(); }\n</script>');
  changed = true;
}

if (changed) {
  fs.writeFileSync('index.html', html);
  console.log("Optimization Applied Successfully");
} else {
  console.log("No changes made. Check matching logic.");
}
