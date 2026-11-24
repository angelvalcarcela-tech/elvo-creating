const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:810}});
await p.goto('file://'+__dirname+'/guion.html');await p.waitForTimeout(1500);
await p.pdf({path:'ELVO-Black-Days-guion-editado.pdf',width:'1440px',height:'810px',printBackground:true});
const n=await p.locator('.pg').count();for(let i=0;i<n;i++)await p.locator('.pg').nth(i).screenshot({path:`/tmp/ge-${i+1}.png`});
await b.close();console.log(n)})();
