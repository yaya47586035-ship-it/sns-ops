const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const fs=require('fs');
for(const f of fs.readdirSync('.').filter(f=>f.endsWith('.html'))){
 const reel=f.startsWith('reel');const p=await b.newPage({viewport:{width:1080,height:reel?1920:1350}});
 await p.goto('file://'+process.cwd()+'/'+f);await p.waitForTimeout(300);
 await p.screenshot({path:f.replace('.html','.png')});await p.close();}
await b.close();})();
