import sys
css=open('base.css').read()
def page(body,cls,safe=False):
    zones=''
    if safe:
        zones='''<div class="zone" style="left:0;top:0;width:1080px;height:220px">상단 UI·상태바 (글씨 금지)</div>
<div class="zone" style="left:0;bottom:0;width:1080px;height:420px">하단 캡션·계정명·음악 (글씨 금지)</div>
<div class="zone" style="right:0;top:820px;width:150px;height:680px;writing-mode:vertical-rl">좋아요·댓글·공유 버튼</div>'''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="frame {cls} {"safe" if safe else ""}">{body}{zones}</div></body></html>'
R={}
# Reel cover / hook (0-3s)
R['reel_01_cover']=('reel','''
<div style="position:absolute;left:80px;top:260px" class="brand"><i></i>디피로그</div>
<div style="position:absolute;left:80px;top:420px;right:170px">
 <div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:52px;padding:14px 30px;border-radius:14px">D-25 · 12월 1일 마감</div>
 <h1 style="font-size:116px;font-weight:900;line-height:1.15;margin-top:50px">근로·자녀<br>장려금<br><span class="acc">아직 안 받았다면?</span></h1>
 <p style="font-size:54px;font-weight:600;line-height:1.4;margin-top:40px;opacity:.92">기한 후 신청하면<br>산정액의 <b class="acc">95%</b> 지급</p>
</div>
<div style="position:absolute;left:80px;right:170px;top:1230px;background:var(--navy2);border-radius:28px;padding:40px 44px;font-size:44px;font-weight:600;line-height:1.5">
 국세청 안내문 받은 <b class="acc">26만 가구</b> 대상<br>11월 2일 발송분</div>''')
R['reel_02_fact']=('reel','''
<div style="position:absolute;left:80px;top:300px;right:170px">
 <p style="font-size:56px;font-weight:700;opacity:.8">핵심만 3가지</p>
 <div style="margin-top:60px;display:flex;flex-direction:column;gap:40px">
  <div style="background:#fff;color:var(--ink);border-radius:30px;padding:46px 50px"><p style="font-size:44px;font-weight:700;color:#5A6B80">마감</p><p style="font-size:96px;font-weight:900">12월 1일<span style="font-size:60px">(화)</span></p></div>
  <div style="background:#fff;color:var(--ink);border-radius:30px;padding:46px 50px"><p style="font-size:44px;font-weight:700;color:#5A6B80">지급액</p><p style="font-size:96px;font-weight:900">산정액 <span class="hl">95%</span></p></div>
  <div style="background:#fff;color:var(--ink);border-radius:30px;padding:46px 50px"><p style="font-size:44px;font-weight:700;color:#5A6B80">지급일</p><p style="font-size:96px;font-weight:900">2027. 1. 15</p></div>
 </div></div>''')
R['reel_03_warn']=('reel','''
<div style="position:absolute;left:80px;top:520px;right:170px;text-align:left">
 <p style="font-size:150px;line-height:1">⚠️</p>
 <h2 style="font-size:110px;font-weight:900;line-height:1.18;margin-top:40px">12월 1일이<br>지나면<br><span class="red">추가 신청 불가</span></h2>
</div>''')
R['reel_04_end']=('reel','''
<div style="position:absolute;left:80px;top:330px;right:170px">
 <p style="font-size:60px;font-weight:700;opacity:.85">신청 경로·대상 확인표</p>
 <h2 style="font-size:104px;font-weight:900;line-height:1.2;margin-top:30px">홈택스 <span class="acc">3단계</span><br>캡처로 정리했어요</h2>
 <div style="margin-top:70px;background:var(--acc);color:var(--ink);border-radius:28px;padding:44px 48px;font-size:52px;font-weight:800;line-height:1.45">프로필 링크 → 디피로그<br><span style="font-weight:600;font-size:44px">저장해 두고 가족에게도 공유하세요</span></div>
</div>''')
# Card news 4:5
def card(n,tot,body,dark=False):
    bg='background:var(--navy)' if dark else ''
    return ('card'+(' dark' if dark else ''),f'''<div style="position:absolute;inset:0;{bg}"></div>
<div style="position:absolute;left:80px;top:70px" class="brand" >{'<i></i>' }디피로그</div>
<div style="position:absolute;right:80px;top:74px;font-size:32px;font-weight:700;opacity:.6">{n}/{tot}</div>{body}''')
R['card_01_cover']=card(1,6,'''
<div style="position:absolute;left:80px;right:80px;top:260px">
 <div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:44px;padding:12px 26px;border-radius:12px">12월 1일 마감</div>
 <h1 style="font-size:116px;font-weight:900;line-height:1.15;margin-top:44px">근로·자녀장려금<br><span class="acc">기한 후 신청</span></h1>
 <p style="font-size:50px;font-weight:600;line-height:1.5;margin-top:44px;opacity:.9">놓친 26만 가구, 지금 신청하면<br>산정액의 95% 받습니다</p>
</div>
<div style="position:absolute;left:80px;bottom:80px;font-size:34px;opacity:.6">넘겨서 확인 →</div>''',dark=True)
R['card_02_who']=card(2,6,'''
<div style="position:absolute;left:80px;right:80px;top:220px">
 <p style="font-size:44px;font-weight:700;color:#5A6B80">누가 대상인가요?</p>
 <h2 style="font-size:84px;font-weight:900;line-height:1.25;margin-top:24px">2025년 귀속 장려금을<br><span class="hl">아직 신청 안 한</span> 가구</h2>
 <div style="margin-top:60px;background:#fff;border-radius:28px;padding:44px;font-size:44px;line-height:1.6;font-weight:500;box-shadow:0 6px 0 #E3E8EF">
 · 11월 2일 국세청 안내문 발송 <b>26만 가구</b><br>· 정기 신청 후 추가 소득자료가<br>&nbsp;&nbsp;확인된 <b>1만 가구</b> 포함</div>
</div>''')
for k,v in R.items():
    open(k+'.html','w').write(page(v[1],v[0]))
    if k.startswith('reel'): open(k+'_safe.html','w').write(page(v[1],v[0],True))
