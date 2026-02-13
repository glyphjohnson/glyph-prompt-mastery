const puppeteer = require('puppeteer');
const marked = require('marked');
const fs = require('fs');
const path = require('path');

marked.use({ 
  breaks: true 
}); // for better md

const packs = [
  'copy-pack.md',
  'cs-pack.md',
  'e-commerce-prompt-mastery.md',
  'seo-pack.md',
  'social-media-pack.md',
  'upsell-pack.md'
];

const inputDir = path.join(__dirname, '../products');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-accelerated-2d-canvas',
      '--no-first-run',
      '--no-zygote',
      '--disable-gpu'
    ]
  });

  for (const pack of packs) {
    const mdPath = path.join(inputDir, pack);
    const pdfPath = path.join(inputDir, pack.replace(/\\.md$/, '.pdf'));
    
    if (!fs.existsSync(mdPath)) {
      console.log(`Missing: ${mdPath}`);
      continue;
    }

    const mdContent = fs.readFileSync(mdPath, 'utf8');
    const title = pack.replace(/\\.md$/, '').replace(/-/g, ' ').toUpperCase();
    const htmlContent = `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Glyph Prompt Mastery: ${title}</title>
  <style>
    @page { margin: 1in; }
    body { 
      font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
      line-height: 1.6; 
      color: #333; 
      max-width: 800px; 
      margin: 0 auto; 
      padding: 1in; 
      background: white;
    }
    h1, h2, h3 { color: #28a745; margin-top: 1.5em; }
    h1 { font-size: 2em; border-bottom: 2px solid #28a745; padding-bottom: 0.5em; }
    strong { color: #0070ba; }
    code, pre { 
      background: #f8f9fa; 
      padding: 0.5em; 
      border-radius: 5px; 
      font-family: 'Courier New', monospace; 
      overflow-x: auto;
    }
    pre { padding: 1em; border-left: 4px solid #28a745; }
    ul, ol { margin-left: 1.5em; }
    blockquote { border-left: 4px solid #ffc107; padding-left: 1em; font-style: italic; }
    .header { text-align: center; margin-bottom: 2em; }
    .footer { text-align: center; font-size: 0.8em; color: #666; margin-top: 2em; border-top: 1px solid #eee; padding-top: 1em; }
  </style>
</head>
<body>
  <div class="header">
    <h1>Glyph Prompt Mastery</h1>
    <h2>${title}</h2>
    <p>Professional AI Prompt Library for E-Commerce Success</p>
  </div>
  ${marked.parse(mdContent)}
  <div class="footer">
    <p>&copy; 2026 Glyph Prompt Mastery | glyphjohnson.github.io/glyph-prompt-mastery/</p>
  </div>
</body>
</html>`;

    const page = await browser.newPage();
    await page.setContent(htmlContent, { waitUntil: 'networkidle0' });
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      preferCSSPageSize: true
    });
    await page.close();
    console.log(`✅ Generated: ${pdfPath}`);
  }

  await browser.close();
  console.log('All PDFs generated!');
})();
