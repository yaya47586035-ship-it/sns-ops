"""디피로그 썸네일/본문 이미지 생성기 (1536x1024)
사용: python3 tools/make_blog_images.py spec.json 출력폴더
spec 예시: tools/example_spec.json
- photo: 로컬 사진 경로(상업 이용 가능 라이선스만). 없으면 이모지 일러스트로 대체.
"""
import json,sys,os,subprocess,tempfile,html
spec=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
E=html.escape
def art(photo,icons,light):
    if photo:
        return f'<div class="ph" style="background-image:url(\'file://{os.path.abspath(photo)}\')"></div>'
    circ='rgba(255,255,255,.08)' if not light else 'rgba(255,255,255,.75)'
    ic=''.join(f'<span style="font-size:{s}px;left:{x}px;top:{y}px">{i}</span>' for i,(s,x,y) in zip(icons,[(260,980,250),(170,1200,520),(150,930,600),(120,1260,220)]))
    return f'<div class="blob" style="background:{circ}"></div><div class="icons">{ic}</div>'
CSS='''*{margin:0;box-sizing:border-box}body{width:1536px;height:1024px;font-family:Pretendard,sans-serif;letter-spacing:-.02em;word-break:keep-all}
.f{position:relative;width:1536px;height:1024px;overflow:hidden}
.ph{position:absolute;right:0;top:0;width:62%;height:100%;background-size:cover;background-position:center}
.blob{position:absolute;right:-120px;top:120px;width:900px;height:900px;border-radius:50%}
.icons span{position:absolute;filter:drop-shadow(0 24px 30px rgba(0,0,0,.25))}'''
def thumb(s):
    photo=s.get('photo'); fade='<div style="position:absolute;inset:0;background:linear-gradient(90deg,#0B2233 0%,#0B2233 42%,rgba(11,34,51,.55) 62%,rgba(11,34,51,0) 85%)"></div>' if photo else ''
    t='<br>'.join(E(x) for x in s['title_lines'])
    return f'''<div class="f" style="background:radial-gradient(circle at 75% 40%,#2A5C78,#0B2233 70%)">{art(photo,s.get('icons',['📄','💰','📅','✅']),False)}{fade}
<div style="position:absolute;left:96px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;width:820px;color:#fff">
<h1 style="font-size:128px;font-weight:900;line-height:1.12">{t}</h1>
<div style="margin-top:36px"><span style="display:inline-block;background:#FFC93C;color:#14202E;font-size:52px;font-weight:800;padding:14px 30px;border-radius:18px">{E(s['badge'])}</span></div>
<p style="margin-top:34px;font-size:44px;font-weight:700;opacity:.92">{E(s.get('sub',''))}</p></div></div>'''
def body(s):
    photo=s.get('body_photo')
    return f'''<div class="f" style="background:linear-gradient(120deg,#FDE8DA,#E9EEFB 55%,#D6E9FB)">{art(photo,s.get('body_icons',['📱','🐷','📁','🪙']),True)}
<div class="icons" style="position:absolute;inset:0"></div></div>''' if not photo else f'<div class="f"><div class="ph" style="width:100%;background-image:url(\'file://{os.path.abspath(photo)}\')"></div></div>'
for kind,fn in [('thumb',thumb),('body',body)]:
    h=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{fn(spec)}</body></html>'
    p=os.path.join(out,f"{spec['slug']}-{kind}.html"); open(p,'w',encoding='utf-8').write(h)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1536,height:1024}}}});await pg.goto('file://{os.path.abspath(p)}');await pg.waitForTimeout(400);await pg.screenshot({{path:'{os.path.abspath(p)[:-5]}.png'}});await b.close();}})();"
    subprocess.run(['node','-e',js],check=True); os.remove(p)
    print('saved',p[:-5]+'.png')
