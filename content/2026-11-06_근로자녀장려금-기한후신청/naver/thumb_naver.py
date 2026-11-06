import os,subprocess
H=os.path.dirname(os.path.abspath(__file__));P=os.path.abspath(os.path.join(H,'..','photos'));F='/home/user/sns-ops/tools/fonts'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:GM;src:url('file://{F}/GmarketSansBold.woff');font-weight:700}}
@font-face{{font-family:GM;src:url('file://{F}/GmarketSansMedium.woff');font-weight:500}}
*{{margin:0;box-sizing:border-box;font-family:GM,sans-serif;letter-spacing:-.04em}}
.f{{position:relative;width:1080px;height:1080px;overflow:hidden;background:#FBF4EA}}
.ph{{position:absolute;left:0;right:0;bottom:0;height:640px;background:url('file://{P}/698a3768.jpg') center 35%/cover}}
.fade{{position:absolute;left:0;right:0;top:420px;height:240px;background:linear-gradient(#FBF4EA,rgba(251,244,234,0))}}
h1{{position:absolute;left:0;right:0;top:110px;text-align:center;font-size:104px;font-weight:700;line-height:1.16;color:#3B2416}}
h1 em{{font-style:normal;color:#D2361E}}
.pill{{position:absolute;left:50%;transform:translateX(-50%);top:420px;background:#FFE7A3;color:#3B2416;font-size:46px;font-weight:700;padding:18px 42px 12px;border-radius:999px;white-space:nowrap;box-shadow:0 6px 0 rgba(59,36,22,.15)}}
.brand{{position:absolute;left:50%;transform:translateX(-50%);bottom:46px;background:#D2361E;color:#fff;font-size:40px;font-weight:700;padding:14px 40px 8px;border-radius:14px}}
.spark{{position:absolute;right:120px;top:70px;width:70px;height:70px}}
</style></head><body><div class="f"><div class="ph"></div><div class="fade"></div>
<h1><em>부모님 장려금</em><br>안내문 확인하셨나요?</h1>
<div class="pill">12월 1일(화) 마감 · ARS 1544-9944</div>
<div class="brand">지식플래너</div></div></body></html>'''
p=os.path.join(H,'_t.html');open(p,'w',encoding='utf-8').write(html)
out=os.path.join(H,'naver-earned-income-credit-late-thumb.png')
js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1080}}}});await pg.goto('file://{p}');await pg.waitForTimeout(400);await pg.screenshot({{path:'{out}'}});await b.close();}})();"
subprocess.run(['node','-e',js],check=True);os.remove(p);print(out)
