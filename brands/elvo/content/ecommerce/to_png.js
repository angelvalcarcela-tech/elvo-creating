const {chromium}=require('playwright');const fs=require('fs');
const dir=process.argv[2]||'/tmp/ecom/html', out=process.argv[3]||'vivo';
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:1500}});
fs.mkdirSync(__dirname+'/'+out,{recursive:true});
for(const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html'))){
 await p.goto('file://'+dir+'/'+f);await p.waitForTimeout(500);
 await p.screenshot({path:__dirname+'/'+out+'/'+f.replace('.html','.jpg'),type:'jpeg',quality:92});console.log('ok',f);}
await b.close();})();
