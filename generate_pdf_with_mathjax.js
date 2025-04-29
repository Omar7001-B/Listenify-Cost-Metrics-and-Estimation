const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  console.log('Starting professional PDF generation with proper MathJax rendering...');

  // Get full path to HTML file
  const htmlPath = path.resolve('./project_report_enhanced.html');
  const pdfPath = path.resolve('./listenify_project_estimation_professional.pdf');
  
  if (!fs.existsSync(htmlPath)) {
    console.error(`Error: HTML file not found at ${htmlPath}`);
    process.exit(1);
  }

  console.log(`Converting ${htmlPath} to PDF...`);
  
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  try {
    const page = await browser.newPage();
    
    // Load the HTML file
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
    
    // Wait for MathJax to render (this is important!)
    await page.waitForFunction('MathJax.typeset && MathJax.typesetPromise', { timeout: 10000 });
    await page.evaluate(async () => {
      // Force MathJax to re-render everything
      if (window.MathJax && window.MathJax.typesetPromise) {
        await window.MathJax.typesetPromise();
      }
    });
    
    // Additional 2-second delay to ensure rendering is complete
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Generate PDF
    await page.pdf({
      path: pdfPath,
      format: 'Letter',
      margin: {
        top: '20mm',
        right: '20mm',
        bottom: '20mm',
        left: '20mm'
      },
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div style="width: 100%; font-size: 8px; padding: 5px 5mm; border-bottom: 1px solid #ddd; text-align: center; color: #777;">Listenify Project Estimation</div>',
      footerTemplate: '<div style="width: 100%; font-size: 8px; padding: 5px 5mm; border-top: 1px solid #ddd; text-align: center; color: #777; font-family: Arial;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
    });
    
    console.log(`PDF successfully generated: ${pdfPath}`);
  } catch (error) {
    console.error('Error during PDF generation:', error);
  } finally {
    await browser.close();
  }
})(); 