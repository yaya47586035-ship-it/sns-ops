import os,subprocess,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spec_photo import ST,bg
out=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','images'))
H=f'''<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">{ST}<div class="frame" style="position:relative;width:1536px;height:1024px;overflow:hidden">{bg('a5b5c64a.jpg','center 40%')}
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,15,25,.75),rgba(5,15,25,.2) 60%,rgba(0,0,0,0))"></div>
<div class="brandp" style="right:48px;top:44px;font-size:34px"><i></i>디피로그</div>
<div style="position:absolute;left:72px;bottom:80px;right:300px"><span class="pill" style="font-size:56px">2025년 소득분 <em>근로·자녀장려금</em></span>
<h1 class="hd" style="font-size:150px;margin-top:30px"><span class="y">기한 후 신청</span><br>12월 1일 마감</h1>
<p class="chk" style="font-size:56px;margin-top:26px"><b>✓</b>산정액 95% · 2027.1.15 지급</p></div></div></body></html>'''
p=os.path.join(out,'_t.html');open(p,'w',encoding='utf-8').write(H)
png=os.path.join(out,'근로장려금-기한후신청-thumb.png')
js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1536,height:1024}}}});await pg.goto('file://{p}');await pg.waitForTimeout(400);await pg.screenshot({{path:'{png}'}});await b.close();}})();"
subprocess.run(['node','-e',js],check=True);os.remove(p);print(png)
