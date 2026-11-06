"""카드뉴스(1080x1350)·릴스 프레임(1080x1920) 생성기. 사용: python3 make_cards.py spec.json outdir
spec: {"cards":[{"dark":bool,"html":"..."}], "reel":[{"html":"..."}]}  (html은 내용부만; 공통 스타일 제공)"""
import json,sys,os,subprocess
spec=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
CSS=open(os.path.join(os.path.dirname(__file__),'sns_mock','base.css')).read()+'.card.dark{color:#fff}'
pages=[]
n=len(spec.get('cards',[]))
for i,c in enumerate(spec.get('cards',[]),1):
    bg='background:var(--navy)' if c.get('dark') else ''
    body=f'<div style="position:absolute;inset:0;{bg}"></div><div style="position:absolute;left:80px;top:70px" class="brand"><i></i>디피로그</div><div style="position:absolute;right:80px;top:74px;font-size:32px;font-weight:700;opacity:.6">{i}/{n}</div>{c["html"]}'
    pages.append((f'card_{i:02d}',1350,f'<div class="frame card {"dark" if c.get("dark") else ""}">{body}</div>'))
for i,r in enumerate(spec.get('reel',[]),1):
    pages.append((f'reel_{i:02d}',1920,f'<div class="frame reel">{r["html"]}</div>'))
for name,h,body in pages:
    p=os.path.abspath(os.path.join(out,name+'.html'))
    open(p,'w',encoding='utf-8').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{h}}}}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{p[:-5]}.png'}});await b.close();}})();"
    subprocess.run(['node','-e',js],check=True); os.remove(p); print('saved',p[:-5]+'.png')
