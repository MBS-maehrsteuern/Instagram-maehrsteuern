# Schnitt v3: Segmente + Pausen-Kürzung (Stille > 0,35 s → 0,22 s) + Zeit-Mapping neu→alt für die Overlays
import json,subprocess,sys,wave,numpy as np
from pathlib import Path
R=Path('/home/user/roh')
REELS={ # (a,b[,quelle]) roh; alt_len = Segmentlänge im alten Schnitt (darauf sind die Overlays synchronisiert)
 'weihnachtsfeier':('VID_114112',[(34.80,39.58,4.70),(66.05,72.70,6.65),(145.12,157.20,11.93),(187.70,193.56,5.80),(40.10,42.70,2.35,'VID_115004')]),
 'kundengeschenk':('VID_115004',[(13.95,18.80,4.85),(19.30,23.30,4.0),(24.05,30.72,6.67),(31.05,39.10,7.93),(40.10,42.70,2.35,'VID_115004')]),
}
KLANG="pan=mono|c0=c0,highpass=f=110,afftdn=nr=14:nf=-40,acompressor=threshold=-24dB:ratio=3:attack=8:release=120:makeup=4"
KLANG_CTA="pan=mono|c0=c0,highpass=f=160,afftdn=nr=22:nf=-35,acompressor=threshold=-24dB:ratio=3:attack=8:release=120:makeup=4"
def pegel(q):
    w=wave.open(str(R/f'{q}_l.wav')); return w.getframerate(),np.frombuffer(w.readframes(10**9),np.int16).astype(float)/32768
CACHE={}
def teile(q,a,b,grenze=-45,minp=0.35,rest=0.11):
    if q not in CACHE: CACHE[q]=pegel(q)
    sr,x=CACHE[q]; st=0.01; t=np.arange(a,b,st)
    db=np.array([20*np.log10(np.sqrt(np.mean(x[int(u*sr):int((u+st)*sr)]**2))+1e-9) for u in t])
    still=db<grenze; out=[]; start=a; i=0
    while i<len(t):
        if still[i]:
            j=i
            while j<len(t) and still[j]: j+=1
            if (j-i)*st>=minp and i>0 and j<len(t):
                out.append((start,t[i]+rest)); start=t[j]-rest
            i=j
        else: i+=1
    out.append((start,b)); return out
for name,(clip,segs) in REELS.items():
    liste=[]; abbild=[]; neu=0; alt=0; cta_neu=None
    for i,s in enumerate(segs):
        a,b,alen=s[:3]; q=s[3] if len(s)>3 else clip; k=KLANG_CTA if len(s)>3 else KLANG
        if i==len(segs)-1: cta_neu=neu
        for j,(p,r) in enumerate(teile(q,a,b) if len(s)<=3 else [(a,b)]):
            teil=R/f'out/{name}_v3_{i}_{j}.mov'; d=r-p
            subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',f'{p:.3f}','-t',f'{d:.3f}','-i',str(R/f'{q}.mp4'),'-vf','fps=30,scale=1080:1920',
              '-af',f"{k},afade=t=in:d=0.02,afade=t=out:st={d-0.04:.3f}:d=0.04",'-c:v','libx264','-crf','17','-preset','fast','-pix_fmt','yuv420p',
              '-c:a','pcm_s16le','-ar','48000',str(teil)],check=True)
            liste.append(f"file '{teil}'")
            dd=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(teil)]))
            abbild.append(dict(neu=neu,dauer=dd,alt=alt+min(p-a,alen-0.01),alt_max=alt+alen-0.01)); neu+=dd
        alt+=alen
    (R/f'out/{name}_v3.txt').write_text('\n'.join(liste))
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',str(R/f'out/{name}_v3.txt'),'-c','copy',str(R/f'out/{name}_schnitt.mov')],check=True)
    n=int(neu*30); zeiten=[]
    for f in range(n):
        t=f/30; m=[x for x in abbild if x['neu']<=t][-1]; zeiten.append(round(min(m['alt']+(t-m['neu']),m['alt_max']),4))
    json.dump(dict(dauer=neu,cta=cta_neu,zeiten=zeiten),open(R/f'out/{name}_mapping.json','w'))
    print(name,'neu',round(neu,2),'s (alt',round(alt,2),') cta ab',round(cta_neu,2),'Teile',len(liste))
