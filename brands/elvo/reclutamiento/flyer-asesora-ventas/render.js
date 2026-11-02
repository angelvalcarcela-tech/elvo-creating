const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext()).newPage();
await p.goto('file://'+process.cwd()+'/flyer.html',{waitUntil:'load'});await p.waitForTimeout(800);
await p.pdf({path:'elvo-flyer-asesora-ventas-v2.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close()})();
