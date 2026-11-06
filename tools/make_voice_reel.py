"""장면 이미지 + 장면별 내레이션(TTS) + BGM → 릴스 mp4
사용: python3 make_voice_reel.py script.json 장면폴더 bgm.wav out.mp4
script.json: [{"img":"reel_01.png","text":"..."}, ...]
TTS: edge-tts (ko-KR-SunHiNeural). 프록시 CA 패치 포함.
"""
import json,sys,os,subprocess,asyncio,ssl
CA='/root/.ccr/ca-bundle.crt'
if os.path.exists(CA):
    import certifi; certifi.where=lambda:CA
    _o=ssl.create_default_context
    def c(*a,**k): k['cafile']=CA; return _o(*a,**k)
    ssl.create_default_context=c
import edge_tts
script=json.load(open(sys.argv[1],encoding='utf-8')); sd=sys.argv[2]; bgm=sys.argv[3]; out=sys.argv[4]
vd=os.path.join(os.path.dirname(os.path.abspath(out)),'..','voice'); vd=os.path.abspath(vd); os.makedirs(vd,exist_ok=True)
VOICE=os.environ.get('VOICE','ko-KR-SunHiNeural'); RATE=os.environ.get('RATE','+12%')
async def tts(t,p): await edge_tts.Communicate(t,VOICE,rate=RATE).save(p)
dur=[];vf=[]
for i,s in enumerate(script,1):
    p=os.path.join(vd,f'v{i:02d}.mp3'); asyncio.run(tts(s['text'],p)); vf.append(p)
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
    dur.append(max(2.8,d+0.7))
X=0.35
inp=[];fc=[]
for i,s in enumerate(script):
    inp+=['-loop','1','-t',f'{dur[i]+X:.3f}','-i',os.path.join(sd,s['img'])]
prev='0:v';off=0
for i in range(1,len(script)):
    off+=dur[i-1]; o=f'x{i}'
    fc.append(f'[{prev}][{i}:v]xfade=transition=slideleft:duration={X}:offset={off-0+0:.3f}[{o}]'); prev=o
    off+=0
total=sum(dur)+X
n=len(script)
for i,p in enumerate(vf): inp+=['-i',p]
inp+=['-stream_loop','-1','-i',bgm]
delays=[];t=0
for i in range(n):
    delays.append(int((t+0.25)*1000)); t+=dur[i]
vs=''.join(f'[{n+i}:a]adelay={delays[i]}|{delays[i]},volume=1.0[va{i}];' for i in range(n))
mix=''.join(f'[va{i}]' for i in range(n))
fc_s=';'.join(fc)+f';[{prev}]format=yuv420p,fps=30[v];'+vs+f'{mix}amix=inputs={n}:normalize=0,apad[vo];[{2*n}:a]atrim=0:{total:.3f},volume=0.16,afade=t=out:st={total-1.5:.3f}:d=1.5[bg];[vo][bg]amix=inputs=2:normalize=0:duration=first,atrim=0:{total:.3f},loudnorm=I=-15:TP=-1.5:LRA=11[a]'
cmd=['ffmpeg','-y','-loglevel','error']+inp+['-filter_complex',fc_s,'-map','[v]','-map','[a]','-t',f'{total:.3f}','-c:v','libx264','-preset','medium','-crf','20','-c:a','aac','-b:a','192k','-movflags','+faststart',out]
subprocess.run(cmd,check=True)
print('saved',out,f'{total:.1f}s',[round(d,1) for d in dur])
