const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const f of fs.readdirSync('/tmp/fichas').filter(x=>x.endsWith('.html'))){
 await p.goto('file:///tmp/fichas/'+f);await p.waitForTimeout(400);
 await p.pdf({path:__dirname+'/'+f.replace('.html','.pdf'),format:'A4',printBackground:true});console.log('ok',f);}
await b.close();})();
