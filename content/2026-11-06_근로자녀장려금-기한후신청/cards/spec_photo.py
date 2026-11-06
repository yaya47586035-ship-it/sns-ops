import json,os
HERE=os.path.dirname(os.path.abspath(__file__))
P=os.path.abspath(os.path.join(HERE,'..','photos'))
F='/home/user/sns-ops/tools/fonts'
ST=f'''<style>
@font-face{{font-family:GM;src:url('file://{F}/GmarketSansBold.woff');font-weight:700}}
@font-face{{font-family:GM;src:url('file://{F}/GmarketSansMedium.woff');font-weight:500}}
.frame *{{font-family:GM,Pretendard,sans-serif}}
.bg{{position:absolute;inset:0;background-size:cover;background-position:center}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,0) 34%,rgba(5,15,25,.45) 52%,rgba(5,15,25,.88) 76%)}}
.pill{{display:inline-block;background:#fff;color:#14304E;font-weight:700;border-radius:999px;padding:16px 40px 12px;border:4px solid #0A1622;box-shadow:0 6px 0 rgba(0,0,0,.35)}}
.pill em{{font-style:normal;color:#1C6FD8}}
.hd{{font-weight:700;line-height:1.16;color:#fff;-webkit-text-stroke:14px #0A1622;paint-order:stroke fill;letter-spacing:-.04em;text-shadow:0 8px 0 rgba(10,22,34,.85)}}
.y{{color:#FFD43B}}
.chk{{color:#fff;font-weight:500;display:flex;align-items:center;gap:18px;-webkit-text-stroke:6px #0A1622;paint-order:stroke fill}}
.chk b{{display:inline-flex;flex:none;width:52px;height:52px;border:5px solid #fff;border-radius:8px;align-items:center;justify-content:center;font-size:40px;color:#FFD43B;-webkit-text-stroke:0;box-shadow:0 0 0 3px #0A1622}}
.bubble{{position:absolute;background:#fff;color:#14202E;font-weight:500;text-align:center;border-radius:70px;padding:34px 44px 28px;line-height:1.45;border:4px solid #0A1622}}
.bubble:after{{content:"";position:absolute;bottom:-34px;left:var(--tail,62%);width:40px;height:40px;background:#fff;border-right:4px solid #0A1622;border-bottom:4px solid #0A1622;transform:skewX(-25deg) rotate(45deg)}}
.brandp{{position:absolute;display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.95);color:#0E2A47;font-weight:700;border-radius:999px;padding:12px 26px 8px}}
.brandp i{{width:16px;height:16px;border-radius:50%;background:#FFC93C;display:inline-block}}
.panel{{background:rgba(255,255,255,.97);color:#14202E;border-radius:28px;border:4px solid #0A1622}}
.bul{{color:#fff;font-weight:500;line-height:1.55;-webkit-text-stroke:6px #0A1622;paint-order:stroke fill}}
</style>'''
def bg(f,pos='center'):
    blur='filter:blur(7px);transform:scale(1.06);' if f=='2d4fae96.jpg' else ''
    return f'<div class="bg" style="{blur}background-image:url(\'file://{P}/{f}\');background-position:{pos}"></div><div class="shade"></div>'
def card(n,f,pos,inner,bubble=None):
    b=f'<div class="bubble" style="left:120px;right:300px;top:110px;font-size:42px">{bubble}</div>' if bubble else ''
    return {"raw":True,"html":ST+bg(f,pos)+f'<div class="brandp" style="right:44px;top:44px;font-size:30px"><i></i>디피로그</div><div class="chk" style="position:absolute;left:48px;top:52px;font-size:34px">{n}/6</div>'+b+inner}
L='position:absolute;left:48px;right:40px'
def row(a,b,c,last=False):
    return f'<div style="display:grid;grid-template-columns:.85fr 1.4fr .9fr;font-size:46px;font-weight:500;padding:24px 28px 18px;{"" if last else "border-bottom:3px solid #E3E8EF"}"><span>{a}</span><span>{b}</span><b style="font-weight:700">{c}</b></div>'
cards=[
 card(1,'a5b5c64a.jpg','center 40%',f'''<div style="{L};bottom:56px"><span class="pill" style="font-size:52px">2025년 소득분 <em>근로·자녀장려금</em></span>
<h1 class="hd" style="font-size:140px;margin-top:30px"><span class="y">5월에 놓쳤다면</span><br>12월 1일까지!</h1>
<p class="chk" style="font-size:54px;margin-top:26px"><b>✓</b>신청기간 : ~2026.12.1.(화)</p></div>''',
  bubble='신청 대상부터 신청 방법,<br>주의할 점까지 한눈에!'),
 card(2,'288025e0.jpg','center',f'''<div style="{L};bottom:56px"><span class="pill" style="font-size:52px">누가 <em>대상</em>인가요?</span>
<h2 class="hd" style="font-size:132px;margin-top:28px">안내문 받은<br><span class="y">26만 가구</span></h2>
<p class="chk" style="font-size:50px;margin-top:26px"><b>✓</b>5월 정기 신청을 놓친 가구</p>
<p class="chk" style="font-size:50px;margin-top:14px"><b>✓</b>지금 퇴직했어도 2025년 소득 있으면</p></div>'''),
 card(3,'2d4fae96.jpg','center 30%',f'''<div style="{L};bottom:56px"><span class="pill" style="font-size:52px">핵심 숫자 <em>3개</em></span>
<div style="display:flex;gap:16px;margin-top:30px">
<div class="panel" style="flex:1;padding:30px 10px 22px;text-align:center"><p style="font-size:38px;font-weight:500;color:#5A6B80">마감</p><p style="font-size:76px;font-weight:700;line-height:1.25">12.1</p></div>
<div class="panel" style="flex:1;padding:30px 10px 22px;text-align:center"><p style="font-size:38px;font-weight:500;color:#5A6B80">지급률</p><p style="font-size:76px;font-weight:700;line-height:1.25;color:#D9480F">95%</p></div>
<div class="panel" style="flex:1;padding:30px 10px 22px;text-align:center"><p style="font-size:38px;font-weight:500;color:#5A6B80">지급일</p><p style="font-size:76px;font-weight:700;line-height:1.25">1.15</p></div></div>
<p class="chk" style="font-size:50px;margin-top:28px"><b>✓</b>2027년 1월 15일(금) 지급</p></div>'''),
 card(4,'2965d9a0.jpg','center 35%',f'''<div style="{L};bottom:52px"><span class="pill" style="font-size:52px">소득 기준 · <em>최대 지급액</em></span>
<div class="panel" style="margin-top:26px;overflow:hidden">
<div style="display:grid;grid-template-columns:.85fr 1.4fr .9fr;font-size:40px;font-weight:700;background:#0E2A47;color:#fff;padding:24px 28px 18px"><span>가구</span><span>부부합산 소득</span><span>최대</span></div>
{row('단독','2,200만 미만','165만')}{row('홑벌이','3,200만 미만','285만')}{row('맞벌이','4,400만 미만','330만',True)}</div>
<p class="chk" style="font-size:46px;margin-top:24px"><b>✓</b>자녀 1명당 50~100만 원</p></div>'''),
 card(5,'698a3768.jpg','center 30%',f'''<div style="{L};bottom:56px"><span class="pill" style="font-size:52px">어떻게 <em>신청</em>하나요?</span>
<h2 class="hd" style="font-size:112px;margin-top:28px">QR·카톡 신청<br>ARS <span class="y">1544-9944</span></h2>
<p class="chk" style="font-size:48px;margin-top:26px"><b>✓</b>안내문 없으면 홈택스 직접 신청</p>
<p class="chk" style="font-size:48px;margin-top:14px"><b>✓</b>상담센터 1566-3636</p></div>'''),
 card(6,'bfff4199.jpg','center',f'''<div style="{L};bottom:56px"><span class="pill" style="font-size:52px;background:#FF5A4E;color:#fff">꼭 기억하세요</span>
<h2 class="hd" style="font-size:132px;margin-top:28px">12월 1일 지나면<br><span class="y">신청 불가!</span></h2>
<p class="chk" style="font-size:50px;margin-top:26px"><b>✓</b>저장하고 가족에게 공유</p>
<p class="chk" style="font-size:44px;margin-top:14px"><b>✓</b>30초 자가진단표는 프로필 링크</p></div>'''),
]
def reel(f,pos,inner,bubble=None,tail='62%'):
    b=f'<div class="bubble" style="--tail:{tail};left:70px;right:190px;top:260px;font-size:50px">{bubble}</div>' if bubble else ''
    return {"html":ST+bg(f,pos)+b+inner}
R='position:absolute;left:48px;right:150px'
reels=[
 reel('a5b5c64a.jpg','58% center',f'''<div style="{R};top:820px"><span class="pill" style="font-size:52px">2025년 <em>근로·자녀장려금</em></span>
<h1 class="hd" style="font-size:150px;margin-top:34px"><span class="y">아직 안</span><br><span class="y">받았다면?</span></h1>
<p class="chk" style="font-size:56px;margin-top:30px"><b>✓</b>12월 1일(화)까지 신청</p></div>''',bubble='5월에 놓친 장려금,<br>아직 기회 있어요!'),
 reel('288025e0.jpg','45% center',f'''<div style="{R};top:820px"><span class="pill" style="font-size:52px">국세청 <em>11월 2일</em> 안내</span>
<h2 class="hd" style="font-size:146px;margin-top:34px"><span class="y">26만 가구</span><br>안내문 발송</h2>
<p class="chk" style="font-size:54px;margin-top:30px"><b>✓</b>5월 정기 신청 놓친 가구</p></div>'''),
 reel('2d4fae96.jpg','center 30%',f'''<div style="{R};top:780px"><span class="pill" style="font-size:52px">핵심만 <em>3가지</em></span>
<h2 class="hd" style="font-size:136px;margin-top:34px;line-height:1.24">마감 <span class="y">12.1</span><br>지급 <span class="y">95%</span><br>지급일 <span class="y">1.15</span></h2></div>'''),
 reel('2965d9a0.jpg','center 35%',f'''<div style="{R};top:780px"><span class="pill" style="font-size:52px">근로장려금 <em>최대</em></span>
<h2 class="hd" style="font-size:128px;margin-top:34px;line-height:1.24">단독 <span class="y">165만</span><br>홑벌이 <span class="y">285만</span><br>맞벌이 <span class="y">330만</span></h2>
<p class="chk" style="font-size:54px;margin-top:26px"><b>✓</b>자녀 1명당 최대 100만</p></div>'''),
 reel('698a3768.jpg','center 30%',f'''<div style="{R};top:800px"><span class="pill" style="font-size:52px"><em>신청</em> 방법</span>
<h2 class="hd" style="font-size:124px;margin-top:34px;line-height:1.22">QR·카톡<br>ARS<br><span class="y">1544-9944</span></h2>
<p class="chk" style="font-size:50px;margin-top:26px"><b>✓</b>안내문 없으면 홈택스</p></div>'''),
 reel('bfff4199.jpg','40% center',f'''<div style="{R};top:860px"><span class="pill" style="font-size:52px;background:#FF5A4E;color:#fff">꼭 기억하세요</span>
<h2 class="hd" style="font-size:146px;margin-top:34px">12월 1일<br>지나면<br><span class="y">신청 불가!</span></h2></div>'''),
 reel('380f7df4.jpg','center 40%',f'''<div style="{R};top:800px"><span class="pill" style="font-size:52px"><em>30초</em> 자가진단</span>
<h2 class="hd" style="font-size:146px;margin-top:34px">나도 대상?<br><span class="y">체크리스트</span></h2>
<p class="chk" style="font-size:52px;margin-top:30px"><b>✓</b>가구별 기준표까지 정리</p>
<p class="chk" style="font-size:52px;margin-top:14px"><b>✓</b>프로필 링크 → 디피로그</p></div>'''),
]
json.dump({"cards":cards,"reel":reels},open(os.path.join(HERE,'spec_photo.json'),'w',encoding='utf-8'),ensure_ascii=False)
