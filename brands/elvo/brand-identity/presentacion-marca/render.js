const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+__dirname+'/deck.html');await p.waitForTimeout(1500);
await p.pdf({path:'elvo-branding-identidad-visual.pdf',width:'1920px',height:'1080px',printBackground:true});
const n=await p.locator('.pg').count();
for(let i=0;i<n;i++){await p.locator('.pg').nth(i).screenshot({path:`/tmp/pg-${String(i+1).padStart(2,'0')}.png`});}
await b.close();console.log(n)})();
