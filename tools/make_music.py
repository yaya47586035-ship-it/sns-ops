"""저작권 없는 자체 제작 배경음악 생성기 (코드 합성, 100% 자체 제작물)
사용: python3 make_music.py out.wav --sec 29.2 --bpm 112 --mood bright|calm
"""
import numpy as np,argparse,wave
ap=argparse.ArgumentParser();ap.add_argument('out');ap.add_argument('--sec',type=float,default=30);ap.add_argument('--bpm',type=float,default=112);ap.add_argument('--mood',default='bright')
a=ap.parse_args();SR=44100;N=int(a.sec*SR);beat=60/a.bpm
L=np.zeros(N);R=np.zeros(N)
def note(m): return 440*2**((m-69)/12)
def add(sig,start,pan=0.0,gain=1.0):
    i=int(start*SR);j=min(N,i+len(sig))
    if i>=N: return
    s=sig[:j-i]*gain;L[i:j]+=s*(1-pan)/1;R[i:j]+=s*(1+pan)/1
def pluck(f,dur,bright=1.0):
    t=np.arange(int(dur*SR))/SR;env=np.exp(-t*5)*(1-np.exp(-t*300))
    s=np.sin(2*np.pi*f*t)+.45*bright*np.sin(4*np.pi*f*t)+.18*bright*np.sin(6*np.pi*f*t)+.08*np.sin(8*np.pi*f*t)
    return s*env*.18
def pad(fs,dur):
    t=np.arange(int(dur*SR))/SR;env=np.minimum(1,t/0.4)*np.minimum(1,(dur-t)/0.4)
    s=sum(np.sin(2*np.pi*f*t+np.sin(2*np.pi*.3*t)*.3)+.3*np.sin(2*np.pi*f*1.003*t) for f in fs)
    return s*env*.035
def bass(f,dur):
    t=np.arange(int(dur*SR))/SR;env=np.exp(-t*3)*(1-np.exp(-t*200))
    return (np.sin(2*np.pi*f*t)+.3*np.sin(4*np.pi*f*t))*env*.32
def kick():
    t=np.arange(int(.35*SR))/SR;f=50+90*np.exp(-t*30);return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)*.55
rng=np.random.default_rng(7)
def hat(): t=np.arange(int(.06*SR))/SR;n=rng.standard_normal(len(t));n=np.diff(n,prepend=0);return n*np.exp(-t*60)*.05
def clap(): t=np.arange(int(.18*SR))/SR;n=rng.standard_normal(len(t));return n*np.exp(-t*22)*.09
# C major: C G Am F  (bright) / Am F C G (calm)
prog={'bright':[(48,[60,64,67]),(43,[59,62,67]),(45,[60,64,69]),(41,[60,65,69])],
      'calm':[(45,[60,64,69]),(41,[60,65,69]),(48,[60,64,67]),(43,[59,62,67])]}[a.mood]
melody=[72,76,79,76, 74,79,74,71, 72,76,81,79, 77,76,74,72]
bar=4*beat;t=0;b=0
while t<a.sec:
    root,ch=prog[b%4]
    add(pad([note(m) for m in ch],bar+.2),t)
    for k in range(4):
        add(bass(note(root),beat*.95),t+k*beat)
        if b>=1: add(kick(),t+k*beat,gain=1.0 if k%2==0 else .7)
        if b>=1 and k%2==1: add(clap(),t+k*beat,pan=.1)
        for h in range(2):
            if b>=1: add(hat(),t+k*beat+h*beat/2,pan=.3 if h else -.3)
    # arpeggio 8ths
    arp=ch+[ch[1]+12]
    for e in range(8):
        add(pluck(note(arp[e%4]+12),beat*.6,.6),t+e*beat/2,pan=-.25,gain=.55)
    if b>=2:
        for q in range(4):
            m=melody[(b*4+q)%16]
            add(pluck(note(m),beat*1.2),t+q*beat,pan=.2,gain=.9)
    t+=bar;b+=1
mix=np.stack([L,R],1)
fade=int(2.0*SR);mix[-fade:]*=np.linspace(1,0,fade)[:,None];mix[:int(.3*SR)]*=np.linspace(0,1,int(.3*SR))[:,None]
mix/=np.max(np.abs(mix))*1.12
with wave.open(a.out,'wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
print('saved',a.out)
