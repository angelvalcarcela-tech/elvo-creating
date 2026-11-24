const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:900}});
await p.goto('file://'+__dirname+'/guion.html');await p.waitForTimeout(1200);
await p.pdf({path:'elvo-guion-black-days-con-objeciones.pdf',width:'1600px',height:'900px',printBackground:true});
const n=await p.locator('.pg').count();for(let i=0;i<n;i++)await p.locator('.pg').nth(i).screenshot({path:`/tmp/gz-${i+1}.png`});
await b.close();console.log(n)})();
