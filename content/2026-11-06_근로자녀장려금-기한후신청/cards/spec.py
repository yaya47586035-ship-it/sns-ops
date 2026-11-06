import json,os
W='position:absolute;left:80px;right:80px'
def box(t,v,extra=''):
    return f'<div style="background:#fff;color:var(--ink);border-radius:28px;padding:34px 44px;{extra}"><p style="font-size:40px;font-weight:700;color:#5A6B80">{t}</p><p style="font-size:78px;font-weight:900;line-height:1.15">{v}</p></div>'
cards=[
 {"dark":True,"html":f'''<div style="position:absolute;right:-60px;top:420px;font-size:520px;opacity:.10">📄</div>
<div style="{W};top:250px"><div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:44px;padding:12px 26px;border-radius:12px">12월 1일(화) 마감</div>
<h1 style="font-size:112px;font-weight:900;line-height:1.15;margin-top:44px">근로·자녀장려금<br><span class="acc">기한 후 신청</span></h1>
<p style="font-size:50px;font-weight:600;line-height:1.5;margin-top:44px;opacity:.92">5월에 놓쳤어도<br>지금 신청하면 산정액의 95%</p></div>
<div style="position:absolute;left:80px;bottom:80px;font-size:34px;opacity:.6">넘겨서 확인 →</div>'''},
 {"html":f'''<div style="{W};top:220px"><p style="font-size:44px;font-weight:700;color:#5A6B80">누가 대상인가요?</p>
<h2 style="font-size:80px;font-weight:900;line-height:1.25;margin-top:24px">2025년 소득분 장려금을<br><span class="hl">아직 신청 안 한</span> 가구</h2>
<div style="margin-top:56px;background:#fff;border-radius:28px;padding:44px;font-size:44px;line-height:1.6;font-weight:500;box-shadow:0 6px 0 #E3E8EF">· 11월 2일 안내문 발송 <b>26만 가구</b><br>· 올해 처음 안내받은 <b>1만 가구</b> 포함<br>· 지금 퇴직했어도 2025년 소득 있으면 가능</div></div>'''},
 {"dark":True,"html":f'''<div style="{W};top:200px"><p style="font-size:46px;font-weight:700;opacity:.85">핵심 숫자 3개</p>
<div style="margin-top:44px;display:flex;flex-direction:column;gap:30px">{box("마감","12월 1일<span style='font-size:52px'>(화)</span>")}{box("지급률","산정액 <span class='hl'>95%</span>")}{box("지급일","2027. 1. 15")}</div></div>'''},
 {"html":f'''<div style="{W};top:200px"><p style="font-size:44px;font-weight:700;color:#5A6B80">소득 기준 (2025년 부부합산)</p>
<div style="margin-top:40px;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 6px 0 #E3E8EF">
<div style="display:grid;grid-template-columns:.8fr 1.35fr .85fr;font-size:40px;font-weight:800;background:var(--navy);color:#fff;padding:26px 30px"><span>가구</span><span>소득</span><span>최대</span></div>
<div style="display:grid;grid-template-columns:.8fr 1.35fr .85fr;font-size:44px;font-weight:600;padding:28px 30px;border-bottom:2px solid #EEF1F5"><span>단독</span><span>2,200만 미만</span><span><b>165만</b></span></div>
<div style="display:grid;grid-template-columns:.8fr 1.35fr .85fr;font-size:44px;font-weight:600;padding:28px 30px;border-bottom:2px solid #EEF1F5"><span>홑벌이</span><span>3,200만 미만</span><span><b>285만</b></span></div>
<div style="display:grid;grid-template-columns:.8fr 1.35fr .85fr;font-size:44px;font-weight:600;padding:28px 30px"><span>맞벌이</span><span>4,400만 미만</span><span><b>330만</b></span></div></div>
<p style="font-size:38px;line-height:1.55;margin-top:36px;font-weight:500">자녀장려금: 18세 미만 자녀, 소득 7,000만 원 미만<br>→ 1명당 <b>50~100만 원</b> · 재산 2억 4천만 원 미만</p></div>'''},
 {"html":f'''<div style="{W};top:200px"><p style="font-size:44px;font-weight:700;color:#5A6B80">어떻게 신청하나요?</p>
<div style="margin-top:36px;display:flex;flex-direction:column;gap:26px;font-size:42px;line-height:1.5">
<div style="background:#fff;border-radius:24px;padding:34px 40px;box-shadow:0 6px 0 #E3E8EF"><b style="font-size:46px">안내문 받았다면</b><br>QR코드 · 카톡/토스/문자 '신청하기'<br>ARS <b>1544-9944</b></div>
<div style="background:#fff;border-radius:24px;padding:34px 40px;box-shadow:0 6px 0 #E3E8EF"><b style="font-size:46px">못 받았다면</b><br>홈택스 → 장려금 → 정기 신청<br>→ 직접입력 신청 (증빙 첨부)</div>
<div style="background:#FFF4D1;border-radius:24px;padding:30px 40px"><b>휴대폰이 어렵다면</b> 상담센터 1566-3636</div></div></div>'''},
 {"dark":True,"html":f'''<div style="{W};top:260px"><p style="font-size:120px">⚠️</p>
<h2 style="font-size:92px;font-weight:900;line-height:1.2;margin-top:24px">12월 1일 지나면<br><span class="red">추가 신청 불가</span></h2>
<div style="margin-top:60px;background:var(--acc);color:var(--ink);border-radius:28px;padding:40px 44px;font-size:44px;font-weight:800;line-height:1.5">저장해 두고 가족에게 공유하세요<br><span style="font-weight:600;font-size:38px">요건표·FAQ 전체 정리는 프로필 링크 디피로그</span></div></div>'''},
]
SAFE='left:80px;right:170px'
reel=[
 {"html":f'''<div style="position:absolute;right:120px;top:980px;font-size:420px;opacity:.10">📄</div>
<div style="position:absolute;left:80px;top:250px" class="brand"><i></i>디피로그</div>
<div style="position:absolute;{SAFE};top:400px"><div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:52px;padding:14px 30px;border-radius:14px">12월 1일(화) 마감</div>
<h1 style="font-size:118px;font-weight:900;line-height:1.15;margin-top:50px">근로·자녀<br>장려금<br><span class="acc">아직 안 받았다면?</span></h1></div>'''},
 {"html":f'''<div style="position:absolute;{SAFE};top:420px"><p style="font-size:60px;font-weight:700;opacity:.85">국세청이 11월 2일</p><h2 style="font-size:104px;font-weight:900;line-height:1.2;margin-top:30px"><span class="acc">26만 가구</span>에<br>안내문을<br>보냈어요</h2>
<p style="font-size:52px;font-weight:600;margin-top:50px;opacity:.9;line-height:1.45">5월 정기 신청을<br>놓친 가구 대상</p></div>'''},
 {"html":f'''<div style="position:absolute;{SAFE};top:300px"><p style="font-size:56px;font-weight:700;opacity:.8">핵심만 3가지</p>
<div style="margin-top:50px;display:flex;flex-direction:column;gap:36px">{box("마감","12월 1일<span style='font-size:56px'>(화)</span>")}{box("지급률","산정액 <span class='hl'>95%</span>")}{box("지급일","2027. 1. 15")}</div></div>'''},
 {"html":f'''<div style="position:absolute;{SAFE};top:360px"><p style="font-size:56px;font-weight:700;opacity:.85">근로장려금 최대</p>
<div style="margin-top:44px;font-size:76px;font-weight:900;line-height:1.55">단독 <span class="acc">165만</span><br>홑벌이 <span class="acc">285만</span><br>맞벌이 <span class="acc">330만</span></div>
<p style="font-size:50px;font-weight:600;margin-top:44px;line-height:1.45;opacity:.92">자녀장려금<br>1명당 최대 <b class="acc">100만 원</b></p></div>'''},
 {"html":f'''<div style="position:absolute;{SAFE};top:360px"><p style="font-size:56px;font-weight:700;opacity:.85">신청 방법</p>
<h2 style="font-size:88px;font-weight:900;line-height:1.25;margin-top:30px">안내문 QR<br>카톡 '신청하기'<br>ARS <span class="acc">1544-9944</span></h2>
<p style="font-size:50px;font-weight:600;margin-top:50px;line-height:1.45;opacity:.92">안내문 못 받았다면<br>홈택스에서 직접 신청</p></div>'''},
 {"html":f'''<div style="position:absolute;{SAFE};top:520px"><p style="font-size:150px;line-height:1">⚠️</p>
<h2 style="font-size:108px;font-weight:900;line-height:1.18;margin-top:40px">12월 1일이<br>지나면<br><span class="red">추가 신청 불가</span></h2></div>'''},
 {"html":f'''<div style="position:absolute;{SAFE};top:360px"><p style="font-size:56px;font-weight:700;opacity:.85">소득 기준표 · 신청 경로</p>
<h2 style="font-size:96px;font-weight:900;line-height:1.22;margin-top:30px">디피로그에<br><span class="acc">표로 정리</span>했어요</h2>
<div style="margin-top:60px;background:var(--acc);color:var(--ink);border-radius:28px;padding:44px 48px;font-size:50px;font-weight:800;line-height:1.45">프로필 링크 → 디피로그<br><span style="font-weight:600;font-size:42px">가족에게도 공유해 주세요</span></div></div>'''},
]
json.dump({"cards":cards,"reel":reel},open(os.path.join(os.path.dirname(__file__),'spec.json'),'w',encoding='utf-8'),ensure_ascii=False)
