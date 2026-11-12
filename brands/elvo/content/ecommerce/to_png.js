const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:1500}});
for(const f of fs.readdirSync('/tmp/ecom/html').filter(x=>x.endsWith('.html'))){
 await p.goto('file:///tmp/ecom/html/'+f);await p.waitForTimeout(500);
 await p.screenshot({path:__dirname+'/vivo/'+f.replace('.html','.jpg'),type:'jpeg',quality:92});console.log('ok',f);}
await b.close();})();
