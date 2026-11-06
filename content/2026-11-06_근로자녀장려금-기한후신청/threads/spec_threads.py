import json,os,sys
H=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(H,'..','cards'))
from spec_photo import ST,bg
L='position:absolute;left:48px;right:40px'
def c(f,pos,inner,bubble=None):
    b=f'<div class="bubble" style="left:110px;right:290px;top:110px;font-size:42px">{bubble}</div>' if bubble else ''
    return {"raw":True,"html":ST+bg(f,pos)+'<div class="brandp" style="right:44px;top:44px;font-size:30px"><i></i>디피로그</div>'+b+inner}
cards=[
 c('90b9f32c.jpg','center 30%',f'''<div style="{L};bottom:60px"><span class="pill" style="font-size:52px;background:#FF5A4E;color:#fff">12월 1일(화) 마감</span>
<h1 class="hd" style="font-size:128px;margin-top:30px">부모님 폰에 온<br><span class="y">장려금 문자</span></h1>
<p class="chk" style="font-size:52px;margin-top:26px"><b>✓</b>지우기 전에 꼭 확인하세요</p></div>''',bubble='국세청 문자,<br>스미싱 아닐 수 있어요!'),
 c('75816635.jpg','center 40%',f'''<div style="{L};bottom:60px"><span class="pill" style="font-size:52px">5월에 놓쳤다면 <em>기한 후 신청</em></span>
<h2 class="hd" style="font-size:136px;margin-top:30px">산정액<br><span class="y">95% 지급</span></h2>
<p class="chk" style="font-size:52px;margin-top:26px"><b>✓</b>2027년 1월 15일(금) 입금</p></div>'''),
 c('3a48016e.jpg','center 35%',f'''<div style="{L};bottom:60px"><span class="pill" style="font-size:52px">안내문을 <em>못 받았다면</em></span>
<h2 class="hd" style="font-size:128px;margin-top:30px">홈택스에서<br><span class="y">직접 신청</span></h2>
<p class="chk" style="font-size:50px;margin-top:26px"><b>✓</b>퇴직했어도 2025년 소득 있으면</p>
<p class="chk" style="font-size:50px;margin-top:14px"><b>✓</b>도움 필요하면 1566-3636</p></div>'''),
]
json.dump({"cards":cards},open(os.path.join(H,'spec_threads.json'),'w',encoding='utf-8'),ensure_ascii=False)
