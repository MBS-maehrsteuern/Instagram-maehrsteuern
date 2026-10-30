# Harter Schnitt: Segmente (Sekunden im Rohclip) -> geschnittenes Video 1080x1920@30 + bereinigte Stimme + Wortzeiten
import json,subprocess,sys
from pathlib import Path
R=Path('/home/user/roh')
REELS={
 'weihnachtsfeier':('VID_114112',[(34.80,39.50),(66.05,72.70),(145.12,157.05),(187.70,193.50),(203.20,207.10)]),
 'kundengeschenk':('VID_115004',[(13.95,18.80),(19.30,23.30),(24.05,30.72),(31.05,38.98),(46.85,50.20)]),
}
KLANG="pan=mono|c0=c0,highpass=f=110,afftdn=nr=14:nf=-40,acompressor=threshold=-24dB:ratio=3:attack=8:release=120:makeup=4"
for name,(clip,segs) in REELS.items():
    if len(sys.argv)>1 and name not in sys.argv[1:]: continue
    woerter=json.load(open(R/f'{clip}_l.json'))
    fc=[];n=len(segs);neu=[];off=0
    for i,(a,b) in enumerate(segs):
        for w in woerter:
            if a-0.05<=w['s'] and w['e']<=b+0.1: neu.append(dict(w=w['w'].strip(),s=round(w['s']-a+off,2),e=round(min(w['e'],b)-a+off,2),seg=i))
        off+=b-a
    liste=R/f'out/{name}_liste.txt'; zeilen=[]
    for i,(a,b) in enumerate(segs):
        teil=R/f'out/{name}_t{i}.mov'
        subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(a),'-t',str(round(b-a,3)),'-i',str(R/f'{clip}.mp4'),
            '-vf','fps=30,scale=1080:1920','-af',f"{KLANG},afade=t=in:d=0.03,afade=t=out:st={b-a-0.04:.3f}:d=0.04",
            '-c:v','libx264','-crf','17','-preset','fast','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',str(teil)],check=True)
        zeilen.append(f"file '{teil}'")
    liste.write_text('\n'.join(zeilen))
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',str(liste),'-c','copy',str(R/f'out/{name}_schnitt.mov')],check=True)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',str(R/f'out/{name}_schnitt.mov'),'-vn',str(R/f'out/{name}_stimme.wav')],check=True)
    json.dump(dict(dauer=round(off,2),segmente=[round(b-a,2) for a,b in segs],woerter=neu),open(R/f'out/{name}_woerter.json','w'),ensure_ascii=False,indent=0)
    print(name,round(off,2),'s')
