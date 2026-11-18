/* Development-only PNG renderer. Uses a local Playwright/Chromium installation.
 * Copyright (c) 2026 Orca Gear Studio (MIT template; see LICENSE).
 * Copyright (c) 2026 Orca Vase Studio.
 */
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require(process.env.ORCA_PLAYWRIGHT_MODULE || 'playwright');
const folder = path.resolve(__dirname, '../assets/marketplace');
(async () => {
  const browser = await chromium.launch({headless:true, ...(process.env.ORCA_CHROMIUM_PATH ? {executablePath:process.env.ORCA_CHROMIUM_PATH} : {})});
  try {
    const page = await browser.newPage({deviceScaleFactor:1});
    for (const name of fs.readdirSync(folder).filter(name => /-(en|pt-BR)\.svg$/.test(name)).sort()) {
      const source = path.join(folder, name);
      const dimensions = fs.readFileSync(source,'utf8').match(/width="(\d+)" height="(\d+)"/);
      await page.setViewportSize({width:Number(dimensions[1]), height:Number(dimensions[2])});
      await page.goto(pathToFileURL(source).href);
      await page.evaluate(() => document.fonts.ready);
      const overflow = await page.locator('text').evaluateAll(elements => elements.map(el => ({text:el.textContent,box:el.getBoundingClientRect().toJSON()})).filter(item=>item.box.x<0||item.box.y<0||item.box.right>1600||item.box.bottom>900));
      if (overflow.length) throw Error(name+': text outside canvas: '+JSON.stringify(overflow));
      await page.screenshot({path:source.replace(/\.svg$/,'.png')});
      console.log(name.replace(/\.svg$/,'.png'));
    }
  } finally {await browser.close();}
})().catch(error => {console.error(error);process.exitCode=1;});
